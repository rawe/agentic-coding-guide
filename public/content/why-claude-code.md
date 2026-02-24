# Why Claude Code

More than an AI coding tool — an extensible platform for agent-driven workflows.

## The Agentic Loop

Most AI coding tools are moving toward agentic workflows — but Claude Code was an early mover and has built a deeply evolved harness around it. The difference isn't the model; it's the harness around it. The same Opus model behaves differently in Claude Code than in other tools because of how the loop is orchestrated.

Claude Code runs a continuous three-phase cycle: **gather context → take action → verify results** — then course-corrects and repeats. It reads files to understand the problem, makes edits or runs commands, then checks whether what it did actually worked. When a test fails, it reads the error, fixes the code, and runs again — without you stepping in. The loop continues until the task is complete or you redirect.

The verification step is what separates a good agent from a reckless one. Anthropic calls it "the single highest-leverage thing you can do" — giving the agent a way to check its own work. Agents that verify their output catch mistakes before they compound and self-correct when they drift.

Claude Code runs in your terminal, in VS Code, in JetBrains, or as a desktop app. Same agent, same loop, multiple surfaces.

<!-- Visualization: Three-node cycle diagram with prominent loop arrow.
Three nodes arranged in a triangle or circular layout:
1. "Gather Context" (magnifying glass icon) — "Read files, search code, understand"
2. "Take Action" (terminal/code icon) — "Edit files, run commands, create"
3. "Verify Results" (checkmark icon) — "Run tests, check output, validate"
Arrows connecting: 1→2→3, then a prominent loop arrow from 3 back to 1
labeled "Course-correct and repeat."
Center or bottom note: "You can interrupt at any point."
The loop arrow should be visually prominent to convey the self-correction cycle. -->

## Composable Extension Primitives

What makes Claude Code truly extensible: five building blocks that let you shape how the agent thinks and acts in your project. No plugin SDK, no proprietary config format — just text files in `.claude/` that you commit to git. Anyone who clones the repo gets the same agent behavior.

### CLAUDE.md — Your project's rulebook

A markdown file the agent reads at the start of every session. Put your coding standards, conventions, and constraints here. "Use pnpm, never npm." "Never modify the database schema directly." It's hierarchical — organization, personal, project, and local levels — where more specific always wins.

### Skills — Teachable expertise

Teach Claude how to do something specific: review a PR your way, deploy with your checklist, write commits in your format. Skills activate automatically when the context matches, or you invoke them as slash commands. They live as markdown files — easy to write, easy to share.

### Subagents — Delegate and conquer

Spin up isolated workers for specific jobs. Need a codebase explored? A doc researched? A review done in parallel? Subagents handle it independently and report back a summary. Three built-in types (Explore, Plan, General Purpose), or define your own with custom tool access and instructions.

### Hooks — Guardrails that never forget

Automation that fires on events — before a command runs, after a file is saved, when a session ends. Block dangerous operations, auto-format code, run tests after every edit. Unlike instructions the AI might overlook, hooks execute every time, guaranteed.

### MCP Servers — Plug in the outside world

Connect external tools through an open protocol. Databases, GitHub, error monitoring, browser automation, design tools. One command to add. The agent uses them like built-in capabilities.

<!-- Visualization: Five building-block cards, each with icon and short label:
CLAUDE.md = "Rules" (book icon)
Skills = "Expertise" (lightbulb icon)
Subagents = "Delegation" (people/fork icon)
Hooks = "Guardrails" (shield icon)
MCP = "Connections" (plug icon)
Tagline below: "Text files. Git-committed. Team-shared." -->

## How They Compose

The primitives aren't isolated features — they're designed to work together. Each one handles a different layer.

**MCP adds capabilities** — connects Claude to services it couldn't reach before.
**Skills teach judgment** — tell Claude *how* to use those capabilities for your workflows.
**Subagents isolate execution** — run complex tasks in their own space, return only what matters.
**Hooks enforce standards** — guarantee rules are followed on every action, every time.
**Skills / Commands remove friction** — package a whole workflow into a single slash command (commands and skills are unified).

### Example: A testing workflow

Five primitives, five roles, one workflow:

