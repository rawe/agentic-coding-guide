---
title: "Subagents vs Agent Teams"
html_file: subagents-vs-teams.html
description: Visual comparison of two agent architecture patterns — subagents (isolated workers) vs agent teams (coordinating peers).
---

# Subagents vs Agent Teams

A side-by-side comparison of two multi-agent architecture patterns for agentic coding. The core decision: **choose based on whether workers need to communicate**.

Source: [Cole Medin — Agent Teams Are Insane](https://www.youtube.com/watch?v=-1K_ZWDKpU0)

## Pattern A: Subagents

A main agent (e.g. Claude Code) spawns isolated worker agents. Each worker receives a focused task, executes independently, and returns a result. Workers cannot communicate with each other.

### Architecture

- **Main Agent** sits at the top, dispatching tasks downward.
- **Worker agents** run in parallel, each scoped to a single task.
- **No lateral communication** between workers. Connections between peers are explicitly blocked.
- Each worker returns its result directly to the main agent.

### Example Tasks and Results

| Worker Task | Result |
|---|---|
| `auth patterns` | Auth uses JWT, 24h expiry |
| `query perf` | Query on line 142 is O(n^2) |
| `scan CVEs` | lodash has CVE-2021-23337 |

Workers report back only. There is no coordination between them.

## Pattern B: Agent Teams

A lead agent (e.g. Claude Code) spawns worker agents that can communicate with each other and share state through a common task list.

### Architecture

- **Lead Agent** sits at the top, assigning initial work.
- **Worker agents** (e.g. Frontend, Backend, Database) operate as peers.
- **Bidirectional communication** between all workers. Frontend talks to Backend, Backend talks to Database, and Frontend can reach Database directly.
- **Shared Task List** acts as the coordination mechanism. All workers read from and write to it.

### Shared Task List Example

- [ ] Define API contract
- [x] Set up database schema
- [ ] Build chat UI components

Workers coordinate peer-to-peer and through shared context.

## When to Use Each Pattern

### Use Subagents When

- Quick, focused tasks (usually research)
- Only the result matters (not the process)
- Cost / token sensitive

### Use Agent Teams When

- Complex multi-component builds
- Agents need to coordinate
- Work requires collaboration

## Key Takeaway

The distinction is about **isolation vs coordination**. Subagents are fire-and-forget: cheap, parallel, independent. Agent teams share state and communicate laterally, which adds overhead but enables complex multi-part work where components depend on each other.
