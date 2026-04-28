# Wiki Index

> Auto-maintained. Updated by `/ingest` when new pages are created.

---

## Sources

- [[marketingskills-coreyhaines31]] — Marketing Skills for AI Agents (Corey Haines, GitHub repo, 40+ markdown skills for AI coding agents)
- [[writing-for-humans-killing-ai-voice]] — Brian Rieb article: AI voice tells, editing rules, and brand voice via exclusion (full text in articles/)
- [[benefit-ladder-copy-lands-one-tier-too-low]] — Brian Rieb article: Feature → Direct Effect → Business Outcome; the most common PMM copy failure (full text in articles/)
- [[slides-dont-talk]] — Brian Rieb article: slides support the story, presenter carries it; leave-behind fallacy; speaker notes structure (full text in articles/)
- [[technical-thinkers-guide-to-messaging]] — Brian Rieb article: empathy + structure; master messaging doc architecture; PM-PMM collaboration (full text in articles/)
- [[competitor-research-battlecard-momentum]] — Momentum AI prompt: six-step battlecard generator; URL-in, SWOT + objection pairs out; sales-use artifact
- [[competitive-research-battlecard-creation-momentum]] — Momentum AI prompt v2 (GRACE framework, Coach K): 8-section output; adds landmines, topics to avoid, follow-up email sequences
- [[30-minute-battlecard-doherty]] — Doherty (2026): three-phase AI workflow; competitive intel extraction, buyer voice, assembly; continuous intelligence framing
- [[stop-turning-antithesis-angus]] — Angus (2026): "It's not X, it's Y" as AI tell and positioning shortcut; antithesis pattern mechanics and fix
- [[hattie-pmm-claude-power-users]] — Hattie the PMM (2026): Claude tool reference table for PMMs; 10 tools mapped to use cases; core thesis: system setup > prompting

---

## Skills

All skills are standalone — no wiki dependency required. Skills with templates use the subfolder pattern (`skills/[name]/[name].md` + `skills/[name]/template.md`).

- [[launch-artifact]] — Build a complete GTM campaign brief: objective, audience sequencing, channel strategy by funnel stage (ORB), messaging shift, content plan, timeline, and success metrics
- [[slide-deck]] — Build a story-driven slide deck plan with per-slide content, visual direction, and speaker notes
- [[pmm-writing-voice]] — Voice constraints and editing checklist for marketing copy; load before any drafting or review session
- [[messaging-framework]] — Build a complete master messaging document: positioning, ICP, personas, pillars, value props, objection handling, proof points
- [[competitive-profile]] — Deep pre-battlecard research artifact; 11-section output; confidence-labeled sourcing discipline
- [[competitive-brief]] — Build a 2–3 page competitive brief on a named competitor; buyer voice guidance embedded; flags research gaps
- [[battle-card]] — Generate a one-page sales battle card for a named competitor; buyer voice guidance embedded; designed for use in live deals
- [[analyst-prep]] — Prepare a structured briefing package for an analyst meeting: agenda, key messages, anticipated questions, what to avoid
- [[content-brief]] — Create a structured content brief for any marketing content type; funnel stage alignment embedded
- [[session-close]] — End-of-session checklist: index sync, wikilinks, hot.md, log, raw folder *(vault-only skill)*

---

## Templates

Templates are colocated with their skill in `skills/[name]/template.md`. Only templates without a paired skill live in root `templates/`.

**Root templates/ (no paired skill yet):**
- [[one-pager-template]] — Product one-pager format

**Colocated in skill subfolders:**
- `skills/messaging-framework/template.md` — Full master messaging document: ICP, personas, pillars, value props, objection handling, proof points
- `skills/competitive-profile/template.md` — 11-section deep research artifact: quick verdict through research gaps
- `skills/competitive-brief/template.md` — 2–3 page competitive brief: overview, positioning, strengths, weaknesses (sourced), differentiation, talk track, gaps
- `skills/battle-card/template.md` — One-page battle card: win themes, landmines, trap questions, topics to avoid, proof points, one-liner, know your enemy
- `skills/launch-artifact/template.md` — GTM campaign brief: objective, ICP, positioning, channel matrix, content plan, timeline, metrics
- `skills/content-brief/template.md` — Content brief: titles, audience, goal, key messages, outline, SEO, CTA
- `skills/analyst-prep/template.md` — Analyst briefing prep: agenda, key messages, anticipated questions, what to avoid, knowledge gaps

---

## Tutorials

