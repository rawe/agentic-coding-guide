# The Command & Skill Journey

From ad-hoc prompts to modular architecture — how Claude Code workflows evolve in four steps.

## The Goal

You have a PDF. You want it as markdown. You ask Claude Code: *"Convert report.pdf to markdown."* Claude writes a script, runs it, hands you the result. Done.

<!-- Visualization: Linear flow diagram
Three elements left to right: PDF document icon (amber "PDF" label) → dashed circle with "?" (teal) → .md document icon (green ".md" label).
Arrows connect each element. Conveys: input → unknown process → output. -->

Next week you do the same thing. Claude writes the script again — differently this time. The week after that, your colleague needs it too, in another project. They start from zero.

The real task isn't converting one document. It's making the conversion **repeatable**, **consistent**, and **shareable**. Claude Code gives you two building blocks for this: **commands** (triggers that start an action) and **skills** (packages that encapsulate knowledge and scripts). This guide walks through four steps of using them — from a one-off prompt to a modular, reusable architecture.

## Step 1: Ad-Hoc: Just Ask Claude

You describe the task. Claude writes a script, runs it, done. Nothing persists.

- "Convert report.pdf to markdown"
- Claude writes a Docling script, executes it, delivers the output
- Tomorrow you ask again — Claude rewrites from scratch

<!-- Visualization: Linear flow diagram, four stages left to right:
1. Chat bubble with three dots, labeled "You ask"
2. Gear icon, labeled "Claude writes script"
3. Document icon with lines, labeled "output.md" (green)
4. Circular arrow with red X in center, labeled "Tomorrow: start over"
Arrows connect each stage. Conveys the ephemeral nature of ad-hoc prompting. -->

```
project/
  |
  +-- report.md              # only the output survives
```

**Limitation:** No memory. No consistency. Different solution each time.

## Step 2: Command: Reusable Trigger

Extract the script. Create a command as a stable entry point with arguments.

<!-- Visualization: Linear flow diagram, three stages left to right:
1. Rounded box with terminal prompt ">_" and "/doc-convert" (amber border), subtitle "same interface, every time"
2. Folder box "scripts/" containing inner box "doc-convert.py"
3. Document icon "report.md" (green)
Arrows connect each stage. -->

```
project/
  |
  |-- scripts/
  |    +-- doc-convert.py         # permanent script
  |
  +-- .claude/
       +-- commands/
            +-- doc-convert.md     # reusable trigger
```

Inside the command:

```markdown
# .claude/commands/doc-convert.md
---
description: Convert a document to markdown.
argument-hint: [filepath]
---

Run `python scripts/doc-convert.py '$ARGUMENTS'`
```

Usage: `/doc-convert report.pdf`

**Gain:** Repeatable. Consistent interface. One command, always the same script.

**Limitation:** Script lives loose in `scripts/`. Not portable. Command is coupled to one path.

## Step 3: Skill: Portable & Self-Contained

Package script + instructions into one folder. Shareable across projects. The skill IS the trigger.

<!-- Visualization: Horizontal flow diagram with three elements:
1. Left: "/doc-convert" label (amber) with arrow pointing into center box
2. Center: Large rounded box (purple border, labeled "doc-convert skill") containing two inner boxes: "SKILL.md" (purple fill) and "doc-convert.py" (subtle border)
3. Right: Arrow out to "report.md" document icon (green)
Below center: two small folder icons with arrow between them, labeled "copy to any project" -->

```
project/
  |
  +-- .claude/
       +-- skills/
            +-- doc-convert/               # self-contained package
                 |-- SKILL.md               # trigger + instructions
                 +-- scripts/
                      +-- doc-convert.py     # moved here
```

Inside the skill:

```markdown
# .claude/skills/doc-convert/SKILL.md
---
name: doc-convert
description: Convert documents (PDF, DOCX) to markdown.
user-invocable: true
argument-hint: [filepath]
---

# Document Conversion

Given a file path via `$ARGUMENTS`:
1. Run: `scripts/doc-convert.py '$ARGUMENTS'`
2. Validate output exists
```

Usage: `/doc-convert report.pdf` — same interface, now portable.

**Gain:** Copy the folder to any project. Script, process, and trigger travel together.

**Limitation:** Works perfectly for conversion. But next week you need downloading from URLs too. Then folder structure for a knowledge base. The skill grows — and a single trigger can't express all the ways you want to use it.

## Step 4: Separated: Skill Grows, Commands Multiply

Your doc-convert skill works. But requirements grow:

- You need to **download** documents from URLs, not just convert local files
- You need to **structure** results into a knowledge base with metadata and folder conventions

You add a download script. You add structural knowledge. The skill is no longer "just conversion" — it's **document processing**: downloading, converting, and structuring.

