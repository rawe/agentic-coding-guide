---
title: "Skills in Practice"
html_file: skills-in-practice.html
description: "What Claude Code skills are, how they load via progressive disclosure, their internal anatomy, and how to create your own."
---

# Skills in Practice

What skills are, how they load, what goes inside them, and how to create your own.

## What Is a Skill?

A self-contained package of workflow instructions and optional resources that teaches Claude Code how to do something it cannot do natively.

The formula:

```
SKILL.md + scripts/ references/ assets/ = new workflow
```

- Project skills live at `.claude/skills/`
- Personal skills live at `~/.claude/skills/`

## Meet doc-processing

To make skills concrete, the page uses a real skill throughout: `doc-processing`. It takes a document (PDF, DOCX, or any supported format) from a URL or local file and produces clean markdown with structured metadata. You point it at a document, and Claude handles the rest: downloading the file, converting it to markdown, writing metadata, and updating your project's source index.

## Anatomy of a Skill

A skill is a folder with a SKILL.md file and optional supporting resources. The `doc-processing` skill uses all three resource types.

### Folder structure

```
.claude/skills/doc-processing/
  |
  |-- SKILL.md              # Frontmatter (metadata)
  |                          # + body (instructions)
  |
  +-- scripts/
  |    |-- doc-download.py   # fetches files from URLs
  |    +-- doc-convert.py    # converts any format to markdown
  |
  +-- references/
       +-- structure.md      # folder layout & meta.md template
```

### Components