- [[How to build your PMM Brain]] — Full setup walkthrough: Obsidian, Git, Claude Code, first ingest; ~30 minutes start to finish
- [[Bootstrap]] — Original scaffold prompt used to generate this vault structure; reference for building a fork from scratch
- [[competitive-intel-playbook]] — Four-artifact competitive system: what each doc is for, build order, update cadences, Claude Code scheduling
- [[stop-building-ugly-slides]] — Primer: slide kit with PPTX deck, cheat sheet, and AI skill; the four offenses and core rules
  - [[cheat-sheet]] — Quick-reference rules: bullets, one concept per slide, speaker notes format

---

## Concepts

- [[battle-card]] — One-page sales reference for winning deals against a named competitor; distinct from competitive brief
- [[objection-handling]] — Anticipating and structuring rebuttals to buyer resistance; upstream of battle cards
- [[buyer-voice-intelligence]] — Mining sales call recordings for authentic buyer language; closes the gap between PMM copy and buyer vocabulary
- [[ai-agent-skills-for-marketing]] — Pattern for packaging marketing workflows as markdown skill files for AI coding agents
- [[ai-voice-tells-in-marketing-copy]] — Seven structural patterns that signal AI-generated copy; editing checklist (origin: Brian Rieb + Angus)
- [[marketing-voice-and-pov]] — Brand voice comes from exclusion; copy requires a position; AI is drafting tool not finishing tool (origin: Brian Rieb)
- [[benefit-ladder]] — Three-tier framework: Feature → Direct Effect → Business Outcome; "so what?" test applied once (origin: Brian Rieb)
- [[presentation-as-story]] — Slides support, presenter carries; see-it/hear-it test; speaker notes structure; build-backwards method (origin: Brian Rieb)
- [[leave-behind-fallacy]] — Why decks became documents and why that constraint is now obsolete (origin: Brian Rieb)
- [[master-messaging-document]] — Three-pillar architecture; problem-named pillars; pain-first internal sequence; forest-and-trees diagnostic (origin: Brian Rieb)
- [[problem-first-messaging]] — Empathy as discipline; customer voice vs. product voice; sitting in the problem before solving (origin: Brian Rieb)
- [[antithesis-positioning-pattern]] — "It's not X, it's Y" rhetorical construction; AI tell and positioning shortcut; negation vs. category clarity
- [[pmm-ai-workflow-architecture]] — System-level Claude setup for PMMs; four leverage layers: Projects, Skills, Cowork, Connectors; power users build systems, not prompts

---

## Tools

Utility scripts for preprocessing content before ingestion. Not Claude Code skills — run standalone from the terminal.

- `tools/eml2md/` — Convert `.eml` email files to clean Markdown with YAML frontmatter; strips layout tables; Obsidian-compatible output

---

## Entities

### People
- [[corey-haines]] — Marketer, creator of marketingskills repo, runs Conversion Factory and Swipe Files
- [[brian-rieb]] — Principal PMM, vault owner, author; enterprise B2B; technical/PM background
- [[april-dunford]] — Positioning consultant, author of *Obviously Awesome*; differentiated value framework
- [[clayton-christensen]] — Innovation theorist; Jobs to Be Done; customers hire products to make progress
- [[matthew-dixon-brent-adamson]] — Authors of *The Challenger Sale*; top reps lead with business outcomes not features
- [[garr-reynolds]] — Author of *Presentation Zen*; coined "slideument"; analog planning
- [[edward-tufte]] — *Cognitive Style of PowerPoint*; Columbia shuttle example; bullet hierarchy degrades analysis
- [[nancy-duarte]] — *Resonate*; what-is/what-could-be oscillation; audience as hero, presenter as mentor
- [[barbara-minto]] — Pyramid Principle; use it to think, not to present

### Companies & Products
- [[mailchimp]] — Email marketing platform; gold-standard open-source brand voice / style guide
- [[37signals]] — Basecamp/HEY; founder-led combative brand voice; DHH + Jason Fried write under own names
- [[slack]] — Positioning case study: "email killer" (direct effect) vs. faster decisions + searchable knowledge (business outcome)
- [[momentum]] — AI-powered Salesforce-native sales platform; acquired by Salesforce; prompt library at momentum.io/prompts
- [[thomas-e-doherty]] — PMM author; "The AI-Accelerated GTM Playbook"; three-phase battlecard methodology
- [[g2]] — B2B software review platform; primary source for buyer voice and competitive intelligence research
- [[jeff-angus]] — Author, *Marketing That Matters* newsletter; copywriting craft, AI-generated copy patterns
- [[hattie-the-pmm]] — Product marketing coach; Visible & Valued PMM Challenge; productmarketers.com; Claude AI workflows for PMMs
