---
title: "Master Your Context Window"
html_file: context-engineering.html
description: "A guide to context engineering for coding agents: what enters the context window, what stays out, and why it determines agent effectiveness."
---

# Master Your Context Window

What goes in, what stays out, and why it decides everything.

## From Prompt Engineering to Context Engineering

In mid-2025, Tobi Lutke and Andrej Karpathy popularized a reframe: you're not just writing a prompt — you're engineering the entire information environment the model sees at inference time. The term "prompt engineering" trivialized what is actually a systems design problem.

Phil Schmid formalized a 7-component model: everything the model can see when it generates a response. Each component is a lever you can control. Understanding all seven is the foundation of working effectively with coding agents.

### The 7 Components of Context

1. **Instructions** — System prompts, CLAUDE.md, rules files — persistent guidance
2. **User Prompt** — Your current request — the task description and constraints
3. **Conversation History** — All prior turns in the session — grows with every exchange
4. **Long-term Memory** — Persistent facts recalled across sessions — user preferences, project conventions
5. **Retrieved Information** — File reads, search results, web fetches — pulled at runtime
6. **Available Tools** — Tool definitions, MCP servers — each tool schema consumes tokens
7. **Output Format** — Structured output schemas, response templates — shapes generation

> **Tobi Lutke:** "Context engineering is the art of providing all the context for the task to be plausibly solvable by the LLM."

## The Context Window as Finite Resource

Think of the context window as working memory. It has a hard capacity limit, and performance degrades as it fills — not linearly, but noticeably past ~75% utilization. Transformer attention spreads thin across n² token pairs. More tokens means weaker attention on the tokens that matter.

### Token Budget — Typical Session (200k context window)

The context window fills with competing demands:

- **Conversation history** — ~25% of budget
- **File reads** — ~20% of budget
- **Tool definitions** — ~10% of budget
- **Instructions (CLAUDE.md)** — ~8% of budget
- **Reasoning headroom** — ~12% of budget
- **Free space** — ~25% remaining

Performance degrades past 75% utilization.

What fills it fast: a single file read can consume thousands of tokens. Command outputs, conversation turns, and tool schemas all accumulate. The goal from Anthropic's engineering blog: "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."

> **The 40–60% rule:** The ACE framework recommends keeping context utilization between 40–60%. Leave headroom for reasoning. Don't maximize token usage — maximize signal density.

## The Context Control Stack

Claude Code's features map directly to context engineering levers. Each one gives you a different way to control what the model sees and when. The hierarchy runs from always-present to fully isolated.

| Level | Feature | Description | Example |
|-------|---------|-------------|---------|
| Always-on | CLAUDE.md | Loaded every session — keep it lean, treat it like code | ~200–500 tokens |
| Scoped | Rules files | Modular project instructions; can be scoped to specific file paths | `.claude/rules/` |
| On-demand | Skills | Lazy-loaded domain knowledge, triggered by description match | `.claude/skills/` |
| Runtime | Tools & MCP servers | Agent pulls what it needs, when it needs it | tool definitions + results |
| Isolated | Subagents | Separate context windows for exploration and review | Task tool -> independent window |
| Zero-cost | Hooks | Run scripts deterministically at lifecycle events — minimal context cost | `.claude/settings.json` |

> **Mental model:** When you have a context problem, think: *which lever do I pull?* Need persistent guidance? CLAUDE.md. Need knowledge only sometimes? Skill. Need exploration without pollution? Subagent. Need a side-effect without tokens? Hook.

## Practical Patterns for High-Signal Context

Actionable strategies for keeping signal high and noise low. Each pattern directly controls what enters — and what stays out of — the context window.

### Right-size Your CLAUDE.md

Only include what Claude can't infer from code. For each line, ask: would removing this cause mistakes? If not, cut it. Prune regularly.

```
# Good: specific, actionable
Use uv for all dependencies. Never pip.
Run tests with: pytest tests/ -x

# Bad: obvious, wastes tokens
Write clean, well-documented code.
Follow best practices.
```

### Scope Investigations

Use subagents for codebase exploration to keep your main context clean. The exploration results stay in the subagent's window — only the summary returns.

```
# Instead of:
"Read all files in src/ and find the auth logic"

# Use:
"Use a subagent to investigate src/ for
 auth patterns, then summarize findings"
```

### Clear Between Tasks

`/clear` resets the window. A clean session with a better prompt beats a cluttered session with corrections stacked on corrections.

```
# Finished the auth feature? Clear before starting the next task.
/clear

# Context too bloated mid-task? Compact with intent.
/compact Focus on the API changes
```

### Let Claude Fetch, Don't Pre-load

Tell Claude to read files and run commands rather than pasting everything in. Claude fetches selectively; you tend to dump everything.

