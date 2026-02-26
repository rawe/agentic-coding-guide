# Debugging with Claude in Chrome

Connect Claude Code to your browser. Inspect, diagnose, and fix — without leaving the terminal.

## Setup (One-Time)

1. Install **Claude in Chrome** extension
2. Run `claude --chrome` or type `/chrome`
3. Done. No ports, no extra config.

## The Debugging Toolkit

### DOM & Visual

- `read_page` — Accessibility tree of all elements
- `find` — Natural language element search
- `computer: screenshot` — Capture current page state
- `computer: zoom` — Inspect a specific region close-up

### Console & Errors

- `read_console_messages` — Read console.log, .error, .warn
- `javascript_tool` — Execute JS in page context

### Network & API

- `read_network_requests` — Monitor XHR, Fetch, resources
- `navigate` — Go to URLs, forward/back

### Interaction

- `computer` — Click, type, scroll, keyboard
- `form_input` — Fill form values by element ref
- `gif_creator` — Record steps as animated GIF

## Debugging Workflows

### Broken Layout

*"The sidebar is overlapping the content area"*

`screenshot` → `read_page` → `find "sidebar"` → `javascript_tool: getComputedStyle` → fix CSS in source

**Key:** Claude sees the visual state AND reads the DOM. Correlates what's visible with what's in the code, then fixes it directly.

### Failing API Call

*"The save button does nothing when I click it"*

`navigate to page` → `computer: click save` → `read_network_requests: /api/` → `read_console_messages: error|reject` → fix request in source

**Key:** Sees the 422 response, reads the payload mismatch, identifies the bug. No manual Network tab inspection.

### Page Crash / JS Error

*"The dashboard just shows a blank white page"*

`navigate` → `read_console_messages: onlyErrors` → `screenshot` → `read_network_requests: check 404s` → trace stack → fix

**Key:** Gets the stack trace, sees the visual state, checks if resources failed to load. Traces back to source and proposes a fix.

## Why This Beats DevTools Alone

### No Context Switching

Claude reads the browser, finds the bug, and fixes the code in one continuous flow. No DevTools → editor → refresh loop.

### Visual + Code in One Step

Screenshots a broken layout AND reads the source. Correlates what you see with what's in the codebase. DevTools can't edit your files.

### Everything at Once

Console errors + network requests + DOM state + screenshots in a single investigation. No clicking between DevTools tabs.

### Reproduces User Flows

Clicks through a 5-step flow, monitors for errors at each step, records it as a GIF. Shares your browser's login state.

## Watch Out For

- `alert()` and `confirm()` dialogs block the browser event loop and prevent Claude from receiving commands. Avoid triggering them.
- Large DOM trees can exceed token limits. Use `ref_id` to focus on specific subtrees.
- Always use the `pattern` parameter when reading console messages. Unfiltered SPA logs will flood the context.
- Screenshots are viewport-only. Scroll first for below-the-fold content.
- Chrome and Edge only. No Brave, Arc, or WSL support yet.
