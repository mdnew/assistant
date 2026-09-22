# Keito time mapping (example)

Copy to **`reference/keito-time-mapping.md`** in the assistant repo, or to **`.claude/skills/log-keito-time/mapping.md`**, then replace placeholders with real IDs from the Keito API.

## How to fill IDs

1. Run `./fetch-mapping.sh` in this skill folder (needs `KEITO_API_KEY`, `KEITO_ACCOUNT_ID`, `jq`). It prints a markdown skeleton of projects and tasks.
2. Or call the API by hand: see [reference.md](reference.md) for `GET /api/v2/projects` and `GET /api/v2/tasks?project_id=...`.
3. For each project Matt uses, pick the default task (often Product, Development, Project Management, or similar).

**Keito IDs are opaque strings** (CUIDs like `cmtundo0r00595gmk2zlnem9u`), not integers. Keep the backticks in the table so nobody pastes them unquoted into a JSON body. Tasks are workspace-level, so the same `task_id` recurs across projects.

## Client / standup codes → Keito

| code   | keito_project_name   | project_id | default_task_name | task_id |
|--------|----------------------|------------|-------------------|---------|
| Gameday| (exact Keito name)   | REPLACE    | (task name)       | REPLACE |
| KQED   |                      | REPLACE    |                   | REPLACE |
| Tanita |                      | REPLACE    |                   | REPLACE |
| Halite |                      | REPLACE    |                   | REPLACE |
| US     | Uptech internal      | REPLACE    |                   | REPLACE |
| Fit3D  |                      | REPLACE    |                   | REPLACE |

## Notes

- Add rows as new clients appear.
- `code` is the short label Matt uses in standups (before the colon).
- If one Keito project serves multiple codes, duplicate the row or note aliases in a comment line.