```
# Instead of pasting 500 lines:
"Here's the whole file: [paste]"

# Let Claude fetch what it needs:
"Fix the validation bug in src/auth.ts"
# Claude reads only the relevant functions
```

### Poor Context Management vs. Good Context Management

**Poor context management:**

- Pastes entire files into the prompt
- Stacks corrections on a bloated session
- Mixes unrelated tasks without clearing
- Explores the codebase in the main context
- Fills CLAUDE.md with generic advice

**Good context management:**

- Describes the task; lets Claude fetch files
- Clears and restarts with a better prompt
- One task per session, `/clear` between
- Delegates exploration to subagents
- Keeps CLAUDE.md to actionable rules only

## Anti-Patterns That Kill Context

Common mistakes that fill the context window with noise. Each one has a diagnosis and fix.

### The Kitchen Sink Session

You fixed a bug, then added a feature, then refactored a test — all in one session. By turn 30, Claude is confused about which task is current, and old file reads from the bug fix are polluting attention for the refactor.

**Fix:** `/clear` between unrelated tasks. One focused session beats one long session.

### The Correction Spiral

Claude made a mistake. You corrected it. Claude made a different mistake. You corrected that too. Five corrections later, the context is full of wrong approaches and conflicting instructions. Claude is now attending to the mistakes as much as the corrections.

**Fix:** After two corrections, stop. `/clear` and write a better initial prompt that prevents the mistake.

### The Bloated CLAUDE.md

Your CLAUDE.md has 200 lines covering every conceivable scenario. Half the rules contradict each other, and Claude can't tell which ones matter for the current task. When everything is important, nothing is.

**Fix:** Cut to <50 lines. Move domain-specific guidance to rules files or skills. If removing a line doesn't cause errors, delete it.

### The Infinite Exploration

You asked Claude to "investigate the authentication system." Without scope constraints, it reads 30 files, fills the context with irrelevant module internals, and returns a meandering summary that buries the answer you needed.

**Fix:** Scope investigations: "Read `src/auth/login.ts` and explain how tokens are validated." Or delegate open-ended exploration to a subagent.

### The Pre-loaded Dump

You paste three entire files into your prompt "for context." Claude now has 4,000 tokens of code it may not need, displacing space for the reasoning and file reads it actually requires.

**Fix:** Describe the task and let Claude fetch what it needs. It reads selectively; you dump indiscriminately.

## Context Engineering for Large Codebases

Strategies that scale beyond small projects. At 100k+ lines of code, context management stops being a nice-to-have and becomes the primary determinant of agent effectiveness.

### Divide Investigation with Subagents

Split codebase exploration across modules. Each subagent gets its own context window and returns a focused summary. The main context stays clean.

```
# Fan out investigation
"Use subagents to investigate:
 1. The auth module in src/auth/
 2. The API routes in src/api/
 3. The database layer in src/db/
 Then synthesize findings."
```

### Create Research Artifacts

Summarize findings into compressed research.md files. These serve as context anchors for future sessions — the investigation cost is paid once, reused many times.

```
# Research artifact
research/auth-architecture.md
  Token flow: login -> /api/token -> JWT
  Middleware: src/middleware/auth.ts
  Key constraint: tokens expire in 1h
```

### Write Skills for Domain Knowledge

Encode domain-specific workflows as skills so they load only when relevant. Zero cost when dormant, full instructions when activated.

```
# Instead of 50 lines in CLAUDE.md:
.claude/skills/deploy-workflow/
  SKILL.md  # loaded only for deploy tasks
```

### Exclude Noise with .gitignore

Claude Code respects .gitignore patterns. Keep generated files, build artifacts, and irrelevant directories out of context. Every excluded file is tokens saved for the files that matter.

```
# .gitignore (also respected by Claude Code)
dist/
node_modules/
*.generated.ts
coverage/
```

### Fan Out with `claude -p`

For batch operations across many files, use headless mode. Each invocation gets a fresh context window — no cross-contamination between files.

```bash
# Batch process across files
for f in src/api/*.ts; do
  claude -p "Add input validation to $f"
done
```

### Compress with Intentional Compaction

When context is deep in a long session, use `/compact` with a focus directive. Claude preserves what matters and discards what doesn't.

```
# Targeted compaction
/compact Retain the database schema
changes and the migration plan.
Drop the earlier debugging.
```

> **300k LOC example:** Practitioners shipping complex features in large Rust codebases report that structured context management — subagent investigation, research artifacts, and intentional compaction — is the difference between the agent succeeding and failing. The model capability is the same; the context engineering determines the outcome.

## Sources

- [Anthropic Engineering — Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Phil Schmid — Context Engineering](https://www.philschmid.de/context-engineering)
- [ACE Guide — Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
