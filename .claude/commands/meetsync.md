# Process Meeting Transcript

Process and file a meeting transcript: $ARGUMENTS

## Instructions

If $ARGUMENTS contains a transcript (or a file path to one), process it directly.
If $ARGUMENTS is a meeting name/date, look it up via Google Calendar and Gemini/Google Docs attachments.

### Step 1: Extract key information
From the transcript:
- Meeting date, time, participants
- Main topics discussed
- Decisions made
- Action items (with owners)
- Important context or background that emerged

### Step 2: Create meeting note
File at `meetings/notes/YYYY-MM-DD-who-topic.md`:
```
# [Meeting Title]
**Date**: YYYY-MM-DD
**Participants**: [names]
**Duration**: [approx]

## Summary
[2-3 sentence overview]

## Key Discussion Points
[Bullet points of main topics]

## Decisions Made
[Any decisions — link to decisions/ if worth a full record]

## Context Captured
[New info about people, companies, products — note where it was filed]
```

### Step 3: Create action items
File at `meetings/actions/YYYY-MM-DD-topic.md`:
```
# Action Items: [Topic]
From meeting on YYYY-MM-DD

- [ ] [Action] — **Owner** — Due: [date if given]
- [ ] [Action] — **Owner**
```

### Step 4: Update other context
- `stakeholders/roster.md` — update any new info about participants
- **HubSpot** — update deal stage or log an engagement if relevant (source of truth); **`deals/pipeline.md`** — add notes and context; keep any stage/value lines consistent with HubSpot
- `context/` files — update if strategic context changed
- `decisions/` — create a decision record if a significant decision was made

### Step 5: Summarize
Tell me what was filed and what the most important action items are.
