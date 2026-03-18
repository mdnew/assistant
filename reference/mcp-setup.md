# MCP Integration Setup

These integrations turn this from a note-taking system into an actual assistant that can act on your behalf.

The `claude mcp add` command syntax is:
```bash
claude mcp add <name> -e KEY=value -- npx -y <package>
```

---

## Slack

**1. Create a Slack app** at https://api.slack.com/apps
- Add OAuth scopes: `channels:read`, `channels:history`, `chat:write`, `users:read`, `groups:read`, `im:read`, `mpim:read`
- Install to your workspace and copy the **Bot User OAuth Token** (`xoxb-...`)
- Copy your **Team ID** from workspace settings (starts with `T`)

**2. Add to Claude Code:**
```bash
claude mcp add slack \
  -e SLACK_BOT_TOKEN=xoxb-your-token \
  -e SLACK_TEAM_ID=T1234567 \
  -- npx -y @modelcontextprotocol/server-slack
```

---

## GitHub

**1. Create a personal access token** at https://github.com/settings/tokens
- Scopes needed: `repo`, `read:org`, `read:user`

**2. Add to Claude Code:**
```bash
claude mcp add github \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your-token \
  -- npx -y @modelcontextprotocol/server-github
```

---

## HubSpot

HubSpot has a native remote MCP server at `https://mcp.hubspot.com/` using OAuth — no API token needed.

**1. Create an MCP Auth App** in HubSpot:
Developer platform → MCP Auth Apps → Create

- **Redirect URL:** `http://localhost:54321/callback`
- Name and description are optional

After creating, copy the **Client ID** and **Client Secret** from the app details page.

**2. Add to Claude Code:**
```bash
claude mcp add hubspot \
  --transport http \
  --callback-port 54321 \
  --client-id YOUR_CLIENT_ID \
  --client-secret \
  https://mcp.hubspot.com/
```

It will prompt for the client secret, then open a browser to complete the OAuth flow.

**3. Add to Cursor** (`~/.cursor/mcp.json`):
```json
{
  "hubspot": {
    "url": "https://mcp.hubspot.com/",
    "transport": "http"
  }
}
```
Cursor will handle the OAuth flow automatically on first use.

With HubSpot connected:
- "What's the status of the Acme deal?" → fetches live from HubSpot
- "Summarize all deals in Negotiation over $10k" → CRM search
- "Who are the contacts at Acme?" → pulls from HubSpot CRM

Note: The remote HubSpot MCP is currently **read-only** (contacts, companies, deals, tickets, etc.). Write operations require the `@hubspot/mcp-server` npm package with a private app token instead.

---

## JIRA (Atlassian)

**1. Create an API token** at https://id.atlassian.com/manage-profile/security/api-tokens

**2. Add to Claude Code:**
```bash
claude mcp add jira \
  -e ATLASSIAN_URL=https://yourcompany.atlassian.net \
  -e ATLASSIAN_EMAIL=you@company.com \
  -e ATLASSIAN_API_TOKEN=your-token \
  -- npx -y @modelcontextprotocol/server-atlassian
```

---

## Google Calendar + Gmail

Google requires OAuth, which is slightly more involved. Two options:

### Option A: Zapier MCP (easiest)
Zapier provides an HTTP-based MCP that covers Gmail and Google Calendar with no OAuth setup:
1. Go to https://zapier.com/mcp and create an MCP endpoint
2. Add Google Calendar and Gmail as connected actions

```bash
claude mcp add zapier \
  --transport http \
  https://mcp.zapier.com/api/mcp/s/your-endpoint-id/mcp
```

### Option B: google-calendar-mcp (direct, more powerful)
```bash
# Install and run OAuth setup first
npx -y @iflow-mcp/google-calendar-mcp auth

# Then add to Claude Code
claude mcp add google-calendar \
  -- npx -y @iflow-mcp/google-calendar-mcp
```

This stores OAuth tokens locally after the one-time auth flow.

---

## Cursor

For Cursor, open **Settings → MCP** (or edit `~/.cursor/mcp.json`) and add the same servers in JSON format:

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-...",
        "SLACK_TEAM_ID": "T..."
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..."
      }
    },
    "hubspot": {
      "url": "https://mcp.hubspot.com/",
      "transport": "http"
    },
    "jira": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-atlassian"],
      "env": {
        "ATLASSIAN_URL": "https://yourcompany.atlassian.net",
        "ATLASSIAN_EMAIL": "you@company.com",
        "ATLASSIAN_API_TOKEN": "your-token"
      }
    }
  }
}
```

---

## Rube (Alternative — all-in-one)

[Rube](https://rube.app/) is a single MCP integration covering Google Calendar, Gmail, Slack, Linear, and Twitter/X with one connection. Worth evaluating if managing multiple MCPs feels like too much overhead.

---

## Wispr Flow (Voice Input)

Highly recommended for stream-of-consciousness updates and meeting debriefs:
- Download at https://wisprflow.ai/
- Works system-wide — dictate directly into Claude Code or Cursor chat
- Much faster than typing for context dumps
