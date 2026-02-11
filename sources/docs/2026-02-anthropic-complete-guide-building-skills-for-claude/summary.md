# The Complete Guide to Building Skills for Claude

> Source: [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) by Anthropic

## Overview

Official Anthropic guide covering the full lifecycle of building Claude Code skills — from structure and planning through testing, iteration, and distribution. Introduces the three-level progressive disclosure model (frontmatter → SKILL.md body → linked references), defines three skill categories (document/asset creation, workflow automation, MCP enhancement), and provides concrete patterns for multi-step orchestration, multi-MCP coordination, iterative refinement, and domain-specific intelligence. Aimed at developers and teams who want Claude to follow repeatable workflows consistently.

## Key Takeaways

- **Skills are instruction folders, not code.** A skill is a folder with a `SKILL.md` (required) plus optional scripts, references, and assets. No SDK or framework needed.
- **Progressive disclosure drives efficiency.** Three levels: YAML frontmatter (always in system prompt, triggers loading), SKILL.md body (loaded when relevant), linked reference files (loaded on demand). Minimizes token usage.
- **The frontmatter description is the most critical field.** It determines whether Claude loads the skill. Must include both what the skill does and when to use it, with specific trigger phrases.
- **Three skill categories cover most use cases.** Document/asset creation (no external tools needed), workflow automation (multi-step processes with validation gates), and MCP enhancement (workflow guidance layered on top of tool access).
- **MCP provides tools, skills provide recipes.** Without skills, users get raw tool access but no workflow guidance — leading to inconsistent results and higher support burden.
- **Five reusable patterns emerge.** Sequential workflow orchestration, multi-MCP coordination, iterative refinement, context-aware tool selection, and domain-specific intelligence.
- **Start with one task, then generalize.** Iterate on a single challenging task until Claude succeeds, extract the winning approach into the skill, then expand test coverage.
- **Testing covers three dimensions.** Triggering accuracy (loads when it should, doesn't when it shouldn't), functional correctness (outputs and API calls work), and performance comparison (fewer messages, fewer tokens, fewer errors vs. baseline).
- **Skills are an open standard.** Portable across Claude.ai, Claude Code, and API. Anthropic published Agent Skills as a cross-platform standard, with early ecosystem adoption.
- **Keep SKILL.md under 5,000 words.** Move detailed docs to `references/`. Too much content degrades performance. Concise, actionable instructions outperform verbose ones.

## Notes

### Skill Anatomy and File Structure

- Required file: `SKILL.md` (exact case, no variations)
- Optional directories: `scripts/` (executable code), `references/` (documentation), `assets/` (templates, fonts, icons)
- Folder naming: kebab-case only. No spaces, underscores, or capitals.
- No `README.md` inside the skill folder — all documentation goes in `SKILL.md` or `references/`. Repo-level README is separate for human visitors.

### Progressive Disclosure Model

- **Level 1 — YAML frontmatter:** Always loaded into Claude's system prompt. Minimal footprint. Determines whether Claude activates the skill.
- **Level 2 — SKILL.md body:** Loaded when Claude judges the skill relevant. Contains full instructions, examples, troubleshooting.
- **Level 3 — Linked files:** Reference docs, API guides, examples in `references/`. Claude navigates these on demand.
- Design goal: minimize token usage while maintaining specialized expertise.

### YAML Frontmatter

- Two required fields: `name` (kebab-case, must match folder name) and `description` (under 1024 characters).
- Optional fields: `license`, `compatibility` (1–500 chars, environment requirements), `metadata` (author, version, mcp-server, etc.).
- Security restrictions: no XML angle brackets (`<` `>`), no "claude" or "anthropic" in the skill name.
- Description structure: `[What it does] + [When to use it] + [Key capabilities]`. Must include trigger phrases users would actually say.

### The Three Skill Categories

