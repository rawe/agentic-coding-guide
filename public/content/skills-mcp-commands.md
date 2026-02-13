---
title: "Skills vs MCP Servers vs Custom Commands"
html_file: skills-mcp-commands.html
description: "Comparison of Claude Code's three extensibility layers: Skills, MCP Servers, and Custom Commands."
---

# Skills vs MCP Servers vs Custom Commands

Claude Code has three extensibility mechanisms, each serving a distinct purpose. This page presents them side by side: what they do, how they activate, and how they complement each other.

The tagline: **MCP adds tools. Skills teach best practices. Commands automate prompts.**

## Three Layers, Three Jobs

### Skills (Auto-Activates)

Markdown files that teach Claude domain knowledge and specialized workflows. Activated automatically when context matches.

- Markdown files containing instructions and resources
- Auto-activate based on context keywords
- Teach workflows, not new capabilities
- Make Claude smarter with its existing tools

### MCP Servers (Always Available)

External servers that give Claude entirely new capabilities: browser automation, databases, APIs, file systems.

- Configured via JSON config entry in Claude Code settings
- Always available once configured
- Enable browser automation, database access, API integrations
- Extend what Claude can do

### Custom Commands (Manual Trigger)

Prompt templates triggered manually via `/command-name`. Shortcuts for repeated instructions you type often.

- Triggered by the user via `/command-name`
- Prompt templates and shortcuts
- Save typing on repeated instructions
- Add no new capabilities

## At a Glance

| Aspect | Skills | MCP Servers | Custom Commands |
|---|---|---|---|
| Purpose | Teaches HOW | Adds NEW TOOLS | Reusable Prompts |
| Activation | Auto-activates on context | Always available | Manual `/command` trigger |
| What it adds | Knowledge & workflows | External APIs & integrations | Prompt shortcuts |
| Format | Markdown files | JSON config entry | `/command` templates |
| Capabilities | Enhances existing tools | Adds entirely new ones | No new capabilities |

## Better Together

### Skills Teach Best Practices

Skills inject domain expertise so Claude uses tools correctly. A Playwright MCP without a testing skill is a tool without technique.

### MCP Adds the Tools

MCP servers connect Claude to external systems -- browsers, databases, APIs. Without MCP, Claude can only read and write files.

### Commands Automate the Prompt

Commands package your best prompts for one-click reuse. The workflow stays consistent even when the person changes.

**Summary:** MCP expands reach. Skills sharpen judgment. Commands remove friction.

## Source

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) -- docs.anthropic.com
