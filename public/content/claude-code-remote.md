# Claude Code Remote Control

Control Claude Code from your phone or any browser -- send prompts, approve permissions, and run agents on remote servers without your laptop.

## What Remote Control Is

`claude rc` (or `claude remote-control`) opens a secure connection through Anthropic's servers. Once active, you can send prompts from the Claude mobile app or web interface directly into your terminal session.

- The session inherits your full local config: skills, MCP servers, plan mode, permission settings
- Messages from the phone appear instantly in the terminal
- Permissions can be approved from mobile when not using `--dangerously-skip-permissions`

> Replaces the old tmux + Tailscale + Terminus workaround with a single built-in command.

## Setup

Three ways to enable remote control:

### Per-Session

```
claude rc
```

Or type `/remote-control` inside an active session.

### Persistent

```
/config
```

Search "remote control" and set to `true`. Enables it for all future sessions.

### On a Remote Server

```
ssh your-server
# Install Claude Code, then:
tmux
claude --dangerously-skip-permissions
/remote-control
# Detach with Ctrl+B :detach
```

The session stays alive in the cloud. Connect from the Claude app's Code tab.

## Three Security Strategies

<!-- Visualization: Three-column card grid (horizontal)
Card 1 (cyan): "Remote Server" - shield icon, VPS isolation
Card 2 (teal): "Sandboxing" - lock icon, settings.local.json config
Card 3 (blue): "Proxy Filtering" - filter icon, HTTP proxy
Each card has a colored top border and label badge -->

### Remote Server Isolation

Deploy Claude Code on a disposable VPS (e.g., $3.49/mo Hetzner). Even with `--dangerously-skip-permissions`, prompt injection damage is confined to the server.

- Install MCP servers for background research, report generation, or 24/7 tasks
- Your laptop can be off -- the agent runs in tmux
- If compromised, nuke the server and spin a new one

### Sandboxing

Configure `settings.local.json` to create a locked-down research environment:

```json
{
  "sandbox": { "enabled": true },
  "permissions": { "defaultMode": "dontAsk" },
  "allowedUrls": ["arxiv.org", "scholar.google.com"],
  "deny": ["edit", "write", "bash"]
}
```

Claude can fetch from allowed sites but cannot modify files or shell out.

### Proxy-Based Filtering

For finer network control when you still need bash/curl access:

- Deny `WebFetch` and `WebSearch` tools (they bypass the proxy)
- Set `httpProxyPort` in settings
- Run a Node.js proxy that allowlists specific domains
- **Critical:** `api.anthropic.com` must be allowed or the remote connection breaks

Combines `--dangerously-skip-permissions` with strict network boundaries -- useful for research agents restricted to a curated set of sites.

## Security Strategy Comparison

| Strategy | Network Control | File System | Best For |
|---|---|---|---|
| **Remote Server** | Full (isolated machine) | Full access on server | Always-on agents, disposable environments |
| **Sandboxing** | URL allowlist | Read-only | Research-only agents, zero-write environments |
| **Proxy** | Domain-level filtering | Full access | Agents that need bash but restricted network |

## Remote Control vs OpenClaw

| Aspect | Remote Control | OpenClaw |
|---|---|---|
| **Interaction model** | Passive -- you prompt it | Proactive -- scheduled tasks, push notifications |
| **Setup** | Built-in (`claude rc`) | Separate tool |
| **Config inheritance** | Full (skills, MCP, permissions) | Separate configuration |
| **Best for** | On-demand mobile access to your Claude Code environment | Automated scheduled workflows |

Remote control covers most use cases for developers who primarily need mobile access to their Claude Code environment (skills, MCP servers, project context). Anthropic is expected to close the gap with features like phone notifications during remote sessions.

---

## Source

- [Anthropic Just Dropped the Feature Everyone Asked For](https://www.youtube.com/watch?v=y3xzYwxQuHc) by Ray Amjad (2026-02-25)
