# Marketing Codex

A personal knowledge base for Product and Technical Marketing Management, built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Generic PMM knowledge for software — frameworks, competitive intelligence, messaging methodology, and reusable marketing skills.

## How it works

This repo is both an [Obsidian](https://obsidian.md/) vault and a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) project. Obsidian provides the visual layer (graph view, wikilinks, search). Claude Code provides the agentic layer (ingestion, synthesis, deliverable generation). Both point at the same directory.

Knowledge compounds over time. Sources go in, Claude Code extracts entities and concepts, cross-references everything, and files it into a structured wiki. The more you ingest, the richer the context for generating marketing deliverables.

## Structure

```
marketing-codex/
├── CLAUDE.md        # Schema, conventions, and slash command definitions for Claude Code
├── log.md           # Reverse-chronological changelog of all wiki activity
├── raw/             # Unprocessed external source material (articles, reports, transcripts)
├── articles/        # Your own writing — full text, authoritative primary source
│   └── _template.md # Frontmatter template for new articles
├── wiki/
│   ├── index.md     # Master index of all wiki pages (auto-maintained)
│   ├── hot.md       # Rolling session context cache (~500 words)
│   ├── sources/     # Processed source summaries — one page per ingested source
│   ├── concepts/    # PMM frameworks, methodologies, patterns
│   └── entities/    # Companies, products, people, analyst firms
├── skills/          # Reusable Claude Code workflows (messaging, battle cards, etc.)
├── templates/       # Output format templates
└── examples/        # Gold-standard reference outputs for quality benchmarking
```

### raw/ vs articles/

Two intake folders serve different purposes:

**`raw/`** is for external source material you haven't processed yet — PDFs, copied articles, analyst reports, interview transcripts. Drop things here before ingesting. Not git-tracked if PDF (see `.gitignore`).

**`articles/`** is for your own writing — blog posts, essays, frameworks, unpublished drafts. Full text lives here as the authoritative source. When ingested, the wiki holds a synopsis that links back to the article file. Articles are first-class citizens, not summaries. Concepts extracted from your own articles carry `origin: self` in frontmatter to distinguish them from externally sourced knowledge.

## Workflows

All workflows run through Claude Code using slash commands defined in `CLAUDE.md`:

- `/ingest [source]` — Process a source into wiki pages with cross-references. Works with URLs, `raw/` files, and `articles/` files. Own articles get a synopsis in `wiki/sources/` plus entity and concept pages; full text stays in `articles/`.
- `/query [question]` — Answer a question grounded in wiki content, not training data
- `/lint` — Find orphan pages, dead links, stale content, contradictions
- `/build [skill] [args]` — Generate a marketing deliverable using wiki context
- `/status` — Wiki stats, recent activity, session context

## Forking for company-specific use

This repo contains generic PMM knowledge. To add company-specific content:

1. Fork the repo to a private copy
2. Add a `company/` directory with parallel structure (`company/wiki/`, `company/skills/`, etc.)
3. Company-specific pages use the same frontmatter schemas with `scope: company`
4. Pull upstream changes from the generic repo without conflicts

## Setting up your own instance

See [How to build your PMM Brain](./tutorials/building%20your%20own%20codex/How%20to%20build%20your%20PMM%20Brain.md) in the tutorials folder.

1. Clone the repo
2. Open the folder as an Obsidian vault
3. Install the [Obsidian Git plugin](https://github.com/denolehov/obsidian-git) for sync
4. Run `claude` in the same directory to start Claude Code
5. Start ingesting sources with `/ingest`

## Git conventions

Commits use conventional format: `ingest: [source]`, `wiki: create [page]`, `wiki: update [page]`, `lint: fix [description]`, `skill: add [name]`, `template: add [name]`, `article: add [title]`.
