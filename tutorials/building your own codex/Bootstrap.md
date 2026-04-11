I'm building a personal knowledge base for Product Marketing Management (PMM) using the LLM Wiki pattern (based on Andrej Karpathy's approach). This vault will be opened in Obsidian AND worked on through Claude Code — both pointing at this same directory.

The goal: a compounding, structured wiki focused on product and technical marketing for enterprise B2B software. This is generic PMM knowledge — not company-specific. I'll fork it later for company-specific use.

Please do the following:

## 1. Create the directory scaffold

pmm-brain/
├── CLAUDE.md
├── log.md
├── .gitignore
├── raw/                        # unprocessed source material
│   └── .gitkeep
├── wiki/
│   ├── index.md                # master index of all wiki pages
│   ├── hot.md                  # session context cache (~500 words, updated each session)
│   ├── sources/                # processed source summaries
│   │   └── .gitkeep
│   ├── concepts/               # PMM frameworks, methodologies, patterns
│   │   └── .gitkeep
│   └── entities/               # companies, products, analysts, competitors
│       └── .gitkeep
├── skills/                     # reusable Claude Code PMM workflows
│   └── .gitkeep
├── templates/                  # output templates (battle cards, one-pagers, etc.)
│   └── .gitkeep
└── examples/                   # gold-standard reference outputs for few-shot prompting
    └── .gitkeep

## 2. Write CLAUDE.md with these sections

### Identity
- This is a PMM knowledge base for enterprise B2B software marketing.
- Voice: direct, concise, no marketing fluff. Substance over polish.

### Vault structure
Document every folder, its purpose, and what goes in it. Be specific.

### Page conventions
Define frontmatter schema for each page type:

**Source pages** (wiki/sources/):
---
type: source
title: ""
author: ""
date: ""
url: ""
ingested: ""
tags: []
---

**Concept pages** (wiki/concepts/):
---
type: concept
title: ""
created: ""
updated: ""
tags: []
related: []
---
Sections: Definition, Why It Matters, How It Works, Examples, Related Concepts

**Entity pages** (wiki/entities/):
---
type: entity
title: ""
entity_type: ""  # company | product | person | analyst-firm
created: ""
updated: ""
tags: []
---
Sections: Overview, Key Facts, Positioning, Competitive Context, Sources

**Skill pages** (skills/):
---
type: skill
title: ""
trigger: ""      # the /command or natural language trigger
created: ""
updated: ""
---
Sections: Purpose, Inputs, Process, Output Format, Example Usage

**Template pages** (templates/):
---
type: template
title: ""
output_type: ""  # battle-card | one-pager | messaging-framework | etc.
created: ""
updated: ""
---

**Example pages** (examples/):
---
type: example
title: ""
demonstrates: ""  # which skill or template this exemplifies
quality: ""       # gold | silver | draft
created: ""
---

### Wikilinks
- Use Obsidian-style wikilinks: [[page-name]]
- All cross-references between pages must use wikilinks
- When creating or updating a page, always check for and add relevant wikilinks to existing pages
- When a new page is created, update the index

### Slash commands
Define these workflows in CLAUDE.md:

**/ingest [source]**
1. Read the source from raw/ (or a pasted URL/text)
2. Create a source summary page in wiki/sources/
3. Extract entities → create or update pages in wiki/entities/
4. Extract concepts → create or update pages in wiki/concepts/
5. Add wikilinks between all new and existing pages
6. Update wiki/index.md
7. Append to log.md

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

### Session management
- At the start of every session, read hot.md and log.md (last 20 entries)
- At the end of every session (or when asked), update hot.md with a summary of what was discussed, decided, or changed
- hot.md should stay under ~500 words — it's a rolling context cache, not a full history

### Log format
Entries in log.md follow this format, reverse-chronological:
## YYYY-MM-DD
- **ingested**: source-filename → wiki/sources/page-name.md
- **created**: wiki/concepts/page-name.md
- **updated**: wiki/entities/page-name.md (reason)
- **lint**: summary of findings
- **build**: skill-name → output description
- **session**: brief summary of session context

### Git conventions
- Do NOT auto-commit. I'll handle commits via Obsidian Git plugin or manually.
- If I explicitly ask you to commit, use conventional commit messages:
  - ingest: [source-name]
  - wiki: create [page-name]
  - wiki: update [page-name]
  - lint: fix [description]
  - skill: add [skill-name]
  - template: add [template-name]

### Forking convention
This vault is designed to be forked for company-specific use. Generic PMM knowledge lives in the standard folders. A future fork will add:
company/
├── wiki/
│   ├── sources/
│   ├── concepts/
│   └── entities/
├── skills/
├── templates/
└── examples/

Company-specific pages use the same frontmatter schemas but add scope: company to frontmatter. Generic pages have scope: generic (or no scope field, which implies generic). CLAUDE.md in the fork extends — not replaces — the base schema.

## 3. Create starter content

### wiki/index.md
Create an empty index with sections for Sources, Concepts, and Entities. Include a note that this is auto-maintained.

### wiki/hot.md
Initialize with a note that this is a session context cache, currently empty.

### log.md
Initialize with a single entry noting the vault was scaffolded.

### skills/ — create these starter skill files

**messaging-framework.md**: Skill for building a messaging framework. Inputs: product name, target persona, key differentiators, competitive context. Output: positioning statement, value pillars (3), proof points per pillar, key objections + responses.

**competitive-brief.md**: Skill for building a competitive analysis brief. Inputs: competitor name, product category. Process: pull from wiki/entities/ for known info, identify gaps. Output: competitor overview, strengths, weaknesses, our differentiation, talk track for sales.

**analyst-prep.md**: Skill for preparing an analyst briefing. Inputs: analyst firm, analyst name, briefing topic. Process: pull from wiki/entities/ for analyst/firm context. Output: briefing agenda, key messages, anticipated questions, supporting data points.

**battle-card.md**: Skill for building a sales battle card. Inputs: competitor name. Process: pull competitive brief + messaging framework. Output: one-page battle card with win themes, landmines, trap questions, proof points.

**content-brief.md**: Skill for creating a content brief. Inputs: content type, target persona, topic, goal. Output: title options, outline, key messages to hit, SEO considerations, CTA.

### templates/ — create starter templates

**battle-card-template.md**: Structured template for a one-page battle card.
**one-pager-template.md**: Structured template for a product one-pager.
**messaging-framework-template.md**: Structured template for a messaging framework document.

## 4. Initialize git

Run git init in this directory. Create a .gitignore that excludes:
- .obsidian/ (Obsidian config is local)
- .trash/ (Obsidian trash)
- raw/*.pdf (large source files — keep .md and .txt sources tracked)
- .DS_Store
- node_modules/

Do NOT make an initial commit — I'll review the scaffold first and commit manually.

## 5. After scaffolding

Show me:
- A tree of everything you created
- The contents of CLAUDE.md
- Any decisions you made that I should review