- **Category 1 — Document & Asset Creation:** No external tools required. Uses embedded style guides, templates, quality checklists. Example: `frontend-design` skill.
- **Category 2 — Workflow Automation:** Multi-step processes with validation gates and iterative refinement loops. Can coordinate across multiple MCP servers. Example: `skill-creator` skill.
- **Category 3 — MCP Enhancement:** Adds workflow guidance on top of existing MCP tool access. Embeds domain expertise, provides context users would otherwise need to specify. Example: Sentry's `sentry-code-review` skill.

### Skills + MCP Integration

- MCP = the kitchen (tools, data access, equipment). Skills = the recipes (step-by-step instructions).
- Without skills: users don't know what to do after connecting MCP, each conversation starts from scratch, inconsistent results, higher support load.
- With skills: pre-built workflows activate automatically, consistent tool usage, lower learning curve.
- Skills give MCP integrations a competitive edge — users comparing connectors favor those with built-in workflow guidance.

### Five Design Patterns

1. **Sequential workflow orchestration:** Explicit step ordering with dependencies, validation at each stage, rollback instructions. Use for multi-step processes in a specific order.
2. **Multi-MCP coordination:** Clear phase separation across services (e.g., Figma → Drive → Linear → Slack). Data passing between MCPs, validation before advancing phases.
3. **Iterative refinement:** Generate draft → run validation script → fix issues → re-validate → repeat until quality threshold met. Use when output quality improves with iteration.
4. **Context-aware tool selection:** Decision tree based on context (file type, size, purpose) routes to different tools. Includes fallback options and transparency about choices.
5. **Domain-specific intelligence:** Embeds specialized knowledge (e.g., compliance rules, risk assessment) into the workflow logic. Compliance-before-action pattern with audit trails.

### Writing Effective Instructions

- Be specific and actionable: "Run `python scripts/validate.py --input {filename}`" beats "Validate the data."
- Include error handling with specific error messages, causes, and solutions.
- Reference bundled resources clearly: "Consult `references/api-patterns.md` for rate limiting guidance."
- Put critical instructions at the top. Use `## Important` or `## Critical` headers.
- For critical validations, bundle a script rather than relying on language instructions — code is deterministic.
- Keep SKILL.md under 5,000 words. Move detailed docs to `references/`.

### Testing Strategy

- **Triggering tests:** Verify skill loads on obvious tasks and paraphrased requests, doesn't load on unrelated queries. Debug by asking Claude: "When would you use the [skill name] skill?"
- **Functional tests:** Valid outputs, API calls succeed, error handling works, edge cases covered. Use Given/When/Then format.
- **Performance comparison:** Measure tool calls, token consumption, retry rates, back-and-forth messages with vs. without the skill.
- Iterate on a single challenging task first, extract the winning approach, then broaden test coverage.
- Three testing surfaces: manual in Claude.ai, scripted in Claude Code, programmatic via skills API.

### Troubleshooting Common Issues

- **Skill won't upload:** Check `SKILL.md` exact casing, YAML `---` delimiters, kebab-case name with no spaces/capitals.
- **Undertriggering:** Description too generic or missing trigger phrases. Add keywords, especially technical terms.
- **Overtriggering:** Add negative triggers ("Do NOT use for..."), narrow scope, clarify boundaries with other skills.
- **MCP calls fail:** Verify server connection, check auth/tokens, test MCP independently without the skill, confirm tool names (case-sensitive).
- **Instructions not followed:** Instructions too verbose, critical steps buried, ambiguous language. Move detail to `references/`, put key instructions at top.
- **Large context issues:** Too many skills enabled simultaneously (watch for 20–50+), SKILL.md too large, not using progressive disclosure.

### Distribution

- Current model: download folder → zip → upload to Claude.ai Settings or place in Claude Code skills directory.
- Organization-level: admins deploy workspace-wide with automatic updates (shipped Dec 2025).
- API access: `/v1/skills` endpoint, `container.skills` parameter in Messages API, works with Claude Agent SDK.
- Recommended: host on GitHub with clear README and examples, link from MCP documentation, provide installation guide.
- Position skills by outcomes, not features: "Set up complete project workspaces in seconds" not "A folder containing YAML frontmatter."
