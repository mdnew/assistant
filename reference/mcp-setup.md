# MCP Integration Setup

These integrations turn this from a note-taking system into an actual assistant that can act on your behalf.

## Claude Code

Add MCP servers to your Claude Code config at `~/.claude/claude_code_config.json` or via `claude mcp add`.

### Google Calendar + Gmail (via Google Workspace MCP)

```bash
claude mcp add google-workspace
```

Or manually add to config:
```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

### Slack

```bash
claude mcp add slack
```

Or:
```json
{
  "slack": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "xoxb-...",
      "SLACK_TEAM_ID": "T..."
    }
  }
}
```

### GitHub

```bash
claude mcp add github
```

Or:
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..."
    }
  }
}
```

### JIRA (Atlassian)

Use the Atlassian MCP server:
```json
{
  "atlassian": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-atlassian"],
    "env": {
      "ATLASSIAN_URL": "https://yourcompany.atlassian.net",
      "ATLASSIAN_EMAIL": "you@company.com",
      "ATLASSIAN_API_TOKEN": "your-api-token"
    }
  }
}
```

Get your Atlassian API token at: https://id.atlassian.com/manage-profile/security/api-tokens

## Cursor

For Cursor, MCPs are configured in Settings > MCP or in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "google-workspace": { ... },
    "slack": { ... },
    "github": { ... },
    "atlassian": { ... }
  }
}
```

You already have Atlassian MCP configured in this Cursor installation.

## Rube (Alternative — all-in-one)

Obie Fernandez uses [Rube](https://rube.app/) as a single MCP integration that covers Google Calendar, Gmail, Slack, Linear, and Twitter/X with a single connection. Worth evaluating if managing multiple MCPs is annoying.

## Wispr Flow (Voice Input)

For voice input (highly recommended for stream-of-consciousness updates):
- Download at https://wisprflow.ai/
- Works system-wide — dictate directly into Claude Code or Cursor chat
- Much faster than typing for context dumps and meeting debriefs
