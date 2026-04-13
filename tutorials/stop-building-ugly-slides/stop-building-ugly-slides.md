# Stop Building Ugly Slides

A practical guide to building presentations that actually work — where the presenter tells the story and the slides support it.

---

## What This Is

Most slide decks fail the same way: walls of text, slides that explain themselves, presenters who narrate their own content. This tutorial covers the principles behind better slides, gives you a quick-reference cheat sheet, and includes an AI skill you can use to build decks from scratch.

**Three things in this kit:**

| Resource | What It Is | Link |
|---|---|---|
| Slide Deck (PPTX) | The "Stop Building Ugly Slides" presentation — the full deck with examples and speaker notes | [Download from Dropbox](https://www.dropbox.com/scl/fi/7zo3jsh1ukez6w35wvjis/Stop-Building-Ugly-Slides.pptx?rlkey=7fql51kv3vyj4idsqqcaqktdx&st=6q4am0f9&dl=0) |
| Cheat Sheet (PDF) | One-page quick reference — the rules, fast | [Download from Dropbox](https://www.dropbox.com/scl/fi/nqrkrxemfsso9g87mc6lq/Stop-Building-Ugly-Slides-Cheat-Sheet.pdf?rlkey=daccg6m63rhdbanxcn8uoogfi&st=9lhe5u0h&dl=0) |
| Cheat Sheet (MD) | Same content, vault-native and linkable | [[cheat-sheet]] |
| AI Skill | Claude Code skill for building decks with this methodology baked in | [[slide-deck]] |

---

## The Core Idea

A presentation is a story told by a person to a room full of people. That sounds obvious. It isn't — because most decks are built as if the slides tell the story.

They don't. You do.

**Slides:** anchor, emphasize, visualize  
**You:** explain, connect, persuade

When slides try to do both jobs, they fail at both. The audience reads instead of listens. The presenter becomes a narrator of their own content. The room checks out.

Read the full argument in [[slides-dont-talk]].

---

## The Four Offenses

The deck covers the four patterns that kill most presentations:

1. **Bullet walls** — too many bullets, each a complete thought the presenter then reads aloud
2. **Text overload** — explanations on slides that should be in speaker notes (or just said)
3. **Spreadsheet on a slide** — raw data with no visual interpretation
4. **Seven concepts on one page** — the presenter is the only one who knows how they connect

These are symptoms. The underlying cause is almost always one of three habits: using the slide as a teleprompter, confusing thoroughness with clarity, or the leave-behind fallacy. See [[leave-behind-fallacy]] for that last one.

---

## The Quick Rules

Full detail in [[cheat-sheet]], but the short version:

- **3–5 bullets max.** 3 is ideal. 5 is the ceiling. Hit 6 and you have two slides.
- **One slide, one concept.** If you're saying "and also" — that's your next slide.
- **Slides are free.** More slides, simpler each, beats fewer slides crammed full.
- **Headlines state the point.** "Integration" is a label. "Connect to Any System Without Code" is a headline.
- **Speaker notes carry the presentation.** On This Slide / What to Know / What to Say.

---

## Using the AI Skill

The [[slide-deck]] skill is a Claude Code workflow that builds decks using this methodology. Feed it a topic, audience, and goal — it outputs a full slide-by-slide plan with content, visual direction, and speaker notes in the three-part format.

**Recommended workflow:**

1. Write your talk track first (or paste in raw notes)
2. Run `/build slide-deck` with topic, audience, and goal
3. Review the slide plan — refine headlines and visual direction
4. Build in PowerPoint; pull speaker notes directly from the skill output
5. Review AI output carefully — hallucinations and word salad are real

See [[slide-deck#Example Usage]] for sample prompts.
