---
type: skill
title: "PMM Writing Voice"
trigger: /writing-voice | load before any copy drafting or review session
created: 2026-04-13
updated: 2026-04-13
---

## Purpose

Load this as context before drafting or reviewing any marketing copy. These are constraints, not preferences. They define what the voice sounds like, how sentences are built, and how benefits are framed.

**Standalone skill** — no external files or wiki required. All rules are embedded here.

---

## Voice Rules

**Direct. Specific. Confident without arrogance.**
Read the sentence out loud. If you'd say it to a sharp colleague, it's probably right. If it sounds like a press release, rewrite it.

**Use "you," not "organizations."**
Second person forces specificity. "Your team can..." requires a claim. "Organizations can leverage..." enables vagueness.

**Lead with the problem.**
The product earns attention only after the problem earns recognition. State the pain before the solution.

---

## Structure Rules

**No em dashes.**
Em dashes are a structural tell for unedited AI copy. If a sentence needs one to work, it needs to be two sentences.

> Wrong: K2 handles complex workflows — including exception routing — without custom code.
> Right: K2 handles complex workflows without custom code. That includes exception routing and escalation logic.

**One comma per sentence, or split it.**
If a sentence has more than one comma, break it up. Two short sentences beat one comma chain every time.

**Bullets: 3 ideal, 5 ceiling.**
No exceptions. Six items means cutting one or finding two organizing principles.

**One idea per paragraph.**
Two points = two paragraphs.

**Positive framing.**
Make the affirmative case. Don't lead with what competitors can't do.

> Wrong: Unlike cloud-only platforms that lock you into their infrastructure...
> Right: K2 runs where your data lives. Your infrastructure, your rules.

---

## Benefit Framing

**Climb the benefit ladder. Stop one tier up.**

The benefit ladder has three tiers:

| Tier | What it is | Example |
|---|---|---|
| Feature | What the product does | "Drag-and-drop workflow builder" |
| Direct effect | The immediate result of using it | "Non-technical users can build workflows without IT" |
| Business outcome | What that result makes possible | "IT backlog shrinks; business teams ship faster" |

The feature is not the benefit. The direct effect is rarely the benefit either. Apply "so what?" once — that lands you at the business outcome. Apply it twice and you're in platitude territory ("achieve competitive advantage," "drive business growth").

**One level up is the sweet spot. Two levels up is noise.**

---

## AI Voice Tells

These structural patterns signal AI-generated copy before you even read for content. When you see them, the copy needs a rewrite pass — not just a word swap.

- **Em dashes used as connectors** — AI uses them to join two thoughts that should be two sentences.
- **Hedging openers** — "It's worth noting," "Ultimately," "In other words," "Of course." Delete and start with the actual claim.
- **Over-parallel structure** — Every bullet the same length. Every sentence the same rhythm. Real writing varies.
- **Ladder-stacking** — Multiple benefit claims stacked in a single sentence without evidence for any of them.
- **Vague amplifiers** — "Incredibly," "highly," "truly," "incredibly powerful." They add no information.
- **Passive problem framing** — "Many organizations face challenges with..." A person faces the challenge. Name them.

Brand voice is defined as much by what you exclude as what you include. A distinctive voice makes choices; AI copy tries to include everything and offend no one.

---

## Banned Words

If you reach for one of these, ask what it actually means and write that instead.

- Seamless
- Robust
- Leverage (as a verb)
- Harness / Empower / Unlock / Streamline
- AI-powered
- Accelerate (as a benefit claim)
- Next-generation / Best-in-class / World-class / Cutting-edge
- Transformative / Game-changing / Holistic
- Future-proof (as a standalone claim)
- Reimagine

---

## Editing Checklist

Run this against any draft before it ships.

- [ ] Em dashes → rewrite as two sentences
- [ ] Sentences with 2+ commas → split them
- [ ] Buzzwords → replace with specific language or cut
- [ ] Hedging openers ("It's worth noting...", "Ultimately...", "In other words...") → delete, start with the actual claim
- [ ] Benefits stated as features or direct effects → apply "so what?" once
- [ ] Problem introduced after the solution → reverse the order
- [ ] Over-parallel structure (every bullet the same length, every section the same shape) → vary rhythm deliberately

---

## How to Use

**Before drafting:**
```
Load skills/pmm-writing-voice.md. Apply all rules to copy in this session.
```

**As a review pass:**
```
Review this copy against skills/pmm-writing-voice.md. Flag each violation with the rule it breaks and a suggested fix.
```
