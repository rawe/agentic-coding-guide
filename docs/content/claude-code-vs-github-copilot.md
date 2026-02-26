# Claude Code vs GitHub Copilot

Two agentic coding platforms. One grew from inline autocomplete into a multi-surface ecosystem spanning IDEs, terminal, and cloud agents. The other was built terminal-first as an autonomous reasoning engine. Both now have agentic loops, plan modes, MCP support, custom agents, skills, and hooks — but their architectures and strengths remain distinct.

## Two Platforms, Two Strengths

Both tools are agentic in 2026. The meaningful difference is no longer "autocomplete vs agent" — it's **platform breadth vs agent depth**. Copilot covers more surfaces, more models, more ecosystem integrations, and now runs third-party agents (including Claude) within its platform. Claude Code goes deeper on agent customization, multi-agent orchestration, and extensibility packaging. Understanding this split determines when to reach for which tool.

<!-- Visualization: Two-column architecture comparison diagram
LEFT COLUMN — "GitHub Copilot" header with GitHub-style blue accent
Shows three stacked layers: IDE agent (top), CLI agent (middle), cloud coding agent (bottom).
Each layer has a small icon and brief label.
Below: "Platform Breadth" label.
Key stats overlaid: "35ms completions", "3 agent surfaces", "Multi-vendor models", "GitHub ecosystem"

RIGHT COLUMN — "Claude Code" header with Anthropic orange/amber accent
Shows a terminal window with a multi-step reasoning chain and branching subagent calls.
Below: "Agent Depth" label.
Key stats overlaid: "200k token context", "Agent Teams", "Plugin system", "Agent SDK"

Divider between columns: dashed vertical line
Bottom center note: "Both are agentic. The question is breadth vs depth." -->

### GitHub Copilot — Platform Breadth

Launched June 2021 as inline autocomplete. Now a multi-surface platform with three distinct agent modes, a multi-vendor model marketplace, and deep GitHub ecosystem integration.

- **Inline completions** — 35ms average latency. The original product and still the dominant daily interaction. Predicts function bodies, completes patterns, generates boilerplate.
- **Three agent surfaces** — synchronous agent mode in IDEs (GA April 2025), async coding agent in GitHub Actions (GA September 2025), terminal-native CLI agent (GA February 2026). Each serves a different workflow.
- **Multi-model marketplace** — GPT-4.1 default, plus models from OpenAI, Anthropic (including Claude Opus 4.6), Google, and xAI. Switch mid-session with `/model`.
- **GitHub Agent HQ** — run Claude, Codex, and Copilot together inside github.com, GitHub Mobile, and VS Code. Assign different agents to different tasks. No additional subscription required.
- **Ecosystem depth** — PR summaries, code review (@copilot mentions), CodeQL security scanning, Advisory Database checks, secret scanning, Copilot Extensions marketplace, GitHub Actions integration.

### Claude Code — Agent Depth

Built by Anthropic. Terminal-first: open a CLI session, describe the problem, and Claude Code reads relevant files across the repository before proposing anything. 200k token context window allows full-project ingestion.

- **Agentic loop** — gather context, take action, verify results. Chains dozens of tool calls together, course-corrects at each step. The agent doesn't just suggest — it acts, verifies, and iterates.
- **Agent Teams** — multiple Claude Code instances work in parallel on a shared codebase with a lead agent coordinating via shared task lists. The most advanced multi-agent orchestration of either tool.
- **Agent SDK** — full SDK for building custom agents powered by Claude Code's tools. Used by Apple's Xcode integration. Enables deep third-party integration.
- **Plugin system** — bundle skills, MCP servers, hooks, and subagents into versioned, shareable packages. No Copilot equivalent.
- **Broader non-IDE surfaces** — desktop app, web (claude.ai/code), Slack integration, Chrome extension for browser debugging.

## Agentic Capabilities: Head-to-Head

Both tools have converged on many agentic features. This section separates what's shared from what's genuinely different.

<!-- Visualization: Three-tier comparison layout
TOP TIER — "Shared Capabilities" with neutral gray background
Grid of feature pills/badges: "Agentic loops", "Plan mode", "MCP support", "Custom instructions", "Skills", "Hooks", "Custom agents", "Checkpoint/undo", "Model switching", "Context compaction", "CI/CD mode"
Subtitle: "These are no longer differentiators."

