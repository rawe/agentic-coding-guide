# The Skill-Agent Fork Pattern

How to combine a skill and a custom sub-agent into a repeatable, isolated workflow — using a real example that generates HTML pages from YouTube research.

## The Problem

Skills teach Claude procedures. Agents provide isolated context windows with restricted tools. But some workflows need both: a repeatable procedure that runs in its own context, every time, without polluting the main conversation.

- A summarization workflow that reads long transcripts shouldn't flood the main context with 10,000 tokens of source material.
- An HTML page generator that reads theme files, existing pages, and source summaries needs room to work — and the main conversation doesn't need to see it.
- Any multi-step procedure you want to invoke with a slash command and get clean results back from.

The `context: fork` pattern solves this. A skill defines WHAT to do. An agent defines WHO does it. The skill body becomes the task; the agent provides the execution environment. One slash command, full isolation.

## Meet generate-html-page

To make this concrete, we'll trace through a real implementation: `/generate-html-page`, which takes a YouTube source folder (containing `summary.md` and `meta.md`) and produces a dark-themed HTML presentation page in `public/`.

Three pieces make it work:

<!-- Visualization: Three-component relationship diagram (horizontal)
Three rounded boxes arranged left-to-right, connected by labeled arrows.

Box 1 (teal border, left): "generate-html-page" — labeled "ACTIVATOR SKILL" above. Contains: "context: fork", "agent: html-page-generator", "7-step procedure".
Arrow from Box 1 to Box 2: labeled "forks into" (dashed line, teal).

Box 2 (amber border, center): "html-page-generator" — labeled "CUSTOM AGENT" above. Contains: "tools: Read, Write, Edit...", "model: opus", "skills: html-pages".
Arrow from Box 3 to Box 2: labeled "preloaded into" (solid line, purple).

Box 3 (purple border, right): "html-pages" — labeled "KNOWLEDGE SKILL" above. Contains: "theme colors", "page skeleton", "card patterns", "index integration".

Below all three boxes, a horizontal bracket labeled "User types: /generate-html-page sources/youtube/2026-02-some-video/" -->

| Piece | Type | Job |
|-------|------|-----|
| `generate-html-page` | Activator skill | Entry point. Holds the 7-step procedure. Has `context: fork` to run in isolation. |
| `html-page-generator` | Custom agent | Execution environment. Defines voice, tone, and tools. Preloads the html-pages skill. |
| `html-pages` | Knowledge skill | Reference material. Theme system, page skeleton, card patterns, index integration. |

## What Happens When You Type the Command

`/generate-html-page sources/youtube/2026-02-leon-van-zyl-claude-code-skills-the-only-tutorial-you-need/`

<!-- Visualization: Two-lane sequence diagram (vertical)
Left lane: "Main Context" (dark background, teal border)
Right lane: "Forked Context" (dark background, amber border)

Left lane, step 1: User types /generate-html-page <path>
Left lane, step 2: System reads skill frontmatter → sees context: fork, agent: html-page-generator
Arrow crossing from left to right lane: "Fork" — labeled "$ARGUMENTS substituted into skill body"

Right lane, step 3: Sub-agent starts with:
  - System prompt = agent body + preloaded html-pages skill content
  - Task = skill body (with path substituted)
  - Tools = Read, Write, Edit, Glob, Grep, Bash
  - Model = Sonnet
Right lane, step 4: Agent reads summary.md, meta.md from source folder
Right lane, step 5: Agent reads existing pages, theme.css, STRUCTURE.md
Right lane, step 6: Agent writes content markdown + HTML + index updates
Right lane, step 7: Agent completes

Arrow crossing from right back to left lane: "Results return"
Left lane, step 8: Main context receives summary of work done. Its context window is clean — never saw the source material or intermediate files. -->

Step by step:

