#LLM

# LLMs aren't just stochastic parrots

While we understand the architecture we don't really know how LLMs do what they do. The little we do know shows that they aren't just stochastic parrots. They use their own bespoke algorithm to multiply numbers, and they use multi-step reasoning to answer questions, rather than just regurgitating answers they have memorised.  

So if I ask you how a neural network or LLM does path finding - i.e. you don't know if they are using the A* algorithm, Dijkstra's algorithm, something bespoke, etc. 

>Sam Altman Says OpenAI Doesn’t Fully Understand How GPT Works Despite Rapid Progress
“We certainly have not solved interpretability,” Altman said.
[https://observer.com/2024/05/sam-altman-openai-gpt-ai-for-good-conference/](https://observer.com/2024/05/sam-altman-openai-gpt-ai-for-good-conference/)

>During that training process, they learn their own strategies to solve problems. These strategies are encoded in the billions of computations a model performs for every word it writes. They arrive inscrutable to us, the model’s developers. **This means that we don’t understand how models do most of the things they do.**
[https://www.anthropic.com/news/tracing-thoughts-language-model](https://www.anthropic.com/news/tracing-thoughts-language-model)

>**People outside the field are often surprised and alarmed to learn that we do not understand how our own AI creations work.**  They are right to be concerned: this lack of understanding is essentially unprecedented in the history of technology.  For several years, we (both Anthropic and the field at large) have been trying to solve this problem, to create the analogue of a highly precise and accurate MRI that would fully reveal the inner workings of an AI model.  This goal has often felt very distant, but multiple [recent](https://www.anthropic.com/research/auditing-hidden-objectives) [breakthroughs](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) have convinced me that we are now on the right track and have a real chance of success.
[https://www.darioamodei.com/post/the-urgency-of-interpretability](https://www.darioamodei.com/post/the-urgency-of-interpretability)

Claude created a bespoke algorithm to multiply numbers rather than regurgitating memorised answers. We couldn't have predicted or known what algorithm it would learn by itself from first principles it's just an empirical investigation into how it works. 

>Claude wasn't designed as a calculator—it was trained on text, not equipped with mathematical algorithms. Yet somehow, it can add numbers correctly "in its head". How does a system trained to predict the next word in a sequence learn to calculate, say, 36+59, without writing out each step?
>
>Maybe the answer is uninteresting: the model might have memorized massive addition tables and simply outputs the answer to any given sum because that answer is in its training data. Another possibility is that it follows the traditional longhand addition algorithms that we learn in school.
>
>Instead, we find that Claude employs multiple computational paths that work in parallel. One path computes a rough approximation of the answer and the other focuses on precisely determining the last digit of the sum. These paths interact and combine with one another to produce the final answer. Addition is a simple behavior, but understanding how it works at this level of detail, involving a mix of approximate and precise strategies, might teach us something about how Claude tackles more complex problems, too.
[https://www.anthropic.com/news/tracing-thoughts-language-model](https://www.anthropic.com/news/tracing-thoughts-language-model)

Claude uses multi-step reasoning, rather than simply regurgitating memorising answers.

>if asked "What is the capital of the state where Dallas is located?", a "regurgitating" model could just learn to output "Austin" without knowing the relationship between Dallas, Texas, and Austin. Perhaps, for example, it saw the exact same question and its answer during its training.
>
But our research reveals something more sophisticated happening inside Claude. When we ask Claude a question requiring multi-step reasoning, we can identify intermediate conceptual steps in Claude's thinking process. In the Dallas example, we observe Claude first activating features representing "Dallas is in Texas" and then connecting this to a separate concept indicating that “the capital of Texas is Austin”. In other words, the model is combining independent facts to reach its answer rather than regurgitating a memorized response.
[https://www.anthropic.com/news/tracing-thoughts-language-model](https://www.anthropic.com/news/tracing-thoughts-language-model)

LLMs, create internal representations of chess board states. 

>Emergent World Models and Latent Variable Estimation in Chess-Playing Language Models
> we find evidence of internal representations of board state.
[https://arxiv.org/html/2403.15498v1](https://arxiv.org/html/2403.15498v1)

And in terms of language it can think conceptually and just translate out to the different languages, which isn't what would happen with a stochastic parrot. 

>Claude sometimes thinks in a conceptual space that is shared between languages, suggesting it has a kind of universal “language of thought.” We show this by translating simple sentences into multiple languages and tracing the overlap in how Claude processes them.
https://www.anthropic.com/news/tracing-thoughts-language-model

Why predicting the next word of a detective Novel, requires real understanding.
https://x.com/vitrupo/status/2050736968041210316



LLM are Turing complete, so there is no fundamental limit preventing them from doing any kind of computation including anything the brain does.

>Memory Augmented Large Language Models are Computationally Universal
[https://arxiv.org/abs/2301.04589](https://arxiv.org/abs/2301.04589)

Maybe not but not sure

[https://lifeiscomputation.com/transformers-are-not-turing-complete/](https://lifeiscomputation.com/transformers-are-not-turing-complete/)
From <[https://www.reddit.com/r/singularity/comments/1mmp2xp/comment/n7z652m/](https://www.reddit.com/r/singularity/comments/1mmp2xp/comment/n7z652m/)>

>Our results indicate that: (1) LLMs consistently encode more factual knowledge internally than what they express externally, with an average relative gap of 40%. (2) Surprisingly, some knowledge is so deeply hidden that a model can internally know an answer perfectly, yet fail to generate it even once, despite large-scale repeated sampling of 1,000 answers.
https://arxiv.org/abs/2503.15299

>To this end, we make the following key contributions: (i) We demonstrate the existence of a two-dimensional subspace, along which the activation vectors of true and false statements can be separated. Notably, this finding is universal and holds for various LLMs, including Gemma-7B, LLaMA2-13B, Mistral-7B and LLaMA3-8B. Our analysis explains the generalisation failures observed in previous studies and sets the stage for more robust lie detection; (ii) Building upon (i), we construct an accurate LLM lie detector. 
https://arxiv.org/html/2407.12831v2

>The Internal State of an LLM Knows When It’s Lying
[https://aclanthology.org/2023.findings-emnlp.68.pdf](https://aclanthology.org/2023.findings-emnlp.68.pdf)


>We present evidence that language models (LMs) of code can learn to represent the formal semantics of programs, despite being trained only to perform next-token prediction.
[Emergent Representations of Program Semantics in Language Models Trained on Programs](https://arxiv.org/pdf/2305.11169)



[No one knows why AI works  😅](https://www.youtube.com/shorts/0FBtmuwoshs)

![[raw/assets/e79047760d1720a51da8f0dd44b7bd13_MD5.png]]


# The most complex model we actually understand
https://www.youtube.com/watch?v=D8GOeCFFby4

The most complex NN we fully understand is a very simple model that adds numbers. It's estimating sins and cosins, using trig identities in order to add the numbers. None of this was taught or embedded, it was all learnt. You can see that it's more than just memorising the training data, it actually removes memorised data.

# Hallucinations

If you look internally at what's happening when it hallucinates it's different than normal activity.

>Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits
>We introduced Gnosis, a lightweight mechanism that allows frozen LLMs to detect their own errors by interpreting internal hidden and attention traces rather than relying on external judges
>https://arxiv.org/abs/2512.20578


# Ability to use understand and use new words

>>wertwert is the act of transferring a substance onto something else and is visible. poipoi is the act of removing any secondary substance on another substance. a jkljkl is a white substance. a iopiop is a graphite substance that can wertwert. a asdads is a rubbery substance that can poipoi. If I want to make an image by wertwert onto a jkljkl, what of the defined objects would I use?

>You would use a **iopiop** to wertwert onto a **jkljkl**.
Based on the definitions:
>- **wertwert** = transferring a visible substance onto something else
>- **jkljkl** = a white substance
>- **iopiop** = a graphite substance that can wertwert
So the graphite substance is the thing that performs the visible transfer onto the white surface. The **asdads** is for removing marks, not making them.

# humans

>Human brains are misaligned, hallucinative, stochastic parrots. Let’s finally build Biological General Intelligence
https://samuelfitoussi.substack.com/p/human-brains-are-misaligned-hallucinative

