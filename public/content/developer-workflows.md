---
title: "The Developer's Daily Loop"
html_file: developer-workflows.html
description: Six workflow patterns that define how experienced developers use Claude Code throughout a typical workday.
---

# The Developer's Daily Loop

Six workflow patterns that define how experienced developers actually use Claude Code. The page is structured around a day-in-the-life timeline and six core patterns, drawing primarily from Boris Cherny (creator of Claude Code) and TDD workflow practices.

## Day-in-the-Life Timeline

The page opens with a four-slot timeline representing a typical developer day:

- **Morning:** Parallel sessions -- feature branches, bug fixes, refactors running simultaneously
- **Midday:** Debugging with screenshots, stack traces, and MCP-fed context
- **Afternoon:** TDD loop for a new module -- red, green, refactor with subagents
- **Evening:** PR creation, code review, slash commands for the final push

## Pattern 1: The Inner Loop -- Plan, Execute, Verify

The core rhythm of working with Claude Code. Boris Cherny describes it: iterate in Plan Mode until you like the plan, switch to auto-accept, let Claude implement in one shot.

### Steps

1. **Plan** -- Activate Plan Mode with `Shift+Tab` twice. Describe the task. Iterate on the plan until every step is clear and scoped. A good plan eliminates 50%+ of rework.

```
# Enter plan mode and iterate
> Add authentication middleware using JWT with 24h expiry.
> Include refresh token rotation and rate limiting.

# Claude outputs a step-by-step plan -- review, ask questions, refine
```

2. **Execute** -- Once the plan looks right, switch to auto-accept mode. Claude implements the entire plan in one pass without stopping for approval at each file edit.

```
# Switch to auto-accept (Shift+Tab to cycle modes)
# Claude creates files, edits code, runs commands
# You watch -- intervene only if something goes off-track
```

3. **Verify** -- Run tests, compile, check output before committing. Never trust -- always verify. Use the actual compiler and test output, not Claude's summary.

```
# Verify the implementation
npm test
npm run build
# Review diff before committing
git diff
```

4. **Checkpoint or Rollback** -- Use `/rewind` to checkpoint and rollback failed attempts. It restores conversation state, code changes, or both independently.

```
# Something went wrong? Roll back
/rewind
# Choose: restore conversation, code, or both
```

### Key Insight

Plan Mode significantly reduces rework compared to direct implementation. As Cherny puts it: "A good plan is really important!" The time spent planning is almost always recovered during execution.

## Pattern 2: Parallel Sessions -- Working Like a Manager

Experienced users don't run one Claude instance. Boris Cherny runs 5 local + 5-10 browser sessions simultaneously, each with its own git checkout. The mental model shift: you're a manager dispatching tasks, not a typist.

### Example Sessions

| Session | Branch | Command | Status |
|---------|--------|---------|--------|
| 1 | auth-feature | `claude --resume auth` | Implementing JWT middleware |
| 2 | fix-query-perf | `claude --resume perf` | Profiling database queries |
| 3 | refactor-api | `claude --resume api` | Awaiting input |
| 4 | write-tests | `claude --resume tests` | Running test suite |
| 5 | docs-update | `claude --resume docs` | Generating API docs |

### Tips

- Use **git worktrees** for file isolation between parallel sessions -- each session gets its own working directory from the same repo
- Terminal tabs with **OS notifications** alert you when a session needs input
- Browser sessions on **claude.com** work as supplementary workers for research and planning
- Name sessions with `/rename` and resume later with `claude --resume <name>`
- ~10-20% of sessions get **abandoned** -- this is normal, not failure. Recognize dead ends early.

### Worktree Setup

```
git worktree add ../project-auth feature/auth
```

Creates an isolated checkout. Each Claude session operates on its own worktree, preventing file conflicts between parallel tasks.

## Pattern 3: Test-Driven Agent Development

Claude's natural instinct is implementation-first. TDD flips this. Context isolation between phases (separate subagents) prevents "implementation bleed" into tests -- the test-writer has no knowledge of planned implementation, producing more honest coverage.

### The TDD Cycle

RED (Write failing test) --> GREEN (Implement to pass) --> REFACTOR (Clean up code) --> repeat

### CLAUDE.md Rules for TDD Enforcement

```markdown
# CLAUDE.md -- TDD enforcement

## Testing Rules
- Always write tests before implementation
- Never modify tests during green phase
- Use subagents: test-writer sees only
  requirements, implementer sees only tests
- Run full test suite before committing
```

### Why Context Isolation Works

- Test-writer subagent sees only requirements -- no anticipated implementation
- Implementer subagent sees only tests -- no knowledge of original intent
- Context isolation prevents the LLM from designing tests around its own implementation
- Hooks enforce discipline: `UserPromptSubmit` evaluation hooks check compliance

### Example /tdd Skill

```markdown
# .claude/commands/tdd.md
Write failing tests for: $ARGUMENTS

Phase 1 (Red): Use a subagent to write comprehensive tests
  based only on the requirements. Do not implement anything yet.
  Run the tests -- they should all fail.

Phase 2 (Green): Implement the minimum code to make
  all tests pass. Do not modify the tests.

Phase 3 (Refactor): Clean up the implementation.
  Tests must still pass after refactoring.
```

