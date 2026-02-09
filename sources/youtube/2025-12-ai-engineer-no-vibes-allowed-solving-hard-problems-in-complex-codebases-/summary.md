# No Vibes Allowed: Solving Hard Problems in Complex Codebases

> Source: [No Vibes Allowed: Solving Hard Problems in Complex Codebases](https://www.youtube.com/watch?v=rmvDxxNubIg) by AI Engineer

## Overview

Dex Horthy (HumanLayer, author of "12 Factor Agents") presents a framework for making AI coding agents effective in large, complex codebases — not just greenfield projects. The core idea: most agent failures stem from poor context management, not model limitations. He introduces "frequent intentional compaction" (research-plan-implement) as a systematic approach to keep agents in the "smart zone" of their context window, demonstrated on a 300k LOC Rust codebase.

## Key Takeaways

- **Context is the only lever.** LLMs are stateless — better input tokens produce better output tokens. Every tool call is influenced solely by what's in the conversation so far.
- **The "dumb zone" is real.** Around 40% context window usage, quality degrades. Too many MCPs or accumulated noise pushes all work into the dumb zone.
- **Frequent intentional compaction beats brute force.** Compress context into markdown artifacts (research docs, plans) and start fresh windows instead of steering a derailed agent.
- **Sub-agents are for context control, not role-playing.** Fork context to investigate, return a succinct answer. Don't create "frontend agent" and "backend agent" — that's anthropomorphizing.
- **Research-Plan-Implement is a compaction pipeline.** Research compresses truth (how the system works). Planning compresses intent (what to change and how). Implementation executes with minimal context.
- **Plans should include actual code snippets.** The more concrete the plan, the higher execution reliability — even a weak model can follow explicit steps with file names and line numbers.
- **Don't outsource the thinking.** AI amplifies thinking you've done, or the lack of it. A bad line of research corrupts the entire downstream pipeline. Humans must review research and plans.
- **"Spec-driven development" is semantically diffused.** The term has lost meaning. Focus on the underlying mechanics: context compression, compaction, and staying in the smart zone.
- **Scale context engineering to task complexity.** Button color change: just talk to the agent. Multi-repo feature: full research-plan-implement. Build intuition through reps, not theory.
- **The hard problem is cultural, not technical.** Teams must adapt their SDLC. Senior engineers avoiding AI while juniors produce slop creates a destructive rift. Change must come from leadership.

## Notes

### Context Window as the Core Constraint

LLMs are stateless. The only way to improve output is to improve what's in the context window. Optimize for four dimensions: correctness (no wrong information), completeness (nothing critical missing), size (stay small), and trajectory (avoid error-correction spirals).

Negative trajectory is self-reinforcing: if the conversation history is "agent fails, human corrects, agent fails again," the model predicts the next step is another failure. When this happens, start a new context window instead of continuing.

Jeff Huntley's finding: the more context window you use, the worse outcomes you get.

### The Dumb Zone

The context window has a "smart zone" and a "dumb zone." Around 40% utilization, diminishing returns kick in (varies by task complexity). If your agent setup loads heavy MCP tools dumping JSON and UUIDs into context, you're starting every task in the dumb zone.

### Frequent Intentional Compaction

The central technique. Instead of running one long agent session, break work into phases that produce compressed artifacts:

1. **Research** — Understand how the system works. Find the right files. Stay objective. Output: a markdown doc with exact files, line numbers, and how things connect.
2. **Plan** — Outline exact steps using research output. Include actual code snippets of what will change, file names, line numbers, and how to test after each change. Output: a plan file.
3. **Implement** — Execute the plan in a fresh context window. The plan is concrete enough that even a weak model can follow it.

Each phase compresses the previous one. Research compresses codebase truth. Planning compresses intent. The agent never carries forward raw exploration noise.

### Sub-Agents for Context Control

Sub-agents should fork a new context window to investigate something specific (e.g., "find how auth works in this codebase"), then return a succinct answer to the parent agent. The parent reads one file instead of doing all the exploration itself.

Wrong use: creating role-based sub-agents ("frontend agent," "QA agent"). That's anthropomorphizing roles, not managing context.

### On-Demand Context over Static Documentation

Static onboarding docs (CLAUDE.md, README) get stale as codebases grow. The more comprehensive they are, the more context they consume and the faster they go out of date. "Between actual code, function names, comments, and documentation — documentation contains the most lies."

Better approach: on-demand compressed context. Before a task, steer the agent to research the specific parts of the codebase that matter. Launch sub-agents to take vertical slices through the codebase and build a research document that reflects the actual current state of the code.

Progressive disclosure helps: put a small context file at the repo root, then additional context at each level. The agent only pulls in what's relevant to where it's working.

### Planning as Leverage and Mental Alignment

Plans serve two purposes: guiding the agent and maintaining team alignment. Code review traditionally keeps everyone on the same page about how a codebase is evolving. With 2-3x more code shipping, reading every line becomes impractical. Reading plans is enough for technical leaders to catch problems early and maintain understanding.

Mitchell Hashimoto's approach: attach full agent session threads (prompts, steps, build results) to pull requests so reviewers can follow the journey, not just see a wall of green diff.

Plans have a reliability/readability tradeoff. Longer plans are more reliable for the agent but harder for humans to review. Find the sweet spot for your team.

### Calibrating Effort to Task Complexity

Not every task needs full research-plan-implement:
- **Simple change** (button color): just tell the agent
- **Small feature**: lightweight plan
- **Medium feature across repos**: research + plan
- **Hard problem in complex codebase**: full multi-round research, plan with code snippets, careful implementation

Building intuition takes reps. Pick one tool and practice. Don't min-max across multiple tools.

### Cultural and Organizational Change

The emerging rift: staff engineers don't adopt AI (marginal gains for them), junior/mid engineers adopt heavily (fills skill gaps but produces slop), senior engineers grow frustrated cleaning up that slop weekly. This is not the AI's fault or the junior engineers' fault — it's a leadership problem. Teams must adapt their SDLC for a world where most code is AI-generated. Cultural change must come from the top.
