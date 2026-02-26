# Claude Code — Vendor Research

> Research compiled from official Anthropic sources (docs, blog, product pages). February 2026.

## Overview

Claude Code is Anthropic's agentic coding tool — a terminal-first AI assistant that reads entire codebases, edits files across projects, runs shell commands, and integrates with development tools via the Model Context Protocol (MCP). Unlike inline autocomplete tools, it operates through an agentic loop: gathering context, taking action, and verifying results across multiple files and systems. Available in the terminal, VS Code, JetBrains, Xcode, a standalone desktop app, the web at claude.ai/code, Slack, and CI/CD pipelines.

## Architecture

### Agentic Loop

Claude Code works through three blended phases per task: **gather context**, **take action**, **verify results**. It chains dozens of tool calls together, course-correcting at each step. The user can interrupt at any point to steer. The underlying model reasons about which tools to invoke; Claude Code provides the harness — tools, context management, execution environment.

Built-in tool categories:
- **File operations**: read, edit, create, rename, reorganize files
- **Search**: find files by glob pattern, search content with regex, explore codebases
- **Execution**: run shell commands, start servers, run tests, use git
- **Web**: search the web, fetch documentation, look up error messages
- **Code intelligence**: type errors/warnings after edits, jump to definitions, find references (via plugins)

### Context Window

Claude Code uses Claude's full context window for reasoning. Multiple models are available — Sonnet for most coding tasks, Opus for complex architectural decisions. Users can switch models mid-session with `/model` or at launch with `--model`. Context is managed automatically: when it fills up, Claude compacts older tool outputs first, then summarizes conversation. Persistent instructions go in `CLAUDE.md` files to survive compaction.

### How It Reads Repositories

When launched in a directory, Claude Code gains access to: all project files and subdirectories, the terminal environment (build tools, git, package managers, scripts), current git state (branch, uncommitted changes, recent history), `CLAUDE.md` project instructions, and any configured extensions (MCP servers, skills, subagents). It can search dependencies, trace imports, identify component relationships, and propose coordinated multi-file diffs.

## MCP (Model Context Protocol) Extensibility

MCP is an open-source standard for connecting AI tools to external data sources and services. Claude Code supports three transport types for MCP servers:

- **HTTP** (recommended): remote cloud-based services via `claude mcp add --transport http`
- **SSE** (deprecated): Server-Sent Events for legacy remote servers
- **stdio**: local processes for tools needing direct system access

### Configuration Scopes

- **Local** (default): private to the user, current project only; stored in `~/.claude.json`
- **Project**: shared via `.mcp.json` in project root, checked into version control
- **User**: available across all projects on the machine

### Key MCP Features

- **OAuth 2.0 authentication** for remote servers requiring login
- **Tool Search**: when MCP tool descriptions exceed 10% of context, tools are deferred and loaded on demand instead of preloaded — configurable via `ENABLE_TOOL_SEARCH` environment variable
- **Dynamic tool updates**: MCP servers can send `list_changed` notifications to update available tools without reconnection
- **MCP resources**: accessible via `@server:protocol://path` mentions in prompts
- **MCP prompts**: exposed as `/mcp__servername__promptname` slash commands
- **Claude Code as MCP server**: `claude mcp serve` exposes Claude Code's tools to other MCP clients
- **Managed MCP**: enterprise admins can deploy `managed-mcp.json` for centralized control, plus allowlist/denylist policies

### Plugin System

Plugins bundle slash commands, subagents, MCP servers, and hooks into shareable packages. Plugin MCP servers start automatically when enabled and support all transport types. Plugins can be pinned to specific git commit SHAs.

## Multi-File Reasoning and Coordinated Diffs

Claude Code's core differentiator is cross-file coordination. It searches for relevant files across the project, reads multiple files to build context, makes coordinated edits across them, runs tests to verify, and commits changes. The agentic loop means it doesn't just suggest — it acts, verifies, and iterates. For complex tasks it breaks work into steps, executes, and adjusts based on results.

## Checkpoint / Rollback Workflow

### Automatic Checkpointing

Every user prompt creates a checkpoint — a snapshot of file state before edits. Checkpoints persist across sessions (cleaned up after 30 days by default). Only file edits made through Claude's editing tools are tracked; bash command side-effects and external changes are not.

### Rewind Menu

Press `Esc` twice or use `/rewind` to open the rewind menu. Actions available at any checkpoint:
- **Restore code and conversation**: revert both to that point
- **Restore conversation**: rewind messages, keep current code
- **Restore code**: revert files, keep conversation
- **Summarize from here**: compress subsequent messages into a summary (frees context window)

### Relationship to Git

Checkpoints are session-level "local undo" — they complement but do not replace git. Claude Code also integrates directly with git: it stages changes, writes commit messages, creates branches, and opens pull requests. Git worktrees enable parallel Claude sessions on separate branches without interference.

## IDE Support

### Terminal (Primary Interface)
Full-featured CLI. Install via native installer (`curl -fsSL https://claude.ai/install.sh | bash`), Homebrew, or WinGet. Supports macOS, Linux, WSL, and native Windows.

### VS Code
Native extension with inline diffs, `@`-mentions of files with line ranges, plan review, conversation history, and multi-tab sessions. Available for VS Code and Cursor. Permission modes: normal (ask before each action), plan mode (describe then approve), auto-accept (edits without asking).

### JetBrains
Plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs. Interactive diff viewing and selection context sharing. Beta status.

### Xcode
Native integration via the Claude Agent SDK (Xcode 26.3+). Full Claude Code capabilities including subagents, background tasks, and plugins. Can capture Xcode Previews to inspect SwiftUI views visually.

### Desktop App
Standalone app for macOS and Windows. Visual diff review, multiple simultaneous sessions, cloud session management.

