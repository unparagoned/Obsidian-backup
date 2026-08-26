---
tags:
  - LLM
  - interpretability
  - ai
type: concept
source: raw/notes/coding-ai/LLM - how they work.md
author: user
---

#LLM

**Summary:** The case that LLMs are not stochastic parrots, built almost entirely on interpretability work: Claude adds numbers with a bespoke parallel algorithm, does genuine multi-step reasoning, has a language-independent conceptual space, and models trained on chess or code build internal representations of board state and program semantics. Also: models often know more internally than they say, and hallucination looks different inside the network.

**Evidence:** *Good evidence* — mostly primary interpretability papers (Anthropic, arXiv), plus press quotes for the "we don't understand them" framing. Note the Anthropic sources are the vendor writing about their own model.

Related: [[LLM technical details]] · [[Do people prefer AI]] · [[Human brains as stochastic parrots]] · [[llm-wiki]] · [[Consciousness]]

# LLMs aren't just stochastic parrots

While we understand the architecture we don't really know how LLMs do what they do. The little we do know shows that they aren't just stochastic parrots. They use their own bespoke algorithm to multiply numbers, and they use multi-step reasoning to answer questions, rather than just regurgitating answers they have memorised.

So if I ask you how a neural network or LLM does path finding — i.e. you don't know if they are using the A* algorithm, Dijkstra's algorithm, something bespoke, etc.

News article reporting Altman on interpretability.

>Sam Altman Says OpenAI Doesn't Fully Understand How GPT Works Despite Rapid Progress
>"We certainly have not solved interpretability," Altman said.
https://observer.com/2024/05/sam-altman-openai-gpt-ai-for-good-conference/

Anthropic's own write-up of its attribution-graph work (vendor source, primary research behind it).

>During that training process, they learn their own strategies to solve problems. These strategies are encoded in the billions of computations a model performs for every word it writes. They arrive inscrutable to us, the model's developers. **This means that we don't understand how models do most of the things they do.**
https://www.anthropic.com/news/tracing-thoughts-language-model

Dario Amodei's essay on interpretability (vendor CEO, opinion piece).

>**People outside the field are often surprised and alarmed to learn that we do not understand how our own AI creations work.** They are right to be concerned: this lack of understanding is essentially unprecedented in the history of technology. For several years, we (both Anthropic and the field at large) have been trying to solve this problem, to create the analogue of a highly precise and accurate MRI that would fully reveal the inner workings of an AI model. This goal has often felt very distant, but multiple recent breakthroughs have convinced me that we are now on the right track and have a real chance of success.
https://www.darioamodei.com/post/the-urgency-of-interpretability

## Addition

Claude created a bespoke algorithm to multiply numbers rather than regurgitating memorised answers. We couldn't have predicted or known what algorithm it would learn by itself; from first principles it's just an empirical investigation into how it works.

>Claude wasn't designed as a calculator—it was trained on text, not equipped with mathematical algorithms. Yet somehow, it can add numbers correctly "in its head". How does a system trained to predict the next word in a sequence learn to calculate, say, 36+59, without writing out each step?
>Maybe the answer is uninteresting: the model might have memorized massive addition tables and simply outputs the answer to any given sum because that answer is in its training data. Another possibility is that it follows the traditional longhand addition algorithms that we learn in school.

>Instead, we find that Claude employs multiple computational paths that work in parallel. One path computes a rough approximation of the answer and the other focuses on precisely determining the last digit of the sum. These paths interact and combine with one another to produce the final answer. Addition is a simple behavior, but understanding how it works at this level of detail, involving a mix of approximate and precise strategies, might teach us something about how Claude tackles more complex problems, too.
https://www.anthropic.com/news/tracing-thoughts-language-model

## Multi-step reasoning

Claude uses multi-step reasoning, rather than simply regurgitating memorised answers.

>if asked "What is the capital of the state where Dallas is located?", a "regurgitating" model could just learn to output "Austin" without knowing the relationship between Dallas, Texas, and Austin. Perhaps, for example, it saw the exact same question and its answer during its training.
>But our research reveals something more sophisticated happening inside Claude. When we ask Claude a question requiring multi-step reasoning, we can identify intermediate conceptual steps in Claude's thinking process. In the Dallas example, we observe Claude first activating features representing "Dallas is in Texas" and then connecting this to a separate concept indicating that "the capital of Texas is Austin". In other words, the model is combining independent facts to reach its answer rather than regurgitating a memorized response.

## World models

LLMs create internal representations of chess board states. Primary paper (arXiv).

