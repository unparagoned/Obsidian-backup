---
tags:
  - systems
  - reference
type: reference
source: raw/notes/systems/VLC.md
author: user
---

**Summary:** Fix for VLC not opening: delete its preference files.

Related: [[Mac]] · [[TV]]

# Bugs

## Doesn't open properly

Remove preference files 

```
rm -rf ~/Library/Application\ Support/org.videolan.vlc
rm -rf ~/Library/Preferences/org.videolan.vlc

```

# TODO

- Only one bug recorded.
