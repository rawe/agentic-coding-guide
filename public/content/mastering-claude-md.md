---
title: "Mastering CLAUDE.md"
html_file: mastering-claude-md.html
description: "How to write and structure CLAUDE.md files that effectively configure Claude Code's behavior across projects."
---

# Mastering CLAUDE.md

Write project instructions that Claude actually follows -- from first file to full configuration stack.

## What CLAUDE.md Actually Is

CLAUDE.md is a project's onboarding document for Claude Code. It is loaded into context at the start of every session, replacing the need to repeat instructions Claude cannot infer from code alone.

- Without it, Claude guesses at your conventions. With it, Claude knows how to build, test, lint, and work the way your team does from the first message.
- The file must be named exactly `CLAUDE.md` (uppercase CLAUDE, lowercase .md). Place it in the project root or inside `.claude/`.
- The `/init` command bootstraps a starter file by analyzing your codebase -- package.json, Makefile, CI configs, project structure. The output needs manual refinement; auto-generated files tend to be too verbose and include things Claude can figure out on its own.

**Key insight:** Anthropic's own teams found that better CLAUDE.md documentation directly correlates with better Claude Code performance. Their Data Infrastructure team reduced researcher onboarding time by ~80% with well-structured project instructions.

## The Configuration Hierarchy

CLAUDE.md is not a single file -- it is a layered system. More specific layers override broader ones, building a full context stack from organization policy down to auto-generated notes.

The layers, from broadest to most specific:

1. **Managed Policy** -- Organization-wide rules set by admins. Cannot be overridden.
2. **~/.claude/CLAUDE.md** -- Personal global instructions. Apply to every project.
3. **./CLAUDE.md** -- Project-level shared instructions. Checked into version control.
4. **.claude/rules/\*.md** -- Modular topic-scoped rules. Auto-loaded, support path matching.
5. **CLAUDE.local.md** -- Personal project overrides. Auto-gitignored.
6. **subdir/CLAUDE.md** -- Child directory instructions. Loaded on demand, not at startup.
7. **Auto Memory** -- `~/.claude/projects/<project>/memory/` -- Claude's own notes. First 200 lines load.

**When to use each layer:**

- Global CLAUDE.md for personal preferences (editor, style)
- Project CLAUDE.md for team-shared conventions
- Rules for topic-specific instructions (testing, security)
- Local for sandbox URLs and personal shortcuts
- Child directories for monorepo sub-projects

## What to Put In (and What to Leave Out)

Frontier models handle ~150-200 instructions reliably. The system prompt already uses ~50. Every line you add competes for attention.

### Include

- Build, test, and lint commands Claude can't guess
- Code style rules that differ from language defaults
- Test runner configuration and how to run specific tests
- Architectural decisions and key patterns
- Branch naming and PR conventions
- Common gotchas specific to your codebase
- Emphasis markers for critical rules: `IMPORTANT`, `YOU MUST`

### Leave Out

- Anything Claude figures out by reading code
- Standard language conventions (PEP 8, Go formatting)
- Detailed API docs -- link with `@path` instead
- Information that changes frequently
- File-by-file codebase descriptions
- Code style rules a linter already handles
- Secrets, API keys, or credentials

**Budget rule:** The HumanLayer blog recommends keeping CLAUDE.md under 60 lines. Builder.io says under 300. Err toward shorter. For each line, ask: "Would removing this cause Claude to make mistakes?" If not, cut it.

## Anatomy of a Good CLAUDE.md

A well-structured file follows the WHAT-WHY-HOW framework: project context, standards, commands, and workflow rules.

Example:

```markdown
# CLAUDE.md

## Project
Acme API -- REST service for order management.
Node.js 20, TypeScript, PostgreSQL.

## Commands
npm run dev        # start dev server
npm test           # run all tests
npm test -- -t "name" # single test
npm run lint       # eslint + prettier

## Standards
- Use zod for all request validation.
- Errors return {error, code, details}.
- DB queries go in src/db/, never in routes.

## Workflow
- Branch from main, prefix: feat/ fix/ chore/
- IMPORTANT: Run tests before committing.
- Never push directly to main.

## Context
@docs/api-spec.yaml
@docs/architecture.md
```

### What each section does

- **Project Context** -- What the project is, what stack it uses. Enough for Claude to understand the domain without reading every file.
- **Commands** -- Build, test, lint -- the commands Claude needs to verify its own work. Without these, Claude can't run tests or check for errors.
- **Standards** -- Rules Claude can't infer from code. Validation library choices, error response shapes, file organization conventions.
- **Workflow Rules** -- How to branch, commit, and ship. `IMPORTANT` emphasis markers for rules that must not be ignored under context pressure.
- **@import References** -- The `@path/to/file` syntax pulls external docs into context without bloating the main file. Keep CLAUDE.md lean, link to details.

## Scaling with Rules and Skills

When a single CLAUDE.md gets too big, split it. Rules are modular instruction files that auto-load. Skills are domain knowledge that loads only when needed.

**Rules** live in `.claude/rules/*.md` and are loaded automatically alongside CLAUDE.md. Each file is a self-contained topic: `code-style.md`, `testing.md`, `security.md`. Rules can be organized in subdirectories and support symlinks for cross-project sharing.

Example rule with path-based activation:

```markdown
# .claude/rules/testing.md
---
paths: src/**/*.test.ts
---

- Use vitest, not jest.
- Every test file needs a describe block matching the module name.
- Mock external services with msw, never stub fetch directly.
- IMPORTANT: Always assert both success and error paths.
```

The `paths:` frontmatter makes this rule activate only when Claude is working on files matching `src/**/*.test.ts`. Universal rules omit the frontmatter and load for every session.

**When to graduate from CLAUDE.md to rules:** If an instruction only applies to a subset of files or a specific topic, move it to a rule. If it only matters sometimes and requires domain knowledge, make it a skill. Keep CLAUDE.md for universal, always-relevant instructions.

Recommended directory structure:

```
.claude/
  CLAUDE.md              # universal instructions (~50 lines)
  rules/
    code-style.md         # formatting, naming conventions
    testing.md            # test patterns, paths: src/**/*.test.*
    security.md           # auth patterns, input validation
    database.md           # query patterns, migration rules
  skills/
    deploy/              # deployment workflow (on-demand)
    migrate-db/          # database migration (on-demand)
```

## The Full .claude/ Directory

CLAUDE.md is one piece of a larger configuration system. The `.claude/` directory holds everything that shapes how Claude Code behaves in your project.

```
CLAUDE.md              # project instructions (alternative to .claude/CLAUDE.md)
CLAUDE.local.md        # personal overrides (auto-gitignored, project root)
.claude/
  CLAUDE.md              # project instructions (shared, versioned)
  settings.json          # tool configuration (shared, versioned)
  settings.local.json    # personal tool config (auto-gitignored)
  .mcp.json              # MCP server connections
  rules/                # modular instruction files
  skills/               # domain knowledge & workflows
  commands/             # custom slash commands
  agents/               # custom agent definitions
```

### File purposes

