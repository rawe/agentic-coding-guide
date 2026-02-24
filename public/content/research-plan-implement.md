# Research → Plan → Implement

Three phases of intentional context compaction for solving hard problems in complex codebases with AI coding agents.

<!-- Visualization: Three phase cards arranged horizontally with gradient arrows between them.
Each card has a teaser image at top and content below.
Card 1 (blue glow): Research
Card 2 (green glow): Plan
Card 3 (orange glow): Implement
Arrows: blue→green gradient between 1→2, green→orange gradient between 2→3. -->

## Session 1: Research

**In:** Task + Codebase → **Out:** `research.md`

Investigate the actual codebase. Extract compressed truth about how the relevant parts of the system work right now.

- Read the real code, not stale docs
- Explore relevant modules & interfaces
- Output disposable truth, not documentation

## Session 2: Plan

**In:** research.md + Task → **Out:** `plan.md`

Combine research with the original request. Design concrete steps, file references, and code snippets. Compress intent.

- Research + task as combined input
- Concrete steps with file references
- Code snippets to guide implementation

## Session 3: Implement

**In:** plan.md → **Out:** `code + tests`

Execute the plan in a clean context window. No accumulated noise from research or exploration. Just the plan.

- Plan as only input — clean context
- Step-by-step execution
- Code changes verified by tests

## Why This Works

### Fresh Context Each Phase

Each session starts a clean context window. No accumulated noise from prior exploration. The output of each phase is a compressed artifact that carries only what matters forward.

### On-Demand Truth

Static documentation drifts from reality. Research reads the actual code for each task, extracting truth that is current, relevant, and disposable after use.

### Progressive Compression

Codebase → research.md → plan.md → code. Each step distills the prior into a denser, more actionable form. This is intentional context compaction.

### Scales Beyond Documentation

Progressive disclosure via layered docs works for small projects. For 300k+ LOC codebases, documentation grows proportionally and becomes lies the agent trusts.

---

## Sources

- [Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg)
