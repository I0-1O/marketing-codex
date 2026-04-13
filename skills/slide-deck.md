---
type: skill
title: "Slide Deck Builder"
trigger: "/build slide-deck [topic] [audience] [goal]"
created: "2026-04-13"
updated: "2026-04-13"
tags: [presentations, slides, storytelling, speaker-notes]
related: ["[[slides-dont-talk]]", "[[presentation-as-story]]"]
---

# Slide Deck Builder

## Purpose

Build a structured, story-driven slide deck plan. Output describes each slide's content, visual direction, and speaker notes. Does not produce actual slide files unless explicitly asked — describes what goes on each slide and why.

Grounded in the principle that **slides enhance the presenter; they don't replace them.** The speaker carries the story. The slides carry the emphasis.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| Topic / title | Yes | What the deck is about |
| Audience | Yes | Who it's for and their context |
| Goal | Yes | What the audience should think, feel, or do after |
| Length / time | No | Default: 30–40 minutes |
| Tone | No | Default: direct, conversational |
| Existing content | No | Paste in raw content, an outline, or notes to build from |

---

## Process

1. Clarify inputs if topic, audience, or goal are underspecified
2. Draft the narrative arc before touching slide structure — identify the story shape (problem → possibility, current state → better future, etc.)
3. Determine slide count based on time target and pacing rules below
4. Build each slide using the output format, applying content rules throughout
5. Populate speaker notes fully — they carry the full presentation, not the slide

---

## Deck Structure Principles

### Pacing and Length
- Default target: **30–40 minutes** of presentation time unless specified otherwise
- Aim for roughly **2–5 minutes per slide** on average
- A slide that would take more than **10–15 minutes** to cover has too many concepts — break it up
- It is fine to have many simple slides rather than fewer complex ones

### Slide Complexity vs. Slide Count
- **Simple slides = more slides allowed.** A single stat or phrase per slide is fine if the story calls for it.
- **Complex slides = fewer slides.** If a slide has an architecture diagram or a detailed comparison, it should stand largely alone.
- Avoid putting too many heavy slides back to back — vary the visual weight

---

## Slide Content Rules

### The Core Principle
What goes on the slide and what you say are two different things. The speaker notes carry the full narrative — the setup, the explanation, the context. The slide carries the emphasis.

Before adding any text to a slide, ask:
- Is this something the audience needs to *see*, or something the presenter needs to *say*?
- If someone read this slide without a presenter, would it fully explain itself? If yes, you've written speaker notes onto the slide.
- Would the audience stop listening and start reading? If yes, cut it.

### What Belongs on the Slide
- Short labels and titles that anchor what the speaker is talking about (e.g., "Regulatory & Compliance" — not a sentence explaining what that means)
- Stats and data points that land harder visually than spoken — large format, single number
- A key phrase or position statement that you *want* the audience to read and absorb simultaneously while hearing it — used intentionally, not as a habit
- Outcomes or claims that benefit from visual reinforcement while being spoken aloud

### What Belongs in Speaker Notes
- The explanation of what's on the slide
- Context, background, and supporting data
- The "so what" behind every bullet or card
- Anything that reads like a complete sentence describing or explaining a concept

### Sentences on Slides — When They're Allowed
A sentence can appear on a slide when it's doing something a label or bullet can't — landing a position statement, closing an argument, or carrying rhetorical weight that benefits from being read *and* heard at the same time.

**The test:** If you removed the sentence from the slide and just spoke it, would the slide still work? If yes, it belongs in the notes. If the slide would lose something meaningful — a punch, a contrast, a claim — it can stay.

**Sentences that earn their place:**
- *"We didn't pivot to meet this moment. We were already here."* — closing statement meant to be read and heard simultaneously
- *"[Product] is the orchestration infrastructure. You choose the AI."* — position statement as a visual anchor for the whole slide's argument

**Sentences that don't:**
- *"Some organizations operate under mandates that restrict where data can be processed or stored."* — this is what you say, not what you show
- *"High-volume processes can make consumption-based cloud pricing unpredictable."* — explanation; belongs in notes

