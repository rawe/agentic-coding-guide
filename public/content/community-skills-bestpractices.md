# Writing Better Skills

The description triggers activation. The body teaches the workflow. Get both right.

## Where Content Goes

### description (frontmatter)

Trigger keywords, capability statements, "Use when..." conditions, file extensions. The **only layer** Claude uses to decide activation.

### SKILL.md body

Core workflow steps, decision trees, quick-start examples, navigation links to reference files.

### references/

Detailed API docs, schemas, domain-specific data. Loaded only when Claude determines relevance.

### scripts/

Deterministic operations, validations, data transforms. Zero context cost — only script output consumes tokens.

## Writing the Description

**Template:**

```
[Verb] [object] with [capabilities]. Use when [trigger conditions], [additional triggers], or [file-type mentions].
```

### Key Rules

- **Third person** — "Processes files..." not "I can help you..." or "You can use this to..."
- **What + when** — capability statement followed by "Use when..." trigger conditions
- **Natural keywords** — include terms users would actually say in conversation
- **File types and domains** — mention extensions (.xlsx, .pdf) and domain terms (BigQuery, React)
- **Specific over generic** — must distinguish your skill from 100+ others in the same context

### Examples

**Good:** Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

**Bad:** Helps with documents

## SKILL.md Body Structure

```markdown
# Skill Title
[1-2 sentence overview of what this skill does]

## Quick Start
[Minimal working example — 3-step process or code block]

## Workflow
[Sequential steps, numbered, with clear decision points]

## Additional Resources
- [Topic]: See references/file.md for details
- [Topic]: See references/other.md for guide
```

- **Under 500 lines** — hard recommendation; split excess into reference files
- **No "When to Use" in body** — body loads after triggering; move all triggers to description
- **Examples over explanations** — Claude is smart; 50 tokens of code beats 150 tokens of prose
- **Reference files clearly** — SKILL.md acts as a navigation hub to bundled resources
- **One level deep** — all reference files link directly from SKILL.md, never nested chains

## Scripts vs Instructions

### Use Scripts When

- Operation is deterministic and fragile
- Same code would be rewritten every invocation
- Consistency is critical (file formats, validations)
- Error-prone if Claude improvises

*Zero context cost, more reliable, self-documenting*

### Use Instructions When

- Multiple valid approaches exist
- Context determines the right approach
- Heuristics and judgment guide the work
- Creative or analytical reasoning needed

*Flexible, adaptive, context-aware*

## Key Patterns

### Thin Command → Rich Skill

User types `/deploy`. Skill loads SKILL.md, determines the cloud provider, reads only the relevant reference file, executes the right script.

### Meta-Skill

A skill for creating other skills. Encodes the meta-knowledge of how to write effective SKILL.md files, descriptions, and folder structures.

### Domain Router

One skill, multiple reference files. SKILL.md acts as a routing table: "Finance? Read `references/finance.md`." Claude loads only what's needed.

### Dynamic Context Injection

`` !`gh pr diff` `` runs before Claude sees content. Live data injected into the prompt — Claude receives actual output, not the command.

## Anti-Patterns

- **"When to Use" in the body** — Body loads after triggering. Claude never sees it for selection. Move all trigger info to the description.
- **Vague descriptions** — "Helps with documents" matches nothing specific. Include capability verbs, domain terms, file extensions, and "Use when" conditions.
- **SKILL.md over 500 lines** — Bloats context, dilutes conversation history. Split into a concise SKILL.md plus focused reference files.
- **Nested reference chains** — SKILL.md → advanced.md → details.md creates unreliable navigation. Keep all references one level deep.

---

## Sources

- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — Official Anthropic guide — writing effective skills, patterns, evaluation
- [Equipping Agents for the Real World](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills) — Anthropic engineering blog — design philosophy, progressive disclosure rationale
- [Stop Bloating Your CLAUDE.md: Progressive Disclosure](https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/) — alexop.dev — practical context management strategies
- [skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) — Anthropic's meta-skill — the reference implementation for skill creation