MIDDLE TIER — Split into two columns
LEFT: "Copilot-Only" with blue background
Feature pills: "Inline completions (35ms)", "Async cloud agent", "Multi-vendor models", "Agent HQ platform", "Copilot Memory", "CodeQL scanning", "Extensions marketplace", "IP indemnity"

RIGHT: "Claude Code-Only" with amber background
Feature pills: "Agent Teams", "Agent SDK", "Plugin system", "Desktop app", "Web interface", "Slack integration", "Chrome extension", "200k direct context"

BOTTOM — Note: "The shared layer is large. The unique edges are where the real decision happens." -->

### What Both Tools Share

These capabilities exist in both tools and should not be treated as differentiators:

| Capability | GitHub Copilot | Claude Code |
|-----------|---------------|-------------|
| **Agentic loop** | IDE agent mode, CLI agent, coding agent — all use reason→act→verify cycles | Single agentic loop across all surfaces |
| **Plan mode** | Shift+Tab in CLI; structured planning before coding | `/plan` command; describe-then-approve workflow |
| **MCP support** | Agent mode, CLI, and coding agent. GitHub MCP server. OAuth. Enterprise policies. | HTTP, SSE, stdio transports. Project/user/managed scopes. Tool search optimization. |
| **Custom instructions** | `.github/copilot-instructions.md` + scoped `.instructions.md` files | `CLAUDE.md` files (project, directory, user, enterprise hierarchy) |
| **Skills / commands** | Agent Skills (open standard), slash commands, community sharing | Skills (auto-discovered), slash commands, team sharing |
| **Hooks** | sessionStart, preToolUse, postToolUse, userPromptSubmitted, sessionEnd. `.github/hooks/*.json`. | After edits, before commits, custom lifecycle points. Exit code 2 blocks + feeds error back. |
| **Custom agents** | `.agent.md` files with own tools, MCP, instructions. Subagent with own context window. | `.claude/agents/` Markdown files with YAML frontmatter. Own prompts, tools, permissions. |
| **Checkpoint / undo** | Esc-Esc rewind in CLI. Session checkpoints. `/diff` review. VS Code chat checkpoints. | Every prompt creates checkpoint. Rewind menu: restore code, conversation, or both. 30-day persistence. |
| **Context compaction** | Automatic at 95% capacity in CLI | Auto-compacts tool outputs, then summarizes conversation |
| **Model switching** | `/model` mid-session across all surfaces | `/model` mid-session or `--model` at launch |
| **CI/CD mode** | GitHub Actions built-in, coding agent | Headless mode for GitHub Actions and GitLab CI/CD |

### Where They Genuinely Differ

| Capability | GitHub Copilot | Claude Code | Advantage |
|-----------|---------------|-------------|-----------|
| **Inline completions** | 35ms autocomplete — the primary daily interaction for most devs | No inline autocomplete | Copilot |
| **Async cloud agent** | Coding agent runs in GitHub Actions. Works while computer is off. Assign issues, get PRs back. | No equivalent autonomous cloud agent | Copilot |
| **Multi-vendor models** | OpenAI, Anthropic, Google, xAI — 15+ models as first-party options | Anthropic models only (third-party via config) | Copilot |
| **Agent HQ** | Run Claude, Codex, and Copilot together. One subscription. Multi-vendor agent platform. | N/A | Copilot |
| **Cross-session memory** | Copilot Memory: automatic, cross-agent, repository-specific. Validated before use. 28-day expiry. | Manual via CLAUDE.md. No automatic memory extraction. | Copilot |
| **Security scanning** | CodeQL, Advisory Database, secret scanning — built into coding agent | External via MCP integrations | Copilot |
| **Extensions marketplace** | Third-party integrations (Sentry, Docker, Stripe, MongoDB). Growing ecosystem. | N/A | Copilot |
| **Agent Teams** | Parallel agent execution, but no lead-agent coordination or shared task lists | Lead agent + task list + parallel workers on shared codebase. Research preview. | Claude Code |
| **Agent SDK** | N/A (Copilot SDK exists but is different in scope) | Full SDK for custom agents. Used by Apple's Xcode. | Claude Code |
| **Plugin system** | No equivalent bundling mechanism | Packages skills + MCP + hooks + subagents into versioned bundles | Claude Code |
| **Context approach** | Retrieval-augmented: repo indexing + Spaces + Memory | Direct ingestion: 200k token window with files loaded in context | Claude Code (transparency) |
| **Checkpoint granularity** | File-level rewind | Code + conversation independent restoration. Summarize-from-here. | Claude Code |
| **Non-IDE surfaces** | GitHub.com, GitHub Mobile | Desktop app, web (claude.ai/code), Slack, Chrome extension | Claude Code |
| **IP indemnity** | Business and Enterprise plans | Not announced | Copilot |
| **Pricing entry** | Free tier; $10/month Pro | $20/month Pro (no free tier) | Copilot |

