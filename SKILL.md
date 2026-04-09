---
name: assistant-workflows
description: Personal assistant workflows for Matt. Use when Matt says "log standup", "save standup", "post standup", "check my inbox", "process this email", "what's in my inbox", or similar daily operations.
---

# Assistant Workflows

---

## Skill: Log Standup

Saves today's standup from the scratch file into the dated archive.

**Triggers:** "log standup", "save standup", "post standup", "record standup"

### Files

| File | Purpose |
|------|---------|
| `daily standup.txt` (repo root) | Scratch file Matt edits throughout the week |
| `standups/YYYY-MM-DD.md` | Dated archive file (one per day) |

### Workflow

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

### Format conversion

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

### Example

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

---

## Skill: Process Inbox Email

Processes one or more emails saved to `inbox/` by Matt's Mimestream shortcut.

**Triggers:** "check my inbox", "process my email", "what's in my inbox", "review this email"

### Inbox file format

Files land in `inbox/` (or an `inbox/[client]/` subfolder) as `.md` files named `YYYY-MM-DD-short-description.md`. Content is typically:

```
---
Date: YYYY-MM-DD
Source: Email forward (Mimestream shortcut)
Topic: [optional description]
---

---
Forwarded: [email body]
```

### Client subfolder mapping

| Subfolder | Client/Project |
|-----------|---------------|
| `kqed/` | KQED |
| `tanita/` | Tanita |
| `halite/` | Halite |
| `gameday/` | Gameday |
| `uptech/` | UpTech internal, BD, outreach |

Create new subfolders as needed for new clients.

### Workflow

1. **Find emails** — if Matt points to a specific file, read that. If he says "check my inbox", glob `inbox/**/*.md` and read recent or uncategorized files.
2. **For each email, extract:**
   - Sender and client/project
   - Key information: what they said, decisions made, dates mentioned
   - Action items: anything Matt or the team needs to do
   - Urgency: anything time-sensitive?
3. **Move/categorize** — if the file is in root `inbox/` and belongs to a known client, move it to the right subfolder. Rename to `YYYY-MM-DD-short-description.md` if needed.
4. **Surface to Matt** — concise summary per email (see format below).
5. **Write outputs** only when warranted:

| Situation | Output |
|-----------|--------|
| Multiple action items across emails | Append to or create `meetings/actions/YYYY-MM-DD-inbox-follow-ups.md` |
| Substantive deal update | Update the deal in **HubSpot** via MCP (source of truth); update `deals/pipeline.md` with **notes and context**, keeping any stage/value lines consistent with HubSpot |
| New or updated contact info | Update `stakeholders/roster.md` |
| Meeting notes referenced in email | Create `meetings/notes/YYYY-MM-DD-topic.md` |

Don't create files speculatively — only when there's something meaningful to capture.

### Summary format

```
### [Client] — [Sender], [Date]
[1-2 sentence summary]

**Actions:**
- [ ] Item 1
- [ ] Item 2
```

If no action items, skip the Actions block.
