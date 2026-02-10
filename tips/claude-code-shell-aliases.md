# Claude Code Shell Aliases

Quick aliases for launching Claude Code with experimental features.

## Setup

Add to `~/.zshrc` (or `~/.bashrc`):

```bash
# Claude Code with agent teams (experimental multi-agent collaboration)
alias clt='CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude'
alias cltc='CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude --chrome'
```

Reload: `source ~/.zshrc`

## What they do

| Alias  | Description |
|--------|-------------|
| `clt`  | Claude Code with agent teams enabled |
| `cltc` | Same + Chrome browser control |

**Agent teams** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`): Enables multi-agent collaboration where Claude can spawn teammate agents that work in parallel.

**Chrome mode** (`--chrome`): Connects Claude Code to your Chrome browser via the [Claude in Chrome](https://claude.ai/chrome) extension. Claude can then navigate pages, click elements, fill forms, take screenshots, and automate browser tasks. Requires the extension installed in Chrome.
