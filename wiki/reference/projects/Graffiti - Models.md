---
tags:
  - project
  - graffiti
  - LLM
type: reference
source: raw/notes/graffiti/Models.md
author: user
---

**Summary:** One note on the Graffiti project's model choice: using the GPT-5 search API instead of building search directly, held up by chunked errors.

Related: [[Compare LLM]] · [[AI tools and learning sources]] · [[Stech Analytics - SSL and DNS]]

gpt-5-search-api — search might be a good thing rather than rolling it all myself. But might need some tech changes to get it to work. Getting chunked errors.

# TODO

- The "chunked errors" aren't described; record the actual error before choosing.
- The Stech Analytics box restarts `graffiti_api.service`, so the two projects share infrastructure — worth one page explaining how.
