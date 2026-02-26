# Claude Code Reference

Everything you need to use Claude Code effectively — from installation to agent teams, in one page.

## Overview & Installation

AI coding agent that understands entire codebases. Terminal-native, editor-integrated, composable via Unix pipes.

### Surfaces

- **Terminal CLI** — primary, full-featured
- **VS Code** — inline diffs, @-mentions, plan review
- **JetBrains** — diff viewer, selection sharing
- **Desktop app** — multiple sessions, cloud sessions
- **Web** (claude.ai/code) — no local setup, parallel tasks

### Key Capabilities

- Build features and fix bugs from natural language
- Create commits and PRs directly via git
- Connect external tools via MCP
- Run agent teams — parallel coordination
- Pipe, script, automate with `claude -p`
- `/teleport` sessions across surfaces

### Installation

```bash
# Install (auto-updates)
curl -fsSL https://claude.ai/install.sh | bash    # macOS / Linux / WSL
irm https://claude.ai/install.ps1 | iex            # Windows PowerShell

# Homebrew (manual updates)
brew install --cask claude-code

# Start
cd your-project && claude
```

## Memory System (CLAUDE.md)

Two types of persistent memory: auto memory (Claude saves context automatically) and CLAUDE.md files (you write and maintain). Both loaded at session start.

### Hierarchy (highest to lowest specificity)

| # | Layer | Location | Scope |
|---|-------|----------|-------|
| 1 | Managed policy | Org-wide CLAUDE.md | All users |
| 2 | Project CLAUDE.md | `./CLAUDE.md` or `.claude/CLAUDE.md` | Team (git) |
| 3 | Project rules | `.claude/rules/*.md` with optional path globs | Team (git) |
| 4 | User CLAUDE.md | `~/.claude/CLAUDE.md` | All projects |
| 5 | Project local | `./CLAUDE.local.md` (gitignored) | Just you |
| 6 | Auto memory | `~/.claude/projects/<project>/memory/` | Just you |

### Imports

Use `@path/to/file` to include external content. Relative and absolute paths supported. Recursive imports up to 5 hops. Not evaluated inside code blocks.

```
# In CLAUDE.md:
See @README for project overview.
@docs/git-instructions.md
@~/.claude/my-project-rules.md
```

### Modular Rules

All `.md` files in `.claude/rules/` auto-loaded. Use YAML frontmatter with `paths` for file-scoped rules. User-level rules at `~/.claude/rules/`.

```yaml
# .claude/rules/api.md
---
paths:
  - "src/api/**/*.ts"
---
Always validate input with zod.
```

> **Auto memory:** Enable with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0`. MEMORY.md acts as index (first 200 lines loaded). Topic files loaded on demand. Use `/memory` to edit.

## Skills

Self-contained knowledge packages that extend Claude. Create a SKILL.md with instructions; invoke manually with `/skill-name` or let Claude auto-trigger by matching the description.

### Skill Locations (priority order)

- **Enterprise** — managed settings (org-wide)
- **Personal** — `~/.claude/skills/<name>/`
- **Project** — `.claude/skills/<name>/`
- **Plugin** — via installed plugin

### File Structure

```
my-skill/
├── SKILL.md          # Instructions (required)
├── template.md       # Template to fill in
├── examples/
│   └── sample.md     # Example output
└── scripts/
    └── validate.sh   # Executable script
