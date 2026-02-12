---
description: List recent videos from a YouTube channel and extract each one.
argument-hint: [channel-handle] [count]
---

Load the `yt-processing` skill.

Parse `$ARGUMENTS`: first argument is the channel (handle like `@Name`, URL, or bare name), second argument is an optional video count (default: 5).

## Step 1: Get channel video list

Use the skill's channel listing to fetch the specified number of videos for the given channel. Present the list to the user.

## Step 2: Prepare channel folder

Derive a lowercase kebab-case channel name from the channel listing output (e.g., `nick-chapsas`). The output directory for all extractions is `sources/youtube/<channel-name>`.

## Step 3: Extract each video

For each video in the list, use the Task tool to invoke `/yt-extract <video-url> sources/youtube/<channel-name>` as a sub-agent. Pass the channel folder as the second argument so each video is extracted into the channel subfolder.

Process videos one by one, sequentially.
