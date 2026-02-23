# Document Structure & Reading Order

17 guides organized into 4 groups following a **progressive depth** principle: understand what it is, learn the mental models, build your toolbox, master advanced patterns.

## 01 — Orientation

*What is this and how does it think?*

| # | Document | Why here |
|---|----------|----------|
| 1 | **What Makes Claude Code Different** | Broadest overview. Defines the 4 extensibility pillars (Commands, Skills, Hooks, MCP) and the architectural differentiators vs. autocomplete tools. Read first. |
| 2 | **Three Layers, Three Jobs** | Narrows focus to the 3 extensibility mechanisms (Skills vs MCP vs Commands) with a side-by-side comparison. Sets vocabulary for everything that follows. |

## 02 — Foundations

*The mental models you need before building anything.*

| # | Document | Why here |
|---|----------|----------|
| 3 | **Master Your Context Window** | The single most important concept. Context engineering underpins every other practice — CLAUDE.md sizing, skill design, subagent isolation, session hygiene. Must come before CLAUDE.md because it explains *why* configuration choices matter. |
| 4 | **Mastering CLAUDE.md** | The configuration system you interact with daily. Covers the full 7-layer hierarchy, rules files, and anti-patterns. Depends on understanding context pressure from the previous page. |
| 5 | **Research → Plan → Implement** | The foundational workflow pattern. Three-phase progressive compression shows how to apply context engineering to real tasks. Bridges theory (context) with practice (extensibility). |

## 03 — Extensibility

*Building your toolbox — from commands to composed workflows.*

| # | Document | Why here |
|---|----------|----------|
| 6 | **The Command & Skill Journey** | Conceptual roadmap. The 4-stage maturity model (ad-hoc → commands → skills → composed) frames everything that follows. Read before the hands-on pages. |
| 7 | **Commands in Practice** | Hands-on commands. How to create, use $ARGUMENTS, and orchestrate skills via thin command files. |
| 8 | **Skills — The Knowledge Layer** | Skills anatomy. File structure, frontmatter fields, progressive disclosure (3 loading layers), and the Skills vs Commands distinction table. |
| 9 | **Skills in Practice** | Hands-on skills. Installing, using, and composing skills with real examples (doc-processing → summarize chain). |
| 10 | **Skills Reference** | Complete spec. Every frontmatter field, string substitution, installation path, and context budget number. Lookup table, not a tutorial. |
| 11 | **Writing Better Skills** | Authoring best practices. Description triggers, body structure, named patterns (Thin Command → Rich Skill, Meta-Skill, Domain Router), and anti-patterns. |
| 12 | **MCP Servers in Practice** | The tools layer in practice. How to connect Claude Code to external tools via `.mcp.json`, common servers (Sentry, GitHub, Playwright, databases), scoping, and security. Complements the conceptual overview in "Three Layers, Three Jobs". |

**Why 7 pages on extensibility?** Commands and skills are where most teams spend their customization time. MCP servers complete the toolbox — they provide the external capabilities that skills teach Claude how to use. The journey page provides the conceptual frame, then each page goes one level deeper.

## 04 — Advanced Patterns

*Putting it all together — assumes knowledge from Groups 1–3.*

| # | Document | Why here |
|---|----------|----------|
| 13 | **The Developer's Daily Loop** | Capstone page. References skills, commands, CLAUDE.md, context management, subagents, MCP, and debugging. Six workflow patterns from Boris Cherny (Claude Code creator). Ties all prior knowledge together. |
| 14 | **Subagents vs Agent Teams** | Multi-agent architecture decision. Hub-and-spoke (subagents) vs mesh (teams) with a single decision axis: do workers need to communicate? |
| 15 | **Custom Subagents** | How to define specialized subagent personas in `.claude/agents/`. File format, tool restrictions, model selection, practical examples (code reviewer, debugger). Builds on subagent concepts from the previous page. |
| 16 | **Hooks** | Event-driven automation. Shell commands and LLM prompts triggered by lifecycle events (PreToolUse, PostToolUse, Stop, etc.) to enforce guardrails, format code, and validate output. The only mechanism that can intercept and block Claude's actions. |
| 17 | **Debugging with Claude in Chrome** | Specialized tool integration. Chrome MCP extension for DOM inspection, console reading, and network monitoring — concrete debugging workflows for frontend developers. |

## Design Decisions

**Context Window before CLAUDE.md**: Understanding context pressure explains *why* you right-size CLAUDE.md, *why* skills use progressive disclosure, and *why* subagents isolate context. It's the conceptual foundation.

**Command & Skill Journey opens Group 3**: The maturity model gives readers a map before they dive into individual pages. Without it, the relationship between commands and skills pages is unclear.

**MCP Servers in Group 3, not Group 4**: MCP is part of the extensibility toolbox — it provides capabilities that skills and commands orchestrate. The "Three Layers" page introduces MCP conceptually; the in-practice page goes hands-on. Placing it after skills authoring means readers already understand the knowledge layer before learning the tools layer.

**Developer's Daily Loop in Advanced, not Foundations**: Despite being about "daily" workflows, it references nearly every other topic. A reader who hasn't seen skills, commands, subagents, and context management would miss most of the value.

**Custom Subagents after Subagents vs Teams**: Custom subagents are the mechanism for creating the specialized roles discussed in the subagents page. Reading order: understand the architecture (subagents vs teams) → learn to define subagents.

**Hooks near the end of Advanced**: Hooks are the most powerful but also most complex extensibility mechanism. They intercept Claude's actions — understanding what those actions are (tools, commands, skills, MCP calls) is prerequisite knowledge.

**Debugging is last**: It's the most specialized page (Chrome MCP only) and the narrowest audience (frontend developers). It's valuable but optional for the general reader.
