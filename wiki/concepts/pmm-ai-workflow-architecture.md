---
type: concept
title: "PMM AI Workflow Architecture"
created: "2026-04-27"
updated: "2026-04-27"
origin: external
tags: [ai-tools, claude, workflows, productivity, pmm, systems-thinking]
related: [ai-agent-skills-for-marketing, buyer-voice-intelligence]
---

# PMM AI Workflow Architecture

## Definition

The system-level configuration that separates AI power users from casual users — not prompting sophistication. For PMMs using Claude specifically, this means stacking four layers: context persistence (Projects), standing briefs (Skills), local file access (Cowork), and tool integrations (Connectors). Each layer compounds the leverage of the one below it.

Coined in practice by [[hattie-the-pmm]]: "Most PMMs are still just chatting with Claude. The power users are building systems with it."

## Why It Matters

Prompting alone has a ceiling. A better prompt gets a better single response. A better system gets better responses across every session, every task, every user — without re-briefing. The gap between casual and power users isn't effort; it's knowledge of which levers exist and in what order to pull them.

For enterprise B2B PMMs, this matters especially because: (a) context is complex (ICP, personas, messaging pillars, competitive intel), (b) tasks are recurring (battle cards, one-pagers, positioning reviews), and (c) stakeholder pressure to show AI ROI is real.

## How It Works

**Layer 1 — Context persistence (Projects)**
Upload once: messaging framework, ICP, personas, competitive intel. Every session in that project already knows your product. No re-briefing. One project per product line or launch.

**Layer 2 — Standing briefs (Skills)**
Define your writing style, brief format, or battle card structure in a reusable file Claude loads automatically. Output standards are consistent without instructions in every prompt. This is the Claude equivalent of the markdown skill files pattern used in [[ai-agent-skills-for-marketing]].

**Layer 3 — Local file access (Cowork)**
Point at folders of call recordings, analyst reports, win/loss data. Claude reads actual files — Word, PDF, Excel — and creates documents from what it finds. No uploading, no copy-pasting.

**Layer 4 — Tool integrations (Connectors)**
Link Slack, Google Drive, Notion, and 50+ other tools. Claude can search Drive, pull Slack threads about feature requests, or reference a Notion roadmap mid-task — without the user bridging data manually.

## PMM Use Cases by Tool

| Tool | Best PMM Use |
|---|---|
| Claude Chat | Positioning drafts, stakeholder prep, messaging stress-test. Use Opus 4.6 + Extended Thinking for strategy. |
| Claude Research | Competitive landscape, analyst positioning, category narrative. Use when citation matters more than speed. |
| Claude Charts | Positioning maps, funnel visuals, 2×2s, category comparison charts — without Slides. |
| Claude Excel | Survey data cleanup, pipeline influence models, formula explanation for Sales/Finance. |
| Claude Code | Product usage CSV analysis, cohort breakdowns, feature adoption, pipeline influence reports. |

## Advanced Hacks

1. **Stakeholder map briefing**: Before any strategy task, brief Claude on who the audience is, what they care about, and how they process information.
2. **Pressure-test persona**: End any positioning prompt with "Now play a sceptical Sales rep who thinks PMM is too fluffy. What's their first objection?"
3. **Global Instructions**: Settings > Profile. Write product category, ICP, tone of voice. Loads before every conversation — a permanent brief.

## Examples

- [[hattie-pmm-claude-power-users]] — full Claude tool reference table for PMMs

## Related Concepts

- [[ai-agent-skills-for-marketing]] — adjacent pattern: packaging marketing workflows as markdown skill files for AI coding agents (Claude Code, Cursor); same system-thinking, different execution layer
- [[buyer-voice-intelligence]] — Cowork + Connectors are the natural delivery mechanism for win/loss and call recording analysis
