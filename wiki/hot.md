# Hot — Session Context Cache

> Rolling context cache. Stays under ~500 words. Updated at the end of each session.
> Not a full history — just enough to orient the next session.

---

## Last Updated: 2026-04-14

### What Was Built This Session

**Competitive intelligence system — full build-out.**

**Slash commands registered** (new): Created `~/.claude/commands/` with five files — ingest, query, lint, build, status. These register the CLAUDE.md workflows as proper Claude Code slash commands with autocomplete.

**Three sources ingested:**
1. **Momentum battlecard prompt v1** (`competitor-research-battlecard-momentum`) — six-step prompt, URL-in, SWOT + objection pairs out
2. **Momentum battlecard prompt v2** (`competitive-research-battlecard-creation-momentum`) — GRACE framework (Coach K); 8-section output; adds landmines, "topics to avoid," follow-up email sequences
3. **Doherty "30-Minute Battlecard"** (`30-minute-battlecard-doherty`) — three-phase AI workflow: competitive intel extraction → buyer voice intelligence → assembly; continuous intelligence framing

**New concepts (3):** `battle-card`, `objection-handling`, `buyer-voice-intelligence`
- buyer-voice-intelligence is the most novel: mining call recordings for four categories (objection triggers, feature perception gaps, pricing intel, authentic buyer vocabulary)

**New entities (3):** `momentum` (Salesforce-acquired sales AI, prompt library), `thomas-e-doherty` (PMM author, AI-accelerated GTM), `g2` (review platform, competitive research source)

**New skill:** `competitive-profile` — deep pre-battlecard research artifact; resolves or prompts for master messaging doc; 11-section output; sits between messaging-framework and competitive-brief in the artifact chain

**Updated skills (2):**
- `competitive-brief` — added Step 0 (check for profile first), buyer voice sourcing priority, claim validation, template reference
- `battle-card` — added buyer voice sourcing step, explicit "topics to avoid" step, trigger-based update cadence

**New templates (2):** `competitive-brief-template`, `competitive-profile-template` (battle-card-template updated with Topics to Avoid section)

**New tutorial:** `competitive-intel-playbook` — four-artifact system (messaging doc → profile → brief → battle card), build chain rationale, research source priority table, trigger-based cadence, Claude Code scheduling examples

### Current Wiki State

**11 concepts** (6 origin: self) | **15 entities** | **8 sources** | **4 articles**

**Skills (10):** messaging-framework, competitive-profile, competitive-brief, battle-card, launch-artifact, slide-deck, pmm-writing-voice, content-brief, analyst-prep, session-close

**Templates (6):** competitive-profile, competitive-brief, battle-card, messaging-framework, launch-artifact, one-pager

### Key Patterns Established This Session

- Artifact chain is now explicit and enforced in skills: messaging-doc → competitive-profile → competitive-brief → battle-card
- "Topics to avoid" is a named section in both the battle-card skill and template — what not to say against a specific competitor
- Trigger-based cadence over fixed quarterly for competitive updates (competitive-intel-playbook tutorial documents the trigger table)
- Buyer voice (call recordings + G2) is the highest-signal competitive source; always prioritized over training data in skill process steps

### Next Session Priorities

- Build a gold-standard example output for competitive-profile
- Analyst-prep and content-brief skills have no templates yet — build them
- Run `/lint` for a full vault health check
- Consider ingesting more competitive intel methodology sources
