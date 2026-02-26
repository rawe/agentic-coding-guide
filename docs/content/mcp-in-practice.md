# MCP Servers in Practice

Connect Claude Code to external tools, APIs, and databases through the Model Context Protocol — the standard interface for AI-to-service communication.

## What MCP Is

MCP (Model Context Protocol) is an open standard for connecting AI applications to external systems. Think of it as USB-C for AI — one standardized plug that works with any service.

<!-- Visualization: Three-box architecture diagram (horizontal flow, left to right)
Box 1 (purple): "MCP Host — Claude Code"
Arrow →
Box 2 (indigo): "MCP Client — 1 per server"
Arrow →
Box 3 (blue): "MCP Server — Sentry, GitHub, ..."
Each box has a colored border matching its theme. -->

**Three primitives:**

- **Tools** — Executable functions Claude can invoke. File ops, API calls, database queries.
- **Resources** — Data sources that provide context. File contents, records, API responses.
- **Prompts** — Reusable interaction templates. System prompts, few-shot examples.

> **Key concept:** Discovery is dynamic. Clients call `tools/list`, `resources/list`, or `prompts/list` to discover what a server offers, then invoke capabilities as needed.

## Configuration

Add servers via CLI commands or declare them in a project `.mcp.json` file. Three transport options: HTTP (remote), stdio (local process), and SSE (deprecated).

### CLI Commands

```
# Remote server (HTTP — recommended for SaaS services)
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# Local process server (stdio)
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgres://..."

# Import servers from Claude Desktop
claude mcp add-from-claude-desktop
```

### Project Config — `.mcp.json`

Lives at the project root. Commit to version control so the whole team shares the same MCP setup.

```json
{
  "mcpServers": {
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    },
    "db": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DB_URL}"]
    }
  }
}
```

### Scoping

| Scope | Storage | Visibility | Use Case |
|---|---|---|---|
| `local` | `~/.claude.json` (project path) | Only you, this project | Personal servers, sensitive creds |
| `project` | `.mcp.json` in repo root | Everyone via version control | Team-shared servers |
| `user` | `~/.claude.json` (global) | You, across all projects | Personal utilities everywhere |

> **Precedence:** Local > Project > User. If the same server name exists at multiple scopes, the most specific scope wins.

## Popular Servers

Production-ready servers you can add in one command. HTTP servers handle auth automatically via OAuth; stdio servers run locally as subprocesses.

### Sentry — Error Tracking

Query errors, stack traces, and production issues. OAuth authentication.

```
claude mcp add --transport http sentry \
  https://mcp.sentry.dev/mcp
```

### GitHub — Code & PRs

PR reviews, issue management, repo operations. OAuth authentication.

```
claude mcp add --transport http github \
  https://api.githubcopilot.com/mcp/
```

### Notion — Knowledge Base

Read and write Notion pages and databases. OAuth authentication.

```
claude mcp add --transport http notion \
  https://mcp.notion.com/mcp
```

### PostgreSQL (DBHub) — Database

Query databases, view schemas, analyze data. Local stdio process.

```
claude mcp add --transport stdio db \
  -- npx -y @bytebase/dbhub \
  --dsn "postgres://user:pass@host/db"
```

### Playwright — Browser Automation

Browser testing, screenshots, web automation. Local stdio process.

```
claude mcp add --transport stdio playwright \
  -- npx -y @playwright/mcp@latest
```

### Fetch — Web Content

Fetch web content and convert to markdown. Official reference server.

```
claude mcp add --transport stdio fetch \
  -- npx -y @anthropic/mcp-fetch
```

## Setup Walkthrough

Adding your first MCP server, step by step. Using Sentry as the example — the flow is identical for any HTTP server.

1. **Add the server**

   ```
   claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
   ```

2. **Start Claude Code and authenticate**

   Run `claude`, then type `/mcp` and select "Authenticate" for Sentry. A browser window opens for OAuth login.

3. **Verify it works**

   Ask Claude a question that requires the server: `"What are the most common errors in the last 24 hours?"`

4. **Share with your team (optional)**

   Re-add with `--scope project` to write to `.mcp.json`, then commit. Team members get prompted for approval on first use.

### Troubleshooting

```
# Check configured servers
claude mcp list
claude mcp get sentry

# Inside Claude Code
/mcp                          # Status, authenticate, troubleshoot

# Increase startup timeout (default 10s)
MCP_TIMEOUT=10000 claude

# Increase output limit (default 25,000 tokens)
MAX_MCP_OUTPUT_TOKENS=50000 claude
```

## MCP vs Other Extensibility

Claude Code has four extension mechanisms. Each solves a different problem. MCP provides tools; Skills teach Claude how to use them.

<!-- Visualization: 2x2 comparison grid of cards
Each card has a colored heading, a role subtitle, and a description paragraph.
- MCP Servers (purple) — "Provides tools"
- Skills (indigo) — "Provides knowledge"
- Slash Commands (teal) — "Provides shortcuts"
- Hooks (amber) — "Provides guardrails" -->

- **MCP Servers** — *Provides tools.* External connections to APIs, databases, and services. Available when the server is running. Claude calls tools, reads resources, and uses prompts exposed by the server.
- **Skills** — *Provides knowledge.* On-demand markdown instructions and workflows. Loaded when relevant. Teaches Claude your conventions, review checklists, or deployment procedures.
- **Slash Commands** — *Provides shortcuts.* User-triggered aliases that expand to full prompts. Think of them as saved macros — type `/deploy` instead of writing a full deployment instruction.
- **Hooks** — *Provides guardrails.* Automated shell triggers on specific events (pre-commit, post-save). Run formatting, linting, or validation without manual invocation.

> **Powerful combo:** An MCP server connects Claude to your database. A Skill (`.claude/skills/database-queries.md`) teaches Claude your schema, naming conventions, and which tables to avoid. The server provides the tools; the skill provides the knowledge.

## Security

MCP servers run code and access external services. Review before installing.

### Best Practices

- **Prefer OAuth over static API keys** — short-lived, scoped tokens are safer than long-lived PATs
- **Review before installing** — check source code, maintenance status, known issues on GitHub
- **Be cautious with content-fetching servers** — servers that fetch web pages or emails increase prompt injection surface
- **Use project-scoped servers** — `.mcp.json` lets you audit exactly which servers a project uses
- **Rotate credentials** — use short-lived tokens and rotate frequently, especially for database connections

### Risks to Watch For

- **Supply-chain risk** — third-party servers may contain vulnerabilities. A SQL injection flaw was found in an official reference server after thousands of forks.
- **Tool poisoning** — modified servers can alter tool outputs to change agent behavior. Only install servers from trusted sources.
- **Static credentials** — over half of servers requiring auth rely on static API keys rather than OAuth. Minimize use of long-lived secrets.

---

## Sources & Further Reading

- [Claude Code MCP Documentation](https://code.claude.com/docs/en/mcp) — official setup, configuration, and auth reference
- [modelcontextprotocol.io](https://modelcontextprotocol.io/) — MCP specification, architecture, and transport docs
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official reference servers and community directory
- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) — curated community list of MCP servers
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) — official security guidance for the protocol