```

### Key Frontmatter Fields

| Field | Purpose |
|-------|---------|
| `description` | Helps Claude decide when to auto-trigger. Write like a search query. |
| `argument-hint` | Autocomplete hint shown in `/` menu, e.g. `[issue-number]` |
| `disable-model-invocation` | Only user can invoke (`/name`), not Claude |
| `user-invocable: false` | Hidden from `/` menu — only Claude triggers it |
| `allowed-tools` | Restrict tool access: `Read, Grep, Glob` |
| `model` | Override model: `sonnet`, `haiku`, `opus` |
| `context: fork` | Run in forked subagent context (isolated window) |
| `agent` | Agent type when forked: `Explore`, `Plan`, `general-purpose` |

### String Substitutions

- `$ARGUMENTS` — all arguments passed
- `$ARGUMENTS[N]` / `$N` — by index
- `${CLAUDE_SESSION_ID}` — session ID

### Dynamic Context

Use `` !`command` `` in SKILL.md body to inject shell command output before the skill content is sent to Claude.

```
PR diff: !`gh pr diff`
Files: !`gh pr diff --name-only`
```

## Hooks

User-defined shell commands or LLM prompts that fire at lifecycle events. Three handler types: **command** (shell script), **prompt** (LLM yes/no), **agent** (multi-turn subagent).

### Lifecycle Events

Events marked with * can block execution (exit code 2 = block with error).

- SessionStart — Session begins/resumes
- UserPromptSubmit* — User submits prompt
- PreToolUse* — Before tool call
- PermissionRequest* — Permission dialog appears
- PostToolUse — After tool succeeds
- PostToolUseFailure — After tool fails
- Notification — Claude sends notification
- SubagentStart/Stop — Subagent spawned/finished
- Stop* — Claude finishes responding
- TeammateIdle* — Agent about to idle
- TaskCompleted* — Task marked completed
- PreCompact — Before compaction
- ConfigChange* — Config file changed
- WorktreeCreate* — Worktree created
- SessionEnd — Session terminates

### Exit Codes

- **Exit 0** — success, proceed; stdout parsed for JSON
- **Exit 2** — blocking error; stderr fed back
- **Other** — non-blocking error; continues

### Key Features

- Regex matchers filter by tool name, session source
- `"async": true` — non-blocking background execution
- `CLAUDE_ENV_FILE` — persist env vars from SessionStart
- `/hooks` — interactive management menu

> **PreToolUse decision control:** Output JSON with `permissionDecision: "allow|deny|ask"`, `updatedInput` to modify tool parameters, and `additionalContext` to inform Claude.

## Subagents

Specialized AI assistants running in isolated context windows. Each gets its own system prompt, tool access, and permissions. Cannot nest (no subagent-of-subagent).

### Built-in Agents

| Agent | Model | Access | Purpose |
|-------|-------|--------|---------|
| Explore | haiku | read-only | File discovery, code search, codebase exploration. Fast and cheap. |
| Plan | inherit | read-only | Codebase research for planning. Returns investigation summaries. |
| general-purpose | inherit | all tools | Complex research, multi-step operations. Full tool access. |
| Bash | inherit | terminal | Running terminal commands in a separate context window. |

### Custom Subagent Config

```yaml
# .claude/agents/code-reviewer.md
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
model: sonnet
maxTurns: 50
memory: user                 # persistent across sessions
isolation: worktree           # git worktree isolation
background: false
---
Your system prompt here...
```

> **Scope priority:** `--agents` CLI flag > `.claude/agents/` (project) > `~/.claude/agents/` (user) > plugin agents. Restrict which agents can be spawned with `tools: Task(worker, researcher)`.

## Agent Teams

Multiple Claude Code instances working together. One session leads, others are teammates with their own context windows. **Experimental** — enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

### Architecture

- **Team lead** — main session, creates team, coordinates
- **Teammates** — separate instances, own context
- **Task list** — shared work items agents claim
- **Mailbox** — inter-agent messaging system

### Best Use Cases

- Parallel investigation across modules
- Independent feature ownership
- Competing hypotheses for debugging
- Cross-layer work (frontend + backend + tests)

### Subagents vs Agent Teams

**Subagents:**
- Own context window; results return to caller
- Report back to main agent only
- Main agent manages all work
- Lower token cost (summarized returns)
- Good for: investigation, review, batch

**Agent Teams:**
- Fully independent context windows
- Teammates message each other directly
- Shared task list, self-coordination
- Higher token cost (separate instances)
- Good for: parallel features, multi-layer work

## MCP (Model Context Protocol)

Open standard for connecting Claude to external tools and data sources. HTTP (recommended for remote), SSE (deprecated), and stdio (local processes).

```bash
# Add servers
claude mcp add --transport http myserver https://example.com/mcp
claude mcp add local-tool -- npx @tool/server
claude mcp add-from-claude-desktop     # import from Claude Desktop
claude mcp add-json name '{"command": "npx", "args": [...]}'

