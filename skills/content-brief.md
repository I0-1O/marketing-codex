---
type: skill
title: Content Brief
trigger: /build content-brief
created: 2026-04-10
updated: 2026-04-10
---

## Purpose

Create a structured content brief for any marketing content type. Gives writers and designers enough context to execute without back-and-forth. Pulls from wiki for persona and messaging context.

## Inputs

- **Content type**: Blog post, whitepaper, ebook, webinar, case study, social campaign, etc.
- **Target persona**: Who this is for (title, role, company type)
- **Topic**: What the content is about
- **Goal**: What we want the reader to do or believe after consuming it

## Process

1. Read `wiki/hot.md` for session context
2. Look up relevant persona or ICP pages in `wiki/entities/`
3. Look up relevant concept pages for the topic area
4. Pull key messages from any existing messaging framework pages
5. Construct the brief using the structure below
6. SEO: if applicable, suggest primary keyword and 2–3 secondary keywords
7. Append to `log.md`

## Output Format

- **Title options**: 3 working title options (vary tone — direct, curiosity, outcome-led)
- **Audience**: Who this is for and what they care about
- **Goal**: What success looks like (awareness, lead gen, pipeline influence, enablement, etc.)
- **Key messages to hit**: 3–5 messages ranked by priority
- **Recommended outline**: Section headers with 1-line descriptions
- **SEO considerations**: Primary keyword, secondary keywords, search intent
- **CTA**: What we want the reader to do next
- **Related assets**: Existing wiki pages, other content, or sources that should inform the writer

## Example Usage

```
/build content-brief
Content type: Blog post
Persona: Director of IT at a 1000-employee financial services firm
Topic: Why no-code automation is replacing legacy BPM platforms
Goal: Drive awareness and top-of-funnel leads for automation category
```
