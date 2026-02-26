# Transcript

[0:00] Most developers using one of these tools
[0:02] have never tried the other. Not because
[0:04] they chose, but because their employer
[0:06] chose or their editor chose or the first
[0:09] one they installed worked well enough
[0:10] that switching felt unnecessary. But
[0:12] these two tools are not interchangeable.
[0:14] One reads your entire project before
[0:16] suggesting a single change. The other
[0:18] responds in 35 milliseconds while your
[0:21] fingers are still on the keyboard. One
[0:23] operates from the terminal like
[0:25] infrastructure. The other lives inside
[0:27] your code editor like a reflex. They are
[0:29] built by companies with fundamentally
[0:31] different histories in artificial
[0:33] intelligence. And the developers who
[0:35] report the highest productivity gains
[0:37] are increasingly using both. Not because
[0:39] they cannot decide, but because each one
[0:41] solves a category of problem the other
[0:43] was never designed for.
[0:46] GitHub Copilot launched in June 2021 as
[0:49] an inline code completion tool developed
[0:52] by GitHub which is owned by Microsoft.
[0:54] The original product was reactive. You
[0:57] typed code and copilot suggested what
[0:59] should come next in line in your editor
[1:02] in milliseconds. It predicted function
[1:04] bodies from signatures, completed
[1:06] patterns from context and generated
[1:08] boiler plate from comments. That core
[1:11] autocomplete experience remains its
[1:13] foundation. The average response time
[1:15] sits at 35 milliseconds. The 99th
[1:18] percentile latency is 43 milliseconds.
[1:21] [music] For most interactions, the
[1:23] suggestion appears before you have
[1:25] finished thinking about what to type
[1:26] next. In 2025, GitHub added agent mode.
[1:31] This extended co-pilot from pure
[1:33] autocomplete into multi-step task
[1:35] execution. You describe what you want
[1:37] built and the agent plans and implements
[1:40] it. But the agent operates within the
[1:42] boundaries of your editor. It sees the
[1:45] files you have, open and nearby files in
[1:48] the project. It does not read the entire
[1:50] repository the way a dedicated codebase
[1:52] analysis tool would. For a task like
[1:54] completing a function or generating a
[1:57] test suite for code already on screen,
[1:59] that limited view is sufficient. [music]
[2:01] For a task like restructuring how
[2:03] authentication works across 12 files
[2:05] that depend on each other, the agent
[2:07] does not have the visibility to
[2:09] coordinate those changes reliably. The
[2:11] strength is speed and integration. The
[2:13] limitation is depth. The editor support
[2:16] is the broadest of any coding assistant
[2:18] available. The deepest integration is in
[2:20] Visual Studio Code with full support
[2:23] across the Jet Brains family, Visual
[2:25] Studio, and Community plugins for
[2:27] terminal based editors. If you work in a
[2:30] mainstream development environment,
[2:32] Copilot has a plug-in for it. The GitHub
[2:34] ecosystem integration goes further. Pull
[2:37] request summaries, code review
[2:39] assistance, commit message generation,
[2:41] and automated security scanning all
[2:43] connect through the same subscription.
[2:46] For teams already building on GitHub,
[2:48] the tool is not just a code assistant.
[2:50] It is part of the platform
[2:51] infrastructure. There are team and
[2:53] enterprise tiers with centralized policy
[2:55] controls and administrative oversight.
[2:58] Students and verified open-source
[3:00] maintainers get access at no cost. By
[3:03] early 2026,
[3:05] 78% of developers reported using some
[3:08] form of coding assistant, up from 30% 2
[3:11] years earlier, and Copilot captured the
[3:14] largest share of that adoption through
[3:15] its first mover advantage and the sheer
[3:18] number of editors it supports.
[3:20] Independent testing puts function level
[3:22] suggestion accuracy at 90%. GitHub's own
[3:25] internal study reported 55% faster task
[3:28] completion across developers using the
[3:30] tool with 46% of all code in those
[3:33] sessions written with assistance from
[3:35] the model. The pattern that emerges from
[3:38] user reports is consistent [music]
[3:40] for daily line by line coding, writing
[3:43] tests, generating standard database
[3:45] operations, completing function
[3:47] signatures, and reducing documentation
[3:49] lookups. Copilot accelerates the work
[3:52] developers already know how to do. It
[3:54] makes the routine faster. It removes the
[3:57] friction of remembering exact syntax,
[3:59] looking up method signatures, and
[4:01] writing the predictable parts of a
[4:02] function that follow from its name and
[4:04] parameters. [music] Where it struggles
[4:06] is with tasks that require understanding
[4:08] how multiple files relate to each other,
[4:10] how a change in one module ripples
[4:12] through the rest of the system, or why
[4:14] an architecture was designed the way it
[4:16] was. Agent mode is improving in this
[4:18] area, but it remains limited by the
[4:20] context available to it inside the
[4:22] editor window.
[4:24] Claude code is built by Anthropic and
[4:26] takes a fundamentally different
[4:28] approach. It is a terminal first tool.
[4:30] You open a command line session,
[4:32] describe what you want, and Claude code
[4:34] reads the relevant files across your
[4:36] repository before proposing anything.
[4:39] >> [music]
[4:39] >> The context window accepts 200,000
[4:41] tokens, which means small to medium
[4:44] projects, can be ingested in their
[4:45] entirety. The tool searches for
[4:47] dependencies, traces imports, identifies
[4:51] relationships between components, and
[4:53] then proposes coordinated changes across
[4:56] multiple files presented as diffs for
[4:58] you to review before anything is
[5:00] applied. The workflow is built around
[5:02] checkpoints and roll back. Every
[5:04] proposed change can be reviewed,
[5:06] accepted, or rejected individually. The
[5:09] tool interacts with version control
[5:12] directly, creating branches and commits
[5:14] as part of the process. If a set of
[5:16] changes causes a problem, you roll back
[5:18] to the checkpoint. The learning curve is
[5:21] steeper than installing an autocomplete
[5:23] plugin. You need to be comfortable with
[5:25] the terminal, with reviewing [music]
[5:27] diffs, and with describing problems
[5:29] clearly enough for the tool to reason
[5:30] about them. The design philosophy treats
[5:32] the developer as the decision maker and
[5:34] the tool as an assistant that has done
[5:36] extensive reading before offering an
[5:38] opinion. The average response time is 42
[5:41] milliseconds, [music] slightly slower
[5:43] than co-pilot because the analysis runs
[5:45] deeper before producing output.
[5:47] Independent testing from early 2026 puts
[5:51] accuracy at 92% on function level
[5:54] suggestions, two percentage points above
[5:56] co-pilot. But the meaningful advantage
[5:59] is not in individual function accuracy.
[6:01] It is in multi-file coordination.
[6:04] Refactoring an authentication system,
[6:06] converting a project from one framework
[6:08] pattern to another, or understanding a
[6:10] legacy codebase you have never seen
[6:12] before are the tasks where the deep
[6:14] context window changes the nature of the
[6:17] assistance. Developers joining new teams
[6:19] [music] report significant reductions in
[6:21] onboarding time because Claude code can
[6:23] explain not just what the code does, but
[6:25] why it was structured that way. It reads
[6:28] the project history, traces the design
[6:30] decisions, and presents the architecture
[6:32] as a coherent narrative rather than a
[6:34] collection of files. Claude Code does
[6:36] not just complete the line you are
[6:38] writing. It understands why the line
[6:40] exists in the context of the broader
[6:42] system. [music] The editor support is
[6:43] narrower. Native extensions exist for
[6:46] Visual Studio Code with support in
[6:48] Apple's development environment and
[6:50] limited integration with Jet Brains
[6:52] editors. [music] The terminal remains
[6:54] the primary interface. For developers
[6:56] who live in the command line and work
[6:58] through version control, scripting, and
[7:00] automation, that is natural. For
[7:03] developers who rarely leave their
[7:04] graphical editor, it requires a real
[7:06] workflow adjustment that not everyone
[7:08] will want to make. Both tools send code
[7:10] to cloud services during operation,
[7:12] which means both require trust that your
[7:14] source code is handled according to the
[7:16] provider's data policies. Copilot offers
[7:19] enterprise controls, including audit
[7:21] logs, and content filters for
[7:23] organizations that need governance.
[7:25] Claude code offers extensibility through
[7:27] the model context protocol which allows
[7:29] connecting external tools, databases,
[7:32] and company knowledge bases into the
[7:34] assistance context, making it adaptable
[7:36] for specialized workflows that go beyond
[7:39] code completion. The emerging pattern
[7:41] across developer teams is not a
[7:43] competition between these tools, but a
[7:45] division of labor. C-Pilot handles the
[7:47] 80% of daily work that is routine, fast,
[7:50] and patternbased. [music]
[7:52] Claude Code handles the 20% that
[7:54] requires thinking across the full scope
[7:55] of a project. [music] The developers
[7:58] reporting the highest efficiency gains
[7:59] are running both. Switching between them
[8:02] depending on whether the task demands
[8:03] speed or depth. One tool makes you type
[8:06] faster, the other makes you think less
[8:08] about where to look and more about what
[8:10] to build. They solve different problems
[8:12] and the assumption that you must choose
[8:14] one is itself the mistake most
[8:15] developers are making. [music] Every
[8:17] choice is a trade-off. At least now you
[8:20] know what you're trading.
