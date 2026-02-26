# GitHub Copilot — Vendor Research

> Research compiled from official GitHub/Microsoft sources, February 2026.

## Overview

GitHub Copilot is GitHub's AI coding assistant, launched June 2021, now evolved from a single-model inline autocomplete tool into a multi-model platform spanning IDE integration, autonomous coding agents, CLI, code review, and full GitHub ecosystem features. It defaults to GPT-4.1 across chat, agent mode, and code completions, but offers model choice from OpenAI, Anthropic, and Google across paid tiers.

## Architecture and Models

### Multi-Model Platform

Copilot transitioned away from its original Codex foundation to a dynamic multi-model architecture. The system matches models to tasks rather than using a fixed pipeline.

- **Default model**: GPT-4.1 — optimized for speed, reasoning, and context handling; tuned for developer workflows; supports 30+ programming languages.
- **Available models** (paid tiers): OpenAI GPT-4.1, GPT-5 mini, GPT-5.1, GPT-5.1-Codex, GPT-5.2, GPT-5.3-Codex; Anthropic Claude Haiku 4.5, Claude Sonnet 4/4.5/4.6, Claude Opus 4.5/4.6; Google Gemini 2.5 Pro, Gemini 3 Flash/Pro; xAI Grok Code Fast 1.
- **Premium request multipliers** vary by model — from 0 (base models on paid plans) to 30 (Claude Opus 4.6 fast mode preview).
- Users can switch models mid-session in both IDE chat and CLI via `/model` command.

**Source**: [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models); [Under the hood: Exploring the AI models powering GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/under-the-hood-exploring-the-ai-models-powering-github-copilot/)

### Context Gathering

- Since September 2025: 2x higher throughput, 37.6% better retrieval accuracy, 8x smaller index size.
- Full repository context analysis with cross-repository awareness.
- Copilot Spaces (preview) allows organizing relevant content — code, docs, specs — to ground responses contextually.
- Copilot Memory (preview) stores repository information for enhanced agent and review outputs across sessions.