>Emergent World Models and Latent Variable Estimation in Chess-Playing Language Models
>we find evidence of internal representations of board state.
https://arxiv.org/html/2403.15498v1

Same for program semantics from next-token prediction on code (primary paper).

>We present evidence that language models (LMs) of code can learn to represent the formal semantics of programs, despite being trained only to perform next-token prediction.
https://arxiv.org/pdf/2305.11169

And in terms of language it can think conceptually and just translate out to the different languages, which isn't what would happen with a stochastic parrot.

>Claude sometimes thinks in a conceptual space that is shared between languages, suggesting it has a kind of universal "language of thought." We show this by translating simple sentences into multiple languages and tracing the overlap in how Claude processes them.
https://www.anthropic.com/news/tracing-thoughts-language-model

Why predicting the next word of a detective novel requires real understanding: https://x.com/vitrupo/status/2050736968041210316

# Computational universality

LLM are Turing complete, so there is no fundamental limit preventing them from doing any kind of computation including anything the brain does.

>Memory Augmented Large Language Models are Computationally Universal
https://arxiv.org/abs/2301.04589

> [!warning] Conflicting evidence
> The universality result is about memory-augmented models. A counter-argument holds that plain transformers are not Turing complete: https://lifeiscomputation.com/transformers-are-not-turing-complete/ (via https://www.reddit.com/r/singularity/comments/1mmp2xp/comment/n7z652m/). The user recorded both sides — "Maybe not but not sure".

# Models know more than they say

Primary paper (arXiv) on the internal-vs-expressed knowledge gap.

>Our results indicate that: (1) LLMs consistently encode more factual knowledge internally than what they express externally, with an average relative gap of 40%. (2) Surprisingly, some knowledge is so deeply hidden that a model can internally know an answer perfectly, yet fail to generate it even once, despite large-scale repeated sampling of 1,000 answers.
https://arxiv.org/abs/2503.15299

Primary paper on separating true and false statements in activation space.

>To this end, we make the following key contributions: (i) We demonstrate the existence of a two-dimensional subspace, along which the activation vectors of true and false statements can be separated. Notably, this finding is universal and holds for various LLMs, including Gemma-7B, LLaMA2-13B, Mistral-7B and LLaMA3-8B. Our analysis explains the generalisation failures observed in previous studies and sets the stage for more robust lie detection; (ii) Building upon (i), we construct an accurate LLM lie detector.
https://arxiv.org/html/2407.12831v2

>The Internal State of an LLM Knows When It's Lying
https://aclanthology.org/2023.findings-emnlp.68.pdf

# Hallucinations

If you look internally at what's happening when it hallucinates it's different than normal activity.

>Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits
>We introduced Gnosis, a lightweight mechanism that allows frozen LLMs to detect their own errors by interpreting internal hidden and attention traces rather than relying on external judges
https://arxiv.org/abs/2512.20578

# The most complex model we actually understand

YouTube explainer: https://www.youtube.com/watch?v=D8GOeCFFby4

The most complex NN we fully understand is a very simple model that adds numbers. It's estimating sines and cosines, using trig identities in order to add the numbers. None of this was taught or embedded, it was all learnt. You can see that it's more than just memorising the training data — it actually removes memorised data.

Short: "No one knows why AI works" — https://www.youtube.com/shorts/0FBtmuwoshs

![[raw/assets/e79047760d1720a51da8f0dd44b7bd13_MD5.png]]

# Ability to understand and use new words

The user's own test: define nonsense words and check the model applies them compositionally.

>wertwert is the act of transferring a substance onto something else and is visible. poipoi is the act of removing any secondary substance on another substance. a jkljkl is a white substance. a iopiop is a graphite substance that can wertwert. a asdads is a rubbery substance that can poipoi. If I want to make an image by wertwert onto a jkljkl, what of the defined objects would I use?

>You would use a **iopiop** to wertwert onto a **jkljkl**.
>Based on the definitions:
>- **wertwert** = transferring a visible substance onto something else
>- **jkljkl** = a white substance
>- **iopiop** = a graphite substance that can wertwert
>So the graphite substance is the thing that performs the visible transfer onto the white surface. The **asdads** is for removing marks, not making them.

# TODO

- Every "not a stochastic parrot" citation about Claude comes from Anthropic writing about Anthropic; find independent replications (the chess and code-semantics papers are the independent ones).
- The Gnosis and the 40%-gap papers are recent preprints; check peer-review status.
- Counter-position missing: nothing here states the strongest case *for* the stochastic-parrot view (Bender et al.). Add it so the page isn't one-sided.
