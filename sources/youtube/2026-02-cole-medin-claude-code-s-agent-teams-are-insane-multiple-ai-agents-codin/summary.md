# Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time

> Source: [Claude Code's Agent Teams Are Insane](https://www.youtube.com/watch?v=-1K_ZWDKpU0) by Cole Medin

## Overview

Cole Medin walks through Claude Code's new experimental agent teams feature, which lets multiple Claude Code instances collaborate on a shared task list in real time via tmux split panes. He compares agent teams to subagents — collaboration vs isolation — demos both a code review and a full project build, and shares a custom skill called "contract first spawning" that makes teams more reliable by establishing upstream dependencies (e.g. database schema) before parallelizing the remaining work.

## Key Takeaways

- **Subagents for research, agent teams for implementation.** Subagents are token-efficient and good for isolated tasks where you only need the summary. Agent teams enable peer-to-peer coordination needed when agents modify shared code (e.g. backend API changes that affect frontend).
- **Agent teams cost 2-4x more tokens** than subagents or solo Claude Code. The coordination overhead — shared task list, inter-agent messaging — is significant.
- **Claude Code is not great at using agent teams by default.** Without specific instructions, it hallucinates weird team compositions or mishandles tmux terminals. You need to be explicit about team size and roles.
- **Naive parallelism causes rework.** Example: database and backend agents running simultaneously led to the backend building against the wrong schema, then having to redo most of its work once the database agent communicated the actual schema.
- **"Contract first spawning" solves the dependency problem.** Instead of launching all agents in parallel, the upstream agent (e.g. database) runs first and sends its contract (schema, API shape) to the lead agent before downstream agents are spawned. Parallel work still happens, but with a correct foundation.
- **Recommended workflow: subagent research → plan → agent team execution.** Use subagents to analyze a codebase and produce a plan, then feed that plan into an agent team for implementation.
- **Visibility into collaboration is limited.** You can navigate tmux panes (Ctrl+B + arrow) and ask individual agents what they're doing, but there's no built-in dashboard for inter-agent communication.

## Notes

### Setup

Agent teams is an experimental feature that must be explicitly enabled. Two options: set the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable, or add it to `settings.json` (either global or per-project in `.claude/`). For the split-pane visual mode, install tmux (recommended) or iTerm 2. Windows requires WSL.

### How Agent Teams Work

A lead agent analyzes the request and decides what team to form. It creates a shared task list, then spawns teammate agents in separate tmux panes, each with a role-specific prompt. Teammates work on the shared task list, communicate with each other and the lead agent, and update progress. When all agents finish, the lead spins down the terminals and returns control to the primary session.

You can navigate between panes with Ctrl+B + arrow keys to chat with individual agents, ask for status updates, or redirect their work.

### Agent Teams vs Subagents

Subagents prioritize **context isolation**. They take a task, run independently, and return only a summary. The main agent's context stays clean. Tradeoff: zero coordination, black-box execution, no awareness of what other subagents are doing. Best for research and information gathering where only the result matters.

Agent teams prioritize **collaboration**. Agents share a task list, send messages to each other, and coordinate in real time. A backend agent can tell a frontend agent about an API change as it happens. Tradeoff: 2-4x token cost and the feature is still rough around the edges. Best for implementation where multiple agents touch interdependent code.

Rule of thumb: subagents for research, agent teams for building.

### Limitations

Two main issues observed across Linux and Mac testing:

1. **Unreliable team formation.** Without very specific prompts (exact number of agents, explicit roles), Claude sometimes creates nonsensical teams or fails to manage tmux properly.
2. **False parallelism.** Agents that have upstream dependencies shouldn't run simultaneously. A database agent defining schema while a backend agent builds against an incomplete/wrong schema wastes tokens on rework even though the communication eventually corrects it.

### Contract First Spawning

Medin's custom skill (`/build-with-agent-team`) addresses both limitations. A version of this skill is available at `.claude/skills/build-with-agent-team/SKILL.md`. Core idea: instead of launching all agents at once, identify the dependency chain and spawn agents in order.

Process:
1. Feed in a pre-built plan (from subagent research or manual)
2. The skill's instructions tell Claude to determine the optimal team composition and dependency order
3. The most upstream agent (e.g. database) spawns first and works until it can send its "contract" — the schema, API surface, or interface definitions
4. The lead agent receives the contract, then spawns the next agent in the chain (e.g. backend)
5. Parallel work still happens — the database agent keeps building while the backend agent starts — but on a correct foundation

The skill also includes explicit instructions for tmux terminal management to reduce hallucinations. Source: [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro/tree/main/use-cases/build-with-agent-team).

### Anthropic's C Compiler Example

Anthropic used 16 agents in an agent team to build an entire C compiler — hundreds of thousands of lines of code, ~$20,000 in API costs. They describe it as something a single agent could not have accomplished regardless of model capability. Demonstrates the ceiling of what multi-agent coordination can achieve, but also illustrates the token cost at scale.
