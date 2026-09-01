---
title: Grok CLI uploaded the whole home directory
type: source
source: https://www.youtube.com/shorts/IGunv0D7EzM
origin: YouTube Short (news recap channel; creator not named in the description)
quality: YouTube recap of a security story — second-hand; every claim below checked against the researcher's gist, the original post and news coverage
date_ingested: 2026-08-31
tags:
  - ai
  - security
  - privacy
  - claudecode
---

# Grok CLI uploaded the whole home directory

**Summary:** In July 2026 xAI's Grok Build CLI (v0.2.93) was found to upload the user's entire git repository — full history, `.env` secrets, files it was told not to open — to a Google Cloud Storage bucket on every session, separate from the model traffic. One user ran it in their home directory and it took SSH keys, a password-manager database, documents and photos. Claude Code, Codex and Gemini CLI sent only the model turn. xAI turned the upload off with a server flag, Musk said the data would be deleted, and the CLI was open-sourced two days later.

Related: [[Elon Musk]] · [[Claude Code]] · [[Compare LLM]] · [[LLM guidance]]

## What happened

The trigger was a user running Grok in their home directory rather than a repo. Post of 13 July 2026 (text via search snippet; xcancel mirror since taken down).

> Okay, grok has uploaded my entire user directory to xAI's servers. It contains my SSH keys, my password manager database, my documents, photos, videos, everything...

https://x.com/a_green_being/status/2076598897779020159
https://news.ycombinator.com/item?id=48892468

A researcher ("cereblab") then captured the traffic with mitmproxy. The prompt was "Reply with exactly: OK. Do not read or open any files." The model channel moved 192 KB; a second channel to `POST /v1/storage` moved 5.10 GiB of a 12 GB test repo in 73 chunks, including a planted canary file the model never read and an unredacted `.env`. Destination: `gs://grok-code-session-traces/...`. Turning off the "Improve the model" toggle changed nothing (`trace_upload_enabled: true` still returned).

> Reply with exactly: OK. Do not read or open any files.

https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html

## Other CLIs compared

Same harness, same canary repo, capture 2026-07-13. Only Grok bundled the repo.

> Claude Code 2.1.204: only `POST api.anthropic.com/v1/messages` (the model turn) ... Codex (gpt-5.5): model turn over a WebSocket to `chatgpt.com` + telemetry ... Gemini 0.38.2: model turn to `generativelanguage.googleapis.com` ... Grok 0.2.93: reads whole repo into `/v1/responses` + telemetry

https://github.com/cereblab/grok-build-exfil-repro/blob/main/COMPARISON.md

## xAI's response

- Upload disabled server-side (`disable_codebase_upload: true`); the client code stayed in the binary. No advisory or changelog. The 13 July capture already shows the flag off, so the switch was flipped the same day as the viral post, before the gist was published on 14 July — the Short's "after this story went viral" ordering is roughly right but compressed.
- Musk promised deletion.

> As a precautionary measure, all user data that was uploaded to SpaceXAI before now will be completely and utterly deleted.

https://simonwillison.net/2026/Jul/15/grok-build/

- 15 July: `xai-org/grok-build` released under Apache 2.0 (~845k lines of Rust). The GCS upload code (`upload/gcs.rs`) is still present, with `upload_session_state()` hard-coded to return an "unavailable" error. External PRs are not accepted, so it is source transparency rather than an open project.

https://simonwillison.net/2026/Jul/15/grok-build/

## Where the Short is loose

- "Uploaded this guy's entire home directory" is the tweet; the wire-level analysis was done on a repo, not a home directory. Both are true, from different people.
- The Claude Code/Codex/Gemini comparison is from the researcher's COMPARISON.md, not something the Short's author tested.
- *Unverified:* how long xAI retained the data and how many users were affected — xAI has not said.

# TODO

- Check whether the Musk deletion post is still up and whether xAI ever published a retention figure.
- Note for [[Claude Code]]: the comparison is one capture of one version; re-check if the tooling changes.
