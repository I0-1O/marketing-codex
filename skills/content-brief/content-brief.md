---
type: skill
title: Content Brief
trigger: /build content-brief
created: 2026-04-10
updated: 2026-04-22
---

## Purpose

Create a structured content brief for any marketing content type. Gives writers and designers enough context to execute without back-and-forth.

**Standalone skill** — no wiki or external files required. Provide persona and messaging context directly as inputs; all guidance is embedded here.

---

## Inputs

- **Content type**: Blog post, whitepaper, ebook, webinar, case study, social campaign, email, etc.
- **Target persona**: Who this is for — job title, role, company type, what they care about
- **Topic**: What the content is about
- **Goal**: What we want the reader to do or believe after consuming it
- **Key messages** (optional but recommended): 3–5 messages from your messaging framework that this piece should reinforce; if you have a messaging doc, paste the relevant section
- **Existing messaging or positioning** (optional): paste short or long messaging for the product, or provide a positioning statement — this grounds the brief in real messaging rather than improvised claims
- **Competitors or alternatives** (optional): if competitive angle is part of the piece, name them

---

## Process

1. **Confirm the job of the content** — is this awareness (problem recognition), consideration (why this product), or decision (remove last objections)? The content type and goal should match the funnel stage.
2. **Define the audience precisely** — build on the persona input; note what this person already knows vs. what they still need to believe; what they'd search for; what objection they'd raise after reading
3. **Identify the single most important thing the reader should take away** — one sentence; if there's no clear answer, the brief isn't ready
4. **Select key messages** — 3–5 ranked by priority; pull from provided messaging doc or user input; the ranking matters: lower in the piece, not equal emphasis
5. **Draft title options** — 3 working titles varying tone (direct, curiosity, outcome-led)
6. **Build the recommended outline** — section headers with 1-line purpose descriptions; sequence matters (problem before solution)
7. **SEO** — if applicable: primary keyword (the search query this targets), 2–3 secondary keywords, search intent (informational / navigational / commercial)
8. **CTA** — what the reader does next; must match funnel stage and goal
9. Apply `template.md` in this folder as the output structure
10. *(If using the full codex: append to `log.md`)*

---

## Funnel Stage Alignment

Match content type, message focus, and CTA to the funnel stage:

| Stage | Message focus | Content types that work | CTA |
|---|---|---|---|
| Awareness | Name the problem; earn recognition | Blog posts, thought leadership, social, PR | Read more, subscribe, share |
| Consideration | Why this product, why now, why not alternatives | Case studies, webinars, comparison guides, whitepapers | Request demo, download, sign up for trial |
| Decision | Remove last objections; prove it's safe | Customer references, ROI calculators, technical briefs, battle cards | Talk to sales, start trial, sign contract |

---

## Writing Voice Rules

All copy and content direction in this brief must follow these rules:

- **Lead with the problem** — the product earns attention after the problem earns recognition
- **Use "you," not "organizations"** — forces specificity and sounds human
- **No em dashes** — split into two sentences if needed
- **One comma per sentence max** — more means split the sentence
- **Bullets: 3 ideal, 5 ceiling** — no exceptions
- **Benefits must pass "so what?" once** — direct effect is not the benefit; one level up is
- **No banned words**: Seamless, Robust, Leverage (verb), Harness, Empower, Unlock, Streamline, AI-powered, Accelerate, Next-generation, Best-in-class, World-class, Cutting-edge, Transformative, Game-changing, Holistic, Future-proof, Reimagine

---

## Output Format

Use `template.md` in this folder.

---

## Example Usage

```
/build content-brief
Content type: Blog post
Persona: Director of IT at a 1,000-employee financial services firm; responsible for compliance and infrastructure; concerned about audit exposure and vendor lock-in
Topic: Why no-code automation is replacing legacy BPM platforms
Goal: Drive awareness and top-of-funnel leads for automation category
Key messages: Manual processes create compliance risk; modern automation doesn't require IT coding; implementation time has dropped from months to days
```
