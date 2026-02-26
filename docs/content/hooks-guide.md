# Hooks

Shell commands and LLM prompts that fire automatically at lifecycle events — deterministic guardrails you don't have to ask Claude to remember.

## What Hooks Are

Hooks are user-defined actions that execute at specific points in Claude Code's lifecycle. Unlike CLAUDE.md instructions (which the LLM may or may not follow), hooks provide **deterministic control** — they always run, every time.

### Handler Types

**Command — Shell Script**
Runs a shell command. Receives JSON on stdin, returns results via exit codes and stdout. The workhorse.

**Prompt — LLM Evaluation**
Sends a prompt to a fast model (Haiku) for single-turn yes/no decisions. Returns `ok: true` or `ok: false`.

**Agent — Multi-Turn Subagent**
Spawns a subagent with Read/Grep/Glob access for multi-turn verification before returning a decision.

> **Key distinction:** Hooks are the only extensibility mechanism that can intercept and block Claude's actions before they happen.

## Lifecycle Events

Claude Code exposes 17 hook events. These are the ones you'll use most often.

**PreToolUse** — Fires before a tool call executes. Can allow, deny, or modify tool input. The most powerful hook. *Can Block*

**PostToolUse** — Fires after a tool call succeeds. Use for formatting, linting, logging. Cannot undo the action. *Side Effect Only*

**UserPromptSubmit** — Fires when the user submits a prompt, before Claude processes it. Can block or transform the prompt. *Can Block*

**Stop** — Fires when Claude finishes responding. Can force Claude to continue if work remains incomplete. *Can Block*

**Notification** — Fires when Claude sends a notification (permission prompt, idle, etc.). Useful for desktop alerts. *Side Effect Only*

**SessionStart** — Fires when a session begins, resumes, or restarts after compaction. Inject context or set env vars. *Side Effect Only*

**PreCompact** — Fires before context compaction. Capture or persist state before the context window shrinks. *Side Effect Only*

**SubagentStop** — Fires when a subagent finishes. Validate subagent output before the parent accepts it. *Can Block*

> **Matchers filter when hooks fire.** For tool events, the matcher is a regex on the tool name: `Bash`, `Edit|Write`, `mcp__.*`. For `SessionStart`, it filters by trigger: `startup`, `resume`, `compact`. Some events (like `Stop`) have no matcher and always fire.

## Configuration

Hooks live in settings files as JSON. Three levels of nesting: event → matcher group → handler array.

```json
// settings.json (project or user-level)
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/validate.sh",
            "timeout": 600
          }
        ]
      }
    ]
  }
}
```

### Where Hooks Live

- `~/.claude/settings.json` — all projects
- `.claude/settings.json` — single project (committable)
- `.claude/settings.local.json` — project, gitignored
- Skill/agent YAML frontmatter — scoped to component

### Exit Code Protocol

- **0** — success, action proceeds
- **2** — block the action, stderr fed to Claude
- **Other** — non-blocking error, logged only

### Interactive Editor

Run `/hooks` inside Claude Code to view, add, and delete hooks without editing JSON manually.

## Practical Examples

Four patterns that cover the most common use cases.

### Block Destructive Commands

**Event:** PreToolUse → **Matcher:** Bash → **Type:** command

```bash
#!/bin/bash
# .claude/hooks/block-rm.sh
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked by hook"
    }
  }'
else
  exit 0
fi
```

### Auto-Format on File Write

**Event:** PostToolUse → **Matcher:** Edit|Write → **Type:** command

```json
// In settings.json — runs Prettier after every file edit
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
      }]
    }]
  }
}
```

### Protect Sensitive Files

**Event:** PreToolUse → **Matcher:** Edit|Write → **Type:** command. Blocks edits to `.env`, `package-lock.json`, and `.git/`.

```bash
#!/bin/bash
# .claude/hooks/protect-files.sh
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/")

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Blocked: $FILE_PATH matches '$pattern'" >&2
    exit 2
  fi
done
exit 0
```

### Re-inject Context After Compaction

**Event:** SessionStart → **Matcher:** compact → **Type:** command. Ensures critical instructions survive context compaction.

```json
// In settings.json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "compact",
      "hooks": [{
        "type": "command",
        "command": "echo 'Reminder: use Bun, not npm. Run bun test before committing. Current sprint: auth refactor.'"
      }]
    }]
  }
}
```

> **Why this matters:** When Claude compacts context, it may lose track of project-specific rules from CLAUDE.md. A SessionStart hook with the `compact` matcher re-injects critical instructions deterministically.

## Hooks vs Other Extensibility

Four ways to extend Claude Code, each filling a different role.

**Hooks** — *Guardrails.* Shell commands triggered by lifecycle events. Can block, allow, or modify actions. Deterministic enforcement.

**Skills** — *Knowledge.* Markdown instructions loaded on demand. Add context, define workflows. Cannot intercept or block.

**MCP Servers** — *Tools.* External tool providers via JSON-RPC. Expose new capabilities (databases, APIs). Cannot block other tools.

**Agents** — *Delegation.* Subagent definitions in `.claude/agents/`. Handle specialized tasks autonomously. Scoped to their own work.

> **The short version:** Skills tell Claude what to know. MCP gives Claude new tools. Agents let Claude delegate. Hooks enforce what Claude must and must not do.

---

## Sources

- [Hooks Reference](https://code.claude.com/docs/en/hooks) — Official Anthropic documentation (comprehensive reference for all 17 events)
- [Hooks Guide](https://code.claude.com/docs/en/hooks-guide) — Official Anthropic documentation (practical guide with worked examples)
- [Bash Command Validator](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py) — Reference implementation on GitHub
