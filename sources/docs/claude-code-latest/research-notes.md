# Claude Code Documentation — Research Notes

> Collected 2026-02-23 from the official Claude Code documentation at code.claude.com/docs/en/

## Pages Visited

1. https://code.claude.com/docs/en/overview — Claude Code Overview
2. https://code.claude.com/docs/en/memory — Manage Claude's Memory (CLAUDE.md)
3. https://code.claude.com/docs/en/skills — Extend Claude with Skills
4. https://code.claude.com/docs/en/hooks — Hooks Reference
5. https://code.claude.com/docs/en/sub-agents — Create Custom Subagents
6. https://code.claude.com/docs/en/agent-teams — Orchestrate Teams of Claude Code Sessions
7. https://code.claude.com/docs/en/mcp — Connect Claude Code to Tools via MCP
8. https://code.claude.com/docs/en/settings — Claude Code Settings
9. https://code.claude.com/docs/en/best-practices — Best Practices for Claude Code
10. https://code.claude.com/docs/en/cli-reference — CLI Reference
11. https://code.claude.com/docs/en/permissions — Configure Permissions

---

## 1. Overview & Installation

Claude Code is an AI-powered coding assistant that understands entire codebases and works across multiple files and tools. Available on:
- **Terminal CLI** — full-featured, the primary surface
- **VS Code** — inline diffs, @-mentions, plan review, conversation history
- **Desktop app** — standalone, run multiple sessions side by side, cloud sessions
- **Web** (claude.ai/code) — no local setup, long-running tasks, parallel tasks
- **JetBrains** — interactive diff viewing, selection context sharing

### Installation Methods
```bash
# Native (recommended — auto-updates)
curl -fsSL https://claude.ai/install.sh | bash    # macOS / Linux / WSL
irm https://claude.ai/install.ps1 | iex            # Windows PowerShell

# Homebrew (manual updates)
brew install --cask claude-code

# WinGet (manual updates)
winget install Anthropic.ClaudeCode
```

Then `cd your-project && claude` to start.

### Key Capabilities
- Automate tedious tasks (tests, lint, merge conflicts, dependency updates, release notes)
- Build features and fix bugs from natural language descriptions
- Create commits and pull requests directly via git
- Connect external tools via MCP (Google Drive, Jira, Slack, custom tooling)
- Customize with CLAUDE.md instructions, skills, and hooks
- Run agent teams — multiple agents working in parallel with coordination
- Pipe, script, and automate with CLI (composable, Unix philosophy)
- Cross-surface sessions — /teleport between web, terminal, desktop

---

## 2. Memory System (CLAUDE.md)

### Two Kinds of Persistent Memory
1. **Auto memory** — Claude automatically saves useful context (project patterns, key commands, preferences). Stored at `~/.claude/projects/<project>/memory/`. First 200 lines of MEMORY.md loaded at session start.
2. **CLAUDE.md files** — Markdown files you write and maintain with instructions, rules, preferences. Loaded into context at start of every session.

### Memory Hierarchy (highest to lowest specificity)

| Type | Location | Shared With |
|------|----------|-------------|
| Managed policy | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) | All users in org |
| Project memory | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team (via source control) |
| Project rules | `./.claude/rules/*.md` | Team (via source control) |
| User memory | `~/.claude/CLAUDE.md` | Just you (all projects) |
| Project local | `./CLAUDE.local.md` | Just you (current project) |
| Auto memory | `~/.claude/projects/<project>/memory/` | Just you (per project) |

More specific instructions take precedence over broader ones.

### CLAUDE.md Imports
Use `@path/to/import` syntax:
```markdown
See @README for project overview and @package.json for npm commands.
@docs/git-instructions.md
@~/.claude/my-project-instructions.md
```
- Relative and absolute paths supported
- Recursive imports (max 5 hops)
- Not evaluated inside code spans/blocks
- First-time approval dialog per project

### Modular Rules (.claude/rules/)
```
.claude/rules/
├── frontend/
│   ├── react.md
│   └── styles.md
├── backend/
│   ├── api.md
│   └── database.md
└── general.md
```
- All `.md` files automatically loaded as project memory
- Path-specific rules via YAML frontmatter with `paths` field and glob patterns:
```yaml
---
paths:
  - "src/api/**/*.ts"
---
```
- Symlinks supported
- User-level rules in `~/.claude/rules/`