Now one trigger can't express everything. `/doc-convert report.pdf` should just convert. `/doc-extract https://...` should do the full pipeline: download, convert, create folder, write metadata, update index.

**The shift:** Pull the trigger OUT of the skill.

- The skill becomes a noun (`doc-processing`) — a capability bundle.
- Commands become verbs (`/doc-convert`, `/doc-extract`) — thin triggers that decide scope.

<!-- Visualization: Diagram with two layers.
Top: Large rounded box (teal border, labeled "doc-processing (skill)") containing three capability pills: "doc-download.py" (purple), "doc-convert.py" (purple), "structure.md" (subtle).
Bottom left: "/doc-convert" command box (amber) — connected by a line from doc-convert.py only. Below it: "report.md" document.
Bottom right: "/doc-extract" command box (amber) — connected by lines from ALL three capability pills. Below it: folder tree "sources/docs/..." with content.md and meta.md.
Conveys: one skill, multiple commands, each command selects different capabilities. -->

```
project/
  |
  +-- .claude/
       |-- commands/
       |    |-- doc-convert.md          # convert only (verb)
       |    +-- doc-extract.md          # full pipeline (verb)
       |
       +-- skills/
            +-- doc-processing/         # capability bundle (noun)
                 |-- SKILL.md            # process description
                 |-- scripts/
                 |    |-- doc-download.py # download from URL
                 |    +-- doc-convert.py  # binary → markdown
                 +-- references/
                      +-- structure.md    # folder naming, meta.md template
```

The skill — capabilities, not a trigger:

```markdown
# .claude/skills/doc-processing/SKILL.md
---
name: doc-processing
description: Download, convert, and organize documents into the knowledge base.
user-invocable: false          # not a trigger anymore
---

## Capabilities

Scripts:
- `scripts/doc-download.py` — download a document from a URL
- `scripts/doc-convert.py` — convert PDF/DOCX to markdown

For folder layout and meta.md template see `references/structure.md`

## Full Pipeline

1. Determine slug, create folder per `references/structure.md`
2. Download or copy source into `_raw-source/`
3. Run `scripts/doc-convert.py <input> <output>`
4. Write `meta.md` using template from references
5. Enrich metadata (tags, summary) from converted content
6. Update `sources/index.md`
```

/doc-convert — uses only the convert script:

```markdown
# .claude/commands/doc-convert.md
---
description: Convert a document to markdown.
argument-hint: [filepath]
---

Load skill `doc-processing`.
Run only `scripts/doc-convert.py` on `$ARGUMENTS`. Output markdown next to the source file.
No folder structure, no metadata.
```

/doc-extract — runs the full pipeline:

```markdown
# .claude/commands/doc-extract.md
---
description: Extract a document into the knowledge base.
argument-hint: [URL or filepath]
---

Load skill `doc-processing`.
Follow all steps in the full pipeline for `$ARGUMENTS`.
```

`/doc-convert report.pdf` →

```
report.md              # just the markdown, same directory
```

`/doc-extract https://example.com/report.pdf` →

```
sources/docs/2026-02-quarterly-report/
  |-- content.md       # converted markdown
  |-- meta.md          # tags, summary, attribution
  +-- _raw-source/
       +-- report.pdf   # downloaded original
```

**Gain:** The skill grew from one script to a full capability bundle — download, convert, structure. Commands stayed thin. `/doc-convert` grabs one capability. `/doc-extract` orchestrates all of them. Same skill, different scope.

## What Is What

Three concepts, each with a distinct role in the architecture.

### Command

- **Purpose:** Trigger an action
- **Location:** `.claude/commands/<verb>.md`
- **Naming:** Verb — what it does
- **Contains:** Description, argument hint, one instruction to load a skill

*Think of it as: the button you press*

### Skill

- **Purpose:** Bundle capabilities — scripts, process knowledge, and reference material
- **Location:** `.claude/skills/<noun>/SKILL.md`
- **Naming:** Noun — what it covers
- **Contains:** Process description, bundled scripts, reference docs

*Think of it as: the toolbox — commands grab different tools from it*

### User-Invocable Skill

- Skill is both trigger and knowledge
- Set `user-invocable: true` in frontmatter
- Trade-off: convenient but less flexible
- Best for single-purpose tools

*The shortcut — one skill, one entry point*

## What You Take Away

- **Step 1:** Without structure, every request starts from zero. Claude solves it, but the solution is gone tomorrow.
- **Step 2:** A **command** gives a script a name and an argument. Now it's repeatable — same interface, same result, every time.
- **Step 3:** A **skill** packages script + instructions into one folder. It becomes portable — copy it to any project and it works.
- **Step 4:** The skill grows beyond one trick — downloading, converting, structuring. Pull triggers out into **commands**. Each command decides its own scope. The skill is the toolbox, commands grab what they need.
