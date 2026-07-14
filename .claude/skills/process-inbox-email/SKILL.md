---
name: process-inbox-email
description: Process an email saved to the inbox/ folder. Use when Matt says "check my inbox", "process this email", "what's in my inbox", "review this email", or similar. Reads inbox files, summarizes content, surfaces action items, and routes output to the right files.
---

# Process Inbox Email

Processes one or more emails saved to `inbox/` by Matt's Mimestream shortcut.

## Inbox file format

Files land in `inbox/` as `.md` or `.txt` files. The Apple Shortcut sometimes saves them with macOS timestamp names like:

```
Apr 2, 2026 at 7:19 AM.txt
```

> **Important:** These filenames contain a Unicode narrow no-break space (U+202F, `\xe2\x80\xaf`) before AM/PM. The Read tool cannot open them — use the Bash tool with Python instead (see §Reading files below).

Properly named files use the convention `YYYY-MM-DD-short-description.md` and may already be in a client subfolder.

## Client subfolder mapping

| Subfolder | Client/Project |
|-----------|---------------|
| `kqed/` | KQED |
| `tanita/` | Tanita |
| `halite/` | Halite |
| `gameday/` | Gameday |
| `uptech/` | UpTech internal, BD, outreach |

Create new subfolders as needed for new clients.

## Workflow

### 1. Find emails

- If Matt points to a specific file, proceed directly to reading it.
- Otherwise, find all unprocessed files:
  - Glob `inbox/**/*.md` for markdown files
  - Also check for `.txt` files in the inbox root with a Bash command (see below), since the glob won't catch them

```python
# Bash: find all .txt files in inbox root
import os
root = 'inbox/'
txt_files = [f for f in os.listdir(root) if f.endswith('.txt') and os.path.isfile(os.path.join(root, f))]
print(txt_files)
```

Focus on files in the root `inbox/` (not yet in a subfolder) — those are unprocessed. Already-categorized files in subfolders are treated as processed unless Matt asks to review them.

### 2. Reading files

**For normally named `.md` files:** use the Read tool.

**For timestamp-named `.txt` files** (or any file the Read tool fails on): use the Bash tool with Python, iterating by filename match rather than constructing the path literally:

```python
import os
inbox = '/path/to/assistant/inbox/'
for fname in os.listdir(inbox):
    if fname.endswith('.txt'):
        with open(os.path.join(inbox, fname), 'r', encoding='utf-8') as f:
            print(f.read())
```

### 3. For each email, extract

- **Sender** and **client/project**
- **Key information**: what they said, decisions made, dates mentioned
- **Action items**: anything Matt or the team needs to do
- **Urgency**: is anything time-sensitive?

### 4. Categorize and move

For each raw file in the inbox root:
1. Determine the right client subfolder
2. Write a clean, renamed copy to `inbox/[client]/YYYY-MM-DD-short-description.md`
3. **Delete the original raw file** from the inbox root using the Bash tool with Python

Always delete via a `listdir` loop, not by constructing the literal path (the narrow no-break space will cause a FileNotFoundError):

```python
import os
inbox = '/path/to/assistant/inbox/'
for fname in os.listdir(inbox):
    if fname.endswith('.txt') and 'Apr 2' in fname:  # match on date or content
        os.remove(os.path.join(inbox, fname))
```

### 5. Surface to Matt

Give a concise summary per email:
- Who/what it's about
- Key info in 1-2 sentences
- Action items (bulleted)

### 6. Write outputs (only when warranted)

| Situation | Output |
|-----------|--------|
| Multiple action items across emails | Append to or create `meetings/actions/YYYY-MM-DD-inbox-follow-ups.md` |
| Substantive deal update | Update `deals/pipeline.md` in `uptech/business-development` via GitHub MCP |
| New or updated contact info | Update `stakeholders/roster.md` |
| Meeting notes referenced in email | Create `meetings/notes/YYYY-MM-DD-topic.md` |

Don't create files speculatively — only when there's something meaningful to capture.

## Summary format

```
### [Client] — [Sender], [Date]
[1-2 sentence summary]

**Actions:**
- [ ] Item 1
- [ ] Item 2
```

If no action items, skip the Actions block.