- **SKILL.md Frontmatter**: YAML block with `name`, `description`, and `user-invocable`. This is the only part always in context.
- **SKILL.md Body**: Five-step workflow the agent follows when activated. Covers obtaining the document, converting it, creating metadata, enriching with tags, and updating the index.
- **scripts/**: Two executables that run as subprocesses. `doc-download.py` fetches files from URLs using httpx. `doc-convert.py` converts any document format to markdown using docling. Both declare dependencies via inline shebangs -- zero context cost.
- **references/**: `structure.md` defines the target folder layout, slug convention, and `meta.md` template. Loaded selectively when Claude needs the template -- small context cost, only when needed.

Not all of this loads at once. Skills use progressive disclosure -- Claude only pays for what it actually needs.

## Progressive Disclosure

Skills are lazy-loaded in three layers. Only the description sits in context until Claude decides the skill is relevant. This is what makes it possible to install dozens of skills with near-zero token overhead.

### Layer 1 -- Metadata (Always Loaded)

The YAML frontmatter (`name` and `description`) is always in context. The description is the primary triggering mechanism: Claude reads it to decide if this skill is relevant to the current task. With `user-invocable: false`, the skill is automatically loaded when Claude recognizes it's relevant -- not directly invoked. Setting it to `true` would additionally register the skill as a slash command.

```yaml
---
name: doc-processing
description: Extract and convert documents (PDF, DOCX, etc.) into structured
              markdown with metadata.
user-invocable: false
---
```

- Context cost: ~25 tokens

### Layer 2 -- Full Instructions (Loaded When Activated)

The SKILL.md body loads only after the skill is activated -- by a command, another skill, or a matching task. Contains the five-step workflow with conditional logic for URLs vs. local files.

```
# Document Extraction

Given a document via `$ARGUMENTS`:

1. Obtain document -- download (URL) or copy (local file)
   uv run .../doc-download.py '<URL>' '<folder>/_raw-source'
2. Convert to markdown
   uv run .../doc-convert.py '<input>' '<folder>/content.md'
3. Create `meta.md` using template from `references/`
4. Enrich metadata with tags and summary
5. Update `sources/index.md` with the new entry
```

- Context cost: ~200 tokens

### Layer 3 -- Bundled Resources (Loaded or Executed on Demand)

**scripts/** run as subprocesses -- zero context cost. **references/** are read selectively when Claude needs a template or schema -- small cost, only when needed. The heavy lifting stays outside the context window.

```python
# doc-convert.py -- runs as subprocess
# /// script
# dependencies = ["docling"]
# ///
"""Convert a document (PDF, DOCX, etc.) to markdown."""
  ... runs as subprocess, never enters context

# references/structure.md -- read selectively
  ... folder layout, slug convention, meta.md template
  ... loaded only when Claude needs the template
```

- Context cost: 0 tokens (scripts), ~150 tokens (references, when read)

## Walk-through: doc-processing

`doc-processing` takes a document and produces structured markdown with metadata -- without you writing any conversion code. Here is what happens when you use it, traced through all three disclosure layers.

1. **Claude sees the description.** At session start, only the frontmatter occupies context. Claude knows this skill exists and what it does -- nothing more.

   ```yaml
   name: doc-processing
   description: Extract and convert documents (PDF, DOCX, etc.)
                 into structured markdown with metadata.
   ```

2. **The skill activates.** A command, another skill, or a matching task triggers activation. The full SKILL.md body enters context -- Claude now has a five-step workflow with conditional logic and explicit script paths.

   ```
   1. Obtain document -- download or copy into `_raw-source/`
   2. Convert to markdown via doc-convert.py
   3. Create `meta.md` using template from `references/`
   4. Enrich metadata with tags and summary
   5. Update `sources/index.md`
   ```

3. **Claude runs the scripts.** `doc-download.py` fetches the file from the URL using httpx. `doc-convert.py` converts it to markdown using docling. Both run as subprocesses with inline uv dependencies -- zero tokens consumed, only the output paths return to context.

   ```python
   # /// script
   # dependencies = ["httpx"]
   # ///
   """Download a document from a URL."""

   # /// script
   # dependencies = ["docling"]
   # ///
   """Convert a document (PDF, DOCX, etc.) to markdown."""
   ```

4. **Claude enriches and indexes.** Claude reads `references/structure.md` for the `meta.md` template, then writes metadata with tags and a two-sentence summary derived from the content. Finally, it appends the new entry to the project's source index.

   ```
   # references/structure.md (loaded selectively)
   | Field     | Value |
   | URL       | <source URL>
   | Author    | <author>
   | Tags      | <derived from content>
   | Summary   | <2 sentences, no filler>
   ```

## Where to Find Skills

Two paths to get skills into your project.

### skills.sh (Recommended)

Vercel's open agent skills ecosystem. Browse, search, one-command install.

1. Browse skills at skills.sh
2. Copy the install command
3. Paste in terminal, choose CLI tool
4. Pick project-level or global install
5. Skill appears in `.claude/skills/`

### Plugin Marketplace (Alternative)

Built into Claude Code. Add marketplace repos, browse and install.

1. Open Claude Code, go to `/plugin`
2. Navigate to marketplaces
3. Add a GitHub repository URL
4. Browse available plugins
5. Select with spacebar, press `I` to install

## Creating Your Own

Here is how `doc-processing` was actually built -- not by writing the SKILL.md by hand, but by collaborating with Claude Code and the `/skill-creator` meta-skill (installable from skills.sh).

### Workflow

1. **Build the Scripts.** Guide Claude Code through writing the download and conversion scripts -- iterate together until they handle all target formats.
2. **Run /skill-creator.** Point the skill creator at your working scripts and reference files. It generates the SKILL.md with frontmatter and instructions.
3. **Organize the Folder.** Arrange scripts, references, and SKILL.md into the standard layout under `.claude/skills/`.
4. **Test & Refine.** Run the skill on a real document, check the markdown output and metadata, tweak the instructions if needed.

### How doc-processing Was Made

- Guided Claude Code to write a download script (httpx) and a conversion script (docling) for handling PDFs, DOCX, and other formats
- Created `references/structure.md` to codify the folder layout, slug convention, and `meta.md` template
- Ran `/skill-creator` -- it analyzed the scripts and reference, generating SKILL.md with the five-step workflow
- Set `user-invocable: false` -- the skill is loaded by commands or triggered autonomously

### The Result

```
.claude/skills/doc-processing/
  |-- SKILL.md              # generated by /skill-creator
  +-- scripts/
  |    |-- doc-download.py   # built collaboratively
  |    +-- doc-convert.py
  +-- references/
       +-- structure.md
```

The same skill dissected above -- created in one session, reusable forever.

---

**Source:** Leon van Zyl -- [Claude Code Skills Tutorial](https://www.youtube.com/watch?v=vIUJ4Hd7be0)
