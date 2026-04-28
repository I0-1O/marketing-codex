# eml2md

Convert `.eml` email files to clean Markdown with YAML frontmatter. Handles
HTML layout-table noise (LinkedIn, Mailchimp, Workday, etc.), prefers plain-text
bodies when available, and outputs Obsidian-compatible files.

## Requirements

Python 3.10+ and the packages in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

### Single file

```bash
python eml2md.py message.eml
# → writes message.md alongside the .eml file

python eml2md.py message.eml -o ./output/
# → writes to a specific output directory
```

### Batch (recursive directory)

```bash
python eml2md.py ./inbox/ -o ./converted/
```

Finds all `.eml` files recursively under `./inbox/` and writes a `.md` for each
into `./converted/`. Exits with code `1` if any file fails; successful files are
still written.

### stdin

```bash
cat message.eml | python eml2md.py - -o ./output/
# → filename derived from subject

cat message.eml | python eml2md.py -
# → markdown written directly to stdout
```

### Machine-readable output (JSON)

```bash
python eml2md.py ./inbox/ -o ./converted/ --json
```

Suppresses human-readable status and prints a JSON array to stdout:

```json
[
  { "input": "inbox/foo.eml", "output": "converted/foo.md", "subject": "Hello" },
  { "input": "inbox/bar.eml", "output": null, "subject": null, "error": "..." }
]
```

Useful for scripting or piping results into another tool.

## Output format

Each `.md` file starts with a YAML frontmatter block followed by the email body
as Markdown:

```markdown
---
title: Your application to Senior PMM at Acme
date: '2026-04-28T18:28:06+00:00'
from: recruiter@acme.com
to: you@example.com
message_id: <abc123@mail.example.com>
eml_filename: message.eml
converted_at: '2026-04-28T15:04:51.016205'
reply_to: recruiter@acme.com
---

# Your application to Senior PMM at Acme

Thank you for your interest...
```

Optional frontmatter fields (only present when the header exists in the email):
`cc`, `bcc`, `reply_to`, `in_reply_to`, `references`

## How HTML cleanup works

Marketing and notification emails (LinkedIn, Indeed, Workday, Ashby, etc.) use
nested HTML tables for layout. Without cleanup this produces hundreds of lines of
`| --- |` noise in the markdown output.

eml2md applies a two-layer strategy:

1. **Prefer `text/plain`** — if the email includes a plain-text part with at
   least 200 characters of content, that is used directly. Most transactional
   senders ship a clean plain-text alternative alongside their HTML.

2. **Unwrap layout tables** — for HTML-only emails, any `<table>` that contains
   another `<table>` is treated as a layout table and replaced with its cell
   contents in document order. Flat data tables (no nesting) are preserved.

## Exit codes

| Code | Meaning |
|------|---------|
| `0`  | All files converted successfully |
| `1`  | One or more files failed (batch mode continues past failures) |
| `2`  | Duplicate / skipped (not used by this tool directly) |
