# Agentic Capabilities Comparison — GitHub Copilot vs Claude Code

> Research compiled from official vendor sources and documentation, February 2026. Covers the agentic features, extensibility, customization, commands/skills, sub-agents, and MCP support of both tools.

## Why This Document Exists

By February 2026, both GitHub Copilot and Claude Code have evolved into agentic coding platforms. The historical framing of "autocomplete vs agentic" no longer holds. This document provides a feature-level comparison of their agentic capabilities, sourced from official documentation, to support a fair and accurate public comparison.

---

## 1. Agent Modes and Agentic Loops

### GitHub Copilot

Copilot operates through **three distinct agent surfaces**:

**Agent Mode (IDE) — GA April 2025**
Synchronous, interactive agent inside VS Code (GA), Visual Studio (preview), JetBrains, Eclipse, and Xcode. Operates as an orchestrator combining prompts, workspace context, and tools via a backend system prompt. When given a request, it parses the request, queries the language model, monitors for errors, and uses tools (`read_file`, `edit_file`, `run_in_terminal`) to reach the outcome. Detects syntax errors and terminal output, then self-corrects iteratively. Supports custom instructions and multiple AI models.

**Coding Agent (Async) — GA September 2025**
Autonomous background agent that runs in GitHub Actions. Assign a GitHub issue to Copilot or delegate from Copilot Chat in VS Code. The agent spins up an ephemeral development environment, explores code, makes modifications, executes tests and linters, and opens a draft pull request. Pushes commits incrementally; users track progress via session logs. Works while the developer's computer is off. Best for low-to-medium complexity tasks in well-tested codebases: bug fixes, incremental features, test coverage, documentation, refactoring.

**Copilot CLI — GA February 25, 2026**
Terminal-native coding agent. Plan mode (Shift+Tab) for structured planning before coding. Autopilot mode for fully autonomous execution. Background delegation with `&` prefix to offload work to cloud-based coding agents. Built-in specialized agents (Explore, Task, Code Review, Plan) that route automatically based on task type. Model selection mid-session via `/model`. Session management with `/diff` for change review, Esc-Esc for rewind.