### Auto Memory Details
- Enable/disable: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0` (on) or `=1` (off)
- MEMORY.md acts as index; topic files loaded on demand
- `/memory` command to open files in editor
- Tell Claude to save: "remember that we use pnpm, not npm"

---

## 3. Skills System

Skills extend what Claude can do. Create a SKILL.md with instructions, and Claude adds it to its toolkit. Invoked by user with /skill-name or automatically by Claude when relevant.

### Skill Locations (priority order)
1. Enterprise — managed settings (all users in org)
2. Personal — `~/.claude/skills/<name>/SKILL.md` (all projects)
3. Project — `.claude/skills/<name>/SKILL.md` (current project)
4. Plugin — `<plugin>/skills/<name>/SKILL.md` (where plugin enabled)

### Skill Structure
```
my-skill/
├── SKILL.md          # Main instructions (required)
├── template.md       # Template for Claude to fill in
├── examples/
│   └── sample.md     # Example output
└── scripts/
    └── validate.sh   # Script Claude can execute
```

### SKILL.md Frontmatter Fields
```yaml
---
name: my-skill                    # Display name (optional, defaults to dir name)
description: What this does       # Recommended — helps Claude decide when to use
argument-hint: [issue-number]     # Hint for autocomplete
disable-model-invocation: true    # Only user can invoke (not Claude)
user-invocable: false             # Only Claude can invoke (hidden from / menu)
allowed-tools: Read, Grep, Glob   # Tool restrictions
model: sonnet                     # Model override
context: fork                     # Run in forked subagent context
agent: Explore                    # Agent type when context: fork
hooks: ...                        # Lifecycle hooks scoped to skill
---
```

### String Substitutions
- `$ARGUMENTS` — all arguments passed
- `$ARGUMENTS[N]` or `$N` — specific argument by index
- `${CLAUDE_SESSION_ID}` — current session ID

### Dynamic Context Injection
Use `!`command`` to run shell commands before content sent to Claude:
```yaml
---
name: pr-summary
context: fork
agent: Explore
---
## PR context
- PR diff: !`gh pr diff`
- Changed files: !`gh pr diff --name-only`
```

### Skills in Subagents (context: fork)
When `context: fork` is set, skill content becomes the prompt driving a subagent. The `agent` field determines agent type (Explore, Plan, general-purpose, or custom).

### Permission Control
- `Skill(name)` — exact match
- `Skill(name *)` — prefix match with any args
- Skills follow Agent Skills open standard

---

## 4. Hooks System

Hooks are user-defined shell commands or LLM prompts that execute at specific points in Claude Code's lifecycle. Three types: command, prompt, agent.

### Hook Events (lifecycle order)

| Event | When | Can Block? |
|-------|------|-----------|
| SessionStart | Session begins/resumes | No |
| UserPromptSubmit | User submits prompt | Yes |
| PreToolUse | Before tool call | Yes |
| PermissionRequest | Permission dialog appears | Yes |
| PostToolUse | After tool succeeds | No |
| PostToolUseFailure | After tool fails | No |
| Notification | Claude sends notification | No |
| SubagentStart | Subagent spawned | No |
| SubagentStop | Subagent finishes | Yes |
| Stop | Claude finishes responding | Yes |
| TeammateIdle | Agent team teammate about to idle | Yes |
| TaskCompleted | Task being marked completed | Yes |
| ConfigChange | Config file changes | Yes (except policy) |
| WorktreeCreate | Worktree created | Yes |
| WorktreeRemove | Worktree removed | No |
| PreCompact | Before compaction | No |
| SessionEnd | Session terminates | No |

### Hook Configuration Locations
- `~/.claude/settings.json` — all projects
- `.claude/settings.json` — single project (committable)
- `.claude/settings.local.json` — single project (gitignored)
- Managed policy settings — org-wide
- Plugin `hooks/hooks.json` — when plugin enabled
- Skill/agent frontmatter — while component active

### Hook Handler Types
1. **Command** (`type: "command"`) — runs shell script; receives JSON on stdin
2. **Prompt** (`type: "prompt"`) — sends prompt to Claude model for yes/no decision
3. **Agent** (`type: "agent"`) — spawns subagent with tool access to verify conditions

### Exit Codes
- **Exit 0** — success, proceed; stdout parsed for JSON
- **Exit 2** — blocking error; stderr fed back as error
- **Any other** — non-blocking error; continues

### Key Features
- Matchers: regex strings filtering when hooks fire (tool name, session source, etc.)
- Async hooks: `"async": true` — runs in background without blocking
- `CLAUDE_ENV_FILE` — SessionStart hooks can persist environment variables
- `CLAUDE_PROJECT_DIR` / `${CLAUDE_PLUGIN_ROOT}` — reference scripts by path
- `once: true` — runs only once per session (skills only)
- `/hooks` interactive menu for managing hooks

### PreToolUse Decision Control
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "Reason",
    "updatedInput": { "field": "new value" },
    "additionalContext": "Extra info for Claude"
  }
}
```