## Feature Comparison

Complete side-by-side breakdown of capabilities, updated for February 2026.

<!-- Visualization: Feature comparison table
Styled as a two-column grid with alternating row backgrounds.
Left column header: GitHub Copilot (blue accent)
Right column header: Claude Code (amber accent)
Each row has a category label on the left edge.
Use checkmarks, partial indicators, or brief text in each cell.
Highlight rows where features are shared with a subtle "shared" indicator. -->

| Dimension | GitHub Copilot | Claude Code |
|-----------|---------------|-------------|
| **Primary interface** | IDE-embedded + CLI (GA Feb 2026) + GitHub.com | Terminal-first CLI + IDE extensions + desktop app + web |
| **Core interaction** | Inline completions + agentic modes (IDE, CLI, cloud) | Agentic loop: reason, act, verify, repeat |
| **Context scope** | Repository indexing + Copilot Spaces + Copilot Memory | Full project via 200k token context window |
| **Model strategy** | Multi-vendor marketplace (OpenAI, Anthropic, Google, xAI) | Anthropic models (Sonnet, Opus, Haiku); third-party via config |
| **Agent surfaces** | IDE agent mode + async coding agent (Actions) + CLI agent | Single agentic loop across terminal, IDE, desktop, web, Slack |
| **Multi-agent** | Parallel specialized agents; custom agents (.agent.md); Agent HQ (Claude + Codex + Copilot) | Agent Teams with lead coordination; custom subagents; Agent SDK |
| **Extensibility** | MCP, Agent Skills, hooks, Copilot Extensions marketplace | MCP, skills, hooks, plugins (bundled packages), Claude Code as MCP server |
| **Custom instructions** | `.github/copilot-instructions.md` + scoped `.instructions.md` | `CLAUDE.md` hierarchy (project → directory → user → enterprise) |
| **Code review** | Built-in — mention @copilot on PRs, blends LLM + CodeQL | Via skills/hooks, or headless mode in CI |
| **Security scanning** | CodeQL, Advisory Database, secret scanning built-in | External via MCP integrations |
| **CLI experience** | GA Feb 2026 — plan, autopilot, background delegation, memory | Native from inception — terminal is primary interface |
| **Execution model** | Inline suggestions + multi-step agentic execution + autonomous cloud agent | Runs commands, edits files, creates commits autonomously |
| **Safety model** | Checkpoint rewind (Esc-Esc), /diff review, sandboxed coding agent | Checkpoints, permission modes, rewind menu (code + conversation) |
| **Cross-session memory** | Copilot Memory (automatic, cross-agent, validated, 28-day) | CLAUDE.md (manual, persistent), session resume (--continue) |
| **Enterprise governance** | Audit logs, content filters, policy controls, IP indemnity, MCP policies | Managed MCP, compliance API, managed settings, permission modes |

## IDE and Surface Support

Where each tool is available, and how deep the integration goes.

<!-- Visualization: Grid matrix with IDE/surface rows and feature columns
Rows: VS Code, JetBrains, Visual Studio, Xcode, Eclipse, Vim/Neovim, Terminal CLI, Desktop App, Web, Mobile, GitHub.com, Slack, CI/CD
Columns grouped: "GitHub Copilot" features (completions, chat, agent mode, code review) and "Claude Code" features (agentic loop, inline diffs, plan review)
Use filled circles (full support), half circles (partial/preview), empty circles (no support)
Color-code the column groups: blue for Copilot, amber for Claude Code -->