### Web
Run at claude.ai/code with no local setup. Long-running tasks, remote repos, parallel sessions. Available on desktop browsers and Claude iOS app.

### Additional Surfaces
- **Slack**: mention `@Claude` with a bug report, get a PR back
- **GitHub Actions / GitLab CI/CD**: automated PR reviews, issue triage
- **Chrome**: debug live web applications via Claude in Chrome extension
- **Remote Control**: continue local sessions from phone or any browser

## Pricing and Plans

### Consumer Plans (claude.ai)
- **Pro** ($20/month or $200/year): includes Claude Code access with Sonnet and Opus models
- **Max — Expanded** ($100/month): 5x Pro usage. Priority access to newest features and models
- **Max — Maximum** ($200/month): 20x Pro usage. For daily heavy users

### Business Plans
- **Team**: premium seats bundling Claude + Claude Code. Self-serve seat management, spend controls, usage analytics
- **Enterprise**: premium seats with managed policy settings, compliance API, granular admin controls, centralized billing

### API Access
Claude Code also works with Anthropic Console (API) accounts. Third-party LLM providers are supported for the Terminal CLI and VS Code extension.

## Recent Features and Updates

### Agent Teams (Research Preview)
Multiple Claude Code instances work in parallel on a shared codebase. A lead agent coordinates work, assigns subtasks via a task list, and merges results. Best for tasks that split into independent, read-heavy work.

### Subagents
Delegate specialized tasks to isolated agents with their own context windows. Custom subagents are defined in Markdown files with YAML frontmatter. Each subagent can have custom prompts, tool restrictions, permission modes, hooks, and skills. Built-in subagent types include general-purpose, Explore (fast codebase search), and Plan (architecture design).

### Skills
Folders of instructions, scripts, and resources that Claude loads dynamically when relevant to the current task. Claude auto-discovers and invokes skills — no manual selection needed. Skills can be shared across teams as custom slash commands (e.g., `/review-pr`, `/deploy-staging`). Skills load on demand to minimize context usage.

### Hooks
Shell commands that trigger automatically at specific points in Claude Code's workflow — e.g., run tests after code changes, lint before commits. Hook receives JSON via stdin; exit code 2 blocks the operation and feeds error back to Claude.

### Background Tasks
Long-running processes (dev servers, builds) run without blocking Claude Code's main work. Useful for tasks requiring server startup alongside development.

### Headless / CI Mode
Run Claude Code non-interactively in CI/CD pipelines. GitHub Actions and GitLab CI/CD integrations for automated code review and issue triage.

### Claude Agent SDK
Build fully custom agents powered by Claude Code's tools and capabilities, with control over orchestration, tool access, and permissions. Used by Apple's Xcode integration.

### Session Management
Sessions persist locally. Resume with `--continue`, fork with `--fork-session` to branch exploration without affecting the original. `/teleport` moves sessions between surfaces (terminal → desktop app → web).

## Architectural Comparison with Copilot

| Dimension | Claude Code | GitHub Copilot |
|-----------|-------------|----------------|
| **Primary interface** | Terminal CLI + IDE extensions | Editor-embedded (VS Code, JetBrains, Visual Studio) |
| **Core interaction** | Agentic loop: reason → act → verify | Reactive inline autocomplete + agent mode |
| **Context scope** | Full project via agentic file search | Open files + nearby project files |
| **Extensibility** | MCP (open protocol), plugins, skills, hooks, subagents | GitHub ecosystem (PR summaries, code review, security scanning) |
| **Execution model** | Runs commands, edits files, creates commits autonomously | Suggests code inline; agent mode extends to multi-step tasks |
| **Safety model** | Checkpoints + permission modes + rewind | Editor-integrated undo |
| **Multi-agent** | Agent teams, custom subagents, Agent SDK | Single-agent (Copilot Workspace for multi-step) |
| **Enterprise** | Managed MCP, compliance API, policy controls | Audit logs, content filters, centralized policy, GHEC integration |

The fundamental difference: Copilot augments the editor with fast, pattern-based suggestions. Claude Code operates as an autonomous agent that reasons across the full project, executes multi-step plans, and verifies its own work.

## Sources

- [Claude Code Overview](https://code.claude.com/docs/en/overview) — official docs, features, installation, IDE support
- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works) — agentic loop, tools, context window, architecture
- [Checkpointing](https://code.claude.com/docs/en/checkpointing) — checkpoint system, rewind, session management
- [Connect Claude Code to Tools via MCP](https://code.claude.com/docs/en/mcp) — MCP configuration, scopes, tool search, authentication
- [Claude Code Product Page](https://www.anthropic.com/claude-code) — product overview, positioning
- [Introducing the Max Plan](https://claude.com/blog/max-plan) — Max plan pricing and features
- [Claude Code on Team and Enterprise](https://www.anthropic.com/news/claude-code-on-team-and-enterprise) — business plans, admin controls, compliance API
- [Introducing Agent Skills](https://claude.com/blog/skills) — skills system, discovery, authoring
- [Enabling Claude Code to Work More Autonomously](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously) — subagents, hooks, background tasks, checkpoints
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — custom subagent creation and configuration
- [Claude in Xcode](https://www.anthropic.com/news/claude-in-xcode) — Xcode native integration
- [Apple's Xcode Now Supports the Claude Agent SDK](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk) — Agent SDK in Xcode 26.3
- [Claude Code Plugins](https://www.anthropic.com/news/claude-code-plugins) — plugin system for packaging extensions
- [Remote MCP Support](https://www.anthropic.com/news/claude-code-remote-mcp) — remote MCP server connectivity
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — MCP open standard announcement
- [Plans & Pricing](https://www.anthropic.com/pricing) — all Claude plan pricing