---

## 5. Subagents

Subagents are specialized AI assistants running in their own context window with custom system prompt, specific tool access, and independent permissions.

### Built-in Subagents
| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| Explore | Haiku | Read-only | File discovery, code search, codebase exploration |
| Plan | Inherit | Read-only | Codebase research for planning |
| general-purpose | Inherit | All tools | Complex research, multi-step operations |
| Bash | Inherit | — | Running terminal commands in separate context |
| Claude Code Guide | Haiku | — | Answering questions about Claude Code features |

### Custom Subagent Configuration
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
model: sonnet
permissionMode: default
maxTurns: 50
skills:
  - api-conventions
mcpServers:
  - slack
memory: user
background: false
isolation: worktree
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
---
Your system prompt here...
```

### Subagent Scopes (priority order)
1. `--agents` CLI flag (current session only)
2. `.claude/agents/` (current project)
3. `~/.claude/agents/` (all projects)
4. Plugin's `agents/` directory

### Key Features
- Foreground vs background execution
- Auto-compaction at ~95% capacity (configurable via CLAUDE_AUTOCOMPACT_PCT_OVERRIDE)
- Resume subagents by agent ID
- Persistent memory with `memory: user|project|local`
- `isolation: worktree` for isolated git worktrees
- Cannot spawn other subagents (no nesting)
- Restrict spawnable agents: `tools: Task(worker, researcher)`

---

## 6. Agent Teams

Agent teams coordinate multiple Claude Code instances working together. One session = team lead; others = teammates. **Experimental** — enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

### Architecture
- **Team lead** — main session, creates team, spawns/coordinates teammates
- **Teammates** — separate Claude Code instances, each in own context window
- **Task list** — shared work items teammates claim and complete
- **Mailbox** — messaging system for inter-agent communication

### Key Features
- Shared task list at `~/.claude/tasks/{team-name}/`
- Team config at `~/.claude/teams/{team-name}/config.json`
- Two display modes: in-process (default) or split panes (tmux/iTerm2)
- Direct teammate messaging (Shift+Down to cycle)
- Plan approval for teammates before implementation
- TeammateIdle and TaskCompleted hooks for quality gates
- Self-claiming tasks from shared list

### Best Use Cases
- Research and review (parallel investigation)
- New modules/features (independent ownership)
- Debugging with competing hypotheses
- Cross-layer coordination (frontend, backend, tests)

### Comparison: Subagents vs Agent Teams

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| Context | Own window; results return to caller | Own window; fully independent |
| Communication | Report back to main agent only | Teammates message each other directly |
| Coordination | Main agent manages all work | Shared task list, self-coordination |
| Token cost | Lower (summarized) | Higher (each teammate = separate instance) |

---

## 7. MCP (Model Context Protocol)

MCP is an open standard for connecting AI tools to external data sources. Supports hundreds of integrations.

### Transport Types
1. **HTTP** (recommended for remote): `claude mcp add --transport http <name> <url>`
2. **SSE** (deprecated): `claude mcp add --transport sse <name> <url>`
3. **stdio** (local processes): `claude mcp add <name> -- <command> [args...]`

### Scopes
- **Local** (default) — private, current project only, stored in `~/.claude.json`
- **Project** — shared via `.mcp.json` in project root (committable)
- **User** — available across all projects, stored in `~/.claude.json`

### Key Commands
```bash
claude mcp add --transport http <name> <url>
claude mcp add --transport stdio <name> -- <command>
claude mcp list
claude mcp get <name>
claude mcp remove <name>
claude mcp add-from-claude-desktop   # Import from Claude Desktop
claude mcp add-json <name> '<json>'  # From JSON config
claude mcp serve                      # Use Claude Code as MCP server
/mcp                                  # In-session: status, auth, manage
```

### Features
- OAuth 2.0 authentication for remote servers
- Environment variable expansion in `.mcp.json`: `${VAR}` and `${VAR:-default}`
- Plugin-provided MCP servers
- `@server:protocol://resource/path` for referencing MCP resources
- MCP Tool Search — auto-enables when tools exceed 10% of context window
- MCP prompts as commands: `/mcp__servername__promptname`
- Managed MCP configuration for organizations
- `MAX_MCP_OUTPUT_TOKENS` env var (default 25,000)
- `MCP_TIMEOUT` for startup timeout

