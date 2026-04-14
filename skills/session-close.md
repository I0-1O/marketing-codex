---
type: skill
title: "Session Close"
trigger: /session-close | end of session | close out the session
created: 2026-04-13
updated: 2026-04-13
---

## Purpose

Run this at the end of every session. Catches the housekeeping that's easy to forget — index drift, orphan skills, stale hot.md — and updates the vault state so the next session starts clean.

---

## Checklist

### 1. Wiki Index — skills
- [ ] Count `.md` files in `skills/` (excluding `.gitkeep`)
- [ ] Count skill entries in `wiki/index.md` under the Skills section
- [ ] If counts don't match: read each unindexed skill file, add a one-line entry to the index

### 2. Wiki Index — templates
- [ ] Count `.md` files in `templates/` (excluding `.gitkeep`)
- [ ] Count template entries in `wiki/index.md`
- [ ] Add any missing entries

### 3. Wiki Index — examples
- [ ] Count `.md` files in `examples/` (excluding `.gitkeep`)
- [ ] Count example entries in `wiki/index.md`
- [ ] Add any missing entries

### 4. Wikilinks on new pages
- [ ] For each page created this session: confirm it has inbound wikilinks from at least one other page
- [ ] For each concept or entity created: confirm it's referenced from a source or related concept page

### 5. Update hot.md
- [ ] Summarize what was built, decided, or changed this session (what, not how)
- [ ] Note the current inventory counts: concepts, entities, sources, skills
- [ ] List anticipated next session priorities
- [ ] Keep it under ~500 words — cut oldest context if needed

### 6. Append to log.md
- [ ] Confirm all creates and updates from this session are logged
- [ ] Add a `session:` entry summarizing the session in one line if not already present

### 7. Raw folder
- [ ] Check `raw/` for any files that were dropped but not ingested
- [ ] If files exist: flag them to the user before closing

---

## Example Usage

```
/session-close
```

Run without arguments. Works through the checklist top to bottom and reports findings before making changes.
