# The Five-Feature Decision Matrix

Claude Code has five customization features. Each loads differently, costs differently, and solves a different problem. One question per feature tells you which to use.

## The Problem

Most developers only use CLAUDE.md. PR review checklists, deployment procedures, commit message formats, brand guidelines — all crammed into one file. **That file loads into every conversation.** Your deployment procedure consumes tokens while you're debugging a memory leak. Your PR checklist sits in context while you're writing unit tests.

**The desk metaphor:** Keeping everything in CLAUDE.md is like keeping your entire reference library on your desk at all times. It works, but it's wasteful, cluttered, and expensive.

## Five Features at a Glance

Each feature has a distinct loading behavior and context window cost. Choosing the right one means matching the problem to the loading pattern.

<!-- Visualization: Five-column grid of feature cards
Each card has a colored top border, a label badge, heading, description, and a loading indicator.
Colors: CLAUDE.md (purple), Skills (amber), Subagents (blue), Hooks (cyan), MCP (pink).
Each card shows: label, title, one-liner description, and "Loads: [pattern]" -->

- **CLAUDE.md** — Always-On Instructions. Non-negotiable project standards. Loads every session, no exceptions. Hierarchical cascade: enterprise → personal → project → local. *Loads: always*
- **Skills** — On-Demand Expertise. Task-specific knowledge that activates when matched. Only the description sits in context; full instructions load on demand. *Loads: on match*
- **Subagents** — Isolated Workers. Separate context window for verbose tasks. Exploration output stays contained; only a summary returns to the main conversation. *Loads: separate context*
- **Hooks** — Event-Driven Automation. Shell commands that fire on lifecycle events. Deterministic — no relying on LLM judgment. Can block, allow, or modify actions. *Loads: outside context*
- **MCP Servers** — External Integrations. Open protocol connecting Claude to external services. Sentry, Postgres, GitHub, Figma. Tool search loads tools dynamically on demand. *Loads: on demand*

## Decision Matrix

Five questions, one per feature. Ask them in order. The first "yes" tells you where to put it.

<!-- Visualization: Five rows, each with a question, arrow, and answer badge
Each row has a colored left border matching its feature.
Layout: [question text] → [feature answer badge] -->

| Question | → | Feature |
|----------|---|---------|
| Should Claude **always** know this, every session, regardless of task? | → | CLAUDE.md |
| Should Claude know this **sometimes**, only when the task is relevant? | → | Skill |
| Should this work run in **isolation**, keeping verbose output out of context? | → | Subagent |
| Should this happen **automatically** on every matching lifecycle event? | → | Hook |
| Does Claude need **external tools** or data from outside services? | → | MCP Server |

**These features compose.** A real-world project uses multiple features simultaneously. Skills can reference MCP tools. Hooks can invoke subagents. CLAUDE.md sets the ground rules that everything else builds on.

## Context Window Cost

Your context window is finite. Each feature trades off differently between availability and token consumption.

<!-- Visualization: Five-column grid of cost cards
Each card has a colored top border, feature label badge, cost level (large text), and explanation.
CLAUDE.md: High (warn color), Skills: Low (green), Subagents: Zero (green), Hooks: Zero (green), MCP: Moderate (amber) -->

- **CLAUDE.md** — High. Loaded every session whether relevant or not.
- **Skills** — Low. Description only until invoked; full content on demand.
- **Subagents** — Zero. Own context window; only summary returns.
- **Hooks** — Zero. Run outside Claude's context entirely.
- **MCP** — Moderate. Tool search loads tools dynamically to mitigate cost.

## CLAUDE.md vs Skills: The Key Distinction

The most common mistake is putting task-specific knowledge in CLAUDE.md instead of a skill. Use this rule:

<!-- Visualization: Four rows in matrix style, alternating CLAUDE.md and Skills
Each row: example instruction → recommended feature badge -->

| Example | → | Feature |
|---------|---|---------|
| "Use TypeScript strict mode" — applies to **every task** | → | CLAUDE.md |
| "PR review checklist" — only relevant **when reviewing** | → | Skill |
| "Never modify the database schema directly" — **non-negotiable rule** | → | CLAUDE.md |
| "Deployment procedure" — only needed **when deploying** | → | Skill |

**The rule is simple.** Project-wide standards that always apply → CLAUDE.md. Task-specific expertise that's only relevant sometimes → Skill. If you're repeating the same explanation to Claude, that's a skill waiting to be written.

## Real-World Setup

A well-configured project uses all five features simultaneously. Each handles its own specialty.

<!-- Visualization: 2x2 grid plus a full-width card at bottom
Each card has a colored left border matching its feature, a heading, and bullet list.
CLAUDE.md (purple), Skills (amber), Subagents (blue), Hooks (cyan), MCP (pink, full-width with 3-column list) -->

**CLAUDE.md — Always-On Standards**
- Use pnpm, never npm
- TypeScript strict mode
- Never mutate the database directly

**Skills — Task-Specific Expertise**
- PR review skill with team checklist
- Deployment skill with step-by-step procedure
- Commit message skill with format rules

**Subagents — Isolated Delegation**
- Code reviewer with read-only access
- Researcher that explores docs without cluttering context

**Hooks — Automated Guardrails**
- Auto-format every file Claude touches
- Block destructive shell commands
- Run tests after every edit

**MCP Servers — External Services**
- GitHub for pull requests
- Sentry for error monitoring
- Postgres for data queries

## Source

- [Why Most Developers Are Using Claude Code Wrong (Here's What You're Missing)!](https://www.youtube.com/watch?v=xuZ2meWfcKg) — DIY Smart Code (Feb 2026, 12 min)
