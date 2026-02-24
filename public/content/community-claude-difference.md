# What Makes Claude Code Different

*Frontend Community Day*

Not another autocomplete. A terminal-native agent with a composable extension system.

## The Core Shift

### Architecture: Terminal-native, not IDE-embedded

Lives in your terminal. Unrestricted filesystem access, process spawning, native Unix composability. Editors integrate it -- VS Code, JetBrains, desktop app -- but it's not embedded in them.

### Interaction: Agentic loop, not tab-completion

Reasons, invokes tools, observes results, continues. Multi-step problem solving by default. Reads files, runs tests, fixes errors -- autonomously.

### Extensibility: Text files, not a plugin SDK

Four extension primitives compose via markdown and JSON. No proprietary API, no binary plugins. Everything lives in `.claude/` and commits to git.

### Context: 200K tokens, full codebase

Operates on your entire project directory. No artificial file limits, no copying code into a chat window. 200K context window with efficient tool use.

## Four Extensibility Pillars

### Commands (Manual trigger)

Prompt templates as markdown files. Type `/deploy`, get a repeatable instruction set. Saves typing.

### Skills (Auto-trigger)

Knowledge modules that auto-activate when context matches. Teach Claude your domain workflows and conventions.

### Hooks (Event-trigger)

Shell commands that fire on lifecycle events (PreToolUse, PostToolUse, Stop). Enforce guardrails, auto-format, gate completions.

### MCP Servers (Always-on)

External servers that add entirely new capabilities. Browser automation, databases, APIs. JSON config, always available.

## How They Compose

MCP adds tools --> Skills teach judgment --> Hooks enforce rules --> Commands remove friction

**Example:** A Playwright MCP connects Claude to browsers (capability). A testing skill teaches your test patterns (knowledge). A PostToolUse hook runs the linter after every file write (enforcement). `/test` packages the whole workflow (shortcut).

MCP expands reach. Skills sharpen judgment. Hooks enforce standards. Commands remove friction.

---

**The whole system is text files you can commit to git.** No proprietary lock-in. Your customizations travel with the project, not the editor. Any teammate who clones the repo gets the same agent behavior.
