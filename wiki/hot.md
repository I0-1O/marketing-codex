# Hot — Session Context Cache

> Rolling context cache. Stays under ~500 words. Updated at the end of each session.
> Not a full history — just enough to orient the next session.

---

## Last Updated: 2026-04-27

### What Was Built This Session

**Single ingest: Hattie the PMM, "How To Get The Most Out of Claude for Product Marketing Managers" (LinkedIn post + infographic, 2026-04)**

**New pages (3):**
- `wiki/sources/hattie-pmm-claude-power-users.md` — source summary with full Claude tool reference table (10 tools × PMM use case + 3 advanced hacks)
- `wiki/entities/hattie-the-pmm.md` — product marketing coach; Visible & Valued PMM Challenge; productmarketers.com; ~47K LinkedIn followers
- `wiki/concepts/pmm-ai-workflow-architecture.md` — system-level Claude setup for PMMs; four leverage layers; the gap between casual and power users is system architecture, not prompting skill

**Updated (1):**
- `wiki/concepts/ai-agent-skills-for-marketing.md` — added related link to pmm-ai-workflow-architecture (Claude Skills layer ≈ markdown skill files pattern for coding agents)

**Also fixed:**
- `wiki/index.md` — added two previously unindexed tutorials: "How to Build Your PMM Brain" and "Bootstrap"

---

### Core Argument (Hattie)

"Prompting is the weakest way to use Claude." The leverage gap is system architecture:
1. **Projects** — context persistence; upload ICP/messaging/competitive intel once
2. **Skills** — standing briefs; writing style, brief format, battle card structure baked in
3. **Cowork** — local file access; reads Word, PDF, Excel without uploading
4. **Connectors** — tool integrations; Slack, Drive, Notion, 50+

Advanced hacks: stakeholder map briefing, pressure-test with skeptical Sales rep persona, Global Instructions for role context.

**Connection to existing concepts:**
- Claude Skills layer ≈ `ai-agent-skills-for-marketing` (markdown skill files for coding agents — same system-thinking, different execution layer)
- Cowork + Connectors are the natural delivery mechanism for `buyer-voice-intelligence` (call recordings, win/loss data)

---

### Current Wiki State

**13 concepts** (6 origin: self) | **17 entities** | **10 sources** | **4 articles**

**Skills (10):** messaging-framework, competitive-profile, competitive-brief, battle-card, launch-artifact, slide-deck, pmm-writing-voice, content-brief, analyst-prep, session-close

**Templates:** 1 root (one-pager) + 7 colocated in skill subfolders

---

### Key Patterns Established (Cumulative)

- Artifact chain enforced: messaging-doc → competitive-profile → competitive-brief → battle-card
- "Topics to avoid" is a named section in battle-card skill and template
- Buyer voice (call recordings + G2) is highest-signal competitive source
- AI voice tells: 7 catalogued patterns; antithesis construction is the newest addition (external source)
- `origin: self` on concepts derived from Brian's own writing; external sources don't inherit this flag
- PMM AI leverage hierarchy: system architecture (Projects/Skills/Cowork/Connectors) > prompting

---

### Next Session Priorities

- Build gold-standard example output for `competitive-profile`
- Analyst-prep and content-brief skills have templates but no example outputs
- Run `/lint` for a full vault health check
- Consider ingesting more AI-voice / copywriting methodology sources (Angus has prior issues worth mining)
