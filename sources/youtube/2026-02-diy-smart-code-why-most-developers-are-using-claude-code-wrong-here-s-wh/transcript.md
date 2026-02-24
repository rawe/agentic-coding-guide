# Transcript

[0:00] Five features, one decision matrix,
[0:02] always on instructions, on demand
[0:04] expertise, isolated agents, event-driven
[0:07] automation, external integrations. After
[0:10] this video, you'll never put the wrong
[0:11] thing in the wrong place again. Every
[0:14] time you explain your team's coding
[0:16] standards to Claude, you're repeating
[0:17] yourself. Every PR review, you
[0:20] redescribe how you want feedback
[0:21] structured. Every commit message, you
[0:24] remind Claude of your preferred format.
[0:26] Every single session you've tried
[0:29] putting everything into one big
[0:30] instructions file. Your rules, your
[0:33] checklists, your deployment procedures,
[0:35] your brand guidelines. All of it crammed
[0:38] into one place. But here's the problem.
[0:41] That file loads into every conversation.
[0:43] Your PR review checklist is sitting in
[0:45] context when you're debugging a memory
[0:47] leak. Your deployment procedure is
[0:49] consuming tokens while you're writing
[0:50] unit tests. It works, but it's like
[0:54] keeping your entire reference library on
[0:55] your desk at all times. Wasteful,
[0:57] cluttered, expensive. Clot code actually
[1:00] gives you five distinct customization
[1:02] features. Clot MD, skills, sub aents,
[1:06] hooks, MCP servers. Each one solves a
[1:09] different problem. Each one loads
[1:10] differently. Each one costs your context
[1:12] window differently. And most developers
[1:14] are only using one of them. Here's what
[1:16] we'll cover. Five features, each with a
[1:18] clear rule for when to use it. First,
[1:21] clot.m MD always on instructions that
[1:23] load every session. Second, skills on
[1:26] demand expertise that loads only when
[1:28] relevant. Third, sub agents, isolated
[1:31] workers that run in their own context
[1:33] window. Fourth, hooks, event-driven
[1:37] automation that fires on specific
[1:38] triggers. And fifth, MCP servers,
[1:41] external tool integrations via open
[1:43] protocol. By the end, you'll have a
[1:45] simple decision matrix. One question per
[1:47] feature. No more guessing. No. Let's
[1:50] start with the foundation.
[1:52] Clot.m MD is a markdown file you add to
[1:55] your project. Clot reads it at the start
[1:57] of every session. Always. No exceptions.
[2:00] Think of it as the company handbook.
[2:02] Everyone reads it. It always applies.
[2:05] You put your non-negotiable standards
[2:06] here. Always use TypeScript strict mode.
[2:09] Use PNPM. Never npm. Never modify the
[2:12] database schema directly. These are
[2:14] rules that apply to every single task,
[2:17] every single conversation.
[2:19] But here's what makes it powerful.
[2:21] Cloud.md is hierarchical. You can have
[2:24] an enterprise level file that applies to
[2:26] everyone in your organization. A
[2:28] personal file in your home directory
[2:30] that follows you across all your
[2:32] projects. A project level file that your
[2:35] whole team shares via version control.
[2:38] And a local file just for you for this
[2:40] specific project. More specific always
[2:42] wins. Your project file overrides your
[2:44] personal file. Your local file overrides
[2:47] the project file. It's a cascade like
[2:50] CSS for your AI assistant. And as of
[2:53] recent versions, Claude also builds its
[2:55] own memory automatically. As you work
[2:57] together, Claude notices patterns,
[2:59] preferences, and conventions. It writes
[3:02] them to a memory directory and loads
[3:04] them back next session. The key rule for
[3:07] Claude MD, if Claude should always know
[3:09] it, put it here. But remember,
[3:12] everything in clot.mdish consumes your
[3:14] context window every session, whether
[3:16] it's relevant or not. That's the
[3:18] trade-off. Now, skills. This is where it
[3:21] gets interesting. A skill is a markdown
[3:23] file called skill.md that teaches Claude
[3:26] how to do something specific. It has a
[3:28] description that tells Claude when to
[3:30] use it and instructions that Claude
[3:32] follows when it activates. Here's the
[3:34] magic. You don't have to type a SL
[3:36] command. Claude reads your request,
[3:38] compares it to all available skill
[3:40] descriptions, and activates the ones
[3:42] that match. You say, "Review this PR,"
[3:44] and Claude automatically loads your PR
[3:46] review skill. You say, "Deploy to
[3:48] production," and your deployment
[3:49] checklist activates. Only the
[3:51] description is in context at all times.
[3:54] The full skill content loads on demand.
[3:56] Your PR review checklist isn't consuming
[3:58] tokens while you're debugging. It loads
[4:01] when you actually ask for a review.
[4:03] Skills can also be SL commands. You can
[4:06] type slreview or slash deploy to invoke
[4:08] them directly. In fact, entropic
[4:10] merged/comands and skills. They're the
[4:13] same thing. Now, a file at do.cl/comands
[4:16] and a skill atcloud/skills.
[4:19] Both create the same slash command.
[4:21] Skills can include supporting files too.
[4:23] Templates, reference docs, scripts. Your
[4:26] skill.md stays focused on the main
[4:28] instructions while detailed reference
[4:29] material lives in separate files that
[4:31] Claude reads only when needed. Where you
[4:34] store a skill determines who uses it.
[4:36] Personal skills in your home directory
[4:38] follow you everywhere. Project skills
[4:40] include/skills get shared with your team
[4:43] through version control. Everyone who
[4:45] clones the repo gets the same skills
[4:47] automatically.
[4:48] The key rule. If cla should know it
[4:50] sometimes, make it a skill. This is the
[4:53] number one confusion point. Let me make
[4:55] it crystal clear. Claude.md loads into
[4:58] every conversation. Always consuming
[5:00] tokens. Always in context. Skills load
[5:03] on demand only when relevant. Minimal
[5:06] context cost. Here's the decision
[5:07] framework. Use TypeScript strict mode.
[5:10] Clot MD that applies to everything. PR
[5:13] review checklist skill only relevant
[5:16] when reviewing. Never modify the
[5:17] database schema. Clot MD non-negotiable
[5:20] rule. Deployment procedure skill only
[5:24] needed when deploying. The rule is
[5:26] simple. Projectwide standards that
[5:28] always apply going claw.md task specific
[5:32] expertise that's only relevant sometimes
[5:34] goes in skills. Wait 91% of solo AI
[5:38] builders quit within 3 months but not
[5:40] this group. Over a thousand builders
[5:43] daily hangouts where you debug together
[5:45] weekly workshops that actually level you
[5:47] up. A full agentic coding course. 72
[5:50] lessons. 12 modules from zero to
[5:53] shipping multi- aent systems. People
[5:55] share projects. Brainstorm ideas, help
[5:57] each other in real time. This is where
[5:59] AI builders actually make it. Link in
[6:02] description, 10% off. Join us. Back to
[6:05] the video. Now, sub agents are a
[6:08] completely different concept. They're
[6:10] specialized AI assistants that run in
[6:12] their own context window, completely
[6:14] isolated from your main conversation.
[6:16] When you ask Claude to research a
[6:18] codebase, it can delegate to an explore
[6:20] sub agent. That agent reads dozens of
[6:22] files, searches through directories,
[6:24] analyzes the architecture. All of that
[6:26] verbose output stays in the sub aents
[6:28] context. Only the relevant summary comes
[6:30] back to your main conversation. Your
[6:32] context window stays clean. Clot code
[6:35] ships with three built-in subgents.
[6:37] Explore runs on high for speed. It's
[6:40] read only, perfect for searching and
[6:41] analyzing. Plan is for research during
[6:43] plan mode and general purpose has access
[6:46] to all tools for complex multi-step
[6:48] tasks, but you can build your own.
[6:50] Create a markdown file include/ aents
[6:52] with a name, description, tool
[6:54] restrictions, and model selection. Want
[6:56] a code reviewer that can only read
[6:58] files? Set tools to read grap glo. Want
[7:02] to optimize costs? Root research tasks
[7:04] to haiku and keep complex reasoning on
[7:06] set. Sub agents can even have their own
[7:09] persistent memory. A code reviewer that
[7:11] remembers patterns it's seen across
[7:12] sessions. A debugger that builds up
[7:15] knowledge about common issues in your
[7:16] codebase. The key rule. if it should run
[7:19] in isolation with its own context. Use a
[7:21] sub agent. Hooks are fundamentally
[7:24] different from everything we've covered
[7:25] so far. Skills add knowledge. Sub agents
[7:28] delegate tasks, but hooks hooks fire on
[7:31] events automatically, deterministically.
[7:34] No hoping the LLM makes the right
[7:36] choice. A hook is a shell command that
[7:39] executes at a specific point in clot
[7:40] code's life cycle. Pre-tool use fires
[7:44] before clot runs a tool. Post tool use
[7:46] fires after. session, start fires when
[7:49] you begin, stop fires when Claude
[7:51] finishes responding. There are 15 event
[7:53] types in total. Here's a concrete
[7:55] example. You write a pre-tool use hook
[7:58] that matches the bash tool. Every time
[8:00] Claude tries to run a shell command,
[8:01] your script checks the command first. If
[8:04] it contains RM-rf,
[8:06] exit code two, blocked, destructive,
[8:09] command denied. Claude never runs it.
[8:11] Another example, post tool use hook
[8:13] matching write and edit. Every time
[8:15] Claude saves a file, your hook runs
[8:17] prettier to auto format. Every file,
[8:19] every time. Consistent formatting
[8:22] without even thinking about it. The
[8:24] critical distinction. Skills are request
[8:26] driven. They activate when you asked for
[8:28] something. Hooks are event driven. They
[8:30] fire on every matching event regardless
[8:32] of what you asked for. You don't hope
[8:34] Claude remembers to lint. The hook
[8:37] guarantees it. Hooks can even use an LLM
[8:39] to make decisions. A prompt-based hook
[8:42] sends context to a fast model that
[8:44] returns a yes or no decision. An
[8:46] agent-based hook spawns a sub agent that
[8:48] can read files and check conditions
[8:50] before deciding. Hooks aren't limited to
[8:53] simple shell scripts. The key rule, if
[8:55] it should happen automatically on every
[8:57] matching event, use a hook. The last
[9:00] piece,
[9:01] MCP stands for model context protocol.
[9:04] It's an open source standard for
[9:06] connecting AI tools to external
[9:08] services. Need claude to check your
[9:10] sentry errors. Connect the sentry MCP
[9:12] server. Want to query your Postgress
[9:14] database directly? Add the database MCP
[9:18] server. GitHub pull requests, Jira
[9:20] issues, Figma designs, Slack messages.
[9:23] There are over 100 official servers in
[9:24] the registry. You connect them with a
[9:26] single command. Claude MCP add. Choose a
[9:29] transport type and you're done. Claude
[9:31] gets access to new tools from external
[9:33] services without any custom code. MCP
[9:36] tools appear alongside Claude's built-in
[9:38] tools. You can use them in hooks, in
[9:40] skills, in sub agents. The whole system
[9:42] composes together. The key rule, if
[9:45] Claude needs external tools or data,
[9:47] connect an MCP server. Let's bring it
[9:50] all together. Five features, five
[9:52] questions, one answer each. Should
[9:54] Claude always notice cloud.md. Should
[9:56] claude notice sometimes skills. Should
[9:59] this run in isolation, sub aents? Should
[10:01] this happen automatically on events
[10:03] hooks? Does clot need external tools?
[10:06] MCP servers. Now look at context window
[10:09] impact. Clot.m MD is high. It's loaded
[10:12] every session consuming tokens where
[10:14] they're relevant or not. Skills are low.
[10:16] Only the description sits in context
[10:18] until invoked. Sub aents and hooks are
[10:20] zero. Sub aents run in their own context
[10:23] window. Hooks run outside Claude's
[10:25] context entirely. MCP is moderate, but
[10:27] tool search dynamically loads tools on
[10:29] demand to mitigate it. Your context
[10:31] window is precious. Use it wisely. A
[10:34] real world setup uses multiple features
[10:36] simultaneously.
[10:38] Here's what a well-configured project
[10:39] looks like. Claw.mde handles your always
[10:43] on standards. Use PNPM.
[10:45] TypeScript strict mode. Never mutate the
[10:48] database directly. Skills handle task
[10:51] specific expertise.
[10:53] A PR review skill with your team's
[10:55] checklist. A deployment skill with your
[10:58] step-by-step procedure.
[11:00] A commit skill with your message format.
[11:03] Sub agents handle delegation.
[11:06] A code reviewer with read only access. A
[11:08] researcher that explores documentation
[11:10] without cluttering your context. Hooks
[11:12] handle automation. Auto format every
[11:14] file cloud touches. Block destructive
[11:16] shell commands. Run tests after every
[11:18] edit. MCP connects external services.
[11:20] GitHub for pull requests. Sentry for
[11:22] error monitoring. Postgress for data
[11:24] queries. Each handles its own specialty.
[11:27] Don't force everything into one feature.
[11:29] You can use all five at the same time.
[11:31] They compose. They complement. They
[11:33] don't compete. If you find yourself
[11:35] explaining the same thing to Claude
[11:36] repeatedly, that's a skill waiting to be
[11:38] written. Here's how to start. Open your
[11:42] project run/init to bootstrap a
[11:44] claude.md.
[11:45] That's your foundation. Then the next
[11:48] time you repeat yourself, write a skill.
[11:50] The next time you want guardrails, add a
[11:53] hook. The next time you need isolation,
[11:55] create a sub agent. And the next time
[11:57] you need external data, connect an MCP
[12:00] server. Links to the full documentation
[12:02] are in the description below. If this
[12:04] helped you level up your cloud code
[12:06] setup, hit subscribe and check out the
[12:08] Dynamos AI agent mastery course to go
[12:10] even deeper with Agentic Workflows.
