#!/usr/bin/env bash
# Fetch Keito projects and their tasks, and print a markdown skeleton for
# reference/keito-time-mapping.md. Read only, makes no writes to Keito.
#
# Usage:  ./fetch-mapping.sh            # active projects + tasks
#         ./fetch-mapping.sh --projects # projects only (faster)
#
# Requires KEITO_API_KEY and KEITO_ACCOUNT_ID in the environment, plus jq.
# Never prints credential values.

set -euo pipefail

: "${KEITO_API_KEY:?Set KEITO_API_KEY (Keito → Settings → API & Developers, full-access key)}"
: "${KEITO_ACCOUNT_ID:?Set KEITO_ACCOUNT_ID (the Company ID on the same page)}"
command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }

BASE="https://app.keito.ai/api/v2"

kget() {
  curl -sS --fail-with-body "$BASE/$1" \
    -H "Authorization: Bearer ${KEITO_API_KEY}" \
    -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
}

echo "## Matt's Keito identity"
echo
kget "users/me" | jq -r '"- user_id: `\(.id)`\n- \(.first_name) \(.last_name) <\(.email)>\n- company: \(.company.name // "?") (`\(.company.id // "?")`)"'
echo

echo "## Active projects"
echo
echo "| project_id | project name | client |"
echo "|------------|--------------|--------|"
projects_json="$(kget "projects?is_active=true&per_page=100")"
echo "$projects_json" | jq -r '.projects[] | "| `\(.id)` | \(.name) | \(.client.name // "-") |"'
echo

if [ "${1:-}" = "--projects" ]; then
  echo "_Tasks skipped (--projects). Re-run without the flag to list task ids._"
  exit 0
fi

echo "## Tasks per project"
echo
echo "$projects_json" | jq -r '.projects[] | "\(.id)\t\(.name)"' | while IFS=$'\t' read -r pid pname; do
  echo "### $pname (\`$pid\`)"
  echo
  kget "tasks?project_id=${pid}&is_active=true" \
    | jq -r '.tasks[]? | "- \(.name): `\(.id)`"' || echo "- (no tasks returned)"
  echo
done
