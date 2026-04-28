"""
eml2md.py — Convert EML files to clean Markdown with YAML frontmatter.

Supports single files, directories (recursive), or stdin via '-'.
Designed for CLI use and easy integration with Claude Code.

Dependencies: pyyaml, beautifulsoup4, markdownify
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from email import policy
from email.header import decode_header as email_decode_header
from email.parser import BytesParser
from email.utils import parsedate_to_datetime

import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md


# Define a list of common email header fields to extract.
HEADER_FIELDS = [
    "subject",
    "from",
    "to",
    "cc",
    "bcc",
    "date",
    "message-id",
    "reply-to",
    "in-reply-to",
    "references",
]


class EMLConversionError(Exception):
    """Raised when an EML file cannot be converted."""


def decode_header_value(value: str | None) -> str:
    """
    Safely decode MIME/email headers that might be encoded (e.g., in UTF-8 or other charsets).

    Args:
        value: The raw header string to decode.

    Returns:
        The decoded header string.
    """
    if not value:
        return ""

    decoded_parts = email_decode_header(value)
    return "".join(
        part.decode(encoding or "utf-8", errors="replace")
        if isinstance(part, bytes)
        else part
        for part, encoding in decoded_parts
    )


def extract_headers(msg) -> dict:
    """
    Extract normalized email headers for metadata/frontmatter.

    Args:
        msg: An email.message.Message object parsed from an EML file.

    Returns:
        A dictionary containing extracted and normalized header key-value pairs.
    """
    headers = {}

    for key in HEADER_FIELDS:
        raw_value = msg.get(key)
        if not raw_value:
            continue

        decoded = decode_header_value(raw_value).strip()
        normalized_key = key.replace("-", "_")  # Convert 'message-id' to 'message_id'

        if key == "date":
            # Attempt to parse the date into a datetime object and then format it.
            try:
                dt = parsedate_to_datetime(decoded)
                headers["date"] = dt.isoformat()
                headers["date_readable"] = dt.strftime("%Y-%m-%d %H:%M:%S %z")
            except Exception:
                # Fallback to the raw decoded date if parsing fails.
                headers["date"] = decoded
        else:
            headers[normalized_key] = decoded

    # Add the original EML file name to the headers.
    headers["eml_file"] = msg.get_filename() or "unknown.eml"
    return headers


def unwrap_layout_tables(soup) -> None:
    """
    Replace tables-used-for-layout with their cell contents in document order.

    Heuristic: any <table> that contains another <table> is being used for layout
    (real data tables don't nest). We walk innermost-first so each unwrap reduces
    nesting depth predictably.
    """
    while True:
        layout_tables = [
            t for t in soup.find_all("table")
            if t.find("table") is not None
        ]
        if not layout_tables:
            break

        # Sort innermost-first: a table with the deepest nested-table descendant goes last.
        # Simpler: process tables that have a nested table but no doubly-nested tables first.
        for table in layout_tables:
            # Collect cell contents in document order, then replace the table with them.
            replacement_nodes = []
            for cell in table.find_all(["td", "th"]):
                # Move each cell's children out; insert a <br> between cells for separation.
                for child in list(cell.contents):
                    replacement_nodes.append(child.extract())
                replacement_nodes.append(soup.new_tag("br"))
            table.replace_with(*replacement_nodes)


def clean_html_for_markdown(html_content: str) -> str:
    """
    Remove problematic HTML tags and attributes that don't translate well to Markdown
    or are unnecessary (e.g., scripts, styles, images).

    Args:
        html_content: The raw HTML string from the email body.

    Returns:
        A cleaned HTML string.
    """
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, "html.parser")

    # Remove specific tags that are usually not desired in Markdown output.
    for tag in soup.find_all([
        "script",
        "style",
        "head",
        "meta",
        "link",
        "iframe",
        "noscript",
    ]):
        tag.decompose()  # Remove the tag and its contents.

    # Remove images as they typically don't convert directly to useful Markdown without URLs.
    for img in soup.find_all("img"):
        img.decompose()

    # Strip layout-only tables so markdownify produces linear prose, not table soup.
    unwrap_layout_tables(soup)

    return str(soup)


def convert_body_to_markdown(msg) -> str:
    """
    Extract the email body, preferring HTML over plain text, and convert it to Markdown.

    Args:
        msg: An email.message.Message object.

    Returns:
        The email body converted to Markdown, or a placeholder if no body is found.
    """
    # Prefer text/plain when it is substantive — marketing emails (LinkedIn, etc.)
    # ship layout-table HTML alongside a clean plain alternative. Fall back to HTML
    # if the plain part is missing or just a stub like "View this email in a browser".
    PLAIN_MIN_CHARS = 200
    plain_part = msg.get_body(preferencelist=("plain",))
    if plain_part is not None and len(plain_part.get_content().strip()) >= PLAIN_MIN_CHARS:
        body_part = plain_part
    else:
        body_part = msg.get_body(preferencelist=("html", "plain"))

    if body_part is None:
        return "*No readable body found in this email.*"

    content = body_part.get_content()

    if body_part.get_content_type() == "text/html":
        # Clean HTML before converting to Markdown for better results.
        cleaned_html = clean_html_for_markdown(content)
        return md(
            cleaned_html,
            heading_style="ATX",         # Use ATX style headers (# Heading).
            bullets="-",                 # Use hyphens for unordered list bullets.
            table_infer_header=True,     # Attempt to infer table headers.
            strip=["img", "script", "style"],  # Safety net on top of clean_html_for_markdown.
        ).strip()
    elif body_part.get_content_type() == "text/plain":
        return content.strip()
    else:
        # For other content types (e.g., attachments as body), return a note.
        return f"*Body content type '{body_part.get_content_type()}' not directly convertible to markdown.*"


def build_frontmatter(subject: str, headers: dict) -> str:
    """
    Build YAML frontmatter string for the Markdown file.

    Args:
        subject: The subject of the email (used as the title).
        headers: A dictionary of extracted email headers.

    Returns:
        A string containing the YAML frontmatter block.
    """
    data = {
        "title": subject,
        "date": headers.get("date", ""),
        "from": headers.get("from", ""),
        "to": headers.get("to", ""),
        "message_id": headers.get("message_id", ""),
        "eml_filename": headers.get("eml_file", ""),
        "converted_at": datetime.now().isoformat(),  # Timestamp of conversion.
    }

    # Add optional fields only if they exist in the headers.
    optional_fields = ["cc", "bcc", "reply_to", "in_reply_to", "references"]
    for field in optional_fields:
        if headers.get(field):
            data[field] = headers[field]

    # Serialize the dictionary to YAML and wrap it in '---' delimiters.
    return "---\n" + yaml.safe_dump(
        data,
        sort_keys=False,          # Preserve insertion order for better readability.
        allow_unicode=True,       # Allow non-ASCII characters.
        default_flow_style=False, # Use block style for better readability.
    ) + "---\n\n"


def parse_eml_bytes(raw_bytes: bytes):
    """
    Parse raw EML bytes into an email message object.

    Args:
        raw_bytes: The raw bytes of an EML file.

    Returns:
        A parsed email.message.Message object.

    Raises:
        EMLConversionError: If parsing fails.
    """
    try:
        return BytesParser(policy=policy.default).parsebytes(raw_bytes)
    except Exception as exc:
        raise EMLConversionError(f"Failed to parse EML: {exc}") from exc


def eml2md(
    eml_path: str | Path,
    output_dir: str | Path | None = None,
    quiet: bool = False,
) -> dict:
    """
    Convert a single EML file to a Markdown file with frontmatter.

    Args:
        eml_path: The path to the EML file.
        output_dir: The directory where the Markdown file should be saved.
                    If None, it defaults to the EML file's parent directory.
        quiet: If True, suppress human-readable status output to stdout.

    Returns:
        A dict with keys: input, output, subject (for machine-readable consumption).

    Raises:
        EMLConversionError: If the EML file cannot be parsed.
    """
    eml_path = Path(eml_path)

    with eml_path.open("rb") as f:
        msg = parse_eml_bytes(f.read())

    headers = extract_headers(msg)
    # Track the source filename in headers for frontmatter.
    headers["eml_file"] = eml_path.name
    subject = headers.get("subject") or "(No Subject)"

    frontmatter = build_frontmatter(subject, headers)
    markdown_body = convert_body_to_markdown(msg)

    # Combine frontmatter, a main heading for the subject, and the markdown body.
    md_content = f"{frontmatter}# {subject}\n\n{markdown_body}\n"

    # Determine the output directory and ensure it exists.
    out_dir = Path(output_dir) if output_dir else eml_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Construct the output Markdown file path.
    out_path = out_dir / f"{eml_path.stem}.md"
    out_path.write_text(md_content, encoding="utf-8")

    if not quiet:
        print(f"✓ Converted: {eml_path.name} → {out_path.name}", file=sys.stderr)

    return {"input": str(eml_path), "output": str(out_path), "subject": subject}


def convert_stdin(output_dir: Path | None, quiet: bool = False) -> dict:
    """
    Read an EML from stdin and write the converted Markdown to stdout (if no output_dir)
    or to a file in output_dir.

    Args:
        output_dir: If provided, write to a file here. Otherwise write to stdout.
        quiet: If True, suppress human-readable status output.

    Returns:
        A dict with keys: input, output, subject.
    """
    raw_bytes = sys.stdin.buffer.read()
    msg = parse_eml_bytes(raw_bytes)

    headers = extract_headers(msg)
    headers["eml_file"] = "stdin.eml"
    subject = headers.get("subject") or "(No Subject)"

    frontmatter = build_frontmatter(subject, headers)
    markdown_body = convert_body_to_markdown(msg)
    md_content = f"{frontmatter}# {subject}\n\n{markdown_body}\n"

    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        # Use a sanitized subject or fallback for the filename.
        safe_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in subject)[:80]
        out_path = output_dir / f"{safe_name.strip() or 'stdin'}.md"
        out_path.write_text(md_content, encoding="utf-8")
        if not quiet:
            print(f"✓ Converted: stdin → {out_path.name}", file=sys.stderr)
        return {"input": "stdin", "output": str(out_path), "subject": subject}
    else:
        # No output dir: write markdown directly to stdout for piping.
        sys.stdout.write(md_content)
        return {"input": "stdin", "output": "stdout", "subject": subject}


def batch_convert(
    path: Path,
    output_dir: Path,
    quiet: bool = False,
) -> list[dict]:
    """
    Convert all EML files in a given directory (and its subdirectories) to Markdown.

    Args:
        path: The root directory to search for EML files.
        output_dir: The directory where all converted Markdown files will be saved.
        quiet: If True, suppress human-readable status output.

    Returns:
        A list of result dicts. Failed conversions include an "error" key.
    """
    # Find all files with a '.eml' extension recursively.
    eml_files = sorted(path.rglob("*.eml"))

    if not quiet:
        print(f"Found {len(eml_files)} .eml files. Starting conversion...\n", file=sys.stderr)

    results = []
    for eml_file in eml_files:
        try:
            results.append(eml2md(eml_file, output_dir, quiet=quiet))
        except Exception as exc:
            error_result = {
                "input": str(eml_file),
                "output": None,
                "subject": None,
                "error": str(exc),
            }
            results.append(error_result)
            if not quiet:
                print(f"✗ Failed {eml_file.name}: {exc}", file=sys.stderr)

    return results


def main() -> None:
    """
    CLI entry point. Supports single file, directory (recursive), or stdin.
    Use --json for machine-readable output (for Claude Code and scripting).
    """
    parser = argparse.ArgumentParser(
        description="Convert EML files to clean Markdown with YAML frontmatter.",
        epilog="Examples:\n"
               "  python eml2md.py message.eml\n"
               "  python eml2md.py ./inbox/ -o ./converted/ --json\n"
               "  cat message.eml | python eml_to_md.py -\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="-",
        help="Single .eml file, directory of .eml files, or '-' for stdin (default: stdin)",
    )
    parser.add_argument(
        "--outdir", "-o",
        default=None,
        help="Output directory (default: input file's directory for single files, "
             "'markdown_output' for batch, stdout for stdin without -o)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON to stdout (for scripting and Claude Code)",
    )
    args = parser.parse_args()

    path_str = args.path
    # When --json is set, suppress human-readable output so stdout is clean JSON.
    quiet = args.json_output

    results: list[dict] = []

    if path_str == "-":
        # Read from stdin.
        result = convert_stdin(
            output_dir=Path(args.outdir) if args.outdir else None,
            quiet=quiet,
        )
        results.append(result)

    else:
        path = Path(path_str)

        if path.is_file() and path.suffix.lower() == ".eml":
            # Single file conversion.
            out_dir = Path(args.outdir) if args.outdir else path.parent
            result = eml2md(path, out_dir, quiet=quiet)
            results.append(result)

        elif path.is_dir():
            # Batch conversion of all .eml files in directory tree.
            out_dir = Path(args.outdir) if args.outdir else Path("markdown_output")
            results = batch_convert(path, out_dir, quiet=quiet)

        else:
            parser.error(f"'{path_str}' is not an .eml file or directory.")

    # JSON output mode: print structured results to stdout.
    if args.json_output:
        print(json.dumps(results, indent=2))

    # Exit with code 1 if any conversions failed, so callers can detect errors.
    if any(r.get("error") for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