| Surface | GitHub Copilot | Claude Code |
|---------|---------------|-------------|
| **VS Code** | Completions, chat, agent mode (GA), edits, code review | Native extension — inline diffs, @-mentions, plan review |
| **JetBrains** | Completions, chat, agent mode, edits, code review, Agent Skills (preview) | Plugin — diff viewing, selection sharing (beta) |
| **Visual Studio** | Completions, chat, agent mode (preview), edits, code review | Not available |
| **Xcode** | Completions, chat, agent mode | Native via Claude Agent SDK (Xcode 26.3+) |
| **Eclipse** | Completions, chat, agent mode | Not available |
| **Vim/Neovim** | Completions only | Not available |
| **Terminal CLI** | GA Feb 2026 — plan mode, autopilot, specialized agents, memory | Primary interface — full-featured from day one |
| **Desktop App** | Not available | Standalone app — visual diffs, multiple sessions |
| **Web** | GitHub.com integration, Agent HQ | claude.ai/code — no local setup, parallel sessions |
| **Slack** | Not available | @Claude mention → get a PR back |
| **GitHub Mobile** | Copilot Chat, Agent HQ | Not available |
| **CI/CD** | GitHub Actions built-in, coding agent | Headless mode for Actions and GitLab CI/CD |

**Copilot's edge:** broadest editor and platform coverage. Seven IDEs, GitHub Mobile, and Agent HQ as a multi-agent hub.

**Claude Code's edge:** unique surfaces. Desktop app, web interface, Slack integration, and Chrome extension for browser debugging — surfaces Copilot doesn't cover.

## Customization and Extensibility

How each tool lets developers and teams tailor behavior.

