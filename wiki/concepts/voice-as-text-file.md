---
type: concept
title: "Voice as a Text File"
created: "2026-05-12"
updated: "2026-05-12"
origin: external
tags: [ai, voice, claude, workflows, personal-knowledge, brand-voice]
related: [ai-voice-tells-in-marketing-copy, marketing-voice-and-pov, pmm-ai-workflow-architecture, pmm-writing-voice]
---

# Voice as a Text File

## Definition

A methodology for encoding an individual's voice, taste, and decision-making patterns into a single 2,000–5,000 token markdown file that any frontier LLM can consume. Coined in practice by [[ruben-hassid]]: *"You're just a text file."* The file is portable across Claude, ChatGPT, Gemini, and Grok; it is the personal-voice equivalent of a brand style guide.

## Why It Matters

For PMMs, voice is the asset that separates differentiated copy from generic copy (see [[marketing-voice-and-pov]]). The two recurring problems: (1) voice doesn't scale across a team, and (2) AI drafting tools regress every author to the LLM mean unless explicitly constrained.

A documented voice file solves both:
- **Team scaling** — distribute the file so anyone (or any agent) can draft in the executive's, founder's, or PMM's voice
- **AI drafting consistency** — the file becomes a standing constraint, not a per-prompt instruction
- **Tool portability** — survives platform switches; outlives any single AI vendor

It also reframes the relationship to AI: you don't delegate taste, you *document* it. Editorial control is preserved by writing down what you reject.

## How It Works

**Two-step process.**

1. **Interview phase** — answer ~100 targeted questions across seven categories
2. **Compression phase** — distill the answers into a 2,000–5,000 token markdown file optimized for AI consumption

**The seven interview categories:**

1. **Contrarian beliefs** — unconventional takes you'll defend in public
2. **Writing mechanics** — sentence length, punctuation, paragraph rhythm
3. **Aesthetic dislikes** — patterns in others' writing that you reject
4. **Voice and personality** — humor, register, persona signals
5. **Structural preferences** — how you organize an argument or post
6. **Hard refusals** — what you will not write, will not say, will not do
7. **Trust / distrust signals** — red flags in others' work that mark them as unserious

**Recommended stack** (per Hassid):
- Claude + Cowork + Opus 4.7 + Extended Thinking
- Voice dictation (Wispr Flow) for faster, more honest answers
- Obsidian for sustainable file editing with sync

## Examples

**Personal use:** Brian's draft voice file would document the seven editing rules from [[marketing-voice-and-pov]] (short sentences, second person, problem before solution, bullets 3 ideal/5 ceiling, positive framing, read it out loud, one idea per paragraph) plus the banned-word list from [[ai-voice-tells-in-marketing-copy]] (em dashes, comma chains, buzzword layer, hedging openers, antithesis construction).

**Team use:** A founder's voice file lets the marketing team draft LinkedIn posts that pass the founder's edit instead of getting rewritten from scratch.

**Brand voice:** The same pattern at the brand level is what [[mailchimp]] published as its open-source style guide — voice as a documented constraint, not a vibe.

## Related Concepts

- [[ai-voice-tells-in-marketing-copy]] — what to *exclude* (the negative space)
- [[marketing-voice-and-pov]] — voice as exclusion; the underlying theory
- [[pmm-ai-workflow-architecture]] — system-level Claude setup; the voice file is the personal layer
- [[pmm-writing-voice]] — operationalizes voice constraints at the skill level

## Sources

- [[youre-just-a-text-file-hassid]] ([[ruben-hassid]])
