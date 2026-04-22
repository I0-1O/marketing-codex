---
type: skill
title: Analyst Briefing Prep
trigger: /build analyst-prep
created: 2026-04-10
updated: 2026-04-22
---

## Purpose

Prepare a structured briefing package for an analyst meeting — agenda, key messages, anticipated questions, supporting data points, and topics to avoid. Works standalone or alongside a messaging framework.

**Standalone skill** — no wiki or external files required. Bring what you know about the analyst; the skill will guide you on what to research and how to prepare.

---

## Inputs

**Required:**
- **Analyst firm**: e.g., Gartner, Forrester, IDC, 451 Research, GigaOm
- **Analyst name**: Specific analyst being briefed
- **Briefing topic**: What the meeting is about (product launch, category update, strategy brief, inquiry, etc.)
- **Meeting type**: Briefing (you present), inquiry (you ask), or strategy session

**Optional (significantly improves output):**
- **Analyst's known coverage area**: What they write about, their specialty (pull from firm's bio or LinkedIn)
- **Published research**: Any relevant reports, blogs, or social posts from this analyst
- **Past interactions**: Prior meeting notes, how they've evaluated your product or category before, known opinions
- **Your messaging**: Paste the relevant section of your messaging framework or positioning statement
- **What you want the analyst to do**: Put you in a report, update their view, provide feedback, introduce you to clients

---

## How to Research the Analyst

If you don't have the inputs above, here's how to find them before running this skill:

1. **Firm bio page** — most firms publish analyst coverage areas; search `[analyst name] [firm]`
2. **Published research** — search for their name on the firm's blog or research portal; note recurring themes, technology POV, and vendors they mention
3. **LinkedIn** — posts often reveal what they're currently thinking about, what events they attended, what they're skeptical of
4. **Prior meeting notes** — if your team has briefed this analyst before, review the last meeting notes and any feedback they gave
5. **Training data** — Claude has knowledge of many major analysts' published positions through its training cutoff; ask and note that it may be outdated

---

## Process

1. **Confirm meeting type and goal** — what does success look like at the end of this meeting? Analyst changes their view? Agrees to include you in a report? Provides feedback you can use?
2. **Research the analyst** — if coverage area, POV, or past research is not provided, research using the guidance above; flag what's sourced vs. inferred
3. **Identify likely probes** — based on the analyst's known coverage and the briefing topic, what questions will they almost certainly ask? What are they skeptical of in your category?
4. **Build key messages** — 3–5 messages to land, ordered by priority; pull from provided messaging or ask for it; messages should be claims the analyst can evaluate and validate, not marketing language
5. **Identify supporting data** — for each key message, what proof exists? Customer examples, metrics, market data, third-party validation?
6. **Identify what to avoid** — what topics, framings, or product angles will land poorly with this analyst or firm? Where have vendors gotten pushback from this person before?
7. **Flag knowledge gaps** — what don't you know about this analyst that would improve prep? What would change your approach if you knew it?
8. Apply `template.md` in this folder as the output structure
9. *(If using the full codex: append to `log.md`)*

---

## Analyst Meeting Dynamics

**What analysts care about:**

- **Accuracy** — they're evaluating whether your claims hold up under scrutiny; don't overstate
- **Differentiation** — they talk to every vendor; "we're better" without proof is noise
- **Market perspective** — they want to understand your view of the market, not just your product pitch
- **Customer evidence** — named customers or specific outcomes carry weight; vague "hundreds of customers" does not
- **Candor** — they appreciate honesty about limitations and gaps; it builds credibility

**What annoys analysts:**

- Marketing-voice presentations that avoid real claims
- Feature lists with no context for what problem they solve
- Ignoring their past research or known POV
- Claiming uniqueness in a crowded category without evidence
- Running over time or not leaving room for dialogue

**Briefing vs. inquiry:**

- **Briefing**: You present; analyst listens and evaluates; they may ask questions; goal is usually to influence their written research
- **Inquiry**: You ask; analyst advises; treat this as a strategic consultation, not a sales call
- **Strategy session**: Collaborative; you're seeking input on direction; be willing to share more than you'd share publicly

---

## Output Format

Use `template.md` in this folder.

---

## Example Usage

```
/build analyst-prep
Analyst firm: Forrester
Analyst: Craig Le Clair
Topic: AI-driven process automation — product strategy update
Meeting type: Briefing
Analyst POV: Le Clair covers intelligent automation; has written critically about "automation theater" where vendors claim AI use without substance; known for rigorous customer evidence requirements
Goal: Update his view on our AI capabilities ahead of the Wave evaluation
Messaging: [paste positioning statement or relevant section]
```
