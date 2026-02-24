# Why Most Developers Are Using Claude Code Wrong (Here's What You're Missing)!

> Source: [Why Most Developers Are Using Claude Code Wrong (Here's What You're Missing)!](https://www.youtube.com/watch?v=xuZ2meWfcKg) by DIY Smart Code

## Overview

DIY Smart Code breaks down the five customization features in Claude Code — CLAUDE.md, skills, subagents, hooks, and MCP servers — and explains the specific problem each one solves. The video provides a decision matrix based on context window cost and activation pattern, giving developers a clear rule for when to use each feature instead of cramming everything into a single instructions file.

## Key Takeaways

- **Most developers only use CLAUDE.md** and miss four other customization features that load differently and cost the context window differently.
- **CLAUDE.md is for non-negotiable, always-on standards** — it loads every session regardless of relevance, so only project-wide rules belong here. It supports a hierarchical cascade (enterprise → personal → project → local), where more specific overrides less specific.
- **Skills are on-demand expertise** — only the description sits in context; the full instructions load when matched. If Claude should know it *sometimes*, make it a skill. Commands and skills are now unified.
- **Subagents run in isolated context windows** — verbose exploration output stays contained, and only a summary returns to the main conversation. Three built-in types (Explore, Plan, General Purpose) plus custom agents with restricted tools and model selection.
- **Hooks are event-driven, deterministic automation** — they fire on specific lifecycle events (pre/post tool use, session start/stop) regardless of what was asked. Unlike skills, hooks guarantee execution rather than relying on LLM judgment.
- **MCP servers connect external tools via open protocol** — Sentry, Postgres, GitHub, Figma, etc. Tool search dynamically loads MCP tools on demand to manage context cost.
- **Decision matrix**: Always know it → CLAUDE.md. Sometimes know it → Skill. Run in isolation → Subagent. Happen automatically on events → Hook. Need external tools → MCP server.
- **Context window cost varies by feature**: CLAUDE.md is high (always loaded), skills are low (description only until invoked), subagents and hooks are zero (separate context / outside context), MCP is moderate (mitigated by dynamic tool search).

## Notes

### CLAUDE.md — Always-On Instructions

CLAUDE.md loads at the start of every session with no exceptions. It's the place for non-negotiable standards: language modes, package managers, database rules. The hierarchy cascades like CSS — enterprise → personal → project → local — where more specific files override less specific ones. Claude also builds its own memory automatically, noticing patterns and conventions across sessions and writing them to a memory directory. The trade-off: everything in CLAUDE.md consumes tokens every session whether it's relevant or not.

### Skills — On-Demand Expertise

A skill is a `skill.md` file with a description and instructions. Claude matches incoming requests against skill descriptions and activates the relevant ones automatically — no slash command required (though slash commands still work). Only the description sits in context at all times; the full content loads on demand. Skills can include supporting files like templates, reference docs, and scripts. Storage location determines scope: personal skills in the home directory follow you everywhere; project skills in `.claude/skills` are shared via version control. Anthropic unified commands and skills — both create the same slash command.

### Subagents — Isolated Workers

Subagents run in their own context window, completely isolated from the main conversation. They handle verbose tasks (codebase exploration, documentation research) and return only a summary. Three built-in types: Explore (read-only, optimized for speed), Plan (research during plan mode), and General Purpose (all tools, multi-step tasks). Custom subagents are defined as markdown files in `.claude/agents` with name, description, tool restrictions, and model selection. They can have persistent memory across sessions. Context window cost is zero — all work happens in a separate context.

### Hooks — Event-Driven Automation

Hooks are shell commands that execute at specific points in Claude Code's lifecycle. They fire deterministically on events, not on request. Example use cases: a pre-tool-use hook on Bash that blocks `rm -rf`, a post-tool-use hook on Write/Edit that runs Prettier on every saved file. There are 15 event types including pre/post tool use, session start, and session stop. Hooks can also use an LLM: prompt-based hooks send context to a fast model for yes/no decisions, agent-based hooks spawn a subagent that checks conditions before deciding. The critical distinction from skills: skills are request-driven, hooks are event-driven and guaranteed.

### MCP Servers — External Integrations

Model Context Protocol is an open standard for connecting AI tools to external services. Servers are added with `claude mcp add`, choosing a transport type. Over 100 official servers exist in the registry (Sentry, Postgres, GitHub, Jira, Figma, Slack). MCP tools appear alongside built-in tools and can be used within hooks, skills, and subagents. Context cost is moderate but mitigated by tool search loading tools dynamically on demand.

### Decision Matrix

Five questions, one per feature. "Should Claude always know it?" → CLAUDE.md. "Should Claude know it sometimes?" → Skill. "Should this run in isolation?" → Subagent. "Should this happen automatically on events?" → Hook. "Does Claude need external tools or data?" → MCP server. The features compose and complement each other — a real-world setup uses multiple features simultaneously.
