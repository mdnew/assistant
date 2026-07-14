# Harvest time mapping (example)

Copy to **`reference/harvest-time-mapping.md`** in the assistant repo, or to **`.claude/skills/log-harvest-time/mapping.md`**, then replace placeholders with real IDs from the Harvest API.

## How to fill IDs

1. List projects: see [reference.md](reference.md).
2. For each project Matt uses, list task assignments and pick default task (often Development, Project Management, or similar).

## Client / standup codes → Harvest

| code   | harvest_project_name   | project_id | default_task_name | task_id |
|--------|------------------------|------------|-------------------|---------|
| Gameday| (exact Harvest name)   | REPLACE    | (task name)       | REPLACE |
| KQED   |                        | REPLACE    |                   | REPLACE |
| Tanita |                        | REPLACE    |                   | REPLACE |
| Halite |                        | REPLACE    |                   | REPLACE |
| US     | Uptech internal        | REPLACE    |                   | REPLACE |
| Fit3D  |                        | REPLACE    |                   | REPLACE |

## Notes

- Add rows as new clients appear.
- `code` is the short label Matt uses in standups (before the colon).
- If one Harvest project serves multiple codes, duplicate the row or note aliases in a comment line.
