# Document Structure & Reading Order

14 guides organized into 4 groups following a **progressive depth** principle: understand what it is, learn the mental models, build your toolbox, master advanced patterns.

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

**Why 6 pages on extensibility?** Commands and skills are where most teams spend their customization time. The journey page provides the conceptual frame, then each page goes one level deeper: commands hands-on → skills anatomy → skills hands-on → skills reference → skills authoring. This progression means you can stop at any depth and still have a complete mental model.

## 04 — Advanced Patterns

*Putting it all together — assumes knowledge from Groups 1–3.*

| # | Document | Why here |
|---|----------|----------|
| 12 | **The Developer's Daily Loop** | Capstone page. References skills, commands, CLAUDE.md, context management, subagents, MCP, and debugging. Six workflow patterns from Boris Cherny (Claude Code creator). Ties all prior knowledge together. |
| 13 | **Subagents vs Agent Teams** | Multi-agent architecture decision. Hub-and-spoke (subagents) vs mesh (teams) with a single decision axis: do workers need to communicate? |
| 14 | **Debugging with Claude in Chrome** | Specialized tool integration. Chrome MCP extension for DOM inspection, console reading, and network monitoring — concrete debugging workflows for frontend developers. |

## Design Decisions

**Context Window before CLAUDE.md**: Understanding context pressure explains *why* you right-size CLAUDE.md, *why* skills use progressive disclosure, and *why* subagents isolate context. It's the conceptual foundation.

**Command & Skill Journey opens Group 3**: The maturity model gives readers a map before they dive into individual pages. Without it, the relationship between commands and skills pages is unclear.

**Developer's Daily Loop in Advanced, not Foundations**: Despite being about "daily" workflows, it references nearly every other topic. A reader who hasn't seen skills, commands, subagents, and context management would miss most of the value.

**Skills get 4 dedicated pages**: Anatomy (what it is), Practice (how to use), Reference (lookup), Best Practices (how to build). This mirrors how teams actually learn: understand → use → look things up → create their own.

**Debugging is last**: It's the most specialized page (Chrome MCP only) and the narrowest audience (frontend developers). It's valuable but optional for the general reader.
