# Claude Code Skills - The Only Tutorial You Need

> Source: [Claude Code Skills - The Only Tutorial You Need](https://www.youtube.com/watch?v=vIUJ4Hd7be0) by Leon van Zyl

## Overview

Leon van Zyl walks through Claude Code skills end-to-end: what they are, how they differ from MCP servers and custom commands, how to find and install them, and how to build your own from scratch. The video uses a fitness app landing page as a running example, progressively enhancing it with a front-end design skill, a browser verification skill, and a custom image generation skill. Covers the critical topic of handling API keys securely when skills need external services.

## Key Takeaways

- Skills are markdown files with precise instructions that teach Claude Code predefined workflows it cannot do natively — they extend the agent without permanently consuming context tokens.
- Skills load into context only when needed, unlike MCP server tools which are always present in the context window. This makes skills the lighter-weight option for capabilities used occasionally.
- MCP servers provide new tools (browser control, database access). Skills orchestrate workflows using existing tools and knowledge. Custom commands are just reusable prompts — unrelated to either.
- The easiest way to find and install skills is through skills.sh (Vercel's open agent skills ecosystem), not the built-in plugin marketplace.
- Creating custom skills is straightforward: define the workflow, provide example code or scripts, and let the skill creator skill generate the markdown and supporting files.
- Never hardcode API keys in skills. Store them in `.env` (gitignored), reference them as environment variables in the underlying scripts.

## Notes

### What Skills Are

Skills are markdown files containing detailed instructions for specific workflows. They can include supporting resources like Python scripts. The agent reads these instructions and follows them step-by-step.

- Markdown file = instructions + workflow definition
- Can bundle scripts (Python, etc.) that the agent executes
- Used to specify domain knowledge, procedural workflows, or capabilities Claude lacks natively
- Example: image generation skill contains instructions plus a Python script that calls an image API

### Skills vs MCP Servers vs Custom Commands

Three distinct concepts that get confused:

- **Skills**: Predetermined workflows in markdown. Auto-activated by the agent based on conversation context. Only loaded when relevant — minimal token footprint until invoked.
- **MCP servers**: Provide new tools (browser control, database access, etc.). Tool definitions and metadata are always loaded in context, consuming tokens whether used or not.
- **Custom commands**: Reusable prompts stored for quick access. User-triggered, not agent-triggered. No relation to skills or MCP servers.

Key distinction: skills combine Claude's built-in knowledge with existing tools to execute specific workflows. MCP servers add entirely new tool capabilities.

### Context Window Efficiency

Skills have a two-phase loading model:

1. **Idle**: Only a short description is loaded — just enough for the agent to know the skill exists and when to use it. Token cost is negligible even with many skills installed.
2. **Active**: Full markdown file (which can be large) loads into context only when the agent decides the skill is needed for the current task.

MCP server tools, by contrast, have their definitions and documentation always in context. For capabilities used infrequently, skills are the more context-efficient choice.

### Installing Skills

Two methods:

**Plugin marketplace (built-in)**:
1. Open Claude Code, go to plugins
2. Navigate to marketplaces, add a GitHub repository URL (e.g., the official Anthropic marketplace)
3. Browse available plugins, select with spacebar, press `I` to install
4. Installs at user level by default

**skills.sh (recommended)**:
1. Go to [skills.sh](https://skills.sh) — Vercel's open agent skills ecosystem
2. Browse trending, all-time favorites, or search
3. Copy the install command for any skill
4. Paste in terminal, select your CLI tool (Claude Code, Cursor, etc.)
5. Choose project-level or global installation
6. Project-level installs go to `.claude/skills/` — committable to repo so the whole team gets them

Notable skills on the marketplace:
- **Find Skills**: lets the agent search the marketplace and install skills itself
- **Skill Creator**: agent creates new skills from your instructions
- **Front-end Design**: detailed UI/UX context and resources
- **React Best Practices**: for Vite/React/Next.js projects
- **Browser Use**: gives the agent browser control for verification

### Creating Custom Skills

Workflow for building a new skill:

1. Figure out the actual workflow (what steps, what tools, what scripts)
2. Create a working example — e.g., get a code snippet from an API provider
3. Use the **skill creator skill** to generate the skill from your description and example code
4. The skill creator produces: a `skill.md` file with instructions, and supporting scripts in a `scripts/` folder

Example from the video — image generation skill:
- Provided a code snippet from Google AI Studio for the Nano Banana Pro model
- Specified defaults (1K resolution, square aspect ratio, output folder)
- Told Claude where the API key lives (`.env` file, variable name)
- Skill creator generated the markdown instructions and a Python script that reads the API key from environment variables

You can also create skills manually by reading the documentation and writing the markdown yourself, or by pasting the docs into Claude and asking it to generate the skill.

### Handling API Keys and Sensitive Data

Critical pattern for skills that need external API access:

1. Create a `.env` file in the project root
2. Add the API key as a variable (e.g., `GEMINI_API_KEY=...`)
3. Ensure `.env` is in `.gitignore` — never commit it
4. Tell Claude the variable name and location when creating the skill
5. The generated script reads from environment variables, never hardcodes the key
6. Never pass API keys directly to Claude or ask it to embed them in skill files

### Image Generation Workflow

The video demonstrates two image generation approaches:

**Paid (Nano Banana Pro / Google)**:
- Uses the Gemini SDK via a Python script
- Supports 1K/2K/4K resolution and multiple aspect ratios
- Requires a Gemini API key stored in `.env`
- Produces high-quality photorealistic images

**Free (open-source local model)**:
- Uses a small model that runs locally — no API key, no cost
- Good for icons or profile images, not photorealistic content
- Any Hugging Face model can be swapped in based on hardware

### Combining Skills into Workflows

The video shows chaining multiple skills for a complete pipeline:

1. **Front-end design skill** → redesigns the fitness app UI from bland/generic to polished
2. **Browser use skill** → agent opens a browser and visually verifies the UI changes
3. **Image generator skill** → creates an AI-generated hero image
4. **Image optimizer skill** (created on the fly) → resizes and converts to WebP, reducing a 631 KB image to 56 KB
5. Agent replaces the placeholder on the homepage with the optimized image

This demonstrates skills composing naturally — each handles one concern, and the agent chains them as needed.
