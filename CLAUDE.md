# CLAUDE.md

Guides and references for effective agentic coding with Claude Code. Sources are collected from talks, docs, and real usage, then distilled into presentation-ready HTML pages (`docs/`) that can be shared in meetings, team onboarding, and workshops. The knowledge covers everything from context engineering fundamentals to skill authoring and multi-agent patterns.

## Writing Rules

- No filler. No AI slop. Every sentence must carry information.
- Write for a human who wants to learn fast.
- Summaries: bullet points over paragraphs. Facts over commentary.
- Guides (later phase): more prose is acceptable, but still no fluff.
- Always cite the original source with URL and author.

## Project Structure

- `sources/` — collected references. See [sources/README.md](sources/README.md) for structure, templates, and workflow.
- `guides/` — distilled best practices (phase 2).
- `.claude/skills/` — processing skills (e.g. `/yt-extract <url>`).

## Index Page (docs/index.html)

The index groups all HTML guide pages into numbered sections ordered by progressive depth — from orientation to advanced patterns. Pages are presentation-ready references for meetings and team onboarding.

When adding a new page:
- Decide which group it belongs to (or whether a new group is needed).
- Place it where it makes sense in the reading order: what prior knowledge does it assume?
- The structure and rationale are documented in `docs/STRUCTURE.md` — update it when the index changes.

## Commit Rules

- Never mention AI, co-authors, Claude, or any coding model in commit messages.
- No `Co-Authored-By` lines.
- Write commits as if a human wrote them. Short, descriptive, conventional.

## Python & Dependencies

- Use `uv` for all dependency management. Never use `pip`, `pip3`, or `pip install`.
- Use `python`, not `python3`.
- For scripts with dependencies, use inline uv shebangs:
  ```
  #!/usr/bin/env -S uv run --with package1 --with package2
  ```
- For one-off commands needing a dependency:
  ```
  uv tool run --with <package> python -c "..."
  ```
- Never install packages globally or with `--system`. Use inline deps or virtual envs.
