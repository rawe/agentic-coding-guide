# Skills — The Knowledge Layer

Self-contained knowledge packages that make Claude smarter about your domain. No new tools — better judgment.

## What is a Skill?

A skill is a **folder with a SKILL.md file** and optional resources (scripts, references, assets) that teaches Claude how to perform a specific task. Skills don't add new capabilities — they teach Claude **when and how to use existing tools well**. Only the description is loaded upfront (~25 tokens). The full instructions load on demand.

## Anatomy of a Skill

```
.claude/skills/my-skill/
  SKILL.md        ← required, everything else optional
  scripts/        ← deterministic operations, zero context cost
  references/     ← detailed docs, loaded selectively
  assets/         ← templates, images, config files
```

### Frontmatter Fields

| Field | Description |
|---|---|
| `name` | Display name. Folder name becomes the `/slash-command`. |
| `description` | Primary trigger — Claude reads this to decide relevance. Must say WHAT it does AND WHEN to use it. |
| `allowed-tools` | Restrict which tools Claude can use when skill is active |
| `context` | Set to `fork` to run in isolated subagent |
| `user-invocable` | `false` = hidden from `/` menu, only Claude invokes |

## Progressive Disclosure — Three Loading Layers

### Layer 1: Metadata

Only `name` + `description` sit in context. Claude knows the skill exists.

~25 tokens — always loaded

### Layer 2: Full SKILL.md Body

Markdown instructions enter context when the skill activates. The actual workflow.

~200–500 tokens — on activation

### Layer 3: Bundled Resources

Scripts execute as subprocesses (zero context). References load selectively when needed.

0 tokens (scripts) — on demand

<!-- Visualization: Three cards arranged horizontally
Card 1: "Layer 1 — Metadata" — ~25 tokens, always loaded
Card 2: "Layer 2 — Full SKILL.md Body" — ~200–500 tokens, on activation
Card 3: "Layer 3 — Bundled Resources" — 0 tokens (scripts), on demand
Each card has a numbered badge, title, description, and token cost at bottom. -->

## Skills vs Commands

| Aspect | Command | Skill |
|---|---|---|
| **Location** | `.claude/commands/verb.md` | `.claude/skills/noun/SKILL.md` |
| **Structure** | Single markdown file | Folder + scripts + references |
| **Trigger** | User types `/name` | Claude auto-detects or user types `/name` |
| **Resources** | None bundled | Scripts, references, assets |
| **Portable** | May depend on external paths | Self-contained, copy to any project |

## Three Ways to Invoke

### Slash Command (User)

Type `/skill-name` with optional args. Works when `user-invocable` is not `false`.

### Auto-Detection (Claude)

Claude reads all skill descriptions and loads one when your task matches. The main differentiator from commands.

### Chain Loading (Other Skill)

A command or another skill can reference it. Thin commands trigger rich skill knowledge.

<!-- Visualization: Three cards arranged horizontally
Card 1 (green accent): "USER — Slash Command"
Card 2 (purple accent): "CLAUDE — Auto-Detection"
Card 3 (magenta accent): "OTHER SKILL — Chain Loading"
Each card has a who-label, title, and short description. -->

## Real Examples from This Project

| Skill | Description |
|---|---|
| **html-pages** | Create dark-themed presentation pages. Instructions only, no scripts. Auto-detects when page creation is needed. |
| **yt-processing** | Extract YouTube transcripts + metadata. Bundles Python scripts. Claude-only (not user-invocable). |
| **chatgpt-image** | Generate images via ChatGPT browser automation. Bundles scripts + reference docs. User-invocable with argument hint. |
| **skill-creator** | Meta-skill for creating new skills. Bundles init scripts + packaging tools + reference docs. |

---

## Sources

- Frontend Community Day — Claude Code Skills
