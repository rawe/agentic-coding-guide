# Custom Subagents

Specialized AI personas with their own context window, tool restrictions, and system prompt — defined as markdown files in your project.

## What Custom Subagents Are

Custom subagents are markdown files that define specialized AI assistants. Each runs in its own context window with an independent system prompt, configurable tool access, and isolated permissions.

- **Isolated context** — Own context window, separate from the main conversation
- **Tool restrictions** — Allowlist or denylist specific tools per agent
- **Model selection** — Use Haiku for cheap tasks, Opus for complex ones

> **How delegation works:** Claude reads the `description` field and automatically delegates matching tasks. You can also explicitly request an agent: `Use the code-reviewer agent to check my changes`.

## File Format

Agent files live in `.claude/agents/` (project) or `~/.claude/agents/` (global). YAML frontmatter defines configuration; the markdown body becomes the system prompt.

<!-- Visualization: Two-column anatomy grid
Left: code block showing a sample agent file with YAML frontmatter and markdown body
Right: three explanation cards stacked vertically:
1. "YAML Frontmatter" — Configuration block between --- fences
2. "Markdown Body" — Everything below becomes the system prompt
3. "File Location" — .claude/agents/ for project, ~/.claude/agents/ for personal -->

```yaml
# .claude/agents/code-reviewer.md
---
name: code-reviewer
description: Reviews code for quality
  and best practices
tools: Read, Glob, Grep, Bash
model: sonnet
---

You are a code reviewer. When invoked,
analyze the code and provide specific,
actionable feedback on quality, security,
and best practices.
```

- **YAML Frontmatter** — Configuration block between `---` fences. Defines the agent's name, description, tool access, model, and other settings.
- **Markdown Body** — Everything below the frontmatter becomes the system prompt. The agent receives only this — not the full Claude Code system prompt.
- **File Location** — `.claude/agents/` for project-scoped (check into VCS). `~/.claude/agents/` for personal agents across all projects.

## Key Frontmatter Fields

The fields developers use most. Only `name` and `description` are required.

| Field | Purpose |
|-------|---------|
| `name` | Unique identifier. Lowercase letters and hyphens. |
| `description` | When Claude should delegate to this agent. Include `use proactively` to encourage automatic delegation. |
| `tools` | Allowlist of available tools: `Read, Edit, Write, Bash, Grep, Glob, WebFetch, WebSearch, Task`. Inherits all if omitted. |
| `disallowedTools` | Denylist — remove specific tools from the inherited set. Combine with `tools` for fine-grained control. |
| `model` | `sonnet`, `opus`, `haiku`, or `inherit` (default). Match cost to task complexity. |
| `permissionMode` | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, or `plan`. |
| `memory` | Persistent memory scope: `user`, `project`, or `local`. Agent remembers across sessions. |
| `hooks` | Lifecycle hooks scoped to this agent: `PreToolUse`, `PostToolUse`, `Stop`. |
| `skills` | Skills to inject at startup. Full content loaded into context — agents don't inherit parent skills. |
| `isolation` | Set to `worktree` for a temporary git worktree (isolated repo copy). |

> **Tool restriction patterns:** Use `tools` for strict allowlists (read-only agents), `disallowedTools` for blocking specific tools while keeping the rest. You can also restrict subagent spawning: `tools: Task(worker, researcher), Read, Bash`.

## Practical Examples

Three agents showing different patterns: read-only review, editing with debugging, and domain-specific work with hooks.

### Code Reviewer (Read-only)

```yaml
---
name: code-reviewer
description: Expert code review specialist. Proactively
  reviews code for quality, security, and maintainability.
  Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards
of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is clear and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
```

**No Write or Edit tools** — can read code, search, and run commands but cannot modify files. Safe to delegate without supervision.

### Debugger (Can edit)

```yaml
---
name: debugger
description: Debugging specialist for errors, test
  failures, and unexpected behavior. Use proactively
  when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root
cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works
```

**Has Edit access** — can both diagnose and fix. The `use proactively` phrase in the description means Claude auto-delegates when it encounters errors.

### Database Query Validator (Hooks)

```yaml
---
name: db-reader
description: Execute read-only database queries.
  Use when analyzing data or generating reports.
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

You are a database analyst with read-only access.
```

**Hook-enforced safety** — the `PreToolUse` hook validates every Bash command through a script before execution. Prevents accidental writes to the database.

## When to Use What

Three different mechanisms for extending Claude's capabilities. They solve different problems.

### Custom Subagents

`.claude/agents/*.md`

Independent workers with isolated context and tool permissions.

**Use when:**
- Task needs tool restrictions (read-only reviewer)
- Work produces verbose output that would flood main context
- You want a different model (Haiku for cheap, Opus for hard)
- Agent needs its own persistent memory

### Skills

`.claude/skills/*.md`

Reusable prompts and instructions loaded into the current context.

**Use when:**
- You need reusable expertise any agent can load
- The task runs fine in the main conversation
- No tool restrictions needed
- Content is about *how* to do something, not *who* does it

### Agent Teams

Created at runtime via TeamCreate.

Multiple Claude instances coordinating tasks in parallel.

**Use when:**
- Work can be parallelized across independent tasks
- Total work exceeds a single context window
- You need sustained coordination (not just one delegation)
- Different team members need different tool sets

> **Key distinction:** Skills teach expertise that any agent can apply. Agents are independent workers with their own permissions. Teams enable sustained parallel work across independent contexts.

---

## Sources

- [Create custom subagents — Official Claude Code docs](https://code.claude.com/docs/en/sub-agents)
- [Example subagents — Official examples](https://code.claude.com/docs/en/sub-agents#example-subagents)
- [CLI reference — --agent and --agents flags](https://code.claude.com/docs/en/cli-reference)