**Source**: [GitHub Copilot features](https://docs.github.com/en/copilot/get-started/features)

## Core Product: Inline Code Completion

Autocomplete-style suggestions in supported IDEs. The primary interaction model — predictions for function bodies, pattern completion, boilerplate from comments. Next edit suggestions available in preview for VS Code, Xcode, and Eclipse.

- Free tier: 2,000 completions/month.
- All paid tiers: unlimited completions.

**Source**: [GitHub Copilot features](https://docs.github.com/en/copilot/get-started/features)

## Agent Mode (IDE)

Released April 2025. An autonomous, synchronous collaborator inside the IDE that performs multi-step coding tasks from natural-language prompts.

### How It Works

Operates as an orchestrator combining prompts, workspace context, and tools via a backend system prompt. When given a request, Copilot parses it, queries the language model, monitors for errors, and uses tools (`read_file`, `edit_file`, `run_in_terminal`) to reach the outcome. Detects syntax errors and terminal output, then self-corrects iteratively.

### Capabilities

- Analyzes full codebases for context.
- Executes multi-step solutions.
- Automatically recognizes and fixes errors.
- Integrates with MCP servers for extended functionality.
- Supports custom instructions and multiple AI models.

### IDE Availability

- VS Code (GA), Visual Studio (preview), JetBrains IDEs, Eclipse, Xcode.

### Limitations

Nondeterministic — identical prompts may produce different results. Requires human oversight to review generated code.

**Source**: [Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/)

## Coding Agent (Asynchronous)

GA for all paid Copilot subscribers as of September 2025. An autonomous background agent that works asynchronously on development tasks.

### How It Works

Assign a GitHub issue to Copilot or request work from Copilot Chat in VS Code. The agent spins up an ephemeral development environment powered by GitHub Actions, explores code, makes modifications, executes tests and linters, and opens a draft pull request with the results. Pushes commits incrementally; users track progress via session logs.

### Task Scope

Best for low-to-medium complexity tasks in well-tested codebases:
- Bug fixes, incremental feature implementation, test coverage improvement.
- Documentation updates, technical debt resolution, refactoring.

### Security Protections

- CodeQL analysis for security issues in generated code.
- GitHub Advisory Database checks for vulnerable dependencies.
- Secret scanning for API keys and tokens.
- Sandboxed environment with controlled internet access.
- Read-only repository access except for `copilot/` branches.
- Cannot approve or merge its own pull requests.

### Limitations

- Single repository operations only.
- One pull request per task assignment.
- Incompatible with certain branch protections (e.g., required signed commits).
- GitHub-hosted repositories only.

### MCP Integration

Teams can give the coding agent access to external data and capabilities via MCP servers configured in repository settings. OAuth support enables secure third-party integrations (Slack, Jira, custom APIs).

**Source**: [About GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent); [Coding agent GA announcement](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/)

## Copilot CLI

GA February 25, 2026. A terminal-native coding agent bringing Copilot directly to the command line.

### Modes

- **Plan mode** (Shift+Tab): structured planning — analyzes requests, builds implementation blueprints before coding.
- **Autopilot mode**: fully autonomous execution without approval for trusted tasks.
- **Background delegation**: prefix prompts with `&` to offload work to cloud-based agents.

### Features

- Specialized agents automatically route tasks to focused agents for exploration, task execution, code review, and planning.
- `/diff` for syntax-highlighted change review; `/review` for staged code analysis.
- Automatic context compression at 95% capacity for indefinite conversations.
- Repository memory — learns codebase conventions across sessions.
- Undo via Esc-Esc to rewind file modifications.
- Model selection: Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.3-Codex, Gemini 3 Pro; switch mid-session.

### Platforms

macOS, Linux, Windows. Install via npm, Homebrew, WinGet, shell scripts, standalone executables. Included in GitHub Codespaces.

### Enterprise Controls

Administrators can control model availability, manage network access, enforce proxy protocols, and implement policy hooks.

**Source**: [GitHub Copilot CLI is now generally available](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/); [GitHub Copilot CLI: Enhanced agents, context management, and new ways to install](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)

## IDE Support

### Supported Editors

| IDE | Completions | Chat | Agent Mode | Edits | Code Review |
|-----|:-----------:|:----:|:----------:|:-----:|:-----------:|
| VS Code | Yes | Yes | Yes (GA) | Yes | Yes |
| Visual Studio | Yes | Yes | Yes (preview) | Yes | Yes |
| JetBrains family | Yes | Yes | Yes | Yes | Yes |
| Xcode | Yes | Yes | Yes | — | Yes |
| Eclipse | Yes | Yes | Yes | — | — |
| Vim/Neovim | Yes | — | — | — | — |
| Azure Data Studio | Yes | — | — | — | — |

Visual Studio 2022 (17.10+) includes the Copilot extension as a built-in component by default.

**Source**: [Installing the GitHub Copilot extension](https://docs.github.com/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment); [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)

## GitHub Ecosystem Integration

### Code Review

Copilot code review (CCR) blends LLM detections with deterministic tools (ESLint, CodeQL). Mention `@copilot` in a pull request to trigger review. CCR can hand suggested changes to the coding agent, which applies them in a stacked PR.

Available in VS Code, Visual Studio, JetBrains, and Xcode.

**Source**: [Copilot code review: AI reviews that see the full picture](https://github.blog/changelog/2025-10-28-new-public-preview-features-in-copilot-code-review-ai-reviews-that-see-the-full-picture/)

### Pull Request Summaries

Automated change descriptions highlighting affected files and review priorities.

### Code Scanning and Security

- Assign code scanning alerts directly to Copilot for automated remediation — Copilot analyzes the vulnerability, creates a remediation plan, opens a draft PR.
- Coding agent proactively runs CodeQL, checks GitHub Advisory Database, and runs secret scanning on its own output.

**Source**: [Assign code scanning alerts to Copilot](https://github.blog/changelog/2025-10-28-assign-code-scanning-alerts-to-copilot-for-automated-fixes-in-public-preview/); [Copilot coding agent validates code security](https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-automatically-validates-code-security-and-quality/)

### GitHub Mobile and Desktop

- Copilot Chat available on GitHub Mobile.
- GitHub Desktop: automatic commit message and description generation.

### GitHub Spark (Preview)

Natural-language full-stack application development with GitHub integration. Available on Pro+ and Enterprise tiers.

## Enterprise Controls

### Policy Management

Organization and enterprise owners can:
- Specify which organizations/members can use Copilot.
- Enable or disable specific features per organization.
- Configure allowed models.

### Content Exclusion

Business and Enterprise tiers can configure Copilot to ignore specific files and repositories. Changes are audit-logged.

### Audit Logs

Available on Business and Enterprise plans. Lists Copilot-related events for the last 180 days, searchable by `action:copilot` category.

### Usage Analytics

Adoption metrics and usage tracking per organization.

**Source**: [Managing policies for Copilot](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization); [Reviewing audit logs](https://docs.github.com/copilot/managing-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business); [Content exclusion](https://docs.github.com/en/copilot/concepts/context/content-exclusion)

## Pricing (February 2026)

| Plan | Price | Premium Requests | Key Differentiators |
|------|-------|-----------------|---------------------|
| **Free** | $0 | 50/month | 2,000 completions/month, 50 chat messages |
| **Pro** | $10/month ($100/year) | 300/month | Unlimited completions, coding agent, code review, model choice |
| **Pro+** | $39/month ($390/year) | 1,500/month | Full access to all models, GitHub Spark |
| **Business** | $19/user/month | 300/user/month | User management, usage metrics, IP indemnity, policy controls |
| **Enterprise** | $39/user/month | 1,000/user/month | All models incl. Opus 4.6, Spark, knowledge bases, full admin controls |

Additional premium requests: $0.04 USD per request on all paid plans.

Free access for verified students, teachers, and maintainers of popular open-source projects (Copilot Pro tier).

**Source**: [GitHub Copilot Plans & pricing](https://github.com/features/copilot/plans); [Individual plans and benefits](https://docs.github.com/en/copilot/concepts/billing/individual-plans)

## Recent Updates (January–February 2026)

- **Feb 25, 2026**: Copilot CLI reaches general availability with autopilot mode, plan mode, background delegation, and repository memory.
- **Feb 13, 2026**: JetBrains IDEs get Agent Skills preview — agent mode supports skills to tailor workflows.
- **Feb 4, 2026**: VS Code v1.109 release — Claude agent support via Anthropic's Claude Agent SDK in public preview; MCP app integration improvements; Copilot Memory; faster code search via external indexing.
- **Feb 4, 2026**: Visual Studio January update — colorized code completions, partial acceptance.
- **Jan 14, 2026**: Copilot CLI enhanced agents with GPT-5 mini and GPT-4.1 (no premium request cost); web_fetch tool; Copilot Spaces integration via GitHub MCP server; auto-compaction.

**Source**: [GitHub Copilot CLI GA](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/); [JetBrains improvements](https://github.blog/changelog/2026-02-13-new-features-and-improvements-in-github-copilot-in-jetbrains-ides-2/); [VS Code v1.109](https://github.blog/changelog/2026-02-04-github-copilot-in-visual-studio-code-v1-109-january-release/); [CLI enhanced agents](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)

## Architectural Comparison with Claude Code

| Dimension | GitHub Copilot | Claude Code |
|-----------|---------------|-------------|
| **Primary interface** | IDE-embedded (completions, chat, agent mode) + CLI + GitHub.com | Terminal-first CLI |
| **Core strength** | Breadth — inline completions, code review, PRs, security scanning, CI/CD integration all in one platform | Depth — 200k token context window, full-project reasoning, multi-file coordination |
| **Agent approach** | Two distinct agents: synchronous agent mode in IDE + asynchronous coding agent via GitHub Actions | Single agentic loop in terminal with checkpoint/rollback |
| **Model strategy** | Multi-vendor marketplace (OpenAI, Anthropic, Google, xAI) with dynamic model matching | Anthropic models only (Claude family) |
| **Ecosystem integration** | Deep GitHub-native: issues, PRs, code review, Actions, security scanning, Codespaces | Version control integration; extensible via MCP for external tools |
| **Enterprise governance** | Centralized policy management, audit logs, content exclusion, usage analytics, IP indemnity | Per-project configuration, permission modes |
| **Context mechanism** | Repository indexing with retrieval; Copilot Spaces for curated context; Memory for cross-session persistence | Full repository ingestion into context window; CLAUDE.md for project instructions |
| **CLI experience** | GA Feb 2026 — plan mode, autopilot, background delegation, repository memory | Native from inception — terminal is the primary interface |

## Sources

- [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models) — model catalog and plan availability
- [Under the hood: Exploring the AI models powering GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/under-the-hood-exploring-the-ai-models-powering-github-copilot/) — architecture and model evolution
- [Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/) — agent mode capabilities and design
- [About GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) — async coding agent docs
- [Coding agent GA](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/) — September 2025 GA announcement
- [GitHub Copilot coding agent announcement](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot) — Microsoft Build 2025 press release
- [GitHub Copilot features](https://docs.github.com/en/copilot/get-started/features) — complete feature list
- [Copilot feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) — feature availability by IDE
- [GitHub Copilot Plans & pricing](https://github.com/features/copilot/plans) — current pricing tiers
- [Individual plans and benefits](https://docs.github.com/en/copilot/concepts/billing/individual-plans) — Pro and Pro+ details
- [Getting free access to Copilot Pro](https://docs.github.com/en/copilot/how-tos/manage-your-account/get-free-access-to-copilot-pro) — student/teacher/maintainer eligibility
- [Managing policies for Copilot](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization) — enterprise policy controls
- [Content exclusion](https://docs.github.com/en/copilot/concepts/context/content-exclusion) — content filtering configuration
- [Reviewing audit logs](https://docs.github.com/copilot/managing-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business) — audit log documentation
- [Copilot code review: AI reviews that see the full picture](https://github.blog/changelog/2025-10-28-new-public-preview-features-in-copilot-code-review-ai-reviews-that-see-the-full-picture/) — code review enhancements
- [Assign code scanning alerts to Copilot](https://github.blog/changelog/2025-10-28-assign-code-scanning-alerts-to-copilot-for-automated-fixes-in-public-preview/) — security alert remediation
- [GitHub Copilot CLI GA](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/) — CLI general availability
- [GitHub Copilot CLI: Enhanced agents](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/) — CLI January 2026 update
- [VS Code v1.109](https://github.blog/changelog/2026-02-04-github-copilot-in-visual-studio-code-v1-109-january-release/) — January 2026 VS Code release
- [JetBrains improvements](https://github.blog/changelog/2026-02-13-new-features-and-improvements-in-github-copilot-in-jetbrains-ides-2/) — February 2026 JetBrains update
- [Installing the GitHub Copilot extension](https://docs.github.com/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment) — installation docs