- **CLAUDE.md** -- Instructions for Claude: what to do, how to work, what matters. Advisory: Claude follows these but may deprioritize under heavy context.
- **settings.json** -- Configuration for the tool: permission allow/deny rules, hooks, model selection, environment variables. Deterministic: always enforced.
- **CLAUDE.local.md** -- Personal overrides that don't belong in version control. Sandbox URLs, personal shortcuts, local environment specifics.
- **.mcp.json** -- MCP server connections that give Claude access to external tools: databases, APIs, custom integrations.
- **rules/** -- Auto-loaded instruction files. Support `paths:` frontmatter for file-type-specific activation. Subdirectories and symlinks supported.
- **commands/** -- Custom slash commands. Each `.md` file becomes a `/command`. Thin orchestrators that delegate to skills.

**Key distinction:** CLAUDE.md = instructions for Claude (advisory). settings.json = configuration for the tool (deterministic). Hooks defined in settings.json always execute; CLAUDE.md instructions may be deprioritized under context pressure.

## Common Mistakes and How to Fix Them

Five patterns that make CLAUDE.md less effective, and the fix for each.

### 1. The Kitchen-Sink File

Before -- a 287-line CLAUDE.md containing code style rules, API docs, file-by-file descriptions, deployment steps, meeting notes, and TODO lists:

```markdown
# CLAUDE.md (287 lines)
## Code Style
- Use 2-space indentation
- Use single quotes
- Use semicolons
... 40 more style rules ...

## API Reference
... 80 lines of endpoint docs ...
```

After -- a 47-line file with only universal, always-relevant rules:

```markdown
# CLAUDE.md (47 lines)
## Commands
npm test / npm run lint

## Standards
- Use zod for validation
- Errors: {error, code, details}

## Context
@docs/api-spec.yaml
@docs/architecture.md
```

**Fix:** Prune ruthlessly. Move style rules to `.claude/rules/`, link docs with `@imports`, delete anything Claude can infer.

### 2. Linter Rules in CLAUDE.md

Before -- duplicating linter configuration as natural-language instructions:

```markdown
# CLAUDE.md
- Always use semicolons
- 2-space indentation
- No trailing whitespace
- Max line length 100
- Prefer const over let
```

After -- a one-line instruction plus a deterministic hook:

```markdown
# CLAUDE.md
Run npm run lint before committing.
```

```json
// settings.json (PostToolUse hook)
{ "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "npm run lint"
      }]
    }]
  }
}
```

**Fix:** Never send an LLM to do a linter's job. Use actual linters via hooks for deterministic enforcement.

### 3. No Verification Commands

Before -- architecture description with no build/test/lint commands anywhere:

```markdown
# CLAUDE.md
## Architecture
We use a layered architecture with services, repositories, and controllers.
```

After -- explicit commands Claude can execute:

```markdown
# CLAUDE.md
## Commands
npm test               # all tests
npm test -- -t "name"  # one test
npm run lint           # eslint
npm run build          # typecheck + build

IMPORTANT: Run tests after every change.
```

**Fix:** Claude can't check its work without commands. Always include test, build, and lint invocations.

### 4. Stale Code Snippets

Before -- pasting implementation code that drifts out of sync:

```markdown
# CLAUDE.md
The auth middleware looks like this:
export function authMiddleware(req) {
  // 30 lines of code that's already
  // changed since this was written
}
```

After -- referencing files and describing patterns:

```markdown
# CLAUDE.md
Auth middleware: @src/middleware/auth.ts
Key pattern: all routes in src/routes/ use requireAuth() wrapper.
```

**Fix:** Use `@imports` to reference files instead of copying code. Point to patterns, not implementations.

### 5. Missing .local.md

Before -- personal preferences committed to the shared repo:

```markdown
# CLAUDE.md (shared repo)
My sandbox URL: http://localhost:3001
Use my personal API key for testing.
Always commit with -S for GPG signing.
```

After -- separation of shared and personal config:

```markdown
# CLAUDE.md (shared)
Dev server: npm run dev

# CLAUDE.local.md (personal, gitignored)
My sandbox: http://localhost:3001
Use --sandbox-port 3001 for dev.
Sign commits with GPG.
```

**Fix:** Create `CLAUDE.local.md` for personal preferences. It is auto-gitignored -- your teammates won't see it, and you won't clutter the shared file.

## Sources

- [Anthropic Docs: Memory](https://code.claude.com/docs/en/memory)
- [HumanLayer: Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Builder.io: CLAUDE.md Guide](https://www.builder.io/blog/claude-md-guide)
