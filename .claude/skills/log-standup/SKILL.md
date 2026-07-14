---
name: log-standup
description: Save today's standup from daily standup.txt into the standups/ archive. Use when Matt says "log standup", "save standup", "post standup", "record standup", or similar. Reads the scratch file, converts it to the archive format, and writes standups/YYYY-MM-DD.md.
---

# Log Standup

Saves today's standup from the scratch file into the dated archive.

## Files

| File | Purpose |
|------|---------|
| `daily standup.txt` (repo root) | Scratch file Matt edits throughout the week |
| `standups/YYYY-MM-DD.md` | Dated archive file (one per day) |

## Date for the archive filename

- **Authoritative "today"** is the **actual current calendar date** from system context (the `Today's date:` field in the session), not an assumption.
- **Do not** derive the archive filename only from the scratch line at the top of `daily standup.txt` (e.g. `_Apr 13, 2026 - Standup_`). That line is often a template or stale; the **archive path must match real today**.
- If the scratch header date and system today disagree, use **system today** for `standups/YYYY-MM-DD.md` and briefly flag the mismatch for Matt if it matters.

## Workflow

1. **Check the current date** from system context — never assume.
2. **Read `daily standup.txt`** fresh.
3. **Extract** the sections relevant to today:
   - The day entry for the prior weekday → `## [Day] (prior day)`
   - The day entry for today → `## [Day] (today)`
   - `*Goals*` → `## Goals`
   - `*Blockers*` → `## Blockers`
4. **Convert format** (see below).
5. **Write** to `standups/YYYY-MM-DD.md` using today's date.
6. **Do not** delete or modify `daily standup.txt` unless Matt explicitly asks.

## Format conversion

`daily standup.txt` uses:
- `*Day*` for day headings
- `• bullet` for items

Target `standups/YYYY-MM-DD.md` uses:
```
# Standup — [Weekday], [Month] [D], [Year]

## [Prior weekday] (prior day)
- item

## [Today weekday] (today)
- item

## Goals
- item

## Blockers
- item
```

Convert `•` bullets to `-` bullets. Strip italic markers from headings.

## Example

**Input** (`daily standup.txt`):
```
_Apr 2, 2026 - Standup_
*Wednesday*
• KQED: Pull data

*Thursday*
• KQED: Coffee with Mark

*Goals*
• Gameday: Expand SOW

*Blockers*
• None
```

**Output** (`standups/2026-04-02.md`):
```markdown
# Standup — Thursday, Apr 2, 2026

## Wednesday (prior day)
- KQED: Pull data

## Thursday (today)
- KQED: Coffee with Mark

## Goals
- Gameday: Expand SOW

## Blockers
- None
```