**Sources:**
- [Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/)
- [About coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
- [Copilot CLI GA](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/)
- [Copilot CLI enhanced agents](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)

### Claude Code

Single agentic loop across all surfaces (terminal, VS Code, JetBrains, Xcode, desktop app, web, Slack). Three blended phases per task: **gather context**, **take action**, **verify results**. Chains dozens of tool calls together, course-correcting at each step. The user can interrupt at any point to steer.

Built-in tool categories: file operations (read, edit, create, rename), search (glob patterns, regex, codebase exploration), execution (shell commands, servers, tests, git), web (search, documentation fetch), code intelligence (type errors, jump to definition, find references via plugins).

The underlying model reasons about which tools to invoke; Claude Code provides the harness — tools, context management, execution environment. Multiple models available — Sonnet for most tasks, Opus for complex architectural decisions. Users switch models mid-session with `/model`.

**Sources:**
- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude Code Overview](https://code.claude.com/docs/en/overview)

### Comparison

Both tools implement agentic loops with tool use, self-correction, and iterative execution. The key structural difference: Copilot spreads its agentic capabilities across three specialized surfaces (IDE agent, async cloud agent, CLI agent), while Claude Code uses a single unified agent across all surfaces. Copilot's async coding agent has no direct Claude Code equivalent — it's a fully autonomous cloud worker that operates independently of any developer session.

---

## 2. Sub-Agents and Multi-Agent Orchestration

### GitHub Copilot

**Built-in Specialized Agents (CLI)**
Copilot CLI automatically delegates to specialized agents when appropriate:
- **Explore**: fast codebase analysis and navigation
- **Task**: running commands like tests and builds
- **Code Review**: high-signal change review
- **Plan**: implementation planning

Multiple agents can execute simultaneously rather than sequentially — parallel agent execution transforms sequential 90-second handoffs into 30-second parallel analysis.

**Custom Agents (.agent.md)**
Each custom agent is defined by a Markdown file with an `.agent.md` extension. Custom agents can specify their own tools, MCP servers, and instructions. When prompted, Copilot may choose to use a custom agent if it determines the agent's expertise is a good fit. Work performed by a custom agent is carried out using a subagent with its own context window, which can be populated independently without cluttering the main agent's context.

Create agents via interactive wizard or by writing `.agent.md` files directly. Invoke with `copilot --agent <name> --prompt "..."`.

**GitHub Agent HQ (February 2026)**
Multi-agent platform that runs Claude (Anthropic), Codex (OpenAI), and Copilot together inside github.com, GitHub Mobile, and VS Code. Developers assign different AI agents to different tasks based on their strengths. No additional subscriptions required — access included with Copilot paid plans. GitHub is also working with Google, Cognition, and xAI to bring more agents.

**Sources:**
- [Creating custom agents for CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
- [Custom Agents & Subagents (DeepWiki)](https://deepwiki.com/github/copilot-cli/3.6-custom-agents-and-subagents)
- [Copilot CLI enhanced agents](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)
- [Pick your agent: Claude and Codex on Agent HQ](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
- [Claude and Codex for Business & Pro](https://github.blog/changelog/2026-02-26-claude-and-codex-now-available-for-copilot-business-pro-users/)

### Claude Code

**Built-in Subagent Types**
- **general-purpose**: full tool access for complex, multi-step tasks
- **Explore**: fast codebase search (read-only)
- **Plan**: architecture design (read-only)

Custom subagents defined in Markdown files with YAML frontmatter (`.claude/agents/`). Each subagent can have custom prompts, tool restrictions, permission modes, hooks, and skills.

**Agent Teams (Research Preview)**
Multiple Claude Code instances work in parallel on a shared codebase. A lead agent coordinates work, assigns subtasks via a shared task list, and merges results. Best for tasks that split into independent, read-heavy work. Each teammate has its own context window and can work on separate branches via git worktrees.

**Agent SDK**
Full SDK for building custom agents powered by Claude Code's tools and capabilities, with control over orchestration, tool access, and permissions. Used by Apple's Xcode integration (Xcode 26.3+). Enables third-party integration at the deepest level.

**Sources:**
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents)
- [Enabling Claude Code to Work More Autonomously](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)
- [Claude Agent SDK in Xcode](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk)

### Comparison

Both tools support subagents with own context windows and custom agents defined in Markdown. Both have built-in specialized agents (Explore and Plan appear in both). Claude Code's Agent Teams (lead-agent coordination with shared task lists) is more advanced than Copilot's parallel agent execution. Claude Code's Agent SDK enables deeper third-party integration. Copilot's Agent HQ is a unique platform play — running multiple vendor agents (Claude, Codex, Copilot) together under one subscription.

---

## 3. MCP (Model Context Protocol) Extensibility

### GitHub Copilot

Full MCP support across multiple surfaces:
- **Agent mode (IDE)**: MCP servers in VS Code, JetBrains, Xcode, Eclipse. Enhances agent mode with access to external resources.
- **Coding agent (async)**: MCP servers configured in repository settings. OAuth support for secure third-party integrations (Slack, Jira, custom APIs).
- **CLI**: MCP server integrations via Copilot Spaces and the GitHub MCP server.

**GitHub MCP Server**: first-party MCP server that allows Copilot Chat to perform tasks on GitHub (repository operations, issue management, PR workflows).

**MCP Policy Governance**: Business and Enterprise tiers can configure MCP access policies per organization. Free/Pro/Pro+ users are not governed by these policies.

**Sources:**
- [About MCP in Copilot](https://docs.github.com/en/copilot/concepts/context/mcp)
- [Extending Copilot Chat with MCP](https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp)
- [MCP and coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/mcp-and-coding-agent)
- [Using the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server)
- [Enhancing agent mode with MCP](https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp)

### Claude Code

MCP support with three transport types:
- **HTTP** (recommended): remote cloud-based services
- **SSE** (deprecated): Server-Sent Events for legacy remote servers
- **stdio**: local processes for tools needing direct system access

**Configuration Scopes**:
- **Local** (default): private to user, current project only (`~/.claude.json`)
- **Project**: shared via `.mcp.json` in project root, version-controlled
- **User**: available across all projects

**Key MCP Features**: OAuth 2.0 authentication, Tool Search (deferred loading when tools exceed 10% of context), dynamic tool updates via `list_changed` notifications, MCP resources via `@server:protocol://path` mentions, MCP prompts as slash commands, Claude Code as MCP server (`claude mcp serve`), managed MCP for enterprise admin deployment with allowlist/denylist policies.

**Sources:**
- [Connect Claude Code to Tools via MCP](https://code.claude.com/docs/en/mcp)
- [Remote MCP Support](https://www.anthropic.com/news/claude-code-remote-mcp)
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)

### Comparison

Both tools fully support MCP. Claude Code has more granular configuration (three transport types, three scopes, tool search optimization, Claude Code as MCP server). Copilot has enterprise MCP policy governance and a first-party GitHub MCP server. Neither tool can claim MCP as an exclusive differentiator.

---

## 4. Custom Instructions and Configuration

### GitHub Copilot

- **`.github/copilot-instructions.md`**: repository-level custom instructions. Natural language in Markdown. Equivalent to Claude Code's CLAUDE.md.
- **Scoped instruction files**: `.instructions.md` files in subdirectories for different rules per file type or framework (e.g., `frontend.instructions.md`, `backend.instructions.md`).
- **`.agent.md` files**: custom agent definitions with their own instructions, tools, and MCP servers.
- **Organization-level settings**: enterprise admins control features, models, and access per organization.

**Sources:**
- [Adding custom instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- [Custom instructions in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Your first custom instructions](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/your-first-custom-instructions)

### Claude Code

- **`CLAUDE.md`**: project-level instructions. Loaded automatically, survives context compaction. Supports hierarchy: project root, subdirectories, user-level (`~/.claude/CLAUDE.md`), enterprise-managed.
- **Skills**: folders of instructions, scripts, and resources loaded dynamically when relevant. Auto-discovered by Claude Code.
- **Managed settings**: enterprise admins deploy `managed-mcp.json` and `managed-settings.json` for centralized control.

**Sources:**
- [Claude Code Overview](https://code.claude.com/docs/en/overview)
- [Introducing Agent Skills](https://claude.com/blog/skills)

### Comparison

Direct functional equivalence. `.github/copilot-instructions.md` ≈ `CLAUDE.md`. Copilot's scoped `.instructions.md` files ≈ Claude Code's directory-level CLAUDE.md. Both support organization/enterprise-level management. Both load instructions automatically into context.

---

## 5. Skills and Commands

### GitHub Copilot

**Agent Skills** — an open standard that works across Copilot in VS Code, CLI, and coding agent. Folders of instructions, scripts, and resources that Copilot loads when relevant. Create skills as markdown files. Invoke directly with `/` slash commands or let Copilot auto-discover them.

**Built-in slash commands** (CLI): `/diff` (syntax-highlighted change review), `/review` (staged code analysis), `/model` (switch models), `/delegate` (hand off to coding agent), `/agent` (switch agents), `/mcp` (MCP connections).

**Community sharing**: github/awesome-copilot repository and skill libraries.

**Sources:**
- [Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Slash commands in Copilot CLI](https://github.blog/ai-and-ml/github-copilot/a-cheat-sheet-to-slash-commands-in-github-copilot-cli/)
- [JetBrains Agent Skills preview](https://github.blog/changelog/2026-02-13-new-features-and-improvements-in-github-copilot-in-jetbrains-ides-2/)

### Claude Code

**Skills** — folders of instructions, scripts, and resources loaded dynamically when relevant. Auto-discovered and invoked by Claude Code without manual selection. Skills can be shared across teams as custom slash commands (e.g., `/review-pr`, `/deploy-staging`). Load on demand to minimize context usage.

**Built-in slash commands**: `/model` (switch models), `/plan` (enter plan mode), `/rewind` (checkpoint navigation), `/teleport` (move session between surfaces), `/help`, `/clear`, etc.

**Plugins**: bundle slash commands, subagents, MCP servers, and hooks into shareable packages. Can be pinned to specific git commit SHAs. Plugin MCP servers start automatically when enabled.

**Sources:**
- [Introducing Agent Skills](https://claude.com/blog/skills)
- [Claude Code Plugins](https://www.anthropic.com/news/claude-code-plugins)

### Comparison

Agent Skills is a shared open standard between both tools. Both auto-discover skills and support slash commands. Claude Code's plugin system (bundling skills + MCP + hooks into shareable packages) has no direct Copilot equivalent. Copilot's community skill sharing via github/awesome-copilot and the Extensions marketplace provide distribution channels Claude Code lacks.

---

## 6. Hooks and Automation

### GitHub Copilot

Hooks in both CLI and coding agent. Configured via `.github/hooks/*.json` files.

**Hook trigger points:**
- `sessionStart`: when a new or resumed session begins
- `userPromptSubmitted`: when the user submits a prompt
- `preToolUse`: before any tool execution (can approve/deny)
- `postToolUse`: after tool execution (custom post-processing)
- `sessionEnd`: when the session completes or terminates

`preToolUse` hooks can block dangerous commands, enforce security policies, require approval for sensitive operations, and log tool usage for compliance. Enterprise admins can enforce policy hooks organization-wide.

**Sources:**
- [Using hooks with Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-hooks)
- [Hooks configuration reference](https://docs.github.com/en/copilot/reference/hooks-configuration)
- [About hooks](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks)
- [Using hooks for policy compliance](https://docs.github.com/en/copilot/tutorials/copilot-cli-hooks)

### Claude Code

Hooks are shell commands that trigger at specific workflow points. Configured in Claude Code settings.

**Hook trigger points:**
- After code changes (e.g., run tests)
- Before commits (e.g., lint)
- Custom lifecycle points

Hook receives JSON via stdin. Exit code 2 blocks the operation and feeds the error message back to Claude for self-correction.

**Sources:**
- [Enabling Claude Code to Work More Autonomously](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)

### Comparison

Both tools support hooks at workflow trigger points with the ability to block operations. Copilot's hook system has more documented trigger points (five named events) and file-based configuration (`.github/hooks/*.json`). Claude Code hooks are more tightly integrated with the agent's self-correction loop (exit code 2 feeds error back to Claude). Functionally equivalent.

---

## 7. Checkpoint, Rollback, and Safety

### GitHub Copilot

**CLI**: Esc-Esc to rewind file changes to any previous snapshot in the session. Session checkpoints stored in `~/.copilot/session-state/`. `/diff` for reviewing all changes since session start.

**VS Code**: Chat checkpoints allow reverting to previous states of the conversation and code edits.

**Coding agent**: sandboxed environment in GitHub Actions with read-only repository access (except `copilot/` branches). CodeQL analysis, Advisory Database checks, and secret scanning on generated code. Cannot approve or merge its own PRs.

**Sources:**
- [Copilot CLI GA](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/)
- [VS Code chat checkpoints](https://code.visualstudio.com/docs/copilot/chat/chat-checkpoints)
- [About coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)

### Claude Code

**Automatic Checkpointing**: every user prompt creates a checkpoint — a snapshot of file state before edits. Persists across sessions (cleaned up after 30 days). Only tracks file edits through Claude's tools (not bash side-effects).

**Rewind Menu** (Esc-Esc or `/rewind`):
- Restore code and conversation (revert both)
- Restore conversation only (rewind messages, keep code)
- Restore code only (revert files, keep conversation)
- Summarize from here (compress subsequent messages)

**Permission Modes**: default (ask before each action), plan mode (describe then approve), auto-accept (edits without asking), bypass permissions (fully autonomous).

**Git Integration**: creates branches, stages changes, writes commit messages, opens PRs. Git worktrees for parallel sessions on separate branches.

**Sources:**
- [Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [Claude Code Overview](https://code.claude.com/docs/en/overview)

### Comparison

Both tools have Esc-Esc rewind and session checkpoints. Claude Code's checkpoint system is more granular — it offers separate restoration of code vs conversation state and persists checkpoints for 30 days. Claude Code's permission modes provide finer-grained control over autonomy levels. Copilot's coding agent has stronger security guardrails (CodeQL, secret scanning, sandboxed environment, no self-merge).

---

## 8. Context Gathering and Memory

### GitHub Copilot

**Repository Indexing**: since September 2025, 2x higher throughput, 37.6% better retrieval accuracy, 8x smaller index size. Full repository context analysis with cross-repository awareness. External indexing service for faster code search.

**Copilot Spaces (Preview)**: organize relevant content — code, docs, specs — into curated context collections that ground responses.

**Copilot Memory (Public Preview, January 2026)**: automatic cross-session, cross-agent memory system. Captures repository-specific "memories" as it works. Shared across Copilot features — what coding agent learns helps code review. Validated against current codebase before use. Auto-expires after 28 days. Available for all paid plans.

**CLI Cross-Session Memory**: remembers past work, files edited, PRs opened, issues triaged across sessions.

**Sources:**
- [GitHub Copilot features](https://docs.github.com/en/copilot/get-started/features)
- [Building an agentic memory system](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
- [Agentic memory public preview](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview/)

### Claude Code

**Direct Context Window Ingestion**: uses Claude's full context window (up to 200k tokens). Reads files directly into context. Searches by glob pattern and regex. When context fills up, auto-compacts older tool outputs first, then summarizes conversation.

**CLAUDE.md**: persistent project instructions that survive compaction. Hierarchy: project root → subdirectories → user-level → enterprise-managed.

**Session Management**: sessions persist locally. Resume with `--continue`. Fork with `--fork-session`. `/teleport` moves sessions between surfaces.

No automatic memory extraction system — cross-session persistence is manual via CLAUDE.md.

**Sources:**
- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude Code Overview](https://code.claude.com/docs/en/overview)

### Comparison

Different architectural approaches. Copilot uses retrieval-augmented generation with repository indexing — more scalable for very large repositories, but the developer doesn't directly control what enters context. Claude Code ingests files directly into the context window — more transparent and deterministic, but limited by the 200k token ceiling. Copilot Memory (automatic cross-session learning) is more sophisticated than Claude Code's manual CLAUDE.md approach. Claude Code's context compaction and session forking provide more developer control over context lifecycle.

---

## 9. Model Strategy

### GitHub Copilot

Multi-vendor marketplace. Default: GPT-4.1. Available models span OpenAI (GPT-4.1, GPT-5 mini, GPT-5.1, GPT-5.1-Codex, GPT-5.2, GPT-5.3-Codex), Anthropic (Claude Haiku 4.5, Claude Sonnet 4/4.5/4.6, Claude Opus 4.5/4.6), Google (Gemini 2.5 Pro, Gemini 3 Flash/Pro), and xAI (Grok Code Fast 1). Premium request multipliers vary by model. Switch mid-session via `/model`.

**Source:** [Supported AI models](https://docs.github.com/en/copilot/reference/ai-models/supported-models)

### Claude Code

Anthropic models only: Claude Sonnet (default for most coding), Claude Opus (complex architectural decisions), Claude Haiku (fast/light tasks). Switch mid-session with `/model` or at launch with `--model`. Third-party LLM providers supported for Terminal CLI and VS Code extension.

**Source:** [Claude Code Overview](https://code.claude.com/docs/en/overview)

### Comparison

Copilot offers broader model choice as a first-party feature. Claude Code is Anthropic-only but supports third-party providers via configuration. Notably, Copilot includes Claude models in its marketplace — a Copilot user can access Claude Opus 4.6 through the Copilot platform.

---

## 10. Copilot Extensions and Claude Code Plugins

### GitHub Copilot Extensions

Third-party integrations available on the GitHub Marketplace: DataStax, Docker, LambdaTest, LaunchDarkly, Sentry, Stripe, MongoDB, and others. Developers can build private extensions for internal tools. Extensions interact via Copilot Chat. Growing partner ecosystem with 77,000+ organizations using Copilot.

**Source:** [Copilot Extensions](https://github.com/features/copilot/extensions)

### Claude Code Plugins

Bundle slash commands, subagents, MCP servers, and hooks into shareable packages. Plugin MCP servers start automatically when enabled. Support all transport types. Can be pinned to specific git commit SHAs for version control.

**Source:** [Claude Code Plugins](https://www.anthropic.com/news/claude-code-plugins)

### Comparison

Different distribution models. Copilot Extensions are marketplace-distributed third-party integrations (similar to an app store). Claude Code Plugins are developer-assembled bundles of capabilities (closer to a package manager). Both enable extensibility; Copilot has the larger third-party ecosystem, Claude Code has deeper per-plugin customization.

---

## Summary: Genuine Differentiators (February 2026)

### Claude Code's Unique Advantages
- Agent Teams with lead-agent coordination, shared task lists, and branch isolation
- Agent SDK for building fully custom agents (used by Apple's Xcode)
- Plugin system bundling skills + MCP + hooks into versioned packages
- 200k token direct context window (transparent, deterministic context)
- Deeper checkpoint system (code + conversation independent restoration)
- More non-IDE surfaces: desktop app, web (claude.ai/code), Slack, Chrome extension
- Claude Code as MCP server (expose tools to other clients)

### GitHub Copilot's Unique Advantages
- Free tier and lower entry price ($10/month vs $20/month)
- IP indemnity on Business and Enterprise plans
- Fully async cloud coding agent (works independently in GitHub Actions)
- Multi-vendor model marketplace (OpenAI, Anthropic, Google, xAI)
- Agent HQ multi-agent platform (run Claude, Codex, Copilot together)
- Copilot Memory (automatic cross-session, cross-agent learning)
- Broader IDE coverage (Visual Studio, Eclipse, Vim/Neovim)
- Deeper GitHub ecosystem integration (issues, PRs, security scanning, code review, Actions)
- Copilot Extensions marketplace with established third-party ecosystem
- CodeQL and security scanning built in

### Shared Capabilities (Not Differentiators)
- Agentic loops with multi-step task execution and self-correction
- Terminal-native CLI agents
- Plan mode
- MCP support
- Custom instructions (.github/copilot-instructions.md ≈ CLAUDE.md)
- Agent Skills / Skills (shared open standard)
- Hooks (lifecycle trigger points that can block operations)
- Custom subagents defined in Markdown
- Checkpoint/undo with rewind
- Mid-session model switching
- Context compaction for long conversations
- Headless/CI mode

---

## Sources

### GitHub Copilot
- [Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/)
- [About coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
- [Coding agent GA](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/)
- [Copilot CLI GA](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/)
- [Copilot CLI enhanced agents](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)
- [Copilot CLI plan mode](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go/)
- [Creating custom agents for CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
- [About MCP in Copilot](https://docs.github.com/en/copilot/concepts/context/mcp)
- [Extending Copilot Chat with MCP](https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp)
- [MCP and coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/mcp-and-coding-agent)
- [Using the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server)
- [Enhancing agent mode with MCP](https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp)
- [Adding custom instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- [Custom instructions in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Slash commands in CLI](https://github.blog/ai-and-ml/github-copilot/a-cheat-sheet-to-slash-commands-in-github-copilot-cli/)
- [JetBrains Agent Skills preview](https://github.blog/changelog/2026-02-13-new-features-and-improvements-in-github-copilot-in-jetbrains-ides-2/)
- [Using hooks with Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-hooks)
- [Hooks configuration](https://docs.github.com/en/copilot/reference/hooks-configuration)
- [About hooks](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks)
- [Using hooks for policy compliance](https://docs.github.com/en/copilot/tutorials/copilot-cli-hooks)
- [Building an agentic memory system](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
- [Agentic memory public preview](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview/)
- [Pick your agent: Agent HQ](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
- [Claude and Codex on GitHub](https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github/)
- [Claude and Codex for Business & Pro](https://github.blog/changelog/2026-02-26-claude-and-codex-now-available-for-copilot-business-pro-users/)
- [Copilot Extensions](https://github.com/features/copilot/extensions)
- [VS Code chat checkpoints](https://code.visualstudio.com/docs/copilot/chat/chat-checkpoints)
- [VS Code multi-agent development](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development)
- [Copilot features](https://docs.github.com/en/copilot/get-started/features)
- [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)
- [Supported AI models](https://docs.github.com/en/copilot/reference/ai-models/supported-models)
- [Copilot Plans & pricing](https://github.com/features/copilot/plans)

### Claude Code
- [Claude Code Overview](https://code.claude.com/docs/en/overview)
- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works)
- [Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [Connect Claude Code to Tools via MCP](https://code.claude.com/docs/en/mcp)
- [Claude Code Product Page](https://www.anthropic.com/claude-code)
- [Introducing Agent Skills](https://claude.com/blog/skills)
- [Enabling Claude Code to Work More Autonomously](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Plugins](https://www.anthropic.com/news/claude-code-plugins)
- [Remote MCP Support](https://www.anthropic.com/news/claude-code-remote-mcp)
- [Claude Agent SDK in Xcode](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk)
- [Anthropic Pricing](https://www.anthropic.com/pricing)
