# Notes: Claude Code Skills

> Personal takeaways from [Claude Code Skills - The Only Tutorial You Need](https://www.youtube.com/watch?v=vIUJ4Hd7be0) by Leon van Zyl (2026-02-09, 20 min)

## Key Insights for Presentations

- **Skills = markdown files with precise instructions + bundled resources (scripts, context).** They teach Claude Code to do things it can't do natively. Not tools, not prompts — procedural workflows.
- **Skills are lazy-loaded.** Only a tiny summary sits in context. The full skill (markdown + scripts + files) loads only when the agent detects it's relevant. MCP tools are always in context, always consuming tokens.
- **Token cost is near-zero until activation.** Multiple skills installed, barely any token usage visible in `/context`. This is the critical differentiator from MCP servers.
- **Skill composition is the power move.** Generate image (image gen skill) -> optimize for web (image optimizer skill) -> insert into UI (frontend design skill). Three skills chained in one session to go from placeholder to production asset.
- **Skills can be committed to a repo.** Install at project level, check `.claude/skills/` into version control, entire team gets the same capabilities. MCP servers require per-machine setup.

## Skills vs MCP Servers vs Custom Commands

| Aspect | Skills | MCP Servers | Custom Commands |
|---|---|---|---|
| **What they are** | Markdown instructions + resources (scripts, files) | External tools (browser, DB, APIs) | Reusable prompts |
| **Context loading** | Lazy — loaded only when needed | Always preloaded with full metadata | User-triggered |
| **Token cost at idle** | Near zero (just a short description) | Constant (tool definitions always in context) | None until invoked |
| **Activation** | Auto-detected by agent from conversation context | Always available | Manually triggered by user |
| **What they provide** | Workflows, domain knowledge, procedural instructions | New capabilities/tools | Convenience for repeated prompts |
| **Shareability** | Commit to repo, install from marketplace | Requires server config per machine | Can share prompt files |
| **Relationship** | Can combine WITH tools | Provides tools skills can use | Unrelated to skills/MCP |

**Key framing:** MCP servers give the agent new *tools*. Skills give the agent new *knowledge and workflows* for using those tools (or scripts) effectively. Custom commands are just saved prompts — different category entirely.

## Installation Workflows

### Method 1: Built-in Plugin Marketplace (more complex)
1. In Claude Code, go to `/plugin`
2. Press right arrow to go to "marketplaces"
3. Add marketplace URL (e.g., Anthropic's official GitHub repo)
4. Browse available plugins, press spacebar to select
5. Press `I` to install

### Method 2: skills.sh (recommended)
1. Go to [skills.sh](https://skills.sh) — open agent skills ecosystem by Vercel
2. Browse trending, all-time favorites, or search
3. Copy the install command for any skill
4. Paste in terminal, select your CLI tool (Claude Code, Cursor, etc.)
5. Choose project-level or global installation
6. Select "symlink" for installation type
7. Skill appears in `.claude/skills/` (and equivalent for other tools)

**Notable skills from the video:**
- **Find Skills** — agent searches skills.sh marketplace automatically
- **Skill Creator** — agent creates new skills from your description
- **Frontend Design** — large context file with UI/design best practices
- **React Best Practices** — for Vite/React/Next.js projects
- **Browser Use** — gives agent browser control for verification

## Skill Creation Patterns

### The Workflow
1. Figure out the procedural workflow you want (what steps does the agent need to follow?)
2. Create a working example first (e.g., get a code snippet from an API docs page)
3. Use the **skill creator skill** to generate the skill from your example + instructions
4. The skill creator produces: `skill.md` (instructions) + `scripts/` folder (executable code)

### Anatomy of a Skill
```
.claude/skills/image-generator/
  skill.md          # Instructions: when to use, parameters, defaults
  scripts/
    generate.py     # The actual executable the agent runs
```

- `skill.md` contains: description, usage instructions, parameter defaults, file paths
- Scripts handle the actual work — Python, shell, whatever
- The agent reads `skill.md`, then follows its instructions to execute scripts

### What Makes a Good Skill
- **Clear procedural workflow** — step-by-step, not vague
- **Sensible defaults** — e.g., default to 1K resolution, square aspect ratio
- **Specified output locations** — tell the agent where to save results
- **Environment variable references** — never hardcoded secrets

## Security Patterns: API Key Handling

- **Never hardcode API keys in skills or scripts.** If you deploy/share the skill, you leak the key.
- **Use `.env` files** in project root. Store keys as environment variables (e.g., `GEMINI_API_KEY=...`).
- **Always add `.env` to `.gitignore`.** Verify it's excluded before committing.
- **Scripts read from environment variables** — `os.environ.get("GEMINI_API_KEY")`, never from hardcoded strings.
- **Tell Claude about the env var name** — "I stored the API key in `.env` under `GEMINI_API_KEY`" so the skill can reference it.
- **Never pass API keys directly to Claude in the prompt.** Don't ask Claude to hardcode them.

## Workflow Composition: The Full Demo

The video demonstrates a three-skill pipeline on a fitness app landing page:

1. **Frontend Design skill** — Rewrites a bland, AI-slop landing page into a professional-looking fitness brand site. Colors, fonts, layout all improved.
2. **Image Generator skill** (custom, using Nano Banana Pro / Gemini API) — Generates a photo-realistic image of a woman jogging on a beach with an AI assistant chatbot floating behind her.
3. **Image Optimizer skill** (custom) — Takes the 631KB generated PNG, resizes for web hero section, converts to WebP, outputs 56KB. Stored in `public/assets/`.
4. **Browser Use skill** — Agent opens browser (non-headless), visually verifies the page looks correct.

Result: Placeholder image replaced with AI-generated, web-optimized image. Four skills, one session.

## Quotable Moments

- "Skills are basically markdown files with very precise instructions." (1:05)
- "MCP servers simply provide new tools to the agent." (1:52)
- "Skills actually take up very little context." (3:05)
- On token usage after installing multiple skills: "We're barely using any tokens." (9:01)
- On lazy loading: "Only if the skill is needed will it dive into these folders to pull in all of these additional files and context." (9:09)
- "Please do not pass [API keys] to Claude directly and please don't ask Claude to hardcode it in the skills itself." (16:24)

## Presentation Slide Ideas

1. **"What Are Claude Code Skills?"** — Markdown instructions + bundled resources. Teach Claude new workflows it can't do natively. Show the infographic.

2. **"Skills vs MCP Servers vs Custom Commands"** — Three-column comparison table. Emphasize the lazy-loading vs always-loaded distinction. This is the slide that clears up the most confusion.

3. **"The Context Window Trade-off"** — Visual: show token usage with 5 skills installed (near zero) vs 5 MCP tools (constant overhead). The "only load what you need" principle.

4. **"Finding & Installing Skills"** — Two paths: skills.sh marketplace (easy) vs Anthropic GitHub plugin system. Show the one-command install flow from skills.sh.

5. **"Anatomy of a Skill"** — Show the folder structure: `skill.md` + `scripts/`. Walk through what the markdown contains and how the agent discovers and activates it.

6. **"Creating Your Own Skills"** — The skill creator meta-skill. Give Claude an example code snippet + instructions, get a complete skill back. Live demo candidate.

7. **"Security: API Keys Done Right"** — `.env` + `.gitignore` + environment variables. What NOT to do (hardcode, pass in prompt). Short but critical slide.

8. **"Skill Composition in Action"** — The four-skill pipeline: design -> generate -> optimize -> verify. Show before/after of the landing page. This is the "wow" slide — demonstrates compound capability.
