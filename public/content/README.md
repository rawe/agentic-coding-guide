# Content Files Index

Markdown content files for each HTML page in `public/`. Each `.md` file shares the same basename as its corresponding `.html` file and contains structured content with YAML frontmatter (`title`, `html_file`, `description`).

## Naming Convention

```
public/<name>.html  →  public/content/<name>.md
```

## Pages

| Markdown File | HTML File | Title |
|---|---|---|
| [index.md](index.md) | [index.html](../index.html) | Agentic Coding |
| [research-plan-implement.md](research-plan-implement.md) | [research-plan-implement.html](../research-plan-implement.html) | Research → Plan → Implement |
| [skills-mcp-commands.md](skills-mcp-commands.md) | [skills-mcp-commands.html](../skills-mcp-commands.html) | Skills vs MCP Servers vs Custom Commands |
| [skills-in-practice.md](skills-in-practice.md) | [skills-in-practice.html](../skills-in-practice.html) | Skills in Practice |
| [commands-in-practice.md](commands-in-practice.md) | [commands-in-practice.html](../commands-in-practice.html) | Commands in Practice |
| [command-skill-journey.md](command-skill-journey.md) | [command-skill-journey.html](../command-skill-journey.html) | The Command & Skill Journey |
| [subagents-vs-teams.md](subagents-vs-teams.md) | [subagents-vs-teams.html](../subagents-vs-teams.html) | Subagents vs Agent Teams |
| [mastering-claude-md.md](mastering-claude-md.md) | [mastering-claude-md.html](../mastering-claude-md.html) | Mastering CLAUDE.md |
| [context-engineering.md](context-engineering.md) | [context-engineering.html](../context-engineering.html) | Master Your Context Window |
| [developer-workflows.md](developer-workflows.md) | [developer-workflows.html](../developer-workflows.html) | The Developer's Daily Loop |

## Structure

Each markdown file contains:

- **YAML frontmatter** with `title`, `html_file`, and `description`
- **Structured body** capturing all sections, key points, code examples, and sources from the HTML page
- Content suitable for regenerating or optimizing the corresponding HTML page
