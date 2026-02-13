---
title: "Agentic Coding"
html_file: index.html
description: "Landing page and navigation hub for agentic coding best practices with AI coding agents."
---

## Purpose

The page serves as the top-level index for the Agentic Coding site. It provides a single entry point to all guides in the collection.

## Branding

- **Site title:** Agentic Coding
- **Subtitle:** "Best practices for building with AI coding agents."
- **Footer attribution:** "Agentic Coding / Best practices collection" (fixed bottom-left, monospace)
- **Visual style:** Dark theme with a fixed abstract background image (`assets/bg-dark-abstract.png`), dark overlay gradient, and color-coded cards with accent borders.
- **Stylesheet:** `css/theme.css`

## Linked Pages

Each card links to a separate HTML page. Listed in display order:

- **Research -> Plan -> Implement** (`research-plan-implement.html`, color: cyan) -- Three phases of intentional context compaction for solving hard problems in complex codebases with AI coding agents.
- **Three Layers, Three Jobs** (`skills-mcp-commands.html`, color: purple) -- Distinguishing Skills, MCP Servers, and Custom Commands -- the three extensibility layers of Claude Code.
- **Skills in Practice** (`skills-in-practice.html`, color: amber) -- From installation to composition -- the practical workflow for extending Claude Code with skills, based on Leon van Zyl's tutorial.
- **Commands in Practice** (`commands-in-practice.html`, color: green) -- One markdown file, one slash command -- how custom commands parse arguments and orchestrate skills.
- **The Command & Skill Journey** (`command-skill-journey.html`, color: teal) -- From ad-hoc prompts to modular architecture -- how Claude Code workflows evolve in four steps.
- **Subagents vs Agent Teams** (`subagents-vs-teams.html`, color: coral) -- Choose based on whether workers need to communicate -- two architecture patterns for delegating work in Claude Code.
- **Mastering CLAUDE.md** (`mastering-claude-md.html`, color: fuchsia) -- Write project instructions that Claude actually follows -- from first file to full configuration stack.
- **Master Your Context Window** (`context-engineering.html`, color: indigo) -- What goes in, what stays out, and why it decides everything.
- **The Developer's Daily Loop** (`developer-workflows.html`, color: orange) -- Six workflow patterns that define how experienced developers actually use Claude Code.

## Navigation Structure

- Flat single-level navigation. The index page links to nine standalone guide pages.
- No shared nav bar or sidebar; each card is a full-width clickable link.
- Cards are stacked vertically in a single column, max-width 800px, centered.
- Each card shows a color-coded title, a one-line description, and a hover arrow indicator.