1. **System reads the skill frontmatter** — sees `context: fork` and `agent: html-page-generator`
2. **`$ARGUMENTS` substitution** — the source path replaces `$ARGUMENTS[0]` in the skill body
3. **Fork** — a new sub-agent starts with its own context window:
   - **System prompt** = agent definition body + full `html-pages` skill content (preloaded via `skills:` field)
   - **Task** = skill body (the 7-step procedure, with the source path baked in)
   - **Tools** = Read, Write, Edit, Glob, Grep, Bash (from agent's `tools:` field)
   - **Model** = Sonnet (from agent's `model:` field)
4. **Agent works** — reads source material, studies existing pages, drafts content markdown, builds HTML, updates index
5. **Results return** — main context receives a summary. It never saw the transcript, theme files, or intermediate drafts.

The main conversation's context window stays clean. The sub-agent had all the room it needed.

## The Activator Skill

`.claude/skills/generate-html-page/SKILL.md` — the entry point and procedure definition.

```yaml
---
name: generate-html-page
description: Generate a presentation-ready HTML page from a source folder.
  Use when converting YouTube or document summaries into dark-themed
  HTML guides for public/.
user-invocable: true
argument-hint: <source-folder-path> [page-name]
context: fork
agent: html-page-generator
---

Generate an HTML presentation page from the source at `$ARGUMENTS[0]`.

## Step 1 — Read source material
Read `meta.md` and `summary.md` from `$ARGUMENTS[0]`.

## Step 2 — Determine page name
If `$ARGUMENTS[1]` is provided, use it. Otherwise, derive a slug.

## Step 3 — Study existing pages
Read STRUCTURE.md, content/README.md, and 1 similar page.

## Step 4 — Draft content markdown
Write public/content/<page-name>.md.

## Step 5 — Choose accent colors
Read theme.css. Reuse existing variables where possible.

## Step 6 — Build HTML
Read one existing page as template. Build public/<page-name>.html.

## Step 7 — Update index and structure
Add card to index.html. Add entry to STRUCTURE.md.
```

Key frontmatter fields:

- **`user-invocable: true`** — registers as `/generate-html-page` in the slash menu
- **`argument-hint`** — shows `<source-folder-path> [page-name]` in autocomplete
- **`context: fork`** — runs in an isolated sub-agent, not the main context
- **`agent: html-page-generator`** — specifies which agent definition provides the execution environment
- **`$ARGUMENTS[0]`, `$ARGUMENTS[1]`** — mechanical substitution. The user's input is baked into the procedure before the agent sees it.

The body is the task — the exact procedure the sub-agent follows. It's version-controlled, carefully authored, and identical every invocation.

## The Agent

`.claude/agents/html-page-generator.md` — the execution environment and persona.

```yaml
---
name: html-page-generator
description: Sub-agent that builds dark-themed HTML presentation pages
  from source material. Knows the project's theme system, page patterns,
  and writing conventions.
tools: Read, Write, Edit, Glob, Grep, Bash
model: opus
skills: html-pages
---

You produce presentation-ready HTML pages for the public/ directory.

The `html-pages` skill (preloaded) is your reference for all HTML/CSS
decisions. Follow it exactly.

## Voice
These pages teach. Every section should help the reader understand fast.

- Visual-first: diagrams, tables, color-coded cards, highlighted
  callouts over running prose.
- No plain-text deserts — if a section is more than 3-4 lines of text,
  break it up with structure.
- Bullet points over paragraphs. Facts over commentary.
- No filler. No AI slop. Every sentence must carry information.
- Always cite the original source with URL and author.
```

What each part does:

- **`skills: html-pages`** — the full `html-pages` SKILL.md content is injected into the agent's context at startup. The agent knows the theme system, page skeleton, and card patterns without being told.
- **`tools:`** — allowlist. The agent can read files, write files, search, and run shell commands. Nothing else.
- **`model: opus`** — highest capability for complex content generation.
- **Body** — the system prompt. Pure voice and identity. It defines *how* the agent communicates, not *what* it does — the procedure lives in the activator skill.

## The Knowledge Skill

`.claude/skills/html-pages/SKILL.md` — the reference material the agent loads at startup.

```yaml
---
name: html-pages
description: Create and maintain dark-themed HTML presentation pages
  in public/. Covers page structure, theme colors, teaser images,
  image optimization, and index page integration.
---

# HTML Presentation Pages

## Project Structure
public/ — index.html, css/theme.css, assets/, individual *.html pages

## Theme & Colors
All accents in theme.css as CSS variables. Never hardcode hex.
New page → add --name-primary and --name-glow to :root.

## Creating a New Page
1. Choose accent colors    2. Page skeleton (bg overlay, wrapper, header, cards)
3. H1 gradient (clip text) 4. Card pattern (card-image + card-body)

## Teaser Images
Generate via /chatgpt-image on dark navy bg with accent glow. Optimize to 720×450.

## Index Page Integration
Card variant CSS with color-mix() accent + card HTML.

## Checklist
Six-step: colors → skeleton → teasers → optimize → index card → verify
```

No workflow fields in the frontmatter. No steps. No voice. Pure reference — this content gets injected into the agent's context via the `skills:` field.

## What Goes Where

Each file answers exactly one question. No information appears in two places.

| Question | Answered by | Contains | Does NOT contain |
|----------|-------------|----------|------------------|
| How do HTML pages work? | `html-pages` (knowledge skill) | Theme system, page skeleton, card patterns, teaser images, index integration | Workflow steps, arguments, persona, tone |
| How should I communicate? | `html-page-generator` (agent) | Voice, didactic approach, writing style, pointer to preloaded skill | Procedure, output files, file paths, steps |
| What do I do, step by step? | `generate-html-page` (activator) | Ordered steps, `$ARGUMENTS`, files to read/write, outputs to produce | HTML/CSS reference (skill's job), writing voice (agent's job) |

Three non-overlapping concerns: **how things look** — **how you speak** — **what you do**.

## Why Fork Beats Agent-Only

Two approaches exist for this workflow:

| | Fork pattern (Approach A) | Agent-only (Approach B) |
|--|--------------------------|------------------------|
| **Entry point** | `/generate-html-page <path>` | User asks Claude to delegate to the agent |
| **Path passing** | `$ARGUMENTS` — mechanical, exact | Main Claude formulates a Task prompt — variable |
| **Procedure** | Skill body — version-controlled, identical every run | Agent system prompt or ad-hoc Task prompt |
| **Discoverability** | Appears in `/` menu with tab-completion | User must know the agent exists |

The fork pattern wins for repeatable workflows because:

- **Skill = WHAT** (the procedure, version-controlled, with argument substitution)
- **Agent = WHO** (the voice, tools, model, preloaded knowledge)
- **Separation of concerns** — change the procedure without touching the agent, or swap the agent without rewriting the procedure

The agent-only approach merges both into one file. That works for ad-hoc delegation, but for a command you'll run dozens of times, the fork pattern gives you a deterministic entry point with exact argument handling.

---

## Sources

- [Claude Code Skills — context: fork](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent)
- [Claude Code Custom Subagents](https://code.claude.com/docs/en/sub-agents)
- [Preload skills into subagents](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents)
