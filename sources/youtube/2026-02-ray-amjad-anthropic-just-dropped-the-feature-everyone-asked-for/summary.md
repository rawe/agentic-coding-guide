# Anthropic Just Dropped the Feature Everyone Asked For

> Source: [Anthropic Just Dropped the Feature Everyone Asked For](https://www.youtube.com/watch?v=y3xzYwxQuHc) by Ray Amjad

## Overview

Ray Amjad walks through Claude Code's new remote control feature, which lets you control a local or cloud-hosted Claude Code session from your phone or another device via the Claude app. The video covers setup, practical use cases like mobile-triggered video editing and coding, and three security strategies for running remote sessions safely: remote server isolation, sandboxing, and proxy-based URL filtering.

## Key Takeaways

- `claude rc` (or `claude remote-control`) opens a secure connection through Anthropic's servers, letting you send prompts from the Claude mobile app or web interface — replacing the old tmux/Tailscale/Terminus workaround.
- Remote sessions inherit the full local Claude Code config: skills, MCP servers, plan mode, and permission settings all work from your phone.
- Running Claude Code on a cheap remote server ($3.49/mo Hetzner) with tmux gives you an always-on agent that can run `--dangerously-skip-permissions` without risking your local machine.
- Sandboxing via `settings.local.json` lets you allowlist specific URLs, deny write/bash tools, and create purpose-built research environments that need no permission prompts.
- A local HTTP proxy adds the strictest network control: only allowlisted domains get through, and `api.anthropic.com` must be included for the remote connection to work.
- Unlike OpenClaw, remote control is passive (you prompt it) rather than proactive (no scheduled tasks or push notifications yet).

## Notes

### Setup and Usage

Three ways to enable remote control:
1. **Per-session**: run `claude rc` or type `/remote-control` inside an active session.
2. **Persistent**: `/config` → search "remote control" → set to `true`. Enables it for all future sessions.
3. **On remote server**: SSH in, install Claude Code, run inside tmux, enable `/remote-control`, then detach with `Ctrl+B :detach`. The session stays alive in the cloud.

On the client side, open the Claude app (mobile or web), go to the Code tab, and pick the session. Messages sent from the phone appear instantly in the terminal session. Permissions can be approved from the phone when not using `--dangerously-skip-permissions`.

### Security Strategies

**Remote server isolation** — deploy Claude Code on a disposable VPS. Even with `--dangerously-skip-permissions`, prompt injection damage is confined to the server. Install MCP servers there for background research, report generation, or any task you want running 24/7 without your laptop being on.

**Sandboxing** — configure `settings.local.json` with:
- `sandbox: { enabled: true }`
- `permissions: { defaultMode: "dontAsk" }`
- An allowlist of URLs for research (e.g., arxiv)
- Deny rules for edit, write, and bash tools

This creates a locked-down research environment. Claude can fetch from allowed sites but cannot modify files or shell out.

**Proxy-based filtering** — for finer network control when you still need bash/curl access:
- Deny the `WebFetch` and `WebSearch` tools (they bypass the proxy).
- Set `httpProxyPort` in settings.
- Run a Node.js proxy that allowlists specific domains.
- Critical: `api.anthropic.com` must be allowed or the remote connection breaks.

The proxy approach lets you combine `--dangerously-skip-permissions` with strict network boundaries — useful for research agents restricted to a curated set of sites.

### Comparison with OpenClaw

Remote control is more passive: you send a prompt, Claude executes. OpenClaw supports scheduled tasks, proactive searches, and push notifications. Ray expects Anthropic to close this gap over time — specifically, he wants hooks to trigger phone notifications during remote sessions. For users who primarily need on-demand mobile access to their Claude Code environment (skills, MCP servers, project context), remote control already covers most use cases without a separate tool.
