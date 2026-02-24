# Subagents vs Agent Teams

Choose based on whether workers need to communicate.

## Subagents (Pattern A)

<!-- Visualization: Tree diagram with blocked lateral communication
Top node: "Main Agent (Claude Code)" — blue/indigo rounded rectangle.
Three downward arrows fan out to three orange-bordered worker nodes: "Explore", "Explore", "Explore".
Between adjacent workers, dashed red lines with ✗ marks indicate NO lateral communication.
Below each worker, a task label in quotes: "auth patterns", "query perf", "scan CVEs".
Dashed return arrows lead down to result text:
- "JWT, 24h expiry"
- "Line 142 is O(n²)"
- "CVE-2021-23337" -->

The main agent spawns isolated workers. Each gets a task, works independently, and returns only its result. Workers cannot communicate with each other.

**Results:**

- `auth patterns` — Auth uses JWT, 24h expiry
- `query perf` — Query on line 142 is O(n²)
- `scan CVEs` — lodash has CVE-2021-23337

*Reports back only — no coordination.*

## Agent Teams (Pattern B)

<!-- Visualization: Tree diagram with bidirectional lateral communication and shared task list
Top node: "Lead Agent (Claude Code)" — blue/indigo rounded rectangle.
Three downward arrows fan out to three green-bordered worker nodes: "Frontend", "Backend", "Database".
Between adjacent workers, green bidirectional arrows indicate peer-to-peer communication.
A curved green bidirectional arrow also connects Frontend and Database underneath.
Dashed gold lines from each worker point down to a shared "SHARED TASK LIST" box (gold-bordered).
Inside the task list box: "☐ Define API contract", "☑ Set up database schema". -->

A lead agent coordinates multiple workers that can communicate with each other and share a task list. Workers are peers — they can message each other, claim tasks, and collaborate.

**Shared Task List:**

- [ ] Define API contract
- [x] Set up database schema
- [ ] Build chat UI components

*Peer-to-peer + shared context.*

## When to Use Each

### Use Subagents When

- Quick, focused tasks (usually research)
- Only the result matters (not the process)
- Cost / token sensitive

### Use Agent Teams When

- Complex multi-component builds
- Agents need to coordinate
- Work requires collaboration

---

## Sources

- [Cole Medin — Agent Teams Are Insane](https://www.youtube.com/watch?v=-1K_ZWDKpU0)
