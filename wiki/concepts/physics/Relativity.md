---
tags:
  - relativity
  - blockuniverse
  - blackholes
  - physics
type: concept
source: raw/notes/physics/Relativity.md
author: user
---

**Summary:** Notes from physics YouTube channels: time dilation as path length in hyperbolic spacetime geometry rather than time "slowing"; relativity of simultaneity as the argument for eternalism; two black-hole puzzles; and Dialect's derivation of length contraction directly from Maxwell's equations, which the user checked and found sound.

**Evidence:** Mixed source quality — mostly YouTube explainers, plus two arXiv papers for the length-contraction section.

Related: [[Block universe]] · [[Time Travel]] · [[Quantum Mechanics]] · [[Anthropic principle]] · [[Free will]]

# I was so wrong about time dilation (My mind is blown)

https://www.youtube.com/watch?v=F_eVrN8Z8gM

Time doesn't slow down. It's just how things are measured.

Straight paths are the longest path between two events due to hyperbolic geometry (t² − x²). And faster speeds are shorter paths, so they experience less time.

So if you were travelling close to c for interstellar travel, you are covering less distance in spacetime meaning you can get there faster, compared to someone travelling slower who takes the long path.

# Eternalism and Block Universe

#blockuniverse

In relativity, there is no objective, universal "now". What one observer considers "now" can correspond to another observer's past or future. All observers' views are equally valid, which means past, present and future can all coexist. Which suggests a block universe.

Fuller treatment in [[Block universe]].

# Black holes

## What Really Happens If You Fall Into an Evaporating Black Hole?

https://www.youtube.com/watch?v=kRIDi-no1BI

Maybe you can't ever fall into a black hole since it will evaporate before you cross the event horizon.

## The most misunderstood idea about black holes! (I finally get it)

https://www.youtube.com/watch?v=lZrW5cGl1fU

- When falling into a black hole, he doesn't see all the future of the world
- From outside you do see someone freeze and never enter.

# Dialect: length contraction from Maxwell's equations

Length contraction can be explained directly from Maxwell's equations.

https://www.youtube.com/watch?v=xfjBhQ2lF4I

Let β = v/c and γ = 1/√(1 − β²).

The video uses the Maxwell/Heaviside field of a uniformly moving charge. This field is weakened longitudinally and strengthened transversely. That result is standard electromagnetism, not speculative; it follows from Maxwell's retarded potentials. Feynman explains the relevant field equations here: https://www.feynmanlectures.caltech.edu/II_21.html

For the charge configuration used in the cited calculation, force equilibrium gives d/b² = b(1 − β²)^(3/2)/d², where b is the longitudinal dimension and d the transverse dimension. Rearranging, d³(1 − β²)^(3/2) = b³, so b = d√(1 − β²) = d/γ.

That is exactly Lorentz contraction. At v = 0.8c, for example, √(1 − 0.8²) = 0.6, so the longitudinal dimension becomes 0.6 of the original. **No algebraic trick or obvious maths error there.** The detailed published version reaches the same result and shows it is a necessary and sufficient equilibrium condition for its five-charge model: Redžić's calculation, https://arxiv.org/pdf/1501.05899

## What is genuinely right

The video correctly demonstrates this:

>If a system is held in equilibrium by Lorentz-covariant electromagnetic interactions, changing its state of motion can alter its lab-frame equilibrium configuration by the Lorentz factor.

That is a valid physical insight. When you actually accelerate a rod, internal forces and stresses must rearrange its constituents. Relativity's rods are not abstract magic sticks; their material dynamics must be consistent with Lorentz symmetry.

This is a recognised approach, associated particularly with Lorentz, FitzGerald and John Bell. It has appeared in academic literature, including:

- Miller, "A constructive approach to the special theory of relativity" — https://arxiv.org/abs/0907.0902
- Redžić, "Direct calculation of length contraction and clock retardation" — https://arxiv.org/abs/1501.05899
- A detailed 2025 treatment of Bell's dynamical route — https://arxiv.org/html/2506.23450v1

# TODO

- The Dialect section is partly a checked-through analysis (voice suggests an LLM assist); the equilibrium equation was mangled in the original and has been rewritten inline — verify against Redžić before relying on it.
- The two black-hole videos state opposite-sounding things about what an infalling observer sees; reconcile or note which frame each is describing.
