---
title: "The Command & Skill Journey"
html_file: command-skill-journey.html
description: "How Claude Code workflows evolve from ad-hoc prompts to modular command-and-skill architecture in four steps."
---

# The Command & Skill Journey

From ad-hoc prompts to modular architecture — how Claude Code workflows evolve in four steps.

## The Goal

You have a PDF. You want it as markdown. You ask Claude Code: "Convert report.pdf to markdown." Claude writes a script, runs it, hands you the result. Done.

Next week you do the same thing. Claude writes the script again — differently this time. The week after that, your colleague needs it too, in another project. They start from zero.

The real task isn't converting one document. It's making the conversion **repeatable**, **consistent**, and **shareable**. Claude Code gives you two building blocks for this: **commands** (triggers that start an action) and **skills** (packages that encapsulate knowledge and scripts). This guide walks through four steps of using them — from a one-off prompt to a modular, reusable architecture.

## Step 1: Ad-Hoc — Just Ask Claude

You describe the task. Claude writes a script, runs it, done. Nothing persists.

- "Convert report.pdf to markdown"
- Claude writes a Docling script, executes it, delivers the output
- Tomorrow you ask again — Claude rewrites from scratch

```
project/
  |
  +-- report.md              # only the output survives
```

- **Limitation:** No memory. No consistency. Different solution each time.

## Step 2: Command — Reusable Trigger

Extract the script. Create a command as a stable entry point with arguments.

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

- **Gain:** Repeatable. Consistent interface. One command, always the same script.
- **Limitation:** Script lives loose in `scripts/`. Not portable. Command is coupled to one path.

## Step 3: Skill — Portable & Self-Contained

Package script + instructions into one folder. Shareable across projects. The skill IS the trigger.

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

- **Gain:** Copy the folder to any project. Script, process, and trigger travel together.
- **Limitation:** One skill = one trigger. As workflows grow, you need multiple entry points sharing the same knowledge.

## Step 4: Separated — Modular Architecture

The conversion script works. But you realize you need it in two different contexts:

- **/doc-convert** — Convert a file to markdown. One file in, one file out. That's it.
- **/doc-ingest** — Ingest a document into your knowledge base. Creates a dated folder (`2026-02-some-paper/`), copies the original into it, converts it, writes metadata with tags and summary, updates the project index.

Both use the same conversion script. But `/doc-ingest` also needs to know *where to put things*: How should the folder be named? What files go inside? What does `meta.md` look like? That structural knowledge lives in `references/structure.md` inside the skill — loaded only when the ingestion workflow needs it.

The skill stops being a trigger. It becomes a **knowledge container** — renamed from verb (`doc-convert`) to noun (`doc-processing`). It holds the scripts, the process description, and the reference material. Commands become thin triggers that load the skill and decide how much of it to use.

### What each command produces

`/doc-convert report.pdf` produces:

```
report.md              # markdown file, same directory
```

`/doc-ingest report.pdf` produces:

```
sources/docs/2026-02-quarterly-report/
  |-- content.md       # converted markdown
  |-- meta.md          # tags, summary, attribution
  +-- _raw-source/
       +-- report.pdf   # original copy
```

Same conversion script underneath. Completely different scope. The skill holds all the knowledge — each command picks how much to use.

### File structure

```
project/
  |
  +-- .claude/
       |-- commands/
       |    |-- doc-convert.md           # convert only
       |    +-- doc-ingest.md            # full workflow
       |
       +-- skills/
            +-- doc-processing/          # noun — knowledge container
                 |-- SKILL.md             # process description
                 |-- scripts/
                 |    +-- doc-convert.py   # conversion script
                 +-- references/
                      +-- structure.md     # folder naming, meta.md template
```

### The skill — all the knowledge, not a trigger

```markdown
# .claude/skills/doc-processing/SKILL.md
---
name: doc-processing
description: Convert and organize documents into the knowledge base.
user-invocable: false
---

For folder layout and meta.md template see `references/structure.md`

## Process
1. Determine slug, create folder per `references/structure.md`
2. Copy original file into `_raw-source/`
3. Run `scripts/doc-convert.py <input> <output>`
4. Write `meta.md` using template from references
5. Enrich metadata from converted content
```

### /doc-convert — uses only step 3 from the skill

```markdown
# .claude/commands/doc-convert.md
---
description: Convert a document to markdown.
argument-hint: [filepath]
---

Load the `doc-processing` skill.
Run only the conversion script on `$ARGUMENTS`. No folder structure, no metadata.
```

### /doc-ingest — runs the full process from the skill

```markdown
# .claude/commands/doc-ingest.md
---
description: Ingest a document into the knowledge base.
argument-hint: [filepath]
---

Load the `doc-processing` skill, then process `$ARGUMENTS`.
Follow all steps in the skill.
```

- **Gain:** Two commands, one skill. `/doc-convert` picks step 3. `/doc-ingest` runs everything. The conversion script is shared. The folder structure knowledge is shared. Each command decides its own scope.

## What Is What

Three concepts, each with a distinct role in the architecture.

### Command

- **Purpose:** Trigger an action
- **Location:** `.claude/commands/<verb>.md`
- **Naming:** Verb — what it does
- **Contains:** Description, argument hint, one instruction to load a skill
- *Think of it as: the button you press*

### Skill

- **Purpose:** Encapsulate knowledge, process, and scripts
- **Location:** `.claude/skills/<noun>/SKILL.md`
- **Naming:** Noun — what it covers
- **Contains:** Process description, bundled scripts, reference docs
- *Think of it as: the manual the button activates*

### User-Invocable Skill

- Skill is both trigger and knowledge
- Set `user-invocable: true` in frontmatter
- Trade-off: convenient but less flexible
- Best for single-purpose tools
- *The shortcut — one skill, one entry point*

## What You Take Away

- **Step 1:** Without structure, every request starts from zero. Claude solves it, but the solution is gone tomorrow.
- **Step 2:** A **command** gives a script a name and an argument. Now it's repeatable — same interface, same result, every time.
- **Step 3:** A **skill** packages script + instructions into one folder. It becomes portable — copy it to any project and it works.
- **Step 4:** Separate **what you know** from **how you start it**. The skill holds all the knowledge. Commands are thin triggers that decide which parts to use. One skill, many entry points.
