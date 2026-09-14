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
| Substantive deal update | Update `deals/pipeline.md` in this repo (HubSpot stays source of truth for stage/amount/date) |
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


## Handling files the Save Email to Assistant shortcut drops

The macOS shortcut writes plain `.txt` files to the **top level** of `inbox/`, named by timestamp, e.g. `Sep 9, 2026 at 2:50 PM.txt`. Body text is prefixed `---\nForwarded: `.

**Three traps, all of which have bitten:**

1. **The filename contains U+202F (narrow no-break space)** before AM/PM, not a regular space. `cat "inbox/Sep 9, 2026 at 2:50 PM.txt"` fails with "No such file or directory" even though `ls` shows it. Always address these files via `find inbox -maxdepth 1 -name "*.txt" -exec ...` or a glob in a script, never by typing the name.

2. **Collisions get a `-2` suffix** (`Sep 9, 2026 at 2:51 PM-2.txt`) when two are saved in the same minute. Do not assume one file per timestamp.

3. **NEVER bulk-delete by glob after processing.** New files can land while you are working, and a glob delete will destroy unread ones. **Delete only the exact paths you actually read and routed**, one by one, immediately after writing each destination file. Re-list the directory afterwards to catch anything that arrived mid-run.

Routing: read the file, write a properly named `inbox/<client>/YYYY-MM-DD-slug.md` with a real title, participants, and structure, then remove the source `.txt`. Create the client subfolder if needed (`npr/`, `laist/` were added Sept 2026).
