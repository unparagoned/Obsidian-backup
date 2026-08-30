---
description: Ingest any new files in raw/inbox into the wiki, then commit on main
---

# Inbox ingest run

## 1. Find what is un-ingested

- List the files in `/Users/unparagoned/Obsidian/raw/inbox/`.
- For each one, search `wiki/log.md` for its filename. Files are never moved out of the inbox after ingest, so the log is the ledger: a filename that appears there is already done. Skip it.
- **If nothing is new, stop immediately.** Reply "Nothing new in the inbox" and make no edits and no commits. Do not tidy, do not run a maintenance pass, do not do unrelated work. An empty run is the correct outcome most of the time.

## 2. Let a new file settle

Check each new file's modification time. If it was modified less than 2 minutes ago it may still be being written, so skip it — the next run will pick it up. Do not sit and wait for it.

## 3. Ingest

Follow the ingest workflow in `/Users/unparagoned/Obsidian/AGENTS.md` exactly, and write in the style that file specifies.

## 4. Commit on main

Stay on `main`. Stage **only** the wiki files this ingest created or changed, naming each path explicitly. Do not use `git add -A` or `git add .` — the vault carries unrelated working changes, untracked scratch directories and `.DS_Store` files that must not go into this commit.

Commit as: `ingest: <source name>`

Never push. Never merge. Never switch or create branches. If git does anything unexpected — a conflict, a detached HEAD, a rejected commit — stop, leave the working tree as you found it, and report it rather than trying to fix it.

## 5. Report

Finish with a short report: which files you ingested, which pages you created or changed, and **anything that needs a human** — claims you could not verify, sources that contradicted each other, links that failed to fetch, corrections you made to the source's own framing, and anything you left out.

Be direct about what you could not confirm. An ingest that flags three uncertainties is more useful than one that reads as finished but is not.

If no new files are present, confirm briefly and take no action.