### Text
- **Bullet lists:** 3 items is ideal, 5 is the maximum. No exceptions.
- Each bullet is a label or short phrase — the speaker provides the meaning. Never write a bullet that is itself a complete explanation.
- Single-concept slides (one phrase, one stat) are high-impact when used selectively. Don't repeat the pattern slide after slide or it loses effect.
- Not every slide needs text or bullets. Sometimes a visual does the work entirely.

### Headlines
- Not every slide needs a headline, but when you use one it should be short, active, and state the point — not just label the topic
- Bad: "Integration" | Good: "Connect to Any System Without Code"
- If in doubt, shorter wins

---

## Visual Direction

### Graphics and Diagrams
- Prefer **simple graphics**: Venn diagrams, two boxes with an arrow, a single flow with 3–4 steps
- Avoid complex diagrams unless the slide's entire purpose is to explain that diagram
- Suggest a specific diagram type when relevant (e.g., "a simple 3-step flow" or "a Venn diagram showing overlap between X and Y")

### Icons
- Use **icons alongside labels** when practical — one icon per item helps visually-oriented audiences retain information
- Icons should complement labels, not substitute for explanation (explanation lives in notes)
- Keep icon style consistent throughout the deck (outline, filled, etc.)

### Photography
- Stock photography is acceptable but should be **used sparingly**
- One strong image per section or as a mood-setter is fine; multiple photo-heavy slides in a row is distracting
- Prefer photos that feel authentic over generic stock poses

### Statistics and Pull Quotes
- A **single large-format statistic** paired with a short framing phrase is a strong visual device
- Use these to punctuate a key claim — not as filler between content slides
- Format: short setup phrase + large stat or quote, nothing else on the slide

---

## Speaker Notes Guidelines

Speaker notes carry the full presentation — everything the audience hears lives here, not on the slide. Every set of notes contains three sections:

### On This Slide
Brief description of what's on the slide or the higher concept behind it.
- If the slide is straightforward, focus on *why* you're showing it — the strategic purpose
- If the slide is complex (architecture diagram, detailed chart), explain the concept behind the visuals

### What to Know
Supplemental information the speaker should have but doesn't necessarily need to say. Use for:
- The full explanation of each label or card — this is where the sentences live
- Background context or data that supports the slide's claim
- Likely questions or objections from the audience
- Technical details relevant only if asked

### What to Say
Direction on what story to tell. Format varies by slide:
- **Verbatim talk track** for high-stakes or precise messaging moments
- **Talking points** as a loose outline for more conversational slides
- **Narrative structure** describing the arc and order

---

## Output Format

Describe each slide using this structure:

```
### Slide [#]: [Slide Title]

**Type:** [Title / Content / Statistic / Visual / Section Break / etc.]

**Headline:** [The slide's main statement. Add an asterisk* if this headline is organizational only and does not appear on the slide.]

**Body Content:**
[Labels, bullets, stats, or short phrases that appear on the slide. Not sentences unless they meet the "earn their place" test.]

**Visual Direction:**
[Describe what graphic, icon set, photo, or diagram should appear and where]

**Speaker Notes:**

*On this slide:* [Brief description of what's on the slide or why you're showing it]

*What to know:* [Full explanations, supporting data, likely objections — everything the presenter needs but the audience doesn't need to read]

*What to say:* [Talk track direction — verbatim, bullet points, or narrative outline]
```

### Slide Type Reference

| Type | When to Use |
|---|---|
| **Title** | Opening slide — deck name, presenter, date |
| **Section Break** | Transition between major topics — simple, minimal text |
| **Content** | Standard bullet-point or concept slide |
| **Visual** | Diagram, flow, or graphic-led slide with minimal text |
| **Statistic** | Single large stat or pull quote with short framing |
| **Comparison** | Side-by-side or table format for contrasting options |
| **Demo/Screenshot** | Product UI or example — keep annotations minimal |
| **Closing** | CTA, summary, or next steps |

---

## Example Usage

```
/build slide-deck
Topic: Workflow automation platform overview
Audience: IT directors at mid-market manufacturing companies
Goal: Get buy-in to schedule a technical discovery call
Length: 20 minutes
```

```
/build slide-deck
Topic: Q3 product roadmap update
Audience: Internal sales team
Goal: Arm reps with talking points for the next quarter's releases
Existing content: [paste raw notes]
```
