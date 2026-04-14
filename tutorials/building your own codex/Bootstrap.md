I'm building a personal knowledge base for Product Marketing Management (PMM) using the LLM Wiki pattern (based on Andrej Karpathy's approach). This vault will be opened in Obsidian AND worked on through Claude Code — both pointing at this same directory.

The goal: a compounding, structured wiki focused on product and technical marketing for enterprise B2B software. This is generic PMM knowledge — not company-specific. I'll fork it later for company-specific use.

Please do the following:

## 1. Create the directory scaffold

```
marketing-codex/
├── CLAUDE.md                   # schema, conventions, slash commands for Claude Code
├── log.md                      # reverse-chronological activity log
├── .gitignore
├── raw/                        # unprocessed external source material
│   └── .gitkeep
├── articles/                   # your own writing — full text, authoritative primary source
│   └── _template.md            # frontmatter template for new articles
├── wiki/
│   ├── index.md                # master index of all wiki pages (auto-maintained)
│   ├── hot.md                  # session context cache (~500 words, updated each session)
│   ├── sources/                # processed source summaries — one page per ingested source
│   │   └── .gitkeep
│   ├── concepts/               # PMM frameworks, methodologies, patterns
│   │   └── .gitkeep
│   └── entities/               # companies, products, people, analyst firms
│       └── .gitkeep
├── skills/                     # reusable Claude Code PMM workflows (slash commands)
│   └── .gitkeep
├── templates/                  # output format templates
│   └── .gitkeep
├── examples/                   # gold-standard reference outputs for quality benchmarking
│   └── .gitkeep
└── tutorials/                  # guides for setting up and using the vault
    └── building your own codex/
        ├── Bootstrap.md        # this file — the scaffold prompt
        └── How to build your PMM Brain.md
```

## 2. Write CLAUDE.md with these sections

### Identity
- This is a PMM knowledge base for enterprise B2B software marketing.
- Voice: direct, concise, no marketing fluff. Substance over polish.

### Vault structure
Document every folder, its purpose, and what goes in it. Be specific.

### Page conventions
Define frontmatter schema for each page type:

**Source pages** (wiki/sources/):
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

**Article pages** (articles/):
```yaml
---
type: article
title: ""
author: ""
date: ""
published: false
url: ""   # fill in if/when published
tags: []
---
```

**Concept pages** (wiki/concepts/):
```yaml
---
type: concept
title: ""
created: ""
updated: ""
origin: ""   # self | external (omit if external)
tags: []
related: []
---
```
Sections: Definition, Why It Matters, How It Works, Examples, Related Concepts

**Entity pages** (wiki/entities/):
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
Sections: Overview, Key Facts, Positioning, Competitive Context, Sources

**Skill pages** (skills/):
```yaml
---
type: skill
title: ""
trigger: ""      # the /command or natural language trigger
created: ""
updated: ""
---
```
Sections: Purpose, Inputs, Process, Output Format, Example Usage

**Template pages** (templates/):
```yaml
---
type: template
title: ""
output_type: ""  # battle-card | one-pager | messaging-framework | etc.
created: ""
updated: ""
---
```

**Example pages** (examples/):
```yaml
---
type: example
title: ""
demonstrates: ""  # which skill or template this exemplifies
quality: ""       # gold | silver | draft
created: ""
---
```

### Wikilinks
- Use Obsidian-style wikilinks: `[[page-name]]`
- All cross-references between pages must use wikilinks
- When creating or updating a page, always check for and add relevant wikilinks to existing pages
- When a new page is created, update wiki/index.md

### Slash commands
Define these workflows in CLAUDE.md:

**/ingest [source]**
1. Determine source type: external (URL, PDF, third-party article) or own article (Brian's writing)
2. For own articles: move from raw/ to articles/ if needed, add frontmatter using articles/_template.md
3. Create a source summary page in wiki/sources/ (for own articles: synopsis only, full text stays in articles/)
4. Extract entities → create or update pages in wiki/entities/
5. Extract concepts → create or update pages in wiki/concepts/ (add `origin: self` for concepts from own articles)
6. Add wikilinks between all new and existing pages
7. Update wiki/index.md
8. Append to log.md

**/query [question]**
1. Read wiki/hot.md for recent context
2. Read wiki/index.md to find relevant pages
3. Read relevant wiki pages
4. Synthesize an answer citing specific wiki pages
5. Never answer from training data when wiki has relevant content

**/lint**
1. Find orphan pages (no inbound wikilinks)
2. Find dead wikilinks (link to nonexistent pages)
3. Find pages missing required frontmatter fields
4. Find stale pages (not updated in 90+ days but referenced by recent sources)
5. Find contradictions (flag with [!contradiction] callout, don't silently overwrite)
6. Report findings organized by severity
7. Offer to fix each issue
8. Append results to log.md

**/build [skill-name] [arguments]**
1. Read the skill file from skills/
2. Pull relevant context from wiki/
3. If a template exists in templates/, use it as the output format
4. If an example exists in examples/, use it as a quality reference
5. Generate the output
6. Append to log.md

**/status**
1. Show wiki stats: total pages by type, recent ingests, last lint results
2. Show hot.md contents
3. Show last 5 log entries

**/session-close**
Run the checklist in skills/session-close.md: index sync, wikilink coverage, hot.md update, log completeness, raw folder check, Bootstrap and README structural drift check.

### Session management
- At the start of every session, read hot.md and log.md (last 20 entries)
- At the end of every session (or when asked), run /session-close
- hot.md must stay under ~500 words — it's a rolling context cache, not a full history

### Log format
Entries in log.md follow this format, reverse-chronological:
```
## YYYY-MM-DD
- **ingested**: source-filename → wiki/sources/page-name.md
- **created**: wiki/concepts/page-name.md
- **updated**: wiki/entities/page-name.md (reason)
- **lint**: summary of findings
- **build**: skill-name → output description
- **session**: brief summary of session context
```

### Git conventions
- Do NOT auto-commit. Commits are handled via Obsidian Git plugin or manually.
- If explicitly asked to commit, use conventional commit messages:
  - `ingest: [source-name]`
  - `wiki: create [page-name]`
  - `wiki: update [page-name]`
  - `lint: fix [description]`
  - `skill: add [skill-name]`
  - `template: add [template-name]`
  - `article: add [title]`

### Forking convention
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
Company-specific pages add `scope: company` to frontmatter. Generic pages have `scope: generic` (or omit — omission implies generic). CLAUDE.md in a fork extends — does not replace — this base schema.

## 3. Create starter content

### wiki/index.md
Create an empty index with sections for Sources, Concepts, Entities, and Skills. Include a note that this is auto-maintained.

### wiki/hot.md
Initialize with a note that this is a session context cache, currently empty.

### log.md
Initialize with a single entry noting the vault was scaffolded.

### articles/_template.md
Create a blank article template with the article frontmatter schema pre-filled.

### skills/ — create these starter skill files

**pmm-writing-voice.md**: Voice and structure rules for all marketing copy. Banned words, structural rules (no em dashes, one comma per sentence, bullets 3–5 ceiling), benefit framing rule, editing checklist. Loaded at the start of any copy drafting or review session.

**messaging-framework.md**: Build a complete master messaging document. Inputs: product name, scope, personas, differentiators, competitive context, proof points, "why now." Output: positioning statement, ICP, per-audience value props, three-pillar architecture, objection handling, proof points. References pmm-writing-voice.

**competitive-brief.md**: Build a competitive analysis brief on a named competitor. Inputs: competitor name, product category. Process: pull from wiki/entities/ for known info, identify and flag gaps. Output: competitor overview, strengths, weaknesses, differentiation, sales talk track, knowledge gaps.

**analyst-prep.md**: Prepare a structured briefing package for an analyst meeting. Inputs: analyst firm, analyst name, briefing topic. Process: pull from wiki/entities/ for analyst and firm context. Output: agenda, key messages, anticipated questions, supporting data points, what to avoid, knowledge gaps.

**battle-card.md**: Generate a one-page sales battle card for a named competitor. Inputs: competitor name. Process: pull competitive brief and messaging framework. Output: win themes, landmines, trap questions, proof points, one-line reframe.

**content-brief.md**: Create a structured content brief for any marketing content type. Inputs: content type, target persona, topic, goal. Output: title options, audience, goal, key messages, outline, SEO considerations, CTA, related assets.

**slide-deck.md**: Build a story-driven slide deck plan. Inputs: topic, audience, goal, key messages. Output: per-slide content direction, visual guidance, speaker notes. References pmm-writing-voice.

**session-close.md**: End-of-session housekeeping checklist. Covers: skills/templates/examples index sync (compare folder counts to wiki/index.md), wikilink coverage on new pages, hot.md update, log completeness, raw folder check, Bootstrap and README structural drift check.

### templates/ — create starter templates

**messaging-framework-template.md**: Full master messaging document template. Sections: positioning statement, top-level messaging (short + long), ICP table, personas with "what they'd do instead," per-audience value props, three pillars (each with pain points, use cases, features/differentiators, value prop, outcomes, short and long messaging), objection handling, competitive framing, proof points, partner messaging.

**battle-card-template.md**: One-page battle card template.

**one-pager-template.md**: Product one-pager template.

## 4. Initialize git

Run git init in this directory. Create a .gitignore that excludes:
- `.obsidian/` (Obsidian config is local)
- `.trash/` (Obsidian trash)
- `raw/*.pdf` (large source files — keep .md and .txt sources tracked)
- `.DS_Store`
- `node_modules/`

Do NOT make an initial commit — review the scaffold first and commit manually.

## 5. After scaffolding

Show me:
- A tree of everything you created
- The contents of CLAUDE.md
- Any decisions you made that I should review