---

## 8. Settings & Configuration

### Settings Hierarchy (highest to lowest precedence)
1. Managed — `/Library/Application Support/ClaudeCode/managed-settings.json` (macOS)
2. Command line arguments
3. Local — `.claude/settings.local.json`
4. Project — `.claude/settings.json`
5. User — `~/.claude/settings.json`

### Key Settings Categories

**Core**: `model`, `availableModels`, `language`, `outputStyle`, `cleanupPeriodDays`, `env`

**Permissions**: `allow`, `ask`, `deny` arrays with tool/specifier rules

**Sandbox**: `enabled`, `autoAllowBashIfSandboxed`, `network.allowedDomains`

**Attribution**: `commit` and `pr` templates for git

**Plugins**: `enabledPlugins`, `extraKnownMarketplaces`

### Permission Rule Syntax
```
Tool                        — matches all uses
Tool(specifier)             — matches specific uses
Bash(npm run *)             — wildcard patterns
Read(./.env)                — file path
Read(src/**)                — recursive glob
WebFetch(domain:example.com) — domain filter
Task(Explore)               — subagent control
Skill(commit)               — skill control
mcp__server__tool           — MCP tool
```

Evaluation order: deny → ask → allow (first match wins)

### Permission Modes
| Mode | Description |
|------|-------------|
| default | Standard prompts for permission |
| acceptEdits | Auto-accept file edits |
| plan | Read-only analysis |
| dontAsk | Auto-deny unless pre-approved |
| bypassPermissions | Skip all checks (use in containers only) |