1. **Playwright MCP** gives Claude browser automation. Without it, Claude can't interact with your web app at all. *(capability)*
2. **A testing skill** defines your team's test patterns — which pages to test, how to write assertions, what edge cases matter. Claude now knows *what* to test and *how*. *(judgment)*
3. **A subagent** picks up the actual test run. It spins up with Playwright access, executes the browser tests, works through all the verbose output — logs, screenshots, assertion details — and returns only the verdict: what passed, what failed, and why. Your main conversation stays clean. *(isolation)*
4. **A PostToolUse hook** fires after every file Claude writes during the fix. It runs the linter automatically — every file, every time, no exceptions. *(enforcement)*
5. **`/test`** triggers this entire flow with one command. *(friction removal)*

Each primitive does one thing. Together, they compose into something none of them could do alone.

<!-- Visualization: Horizontal flow diagram, five connected stages left to right:
MCP "Add capability" → Skill "Teach judgment" → Subagent "Isolate execution" → Hook "Enforce rules" → Command "Remove friction"
Below, concrete mapping row:
"Playwright" → "Test patterns" → "Run tests, return results" → "Auto-lint on fix" → "/test"
The Subagent box has a dashed border to convey isolation. -->

## Beyond Interactive Use

The primitives work in interactive sessions — but Claude Code goes further. Four capabilities take it beyond a tool you chat with.

### Plugins — Ship your setup as one package

Skills, subagents, hooks, and MCP server configs can be bundled into a plugin: a single directory with a manifest (`plugin.json`) and folders for each primitive. One install command wires everything up. Distribute plugins via git-based marketplaces or load them locally during development. Instead of telling teammates "add this skill, configure that hook, connect this MCP server" — you hand them one plugin.

### Headless mode — Script it like any CLI tool

Run Claude Code non-interactively with `claude -p "your prompt"`. Pipe input, get structured JSON output, chain sessions. Use it in shell scripts, CI/CD pipelines, batch processing. Constrain which tools it may use, append system prompts, resume previous sessions by ID. Claude Code becomes a programmable building block in your automation.

### Claude Agent SDK — Build your own agents

The same agentic loop that powers Claude Code, available as a Python and TypeScript library. Built-in tools — file operations, shell, search — work out of the box without implementing a tool loop. Define hooks, subagents, and MCP connections programmatically. Build custom agents for code review, research, compliance, debugging — anything that benefits from the gather-act-verify cycle running in your own application.

### Extensions — The browser is part of the loop

Anthropic provides a growing ecosystem of extensions that connect Claude Code to the tools around it — VS Code, JetBrains, GitHub Actions, a desktop app. The standout: the **Claude in Chrome** extension. Standalone, it's a browser assistant. Paired with Claude Code, it becomes a built-in browser MCP server that lets the agent see, click, and interact with any page you're logged into — no API keys, no Selenium setup. Build a UI in the terminal, verify it in the browser, fix the code, verify again — all in one session. The same agentic loop, extended into the browser.

<!-- Visualization: Four equal-weight cards or columns side by side:
Plugins (package icon) — "Bundle & distribute"
Headless CLI (terminal icon) — "Script & automate"
Agent SDK (code icon) — "Build custom agents"
Extensions (browser icon) — "See & interact"
Shared header above: "Beyond interactive use." -->

## The Bottom Line

Claude Code isn't just a coding assistant — it's a platform for building agent-driven workflows. Text files define the behavior. Git carries it across your team. Plugins package it for distribution. The CLI and SDK let you build on top of it.

The agent loop runs the same whether you're in the terminal, VS Code, or a CI pipeline. What you customize travels with the project, not the editor.

---

## Sources

- [How Claude Code Works — Claude Code Docs](https://code.claude.com/docs/en/how-claude-code-works)
- [Best Practices for Claude Code — Claude Code Docs](https://code.claude.com/docs/en/best-practices)
- [Building Effective AI Agents — Anthropic Research](https://www.anthropic.com/research/building-effective-agents)
- [Building Agents with the Claude Agent SDK — Anthropic Blog](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)
- [Claude Code: Headless Usage — Claude Code Docs](https://code.claude.com/docs/en/headless)
- [Agent SDK Overview — Claude Docs](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Create Plugins — Claude Code Docs](https://code.claude.com/docs/en/plugins)
- [Plugins Reference — Claude Code Docs](https://code.claude.com/docs/en/plugins-reference)
- [Use Claude Code with Chrome — Claude Code Docs](https://code.claude.com/docs/en/chrome)
- [Piloting Claude in Chrome — Anthropic Blog](https://claude.com/blog/claude-for-chrome)
