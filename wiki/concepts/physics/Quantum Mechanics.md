---
tags:
  - qm
  - mwi
  - bornrule
  - physics
type: concept
source: raw/notes/physics/Quantum Mechanics.md
author: user
---

#qm

**Summary:** The user's case against wavefunction collapse and for Everett. The central argument is empirical: in a double slit with polarisers, the interference pattern disappears with perpendicular polarisers and returns when a 45° polariser is added afterwards, so the photon's position was never physically collapsed at the polarisers. Also covers Schrödinger's cat by interpretation, Born-rule derivations, and short notes on spin, QFT and angular momentum.

**Evidence:** Mixed — the interpretation sections are the user's argument; the quoted material is primary papers (arXiv), one Reddit comment and several YouTube explainers. The Spin and QFT sections are unattributed pasted explainer text.

Related: [[Relativity]] · [[Block universe]] · [[Simulation hypothesis#Physics read as computational shortcuts]] · [[Consciousness]]

# Collapse

This is the biggest unresolved issue with QM. It's the main reason geniuses like Einstein and Schrödinger had issues with the Copenhagen interpretation.

You have various QM interpretations and they all suggest different answers.

- Copenhagen interpretation, doesn't define what a wavefunction collapse is or when it happens or why. This results in various issues like Schrödinger's cat, or that it suggests FTL wavefunction collapse. But nowadays many people don't take it as ontological (what is actually happening) but just epistemic (shut up and calculate). The wavefunction collapse has never been established and isn't even testable in theory.
- Objective collapse, there is a real physical interaction which collapses the wavefunction, like Penrose's theory around how if the gravity gets high enough it causes it to collapse. The nice thing about it is that it makes testable predictions, but so far all the experiments have failed and not many people expect it to pan out.
- Hidden variables, so you have the wavefunction acting deterministically, and a separate particle which is what you are actually observing when you do a measurement. It still requires non-locality and doesn't play nicely with special relativity.
- Everett (MWI), basically says you just have deterministic wavefunction evolution. What looks like collapse is essentially just decoherence. It's nice in that it's deterministic, local, no FTL activity, and is just based on the well evidenced QM postulates. Some think there might be an issue with how to derive the probabilities but others think it's mainly solved or a minor issue.

The three quotes below are the position the user is arguing against; the note doesn't say where they come from.

>In the double slit experiment, the wave function of the particle being studied isn't collapsed until the screen or a detector measures the particle

I think an interesting variant is where you put perpendicular polarisers across the slits, which means that you can detect which slit the photon went through, and the interference pattern disappears and many would say the wavefunction collapses going through one slit or the other. Many argue it's the physical interaction between the polariser and the photon which collapses its position. But if you put a 45 degree polariser between the slits and the screen, the interference pattern comes back. Which means the photon's position was never physically collapsed at the initial polarisers.

>Yet none of these "regular" interactions collapse the particle's wave function (they do cause decoherence, but decoherence doesn't cause wave function collapse)

Decoherence would look like collapse in whatever model you use. If it's impossible to tell the difference between collapse and decoherence it's a good question to ask if they really are different.

>Why is this? What makes the interaction with the detector or screen special?

I think that's a good reason to question some QM interpretations. So with Copenhagen measurement is special but it can't tell you why or what a measurement is.

With Everett, the interaction with the detector or screen is nothing special, it's just the standard wavefunction evolution.

Now do people really believe in a wavefunction collapse? One of the biggest problems has been around does a black hole destroy information. Now if people really believed in a wavefunction collapse which does destroy information, then it's perfectly possible for a black hole to destroy information and it's not really a big problem. But it seems like people are assuming that there is just unitary evolution and information isn't destroyed according to QM.

Now people often treat Copenhagen just as a method of doing calculations not what's really happening, which would then mean actually you could treat Copenhagen as the epistemic side of an ontological interpretation like Everett's, rather than them really being competing interpretations.

Say you have a double slit experiment but put polarisers perpendicularly aligned across the slits, then the interference pattern goes away. People often say it's the interaction between the photon and the polariser which collapses the wavefunction. But if the polarisers across a double slit are aligned you get the interference pattern. So you have the photon interacting with the polariser but no collapse.

Primary paper (arXiv) on the polariser double-slit analysis, supporting the point that only θ = π/2 makes the polarisers act as which-way detectors.

>Only if θ = π/2 do our pair of polarizers act as "which way" detectors. In this case slit "1" will only allow vertically polarized photons to pass through while slit "2" admits only horizontally polarized photons, so that no interference pattern emerges, as can be seen from eq. (7). For θ ≠ π/2, then a vertically polarized photon can in principle pass through either slit and an interference pattern results; superimposed on this interference pattern for vertically polarized photons is a diffraction pattern for horizontally polarized photons which only pass through one slit.
https://arxiv.org/pdf/1110.4309

Also the usual experiment people use is the quantum eraser experiment, where adding a polariser after the perpendicular polarisers brings back the interference pattern. But if the perpendicular polarisers collapsed the wavefunction it shouldn't be possible to bring it back.

# Schrödinger's cat

The answer depends on your interpretation of QM.

Copenhagen interpretation doesn't have an answer. The point in the thought experiment was to poke holes in the Copenhagen interpretation and it works. It's not clear what happens, since the Copenhagen interpretation never defines when or why a wavefunction collapses. The wavefunction collapse in the Copenhagen interpretation has never been established, it's not testable even in theory.

Objective collapse. This is where a physical interaction causes a real collapse. This is like Penrose's theory that when the gravity gets large enough it causes a wavefunction collapse. So there is actual physics around something that physically causes the wavefunction to collapse. This is nice in that it makes testable predictions, but so far every experiment has failed and people don't really expect it to pan out. I think the double slit polarizer experiments cause issues for this. If the polarizers are perpendicular the interference disappears, and it's often claimed the polarizer interacts with the photon physically causing a collapse. But if the polarizers are aligned you have the interference pattern so it's not the physical interaction with the polarizer which causes a collapse.

Superdeterminism, the cat is either alive or dead, never in a superposition.

Everett. Since there is no evidence for the wavefunction collapse postulate, it just drops that postulate. Basically everything obeys the same laws of physics, a cat or person isn't magical or different and doesn't have its own rules. So the cat becomes a superposition of half alive and half dead, but there is decoherence meaning the two parts don't interact. Then when a human views the cat they become a superposition as well of seeing half alive and half dead. It uses the foundation that most other interpretations have, but they add in an unproven postulate to get rid of the superposition state whereas this doesn't.

# MWI

#mwi

Primary paper (arXiv preprint) introducing a time-ordered analogue of the Local Friendliness theorem.

>Building on a recent result that developed these paradoxes into a no-go theorem, namely the _Local Friendliness Theorem_, we introduce the _Causal Friendliness Paradox_, a time-ordered analogue of it. In this framework, we replace the usual locality assumption with _Axiological Time Symmetry_ (ATS), and show that, when combined with the assumptions of _Absoluteness of Observed Events_ (AOE), _No Retrocausality_ (NRC), and _Screening via Pseudo Events_ (SPE), we obtain a causal inequality. We then show that quantum mechanics violates this inequality and is therefore incompatible with at least one of these assumptions.
https://arxiv.org/html/2510.26562v1

# Born rule

#bornrule

You can derive the Born rule, as being the only way probabilities work with certain assumptions (YouTube explainer).

https://www.youtube.com/watch?v=PZUZgOUOOIU

Gleason's theorem is often used in discussions of MWI as a route to the Born rule: it shows that, under noncontextuality and standard Hilbert-space assumptions, the only consistent probability assignments are given by the Born rule P = ⟨ψ|Π|ψ⟩.

Reddit comment (r/seancarroll) arguing the Born rule follows from normalising a complex-valued wavefunction; anecdote-quality source, kept for the argument not the authority.

>The standard approach OP is referencing can be found starting at p71 of Hugh Everett's thesis. Carroll/Sebens don't add that much to what Everett wrote, IMO, apart from emphasizing the interpretation of where the probabilities are coming from as arising from self-locating uncertainty, though I think arguably this was implicit in Everett's thesis. Mathematically, there is no question about the Born rule being the only one that is possible. This is what Everett showed in the above link, and what Gleason and others proved around the same time.
>The real question that remains, that I think OP is gesturing at, is not whether _mathematically_ the rule must be Born, but intuitively and conceptually, why the wave function amplitude _is not itself the thing we should count_ when we measure the "volume of branches."…
>The heart of that maneuver is the assumption that the wave function must be unambiguously normalized, and the fact that our wave function is complex valued. The only way of normalizing a complex wave function is through the standard Euclidean norm. That is where the Born rule ultimately comes from: if we start with a wave function of the form A|x> + B|y>, the Born rule is already snuck in through the normalization…
>This all boils down to the question "what it is like to live as an observer who is complex-valued"; the only way to "count" complex-valued observers' "weightiness" (i.e. a scalar) is to measure some scalar value of them, and the only way to do that is through the absolute value, the Euclidean norm.
https://www.reddit.com/r/seancarroll/comments/1r1j980/comment/o4qrkpv/

Everett's own derivation is at p71 of his thesis: https://cqi.inf.usi.ch/qic/everett_phd.pdf

Primary paper (arXiv) claiming inter-branch communication is possible within standard quantum theory.

>It is commonly thought that observers in distinct branches of an Everettian multiverse cannot communicate without violating the linearity of quantum theory. Here we show a counterexample, demonstrating that inter-branch communication is in fact possible, entirely within standard quantum theory. We do this by considering a Wigner's-friend scenario, where an observer (Wigner) can have quantum control over another observer (the friend). We present a thought experiment where the friend in superposition can receive a message written by a distinct copy of themselves in the multiverse, with the aid of Wigner. To maintain the unitarity of quantum theory, the observers must have no memory of the message that they sent. Our thought experiment challenges conventional wisdom regarding the ultimate limits of what is possible in an Everettian multiverse. It has a surprising potential application which involves using knowledge-creation paradoxes for testing Everettian quantum theory against single-world theories.
https://arxiv.org/abs/2601.08102

Sebens & Carroll's self-locating uncertainty derivation (primary paper).

>We provide a derivation of the Born Rule in the context of the Everett (Many-Worlds) approach to quantum mechanics. Our argument is based on the idea of self-locating uncertainty: in the period between the wave function branching via decoherence and an observer registering the outcome of the measurement, that observer can know the state of the universe precisely without knowing which branch they are on. We show that there is a uniquely rational way to apportion credence in such cases, which leads directly to the Born Rule. Our analysis generalizes straightforwardly to cases of combined classical and quantum self-locating uncertainty, as in the cosmological multiverse.
>https://arxiv.org/abs/1405.7907

## Solo: Looking Quantum Mechanics in the Eyeball | Mindscape 355

https://www.youtube.com/watch?v=b-d-5z3CUxQ

Like in relativity coordinates are arbitrary and not reality. Similarly in QM position and momentum are just useful coordinates, what is real is the wavefunction.

# Basics

Unitary operators are rotations, so ⟨Uo|Uw⟩ = ⟨o|w⟩, they preserve probabilities. U hermitian = U inverse.

# Angular momentum

YouTube explainer.

>This Simple Wave Explains Quantum Mechanics
https://www.youtube.com/watch?v=pJvV7MI-LyY

Electrons have angular momentum when rotating in an atom.

The static picture is due to rotations cancelling out.

## Schrodinger equation

YouTube explainer on why the Schrödinger equation contains i.

https://www.youtube.com/watch?v=3QU-_PSbKlo

# QFT

Unverified: pasted explainer text, no source given in the note.

## Where is the Hilbert space?

A quantum field is an operator attached to every spacetime point, and particles are quantized excitations of those fields. The Hilbert space contains all possible excitation states of the fields.

The Hilbert space still exists. In fact QFT is often defined as:

1. A Hilbert space H
2. A collection of field operators φ̂(x)
3. Rules relating them (commutation relations, dynamics, symmetries)

The fields act on the Hilbert space, so schematically φ̂(x): H → H for every spacetime point x.

# Spin

Unverified: pasted explainer text, no source given beyond the two links below. The original note's equations were mangled by duplicated rendering; they are written out plainly here.

>**Spin is not classical spinning, but it is a real rotational property of the quantum wavefunction.**

More precisely, the electron's wavefunction has two parts, Ψ(r) = ψ(r) χ, where ψ(r) describes spatial dependence and χ is a two-component spinor. A physical rotation acts on both: Ψ → e^(−iθ·L/ℏ) e^(−iθ·S/ℏ) Ψ.

The orbital operator L rotates the spatial wave pattern. The spin operator S rotates the spinor part. Thus spin is not an arbitrary extra label glued onto the electron; it is part of how the complete wavefunction represents rotations.

For a z-rotation, the spin transformation is e^(−iθSz/ℏ). For spin up and down, |+⟩ → e^(−iθ/2)|+⟩ and |−⟩ → e^(+iθ/2)|−⟩.

For a superposition, these opposite phase changes alter the relative phase and therefore rotate the measurable spin direction. This is a genuine quantum-mechanical analogue of rotation, not merely an analogy. The expectation values ⟨Sx⟩, ⟨Sy⟩, ⟨Sz⟩ transform like a rotating vector.

https://sciold.ui.ac.ir/~sjalali/MSc.Students/Avanced_Quantum_Mechanics/AQM3_2.pdf

The key distinction is between **where** the rotation occurs:

- Orbital angular momentum rotates the wavefunction over ordinary space.
- Spin angular momentum rotates the wavefunction in its internal two-component spinor space.

The latter is sometimes called an "internal" or "non-geometrical" space, but it is still tied fundamentally to the physical rotation group. In relativistic quantum theory, spin-1/2 is a consequence of the way the electron's field transforms under spacetime rotations and Lorentz transformations.

So your conceptual picture is essentially right:

>**Spin is an intrinsic rotational structure of the quantum state, expressed through the phase and transformation of its spinor components, rather than through the mechanical rotation of an extended object.**

That is also why a 2π rotation produces the distinctive spinor phase change Ψ → −Ψ, while a 4π rotation restores the state exactly.

# TODO

- The three unattributed quotes in [[#Collapse]] look like they come from one article the user was replying to; find it so the counterargument has a target.
- The Spin and QFT sections read as LLM output pasted in ("So your conceptual picture is essentially right"). Either replace with a cited textbook treatment or keep them clearly marked as an explainer.
- The inter-branch communication preprint (arXiv 2601.08102) is very recent and unreviewed; check whether it survived scrutiny.
- Superdeterminism is listed for the cat but not in the collapse interpretation list; make the two lists consistent.
