# Skills Reference

Every frontmatter field, string substitution, and installation path — in one place.

## Frontmatter Properties

### Open Standard (agentskills.io)

| Field | Type / Default | Description |
|---|---|---|
| `name` | string, req | Display name and `/slash-command`. Max 64 chars, lowercase + hyphens only. |
| `description` | string, req | **Primary trigger.** Claude reads this to decide relevance. Must state what it does AND when to use it. Max 1024 chars. |
| `license` | string | License identifier or reference to bundled file. E.g. `Apache-2.0` |
| `compatibility` | string | Environment requirements (OS, packages, network). Max 500 chars. |
| `metadata` | map | Arbitrary key-value pairs. E.g. `author: my-org`, `version: "1.0"` |
| `allowed-tools` | string | Space-delimited list of tools Claude can use. E.g. `Read Grep Glob` or `Bash(git:*)` |

### Claude Code Extensions

| Field | Type / Default | Description |
|---|---|---|
| `argument-hint` | string | Autocomplete hint shown in `/` menu. E.g. `[issue-number]` |
| `user-invocable` | bool, true | `false` hides from `/` menu. Only Claude can invoke it. |
| `disable-model-invocation` | bool, false | `true` = user-only via `/name`. Description removed from Claude's context entirely. |
| `context` | string | `fork` runs the skill in an isolated subagent with no conversation history. |
| `agent` | string, general-purpose | Subagent type when `context: fork`. Options: `Explore`, `Plan`, or custom subagents. |
| `model` | string | Override the session model for this skill. |
| `hooks` | object | Lifecycle hooks scoped to skill execution. Same format as settings hooks, cleaned up when skill finishes. |

## String Substitutions

| Variable | What It Does |
|---|---|
| `$ARGUMENTS` | All arguments passed when invoking. `/fix-issue 123` → `$ARGUMENTS` becomes `123` |
| `$N` | Specific argument by 0-based index. `$0` = first, `$1` = second. |
| `` !`command` `` | Shell preprocessing. Runs before Claude sees content; output replaces placeholder. E.g. `` !`gh pr diff` `` |
| `${CLAUDE_SESSION_ID}` | Current session identifier. Useful for session-specific files or logging. |

If `$ARGUMENTS` is absent from skill content, arguments are appended automatically as `ARGUMENTS: <value>`.

## Installation Methods

- **Project** — `.claude/skills/<name>/SKILL.md` — committed to git, shared with team
- **Personal** — `~/.claude/skills/<name>/SKILL.md` — applies to all your projects
- **Enterprise** — deployed via managed settings, highest priority
- **Plugin** — `<plugin>/skills/<name>/` — namespaced, via Claude Code plugins
- **--add-dir** — skills in directories added at launch, supports live reload during session
- **npx skills** — `npx skills add <owner/repo>` from the [skills.sh](https://skills.sh) ecosystem

**Priority:** Enterprise > Personal > Project. Plugin skills use namespaces and cannot conflict. Monorepo subdirectories with `.claude/skills/` are auto-discovered.

## Context Budget

| Metric | Value |
|---|---|
| All skill descriptions combined | ~16K chars (2% of context window) |
| Max chars per individual description | 1024 |
| Max lines recommended for SKILL.md body | 500 |

Override with `SLASH_COMMAND_TOOL_CHAR_BUDGET=<number>`. Run `/context` to check if skills are being excluded.

---

## Sources & Further Reading

- [Extend Claude with Skills](https://code.claude.com/docs/en/skills) — Official Claude Code documentation — frontmatter, structure, patterns
- [Agent Skills Specification](https://agentskills.io/specification) — The open standard spec — field constraints, validation rules
- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — Cross-platform architecture, progressive disclosure
- [Claude Code Skills: Structure, Prompts, Invocation](https://mikhail.io/2025/10/claude-code-skills/) — Mikhail Shilkov — deep dive into runtime tool injection and invocation
- [Anthropic Skills Repository](https://github.com/anthropics/skills) — Official example skills including the skill-creator meta-skill
