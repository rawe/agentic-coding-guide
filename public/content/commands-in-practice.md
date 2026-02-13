---
title: "Commands in Practice"
html_file: commands-in-practice.html
description: "How Claude Code custom commands work: anatomy, arguments, execution flow, and creation."
---

# Commands in Practice

One markdown file, one slash command. This page explains how custom commands in Claude Code parse arguments and orchestrate skills.

## What Is a Command?

A command is a single markdown file that gives Claude Code a new slash command. No folder structure, no scripts, no build step -- just frontmatter and instructions.

The formula:

```
frontmatter + instructions = /slash-command
```

- Project commands live at `.claude/commands/`
- Personal commands live at `~/.claude/commands/`

## Meet doc-extract

`/doc-extract` takes a URL or local file path and delegates to the `doc-processing` skill. It downloads the document, converts it to markdown, writes structured metadata, and updates the project index. One command, full pipeline.

The command itself is 6 lines. The skill it loads does the heavy lifting.

## Anatomy of a Command

A command is a single `.md` file with YAML frontmatter and a markdown body. Here is the real `doc-extract.md` with every field annotated.

```markdown
---
description: Download/copy a document and extract
              its content as markdown into
              sources/docs.
argument-hint: [url-or-filepath]
context: fork
---

Load the `doc-processing` skill, then process
the document at `$ARGUMENTS`.

Determine if the argument is a URL (starts
with `http`) or a local file path.
Follow all steps in the skill (obtain,
convert, create meta.md, enrich metadata,
update index).
```

### Frontmatter

YAML between `---` markers. Three fields:

- `description` -- shown in `/help`, used for slash command discovery.
- `argument-hint` -- tells users what to type after the command.
- `context: fork` -- runs in an isolated session so it doesn't pollute your main conversation.

### Body

Free-form markdown instructions Claude follows when the command runs. This body references a skill by name, uses `$ARGUMENTS` to receive user input, and defines the conditional workflow -- URL vs. local file path.

### File location

The filename becomes the command name. `.claude/commands/doc-extract.md` registers as `/doc-extract`. No configuration beyond placing the file.

## How Arguments Work

`$ARGUMENTS` captures everything the user types after the command name. The command body is responsible for parsing it.

### Single argument

Most commands take one input. `$ARGUMENTS` is the entire string after the command name.

```
/doc-extract https://example.com/paper.pdf

# $ARGUMENTS = "https://example.com/paper.pdf"
```

### Multiple arguments

For commands that accept more than one input, the body instructions tell Claude how to parse. The `argument-hint` signals the expected format.

```
/yt-extract https://youtube.com/watch?v=abc sources/youtube/channel

# argument-hint: [youtube-url] [output-dir]
# Body says: "Parse $ARGUMENTS: first argument is the YouTube URL,
#             second argument is an optional output directory"
```

### The argument-hint field

Displayed as placeholder text in the Claude Code UI when the user types `/`. Communicates expected input without enforcing a schema -- parsing is always done by the body instructions.

```yaml
argument-hint: [url-or-filepath]           # doc-extract
argument-hint: [youtube-url] [output-dir]   # yt-extract
argument-hint: [channel-handle] [count]    # yt-channel
argument-hint: [source-folder-path]        # summarize
```

## Walk-through: doc-extract

Three steps from slash command to structured output. Commands are thin orchestrators -- they parse input and delegate to skills that do the real work.

### Step 1: You type the command

In Claude Code, you enter the command with a URL. The CLI matches the filename to the slash command and reads the file.

```
/doc-extract https://arxiv.org/pdf/2401.12345
```

### Step 2: Claude reads the command file

Frontmatter and body enter context. `context: fork` spins up an isolated session. `$ARGUMENTS` binds to `https://arxiv.org/pdf/2401.12345`. Claude now has its instructions: load a skill, determine URL vs. file path, follow the workflow.

```
# $ARGUMENTS = "https://arxiv.org/pdf/2401.12345"
# context: fork -> isolated session

Load the `doc-processing` skill, then process
the document at `$ARGUMENTS`.
```

### Step 3: The skill takes over

Claude loads `doc-processing` -- its full SKILL.md body enters context. The skill's five-step workflow runs:

1. Obtain document -- download via `doc-download.py`
2. Convert to markdown via `doc-convert.py`
3. Create `meta.md` from `references/structure.md`
4. Enrich metadata with tags and summary
5. Update `sources/index.md`

**Key insight:** The command is 6 lines. The skill is a full folder with scripts, references, and a multi-step workflow. Commands are the user-facing entry point; skills are the engine underneath.

## Creating Your Own

Three steps to a working command. No tooling required.

### Step 1: Create the File

Add a `.md` file in `.claude/commands/`. The filename becomes the command name.

### Step 2: Add Frontmatter

Set `description` and `argument-hint`. Add `context: fork` if the command should run in isolation.

### Step 3: Write Instructions

Tell Claude what to do with `$ARGUMENTS`. Reference skills, define parsing logic, set the workflow.

### Minimal template

A command that loads a skill -- the pattern used by every command in this project.

```markdown
---
description: Short description shown in /help.
argument-hint: [input]
context: fork
---

Load the `your-skill-name` skill.

Parse `$ARGUMENTS`: first argument is the input.
Follow all steps in the skill.
```

### Input/Output Example

**You type:**

```
/doc-extract https://arxiv.org/pdf/2401.12345
```

**You get:**

- `sources/docs/2024-01-some-paper/meta.md` -- structured metadata with tags, summary, source URL
- `sources/docs/2024-01-some-paper/content.md` -- full document converted to clean markdown
- `sources/index.md` updated with the new entry
