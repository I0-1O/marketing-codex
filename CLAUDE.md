# PMM Brain — Claude Code Instructions

## Identity

This is a PMM knowledge base for enterprise B2B software marketing. It follows the LLM Wiki pattern (Karpathy-style): structured, compounding, and designed to be queried by Claude Code.

The owner is a Principal Product Marketing Manager with deep experience in workflow automation, business process platforms, and technical marketing.

**Voice:** Direct, concise, no marketing fluff. Substance over polish.

This vault contains **generic PMM knowledge** — not company-specific. It is designed to be forked for company-specific use.

---

## Vault Structure

```
marketing-codex/
├── CLAUDE.md              # This file — instructions for Claude Code
├── log.md                 # Reverse-chronological activity log
├── .gitignore
├── raw/                   # Unprocessed source material (PDFs, .txt, pasted content)
│   └── .gitkeep
├── wiki/
│   ├── index.md           # Master index of all wiki pages (auto-maintained)
│   ├── hot.md             # Session context cache (~500 words, rolling)
│   ├── sources/           # Processed source summaries — one page per source ingested
│   ├── concepts/          # PMM frameworks, methodologies, patterns
│   └── entities/          # Companies, products, analysts, competitors
├── skills/                # Reusable Claude Code PMM workflows (slash commands)
├── templates/             # Output templates (battle cards, one-pagers, etc.)
└── examples/              # Gold-standard reference outputs for few-shot prompting
```

**raw/**: Drop source material here before ingesting. PDFs, copied articles, interview transcripts, analyst reports. Not tracked in git if PDF (see .gitignore).

**wiki/sources/**: One page per ingested source. Summarizes the source and links to extracted entities and concepts. Auto-created by `/ingest`.

**wiki/concepts/**: One page per PMM concept, framework, or methodology. Examples: Jobs to Be Done, Positioning, Win/Loss Analysis, ICP, Category Creation. Created and updated by `/ingest` or manually.

**wiki/entities/**: One page per named entity — company, product, analyst, analyst firm, or person. Created and updated by `/ingest` or manually.

**skills/**: Skill files define reusable Claude Code workflows. Each maps to a slash command and documents inputs, process steps, and output format.

**templates/**: Output format shells. Used by `/build` as the structure for generated deliverables.

**examples/**: Gold-standard completed outputs. Used by `/build` as quality references for few-shot prompting.

---

## Page Conventions

### Frontmatter Schemas

**Source pages** (`wiki/sources/`):
```yaml
---
type: source
title: ""
author: ""
date: ""
url: ""
ingested: ""
tags: []
---
```

**Concept pages** (`wiki/concepts/`):
```yaml
---
type: concept
title: ""
created: ""
updated: ""
tags: []
related: []
---
```
Required sections: Definition, Why It Matters, How It Works, Examples, Related Concepts

**Entity pages** (`wiki/entities/`):
```yaml
---
type: entity
title: ""
entity_type: ""  # company | product | person | analyst-firm
created: ""
updated: ""
tags: []
---
```
Required sections: Overview, Key Facts, Positioning, Competitive Context, Sources

**Skill pages** (`skills/`):
```yaml
---
type: skill
title: ""
trigger: ""      # the /command or natural language trigger
created: ""
updated: ""
---
```
Required sections: Purpose, Inputs, Process, Output Format, Example Usage

**Template pages** (`templates/`):
```yaml
---
type: template
title: ""
output_type: ""  # battle-card | one-pager | messaging-framework | etc.
created: ""
updated: ""
---
```

**Example pages** (`examples/`):
```yaml
---
type: example
title: ""
demonstrates: ""  # which skill or template this exemplifies
quality: ""       # gold | silver | draft
created: ""
---
```

---

## Wikilinks

- Use Obsidian-style wikilinks: `[[page-name]]`
- All cross-references between pages must use wikilinks
- When creating or updating a page, always check for and add relevant wikilinks to existing pages
- When a new page is created, update `wiki/index.md`

---

## Slash Commands

### /ingest [source]
1. Read the source from `raw/` (or a pasted URL/text)
2. Create a source summary page in `wiki/sources/`
3. Extract entities → create or update pages in `wiki/entities/`
4. Extract concepts → create or update pages in `wiki/concepts/`
5. Add wikilinks between all new and existing pages
6. Update `wiki/index.md`
7. Append to `log.md`

### /query [question]
1. Read `wiki/hot.md` for recent context
2. Read `wiki/index.md` to find relevant pages
3. Read relevant wiki pages
4. Synthesize an answer citing specific wiki pages
5. Never answer from training data when wiki has relevant content

### /lint
1. Find orphan pages (no inbound wikilinks)
2. Find dead wikilinks (link to nonexistent pages)
3. Find pages missing required frontmatter fields
4. Find stale pages (not updated in 90+ days but referenced by recent sources)
5. Find contradictions (flag with `[!contradiction]` callout, don't silently overwrite)
6. Report findings organized by severity
7. Offer to fix each issue
8. Append results to `log.md`

### /build [skill-name] [arguments]
1. Read the skill file from `skills/`
2. Pull relevant context from `wiki/`
3. If a template exists in `templates/`, use it as the output format
4. If an example exists in `examples/`, use it as a quality reference
5. Generate the output
6. Append to `log.md`

### /status
1. Show wiki stats: total pages by type, recent ingests, last lint results
2. Show `hot.md` contents
3. Show last 5 log entries

---

## Session Management

- At the start of every session, read `hot.md` and the last 20 entries in `log.md`
- At the end of every session (or when asked), update `hot.md` with a summary of what was discussed, decided, or changed
- `hot.md` must stay under ~500 words — it is a rolling context cache, not a full history

---

## Log Format

Entries in `log.md` follow this format, reverse-chronological:

```markdown
## YYYY-MM-DD
- **ingested**: source-filename → wiki/sources/page-name.md
- **created**: wiki/concepts/page-name.md
- **updated**: wiki/entities/page-name.md (reason)
- **lint**: summary of findings
- **build**: skill-name → output description
- **session**: brief summary of session context
```

---

## Git Conventions

- Do NOT auto-commit. Git is managed via Obsidian Git plugin or manually.
- If explicitly asked to commit, use conventional commit messages:
  - `ingest: [source-name]`
  - `wiki: create [page-name]`
  - `wiki: update [page-name]`
  - `lint: fix [description]`
  - `skill: add [skill-name]`
  - `template: add [template-name]`

---

## Forking Convention

This vault is designed to be forked for company-specific use. Generic PMM knowledge lives in the standard folders. A future fork adds:

```
company/
├── wiki/
│   ├── sources/
│   ├── concepts/
│   └── entities/
├── skills/
├── templates/
└── examples/
```

Company-specific pages add `scope: company` to frontmatter. Generic pages have `scope: generic` (or omit the field — omission implies generic). `CLAUDE.md` in a fork extends — does not replace — this base schema.