# Manage
claude mcp list
claude mcp get name
claude mcp remove name
claude mcp serve              # use Claude Code as MCP server
/mcp                           # in-session: status, auth, manage
```

### Scopes

- **Local** (default) — private, in `~/.claude.json`
- **Project** — shared via `.mcp.json` (committable)
- **User** — all projects, in `~/.claude.json`

### Features

- OAuth 2.0 authentication for remote servers
- Env var expansion in `.mcp.json`: `${VAR:-default}`
- Tool Search — auto-enables when tools exceed context budget
- MCP prompts as commands: `/mcp__server__prompt`
- `MAX_MCP_OUTPUT_TOKENS` (default 25,000)

## Settings & Permissions

JSON-based configuration with a clear precedence hierarchy. Permission rules evaluated in order: deny → ask → allow (first match wins).

### Settings Precedence

| # | Source | Location |
|---|--------|----------|
| 1 | Managed (org) | System-level managed-settings.json |
| 2 | CLI arguments | `--model`, `--permission-mode`, etc. |
| 3 | Local project | `.claude/settings.local.json` |
| 4 | Project | `.claude/settings.json` |
| 5 | User | `~/.claude/settings.json` |

### Permission Evaluation

deny[] → ask[] → allow[] → first match wins

### Rule Syntax

```
Tool                        # matches all uses of tool
Tool(specifier)             # matches specific use
Bash(npm run *)             # wildcard patterns
Read(./.env)                # file path
Read(src/**)                # recursive glob
WebFetch(domain:example.com) # domain filter
Task(Explore)               # subagent control
Skill(commit)               # skill control
mcp__server__tool           # MCP tool
```

### Permission Modes

| Mode | Behavior |
|------|----------|
| default | Standard prompts for each tool call |
| acceptEdits | Auto-accept file edits, prompt for others |
| plan | Read-only analysis, no writes |
| dontAsk | Auto-deny unless pre-approved in allow[] |
| bypassPermissions | Skip all checks (sandboxed containers only) |

> **Sandbox mode:** OS-level isolation for Bash. Enable with `"sandbox": {"enabled": true}`. Auto-allow bash when sandboxed with `autoAllowBashIfSandboxed`. Restrict network with `allowedDomains`.

## CLI Reference

Core commands and flags for terminal usage. Composable with pipes, loops, and scripts.

### Core Commands

```bash
claude                    # interactive REPL
claude "query"            # start with prompt
claude -p "query"         # print mode (non-interactive)
claude -c                 # continue last conversation
claude -r "id" "query"   # resume specific session
claude update             # update to latest
claude agents             # list subagents
claude mcp                # configure MCP
```

### Session Commands

```
/clear       # reset context window
/compact     # compress context (+ focus)
/rewind      # restore previous state
/rename      # rename session
/teleport    # move session across surfaces
/desktop     # hand off to desktop app
/memory      # edit memory files
/hooks       # manage hooks
/mcp         # MCP status & management
/init        # generate starter CLAUDE.md
```

### Key Flags

| Flag | Purpose |
|------|---------|
| `--model` | Set model (sonnet, opus, haiku, or full ID) |
| `--permission-mode` | Start in specific permission mode |
| `--allowedTools` | Whitelist specific tools for this session |
| `--max-turns` | Limit agentic turns (good for batch scripts) |
| `--max-budget-usd` | Spending cap for the session |
| `--output-format` | `text`, `json`, `stream-json` |
| `--json-schema` | Structured output with validation (print mode) |
| `--worktree` | Isolated git worktree for the session |
| `--agent` | Specify which agent to use |
| `--add-dir` | Additional working directories |
| `--chrome` | Enable Chrome browser integration |
| `--remote` | Create web session on claude.ai |
| `--debug` | Debug mode with category filtering |
| `--fallback-model` | Auto-fallback on overload |

### Key Environment Variables

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | API key for authentication |
| `ANTHROPIC_MODEL` | Model override |
| `CLAUDE_CODE_EFFORT_LEVEL` | `low` / `medium` / `high` |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output (default 32K, max 64K) |
| `CLAUDE_CODE_AUTOCOMPACT_PCT_OVERRIDE` | Auto-compaction threshold |
| `MAX_THINKING_TOKENS` | Extended thinking budget |
| `CLAUDE_CODE_SIMPLE` | Minimal mode (bash, read, edit only) |
| `ENABLE_TOOL_SEARCH` | MCP tool search: `auto`/`true`/`false` |

## Best Practices

Core principles, workflow patterns, and common failure modes.

### Core Principles

- **Give Claude verification** — tests, screenshots, expected outputs. Single highest-leverage practice.
- **Explore, plan, then code** — Plan Mode (Ctrl+G) separates research from implementation.
- **Provide specific context** — reference files, mention constraints, point to patterns.
- **Manage context aggressively** — `/clear` between tasks, subagents for investigation.

### Effective CLAUDE.md

- Run `/init` to generate starter file
- Only include what Claude can't infer from code
- Include: bash commands, code style, test commands, architecture
- Exclude: standard conventions, detailed API docs, volatile info
- If Claude ignores rules, file is too long — prune

### Workflow Patterns

- **Plan Mode** — Explore → Plan → Implement → Commit
- **Subagent investigation** — "use subagents to investigate X"
- **Rewind** — Esc+Esc or `/rewind` to restore state
- **Rich input** — `@` files, paste images, pipe data, URLs
- **Writer/Reviewer** — Session A writes, Session B reviews

### Scaling Patterns

- **Headless** — `claude -p "prompt"` for CI/scripts
- **Fan-out** — loop `claude -p` across files
- **Parallel sessions** — Desktop, web, or agent teams
- **Auto mode** — `--dangerously-skip-permissions` in sandboxed containers only

### Common Failure Patterns

**Kitchen Sink Session** — Mixing unrelated tasks in one context. Claude confuses which task is current. Fix: `/clear` between tasks. One focused session beats one long session.

**Correction Spiral** — Stacking corrections fills context with wrong approaches. Claude attends to mistakes as much as fixes. Fix: After two corrections, `/clear` and write a better initial prompt.

**Bloated CLAUDE.md** — 200 lines of contradicting rules. When everything is important, nothing is. Fix: Cut to <50 lines. Move domain knowledge to skills and rules files.

**Infinite Exploration** — Unscoped investigation reads 30 files, fills context with irrelevant internals. Fix: Scope investigations to specific files. Delegate open-ended exploration to subagents.

**Trust Without Verification** — No tests, no screenshots, no expected outputs. No way for Claude to self-correct. Fix: Always give Claude a way to verify its work. Tests are the highest-leverage practice.