<!-- Visualization: Side-by-side stacked feature cards
LEFT STACK — "GitHub Copilot" with blue accent
Card 1: "Custom Instructions" — .github/copilot-instructions.md, scoped .instructions.md
Card 2: "Agent Skills" — Markdown-based, auto-discovered, open standard
Card 3: "Custom Agents" — .agent.md files with own tools and MCP
Card 4: "Hooks" — 5 trigger points, policy enforcement, .github/hooks/*.json
Card 5: "MCP Servers" — Agent mode, CLI, coding agent. GitHub MCP server.
Card 6: "Extensions" — Marketplace with third-party integrations

RIGHT STACK — "Claude Code" with amber accent
Card 1: "CLAUDE.md" — Hierarchical, survives compaction, enterprise-managed
Card 2: "Skills" — Auto-discovered folders, slash commands, team sharing
Card 3: "Subagents" — .claude/agents/ with YAML frontmatter, custom permissions
Card 4: "Hooks" — Shell triggers, exit code 2 blocks + feeds error to agent
Card 5: "MCP Servers" — HTTP/SSE/stdio, project/user/managed scopes, tool search
Card 6: "Plugins" — Bundles skills + MCP + hooks + subagents into packages -->

| Layer | GitHub Copilot | Claude Code |
|-------|---------------|-------------|
| **Project instructions** | `.github/copilot-instructions.md` + scoped `.instructions.md` | `CLAUDE.md` hierarchy (project, directory, user, enterprise) |
| **Skills** | Agent Skills: markdown files, auto-discovered, slash commands. Open standard shared with Claude Code. | Skills: instruction folders, auto-discovered, slash commands. Same open standard. |
| **Custom agents** | `.agent.md` with tools, MCP, instructions. Subagent gets own context window. | `.claude/agents/` with YAML frontmatter, tool restrictions, permission modes. |
| **Hooks** | `.github/hooks/*.json` — sessionStart, preToolUse, postToolUse, userPromptSubmitted, sessionEnd | Settings-configured — after edits, before commits. Exit code 2 feeds error back to Claude. |
| **MCP** | IDE, CLI, and coding agent. OAuth. Enterprise MCP policies. GitHub MCP server. | HTTP/SSE/stdio. Project/user/managed scopes. Tool search. Claude Code as MCP server. |
| **Plugins / Extensions** | Copilot Extensions marketplace (Sentry, Docker, Stripe, etc.) | Plugins: bundles of skills + MCP + hooks + subagents. Pinnable to git SHAs. |
| **Memory** | Copilot Memory (automatic, cross-agent, repository-specific, 28-day) | CLAUDE.md (manual, persistent, survives compaction) |

## Pricing Comparison

What each tool costs as of February 2026.

<!-- Visualization: Two side-by-side pricing card stacks
LEFT — "GitHub Copilot" pricing cards stacked vertically:
Free ($0), Pro ($10/mo), Pro+ ($39/mo), Business ($19/user/mo), Enterprise ($39/user/mo)
Each card shows: price, key limits (completions, premium requests), standout feature

RIGHT — "Claude Code" pricing cards stacked vertically:
Pro ($20/mo), Max Expanded ($100/mo), Max Maximum ($200/mo), Team (per-seat), Enterprise (per-seat)
Each card shows: price, usage level, standout feature

Bottom callout: "Copilot has a free tier and starts at $10/mo. Claude Code starts at $20/mo with no free tier." -->

### GitHub Copilot Plans

| Plan | Price | Highlights |
|------|-------|------------|
| **Free** | $0 | 2,000 completions/month, 50 chat messages, 50 premium requests |
| **Pro** | $10/month | Unlimited completions, coding agent, code review, 300 premium requests |
| **Pro+** | $39/month | All models, GitHub Spark, 1,500 premium requests |
| **Business** | $19/user/month | User management, usage metrics, IP indemnity, 300 premium requests |
| **Enterprise** | $39/user/month | All models incl. Opus 4.6, full admin controls, 1,000 premium requests |

Free access for verified students, teachers, and open-source maintainers (Pro tier).

### Claude Code Plans

| Plan | Price | Highlights |
|------|-------|------------|
| **Pro** | $20/month | Claude Code access with Sonnet and Opus models |
| **Max Expanded** | $100/month | 5x Pro usage, priority access to new features |
| **Max Maximum** | $200/month | 20x Pro usage, for daily heavy users |
| **Team** | Per-seat pricing | Self-serve seat management, spend controls, analytics |
| **Enterprise** | Per-seat pricing | Managed policies, compliance API, granular admin controls |

API access also available for both tools via their respective platforms.

### Pricing Takeaway

Copilot offers a free tier and lower entry price ($10/month vs $20/month). For individual developers, Copilot is the more accessible starting point. For teams already invested in the Anthropic ecosystem or needing deep agent orchestration (Agent Teams, Agent SDK, plugins), Claude Code's pricing aligns with its deeper capability set. Both offer enterprise tiers with governance controls. Note: Copilot Pro+ and Enterprise subscribers get access to Claude models within Copilot via Agent HQ.

## Enterprise and Governance

Both tools address enterprise concerns — through different mechanisms.

<!-- Visualization: Two-column comparison card
LEFT — "GitHub Copilot" with blue border
Bullet items: Centralized policy management, Audit logs (180 days), Content exclusion rules, IP indemnity on Business+, Usage analytics per org, Model availability controls, MCP policy governance, GHEC integration

RIGHT — "Claude Code" with amber border
Bullet items: Managed MCP for centralized tool deployment, Compliance API, Permission modes (default/plan/dontAsk/bypassPermissions), Per-project configuration via CLAUDE.md hierarchy, Checkpoint audit trail, Sandbox mode with OS-level isolation, Managed settings.json for org-wide policy, Hook-based policy enforcement -->

| Concern | GitHub Copilot | Claude Code |
|---------|---------------|-------------|
| **Policy management** | Org/enterprise owners control features, models, access. MCP policies. | Managed settings.json, permission modes, CLAUDE.md hierarchy |
| **Audit** | Audit logs (180 days), action-searchable | Checkpoint history, compliance API |
| **Content filtering** | Content exclusion for files/repos | Permission rules (deny/ask/allow), tool restrictions |
| **IP protection** | IP indemnity on Business and Enterprise | No IP indemnity announced |
| **Usage tracking** | Per-org adoption metrics | Spend controls, usage analytics on Team/Enterprise |
| **Sandbox/isolation** | Coding agent in sandboxed Actions environment | OS-level sandbox mode, git worktree isolation |
| **Hook-based policy** | preToolUse hooks can block operations, enforce standards | Exit code 2 blocks operations, feeds error to agent |

## The GitHub Agent HQ Factor

A development that changes the competitive landscape: as of February 2026, GitHub Agent HQ runs Claude, Codex, and Copilot together inside github.com, GitHub Mobile, and VS Code. No additional subscription required for Copilot paid users.

This means a team using Copilot Business or Enterprise gets access to Claude's reasoning within the Copilot platform. The "which tool to choose" question becomes less binary — you can use Claude through Copilot rather than alongside it.

**What Agent HQ does:** lets developers assign different AI agents to different tasks based on strengths. Claude for complex reasoning, Codex for rapid generation, Copilot for ecosystem integration. Agents run asynchronously by default. GitHub is also working with Google, Cognition, and xAI to bring more agents.

**What Agent HQ doesn't do:** provide Claude Code's full feature set. Agent HQ runs Claude as an agent within Copilot's framework — it doesn't provide Agent Teams, the Agent SDK, the plugin system, CLAUDE.md, or Claude Code's checkpoint system. For Claude Code's deepest capabilities, you still need Claude Code itself.

## When to Use Which

A decision guide based on the task, the workflow, and the ecosystem you're already in.

<!-- Visualization: Decision flowchart / tree
Start node: "What kind of task?"
Branch 1: "Inline completions while typing?" → "Copilot" (blue)
Branch 2: "Multi-agent orchestrated refactor?" → "Claude Code Agent Teams" (amber)
Branch 3: "Async issue resolution in background?" → "Copilot coding agent" (blue)
Branch 4: "Need custom agent with plugin bundle?" → "Claude Code" (amber)
Branch 5: "PR code review with security scan?" → "Copilot" (blue)
Branch 6: "Complex terminal-driven development?" → "Either — both have full CLI agents" (green)
Branch 7: "Already on GitHub ecosystem?" → "Copilot (can include Claude via Agent HQ)" (blue)
Branch 8: "Need deep Anthropic integration?" → "Claude Code" (amber) -->

| Task | Recommended | Why |
|------|------------|-----|
| Inline completions while typing | Copilot | 35ms autocomplete. Claude Code has no equivalent. |
| Refactoring across many files | Either | Both have agentic loops with multi-file editing. Claude Code's 200k context gives an edge on very large scopes. |
| Async background issue resolution | Copilot | Coding agent works autonomously in GitHub Actions. Claude Code has no equivalent cloud agent. |
| PR code review | Copilot | Native @copilot mention, blends LLM + CodeQL. Claude Code requires CI setup. |
| Security vulnerability scanning | Copilot | CodeQL + Advisory Database + secret scanning built in. |
| Complex terminal-driven development | Either | Both have full-featured CLI agents with plan mode. Claude Code has more experience here. |
| Multi-agent coordinated development | Claude Code | Agent Teams with lead agent, task lists, and branch isolation. |
| Custom agent ecosystem (bundled tools) | Claude Code | Plugin system packages skills + MCP + hooks. No Copilot equivalent. |
| Connecting external tools via MCP | Either | Both support MCP. Copilot has enterprise MCP policies; Claude Code has more transport options. |
| Onboarding to a legacy codebase | Either | Both can analyze full repositories. Claude Code's direct context ingestion may provide more thorough understanding. |
| Already in the GitHub ecosystem | Copilot | Deepest GitHub integration. Agent HQ adds Claude reasoning when needed. |
| Need model variety | Copilot | Multi-vendor marketplace with 15+ models. |
| Building custom agent applications | Claude Code | Agent SDK for fully custom agents. Used by Apple's Xcode. |

## The Complementary Pattern

The emerging pattern among high-productivity developers: run both. Not as redundancy — as division of labor.

<!-- Visualization: Workflow timeline / day-in-the-life horizontal strip
Left to right, alternating colored blocks representing a developer's day:

1. [Blue] Morning — Copilot autocompletes as you write new API endpoints. 35ms inline, zero friction.
2. [Amber] Mid-morning — Claude Code Agent Teams refactor the authentication module across 12 files. Multi-agent, deep reasoning.
3. [Blue] Afternoon — Assign a bug-fix issue to Copilot's coding agent. It works in the background while you move on.
4. [Amber] Late afternoon — Claude Code explains the payment system architecture to a new team member. Full-project context.
5. [Blue] End of day — Copilot reviews your PR with CodeQL and suggests improvements. GitHub-native.

Bottom label: "Copilot for the rhythm. Claude Code for the inflection points." -->

Copilot handles the constant rhythm of daily coding — inline completions, test generation, PR reviews, security scanning, background issue resolution. Claude Code handles the inflection points — the deep refactors, the multi-agent coordinated changes, the custom tool integrations that shape how the codebase evolves.

With Agent HQ, the line blurs further — Copilot subscribers can access Claude's reasoning within the Copilot platform for specific tasks, while still reaching for standalone Claude Code when they need its full depth (Agent Teams, plugins, Agent SDK).

**The question isn't which to choose. It's how to combine them.**

---

## Sources

<!-- HTML color coding suggestion:
  - GitHub Copilot sources: blue accent (#58a6ff / var(--compare-copilot))
  - Claude Code sources: amber accent (#f6a44c / var(--compare-claude))
  - Comparison sources: neutral color (e.g., var(--text-secondary) or white)
-->

### Comparison

- [GitHub Copilot vs Claude Code](https://www.youtube.com/watch?v=rNojsNYFBd4) — Trader Jono Blueprint (Feb 2026)

### GitHub Copilot

- [GitHub Copilot Features](https://docs.github.com/en/copilot/get-started/features) — GitHub docs
- [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) — GitHub docs
- [Supported AI Models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models) — GitHub docs
- [Agent Mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/) — GitHub blog
- [About GitHub Copilot Coding Agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) — GitHub docs
- [GitHub Copilot CLI GA](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/) — GitHub blog
- [Copilot CLI Enhanced Agents](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/) — GitHub blog
- [Copilot CLI Plan Mode](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go/) — GitHub blog
- [Creating Custom Agents for CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli) — GitHub docs
- [About MCP in Copilot](https://docs.github.com/en/copilot/concepts/context/mcp) — GitHub docs
- [Adding Custom Instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) — GitHub docs
- [Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills) — VS Code docs
- [Using Hooks with Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-hooks) — GitHub docs
- [Hooks Configuration](https://docs.github.com/en/copilot/reference/hooks-configuration) — GitHub docs
- [Building an Agentic Memory System](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) — GitHub blog
- [Pick Your Agent: Agent HQ](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/) — GitHub blog
- [Claude and Codex for Business & Pro](https://github.blog/changelog/2026-02-26-claude-and-codex-now-available-for-copilot-business-pro-users/) — GitHub blog
- [VS Code Chat Checkpoints](https://code.visualstudio.com/docs/copilot/chat/chat-checkpoints) — VS Code docs
- [Copilot Extensions](https://github.com/features/copilot/extensions) — GitHub
- [GitHub Copilot Plans & Pricing](https://github.com/features/copilot/plans) — GitHub

### Claude Code

- [Claude Code Overview](https://code.claude.com/docs/en/overview) — Anthropic docs
- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works) — Anthropic docs
- [Claude Code Product Page](https://www.anthropic.com/claude-code) — Anthropic
- [Claude Code Checkpointing](https://code.claude.com/docs/en/checkpointing) — Anthropic docs
- [Claude Code MCP](https://code.claude.com/docs/en/mcp) — Anthropic docs
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — Anthropic docs
- [Introducing Agent Skills](https://claude.com/blog/skills) — Anthropic blog
- [Enabling Claude Code to Work More Autonomously](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously) — Anthropic
- [Claude Code Plugins](https://www.anthropic.com/news/claude-code-plugins) — Anthropic
- [Claude Agent SDK in Xcode](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk) — Anthropic
- [Anthropic Pricing](https://www.anthropic.com/pricing) — Anthropic