### Hook-Based Evaluation

A `UserPromptSubmit` hook can check whether the developer's prompt matches TDD patterns, increasing automatic skill activation from ~20% to ~84%.

## Pattern 4: Debugging -- Feed the Loop

Debugging with Claude Code is an iterative feedback loop, not a one-shot prompt. The principle: "Never describe when you can show." Paste screenshots, compiler output, and stack traces directly.

### Steps

1. **Show Context** -- Paste the actual error, screenshot, or stack trace. Don't describe the bug -- show it. Claude handles images, terminal output, and log files natively.
2. **Get Analysis** -- Claude reads the error, traces the code path, and proposes a fix with reasoning.
3. **Apply & Re-test** -- Apply the fix, run the failing test or reproduce the scenario. Paste the new output back.
4. **Iterate or Close** -- If the fix works, move on. If not, paste the new error and repeat. Use `/clear` and restart if context gets polluted.

### Tips

- **Screenshot debugging:** paste browser screenshots, console output, or styling issues directly into the prompt
- **MCP integrations:** Chrome DevTools, Playwright, and Sentry MCP servers feed real-time context automatically
- **Use real output:** paste actual compiler errors and test failures, not your description of them
- Use `/clear` to restart with a fresh context when the conversation gets too tangled

### Anti-Pattern

"The login page is broken." -- Better: paste the screenshot, the console error, and the network tab response. Real data beats descriptions every time.

## Pattern 5: Slash Commands as Workflow Atoms

Repeatable workflows become slash commands. Cherny uses `/commit-push-pr` "dozens of times a day." Commands capture institutional knowledge -- team conventions, PR templates, review checklists.

### Example Commands

| Command | Purpose |
|---------|---------|
| `/commit-push-pr` | Stage, commit, push, and create a PR with pre-computed git status for context |
| `/refactor-plan` | Enter plan mode, analyze the target code, propose a refactoring strategy |
| `/bug-report` | Gather reproduction steps, system info, and logs into a structured report |
| `/code-review` | Review staged changes against team standards, flag issues, suggest improvements |

### Command with Inline Bash for Pre-Computed Context

```markdown
# .claude/commands/commit-push-pr.md

Review and commit the current changes.

Current branch: `git branch --show-current`
Changed files: `git diff --stat`
Recent commits: `git log --oneline -5`

Write a concise commit message following our conventions.
Push and create a PR with a clear description.
```

### Evolution of Workflows

Ad-hoc prompt --> Repeated prompt --> Slash command --> Full skill

### Tips

- **Inline bash** in commands pre-computes context (git status, branch info) to avoid model round-trips
- **PostToolUse hooks** auto-format code after every edit (e.g., `bun run format`), catching formatting issues before CI
- Commands evolve: ad-hoc prompt --> repeated prompt --> slash command --> full skill with tools

### Real Impact

Cherny's team runs a PostToolUse hook (`bun run format || true`) after each file edit to auto-format code, avoiding the formatting-related CI failures that would otherwise slip through. Small automations compound into significant time savings.

## Pattern 6: The Outer Loop -- Session Lifecycle Management

How to manage Claude Code across a full workday. The verification mindset: "You don't trust; you instrument." CLAUDE.md is the persistent brain across all sessions.

### Key Commands and Concepts

- **/clear** -- Start fresh between tasks. Context pollution from prior work causes drift. Clear between unrelated tasks.
- **/compact** -- Preserve insights while reducing tokens when continuing related work. Keeps the conversation thread alive without the full history.
- **CLAUDE.md** -- The persistent brain across all sessions. Architecture decisions, conventions, past mistakes. Cherny's team keeps theirs at ~2.5k tokens, updated multiple times weekly from code reviews.
- **/permissions** -- Whitelist common safe commands. Never use blanket `--dangerously-skip-permissions`. Scope permissions narrowly.
- **Model choice** -- Opus for complex reasoning, automatic Sonnet switching for routine tasks. Cherny uses Opus exclusively with thinking enabled -- "a wrong fast answer is slower than a right slow answer."

### CLAUDE.md as Institutional Memory

```markdown
# CLAUDE.md -- updated multiple times weekly

## Architecture
- API: Express + TypeScript, deployed on Railway
- Frontend: Next.js 14 with App Router
- Auth: JWT with refresh rotation, 24h access tokens

## Conventions
- All API responses use { data, error, meta } envelope
- Tests: colocated, *.test.ts, run with vitest
- Commits: conventional commits, no AI mentions

## Known Issues
- Query on line 142 of users.ts is O(n^2) -- fix pending
- Safari has a z-index bug on the modal component
```

### Verification Mindset

Always check Claude's output. Run the tests, read the diff, build the project. Trust the toolchain output, not the model's claim that it worked.

## Sources

- [Boris Cherny -- Claude Code Creator Workflow](https://www.infoq.com/news/2026/01/claude-code-creator-workflow/) (InfoQ, 2026-01)
- [TDD with Claude Code](https://alexop.dev/posts/custom-tdd-workflow-claude-code-vue/) (alexop.dev)
