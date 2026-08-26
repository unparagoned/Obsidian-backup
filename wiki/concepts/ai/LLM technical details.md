---
tags:
  - LLM
  - attention
  - ai
type: concept
source: raw/notes/coding-ai/LLM technical details.md
author: user
---

**Summary:** Mechanism notes: how attention computes query/key/value interactions, why multi-head and layers matter, sinusoidal position encoding, and what RL post-training changes.

Related: [[LLM - how they work]] · [[llm-wiki]] · [[AI tools and learning sources#Notebooks]]

# Attention

A word will have a query vector which asks stuff like what adjectives are before me.

Words will have key vectors which say what they are, like "I'm an adjective".

You take the dot product between the keys and query vectors, giving you an attention pattern, so what words relate to others.

Then you multiply the value matrix against previous word embeddings, so you then add the value vectors to the original vectors.

Use multi-head, so you can do it in parallel, with lots of different ways and vectors. Having one massive matrix wouldn't be efficient, and you can't do it in parallel.

There are various layers, so in the first layer "hoodie" just attends to "red", but in layer 2 the updated "hoodie" attends to the updated "red".

Position uses lots of sine waves, so it knows if it's every two tokens or every token, etc.

# Reinforcement learning

Reinforcement learning still uses back propagation, but the signal is from trying different answers (from the output distribution) and rewarding ones that are good.

# TODO

- No source is recorded; this reads as notes from 3Blue1Brown's transformer series. Add the link.
- Sinusoidal position encoding is one option among several (RoPE, ALiBi, learned); note what current models actually use.
