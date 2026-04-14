# Hot — Session Context Cache

> Rolling context cache. Stays under ~500 words. Updated at the end of each session.
> Not a full history — just enough to orient the next session.

---

## Last Updated: 2026-04-13

### What Was Built This Session

**Skills ported and rebuilt from an external interview project:**

Two skills added/upgraded. Both were genericized (interview-specific references removed) and reformatted to the vault's skill schema. Writing voice is a constraint file loaded at the start of copy sessions; messaging framework is the full build workflow for a master messaging doc.

1. **`skills/pmm-writing-voice.md`** (new) — Voice and structure rules for marketing copy. Em dash rule, comma chain rule, banned word list, benefit framing, editing checklist. Trimmed for modern LLMs (removed redundant before/after examples that live in concept pages). References [[ai-voice-tells-in-marketing-copy]], [[marketing-voice-and-pov]], [[benefit-ladder]].

2. **`skills/messaging-framework.md`** (major rewrite) — Complete master messaging document builder. Merged the skill file and a separate process guide into one. Covers: inputs (with "why now" as required), positioning statement, ICP + personas, per-audience value props, three-pillar architecture, objection handling, competitive framing, proof points. Links [[pmm-writing-voice]] as a load instruction.

3. **`templates/messaging-framework-template.md`** (major upgrade) — Template now matches the skill's full scope: ICP table, personas with "what they'd do instead" column, per-audience VP section, full pain→use cases→features→VP→outcomes pillar sequence, sourced proof points, optional partner messaging.

### Current Wiki State

**8 concepts** (6 origin: self), **13 entities**, **5 sources**, **4 articles**

**Skills inventory (7):** slide-deck, pmm-writing-voice, messaging-framework, competitive-brief, analyst-prep, battle-card, content-brief — all indexed in `wiki/index.md`

### Key Patterns Established This Session

- `[[pmm-writing-voice]]` is now the standard load instruction referenced in other skills — future skills that produce copy should reference it the same way
- "Why now" is a required input in the messaging framework — forces urgency thinking at the architecture level; if the buyer could wait six months and nothing changes, the messaging has a hole
- Competitive framing rule: attack specific trade-offs, not categories — especially important if the portfolio includes both sides of a comparison

### Next Session Priorities (anticipated)

- Continue porting remaining skills from the external project (battle card, competitive brief, content brief — check what's already in `skills/` vs. what needs upgrading)
- Ingest any new articles or external sources
- Consider building an examples page for the messaging framework (gold-standard completed output)