### Key Environment Variables
- `ANTHROPIC_API_KEY` — API key
- `ANTHROPIC_MODEL` — model override
- `CLAUDE_CODE_EFFORT_LEVEL` — low/medium/high
- `CLAUDE_CODE_MAX_OUTPUT_TOKENS` — max output (default 32K, max 64K)
- `CLAUDE_CODE_AUTOCOMPACT_PCT_OVERRIDE` — auto-compaction threshold
- `CLAUDE_CODE_SHELL` — override shell detection
- `MAX_THINKING_TOKENS` — extended thinking budget
- `CLAUDE_CODE_DISABLE_AUTO_MEMORY` — 0=on, 1=off
- `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` — 1=disable
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` — 1=enable
- `ENABLE_TOOL_SEARCH` — auto/true/false
- `CLAUDE_CODE_SIMPLE` — minimal mode (bash, read, edit only)

---

## 9. CLI Reference

### Core Commands
```bash
claude                       # Start interactive REPL
claude "query"               # Start with initial prompt
claude -p "query"            # Print mode (non-interactive)
claude -c                    # Continue most recent conversation
claude -r "session" "query"  # Resume specific session
claude update                # Update to latest version
claude agents                # List configured subagents
claude mcp                   # Configure MCP servers
```

### Key Flags
- `--model` — set model (sonnet, opus, haiku, or full name)
- `--permission-mode` — start in specific mode
- `--allowedTools` / `--disallowedTools` — tool permissions
- `--tools` — restrict which tools available
- `--system-prompt` — replace entire system prompt
- `--append-system-prompt` — add to default prompt
- `--output-format` — text, json, stream-json
- `--max-turns` — limit agentic turns
- `--max-budget-usd` — spending cap
- `--agent` — specify agent for session
- `--agents` — define subagents via JSON
- `--worktree` / `-w` — isolated git worktree
- `--add-dir` — additional working directories
- `--chrome` — enable Chrome browser integration
- `--remote` — create web session on claude.ai
- `--teleport` — resume web session locally
- `--debug` — debug mode with category filtering
- `--verbose` — verbose logging
- `--json-schema` — structured output validation
- `--mcp-config` — load MCP servers from JSON
- `--fallback-model` — auto-fallback on overload

---

## 10. Best Practices

### Core Principles
1. **Give Claude a way to verify its work** — tests, screenshots, expected outputs. Single highest-leverage practice.
2. **Explore first, plan, then code** — use Plan Mode to separate research from implementation.
3. **Provide specific context** — reference files, mention constraints, point to patterns.
4. **Manage context aggressively** — `/clear` between tasks, use subagents for investigation.

### Effective CLAUDE.md
- Run `/init` to generate starter file
- Keep concise — only include what Claude can't infer from code
- Include: bash commands, code style, testing instructions, architecture decisions
- Exclude: standard conventions, detailed API docs, information that changes often
- Check into git, treat like code
- Prune regularly — if Claude ignores rules, file is too long

### Workflow Recommendations
- **Plan Mode** (Ctrl+G): Explore → Plan → Implement → Commit
- **Subagents** for investigation: "use subagents to investigate X"
- **Rewind/checkpoints**: Esc+Esc or /rewind to restore state
- **Session management**: /clear, /compact, /rename, --continue, --resume
- **Rich input**: @ for files, paste images, pipe data, give URLs

### Scaling Patterns
- **Headless mode**: `claude -p "prompt"` for CI/scripts
- **Parallel sessions**: Desktop app, web, or agent teams
- **Fan-out**: Loop `claude -p` across file list with `--allowedTools`
- **Writer/Reviewer pattern**: Session A writes, Session B reviews
- **Auto mode**: `--dangerously-skip-permissions` in sandboxed containers only

### Common Failure Patterns
1. Kitchen sink session — mixing unrelated tasks in one context
2. Over-correcting — fix: `/clear` and write better initial prompt
3. Over-specified CLAUDE.md — too long = rules get ignored
4. Trust-then-verify gap — no verification = unreliable output
5. Infinite exploration — unscoped investigation fills context

---

## 11. Plugins (Referenced)

Plugins bundle skills, hooks, subagents, and MCP servers into installable units. Available via `/plugin` marketplace. Code intelligence plugins give Claude precise symbol navigation.

Plugin components:
- skills/ — skill files
- agents/ — subagent definitions
- hooks/hooks.json — hook configuration
- .mcp.json — MCP server configs
- plugin.json — manifest

---

## 12. Notable New Features

### Docs URL Change
The official docs have moved from docs.anthropic.com to **code.claude.com/docs/en/**

### Agent Skills Open Standard
Skills now follow the Agent Skills open standard, working across multiple AI tools.

### Cross-Surface Sessions
Sessions can move between Terminal, Web, Desktop, and iOS:
- `/teleport` — bring web session to terminal
- `/desktop` — hand off terminal to desktop app
- `--remote` — start web session from CLI
- Slack integration with @Claude

### MCP Tool Search
Automatically enables when MCP tools exceed context budget. Uses `tool_reference` blocks. Configurable via `ENABLE_TOOL_SEARCH`.

### Sandbox Mode
OS-level isolation for Bash commands:
```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "network": { "allowedDomains": ["github.com"] }
  }
}
```

### Auto Memory (Gradual Rollout)
Claude automatically saves project patterns, debugging insights, and preferences. Enable with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0`.

### Subagent Persistent Memory
Subagents can maintain memory across sessions:
```yaml
memory: user    # or project, local
```

### Prompt & Agent Hooks
Beyond shell command hooks, now support:
- `type: "prompt"` — LLM-based evaluation
- `type: "agent"` — multi-turn subagent verification

### Agent Teams (Experimental)
Full multi-agent coordination with team lead, shared task list, messaging, and parallel work. Enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

### Git Worktree Isolation
`--worktree` flag or `isolation: "worktree"` for subagents creates isolated repo copies.

### Desktop App
Standalone app for managing multiple sessions visually with isolated worktrees.

### Web (claude.ai/code)
Run Claude Code in browser with no local setup. Long-running tasks, parallel execution.

### JSON Schema Output
`--json-schema` flag for validated structured output in print mode.

### Extended Thinking
`alwaysThinkingEnabled` setting; `MAX_THINKING_TOKENS` env var; "ultrathink" keyword in skills.
