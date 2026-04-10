---
type: skill
title: Analyst Briefing Prep
trigger: /build analyst-prep
created: 2026-04-10
updated: 2026-04-10
---

## Purpose

Prepare a structured briefing package for an analyst meeting — agenda, key messages, anticipated questions, and supporting data points. Surfaces relevant wiki context on the analyst and firm before you walk in.

## Inputs

- **Analyst firm**: e.g., Gartner, Forrester, IDC
- **Analyst name**: Specific analyst being briefed
- **Briefing topic**: What the meeting is about (product launch, category update, strategy brief, etc.)

## Process

1. Read `wiki/hot.md` for session context
2. Look up `wiki/entities/[analyst-name].md` and `wiki/entities/[analyst-firm].md` for known context on their coverage area, past opinions, and published research
3. Look up any relevant concept pages for the briefing topic
4. Identify what the analyst is likely to probe based on their known POV
5. Build the briefing package using the structure below
6. Flag gaps: what wiki knowledge is missing that would strengthen prep

## Output Format

- **Briefing agenda**: Time-boxed agenda (typical 30–60 min format)
- **Key messages**: 3–5 messages to land, ordered by priority
- **Anticipated questions**: What this analyst is likely to ask, based on their known coverage
- **Supporting data points**: Metrics, customer stories, or proof points that back up key messages
- **What to avoid**: Topics or framings that tend to land poorly with this analyst or firm
- **Knowledge gaps**: What we don't know about this analyst that would improve prep

## Example Usage

```
/build analyst-prep
Analyst firm: Forrester
Analyst: Craig Le Clair
Topic: AI-driven process automation — product strategy update
```
