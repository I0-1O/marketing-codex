# Marketing Codex

A personal knowledge base for Product and Technical Marketing Management, built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Generic PMM knowledge for software - frameworks, competitive intelligence, messaging methodology, and reusable marketing skills.
## How it works
This repo is both an [Obsidian](https://obsidian.md/) vault and a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) project. Obsidian provides the visual layer (graph view, wikilinks, search). Claude Code provides the agentic layer (ingestion, synthesis, deliverable generation). Both point at this same directory.

Knowledge compounds over time. Sources go in, Claude Code extracts entities and concepts, cross-references everything, and files it into a structured wiki. The more you ingest, the richer the context for generating marketing deliverables.
## Structure
```
pmm-brain/
├── CLAUDE.md        # Schema, conventions, and workflows for Claude Code
├── log.md           # Reverse-chronological changelog of all wiki activity
├── raw/             # Unprocessed source material (articles, reports, transcripts)
├── wiki/
│   ├── index.md     # Master index of all wiki pages
│   ├── hot.md       # Rolling session context cache
│   ├── sources/     # Processed source summaries
│   ├── concepts/    # PMM frameworks, methodologies, patterns
│   └── entities/    # Companies, products, analysts, competitors
├── skills/          # Reusable Claude Code workflows (messaging, battle cards, etc.)
├── templates/       # Output format templates
└── examples/        # Gold-standard reference outputs for quality benchmarking
```

## Workflows
All workflows are run through Claude Code using slash commands defined in `CLAUDE.md`:

- `/ingest [source]` — Process a source into wiki pages with cross-references
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

## Setup
1. Clone the repo
2. Open the folder as an Obsidian vault
3. Install the Obsidian Git plugin for sync
4. Run `claude` in the same directory to start Claude Code
5. Start ingesting sources with `/ingest`

## Git conventions
Commits use conventional format: `ingest: [source]`, `wiki: create [page]`, `wiki: update [page]`, `lint: fix [description]`, `skill: add [name]`, `template: add [name]`.