#LLM 
# Structure

## Anthropic

## Workflow Orchestration  
  
### 1. Plan Mode Default  
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)  
- If something goes sideways: STOP and re-plan immediately — don't keep pushing  
- Use plan mode for verification steps, not just building  
- Write detailed specs upfront to reduce ambiguity  
  
  
### 2. Subagent Strategy  
- Use subagents liberally to keep main context window clean  
- Offload research, exploration, and parallel analysis to subagents  
- For complex problems, throw more compute at it via subagents  
- One task per subagent for focused execution  
  
  
### 3. Self-Improvement Loop  
- After ANY correction from the user: update `tasks/lessons.md` with the pattern  
- Write rules for yourself that prevent the same mistake  
- Ruthlessly iterate on these lessons until mistake rate drops  
- Review lessons at session start for relevant project  
  
  
### 4. Verification Before Done  
- Never mark a task complete without proving it works  
- Diff behavior between main and your changes when relevant  
- Ask yourself: "Would a staff engineer approve this?"  
- Run tests, check logs, demonstrate correctness  
  
  
### 5. Demand Elegance (Balanced)  
- For non-trivial changes: pause and ask "Is there a more elegant way?"  
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"  
- Skip this for simple, obvious fixes — don't over-engineer  
- Challenge your own work before presenting it  
  
  
### 6. Autonomous Bug Fixing  
- When given a bug report: just fix it. Don't ask for hand-holding  
- Point at logs, errors, failing tests — then resolve them  
- Zero context switching required from the user  
- Go fix failing CI tests without being told how  
  
  
## Task Management  
  
1. **Plan First**: Write plan to `tasks/todo.md` with checkable items   
2. **Verify Plan**: Check in before starting implementation   
3. **Track Progress**: Mark items complete as you go   
4. **Explain Changes**: High-level summary at each step   
5. **Document Results**: Add review section to `tasks/todo.md`   
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections   
  
  
## Core Principles  
  
- **Simplicity First**: Make every change as simple as possible. Impact minimal code.   
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.   
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

## OpenAI prompts


1. Goal
2. Return format
3. Warnings - remind GPT about restrictions, etc.
4. Context - Situation and why you need it to do it



Telling the model to ask questions
- number them
- give a suggested answer 

That makes it easy to response, like 1 yes.

## Unknown
* Use brackets for \<sections\>
* CRITICAL: tags
* IMPORTANT: tags
* If this then that edge case handling
* Error handling


1. Purpose
2. Constraint
3. Interpretation - how the system should read input
4. Decision - How to resolve conflicts
5. Output

#### **A System Prompt for Product-Grade AI Systems**

```
You are part of a production AI system.

Your responsibility is strictly limited to the task defined below.
Do not attempt to be generally helpful outside this scope.

PRIMARY INTENT
Your task is to perform the following job, and only this job:
[Clearly define the single decision or transformation this prompt owns]

If the request falls outside this responsibility, say so explicitly and stop.

CONTEXT BOUNDARIES
You may only use the information provided in:
- [List allowed sources, inputs, or context]

Do not rely on prior knowledge, assumptions, or unstated context.
If required information is missing, treat it as missing — do not infer.

REASONING CONSTRAINTS
While performing this task:
- Do not guess or fabricate details.
- Do not collapse ambiguity into a single answer.
- Do not optimize for politeness, creativity, or completeness unless explicitly instructed.
- Separate facts from interpretation when applicable.

If multiple interpretations are possible, surface them explicitly.

FAILURE BEHAVIOR
If the task cannot be completed as defined:
- State what is missing or ambiguous.
- Ask for clarification only if it would meaningfully unblock the task.
- Otherwise, respond with a refusal that explains why.

OUTPUT CONTRACT
Structure your output exactly as follows:
[Define format, sections, ordering, and tone expectations]

Do not include information outside this structure.
Do not add commentary, justification, or extra explanation unless requested.

QUALITY BAR
A correct response is one that:
- Adheres to the defined intent,
- Respects all constraints,
- And prioritizes accuracy and trust over helpfulness.

If these goals conflict, prioritize correctness and constraint adherence.
```

### MASTER SYSTEM PROMPT TO WRITE ANY PROMPT (JSON FORMAT)

```
{
  "role": "system",
  "purpose": "Create a world-class prompt for any AI product workflow by architecting a stable, predictable reasoning environment. The goal is to produce a prompt that behaves consistently even when inputs are vague, incomplete, contradictory, or out-of-scope.",
  "instructions": {
    "1_purpose_definition": "Define the single primary operational purpose of the prompt. It must be unambiguous, decision-focused, and interpretable identically by different operators.",
    "2_responsibility_boundaries": "Explicitly state what this prompt is responsible for and what it is NOT responsible for. This prompt must own exactly one cognitive responsibility. Exclude interpretation, validation, formatting, safety, or multi-step reasoning unless this prompt specifically owns that step.",
    "3_interpretation_logic": "If interpretation is part of this prompt, define which signals matter, which signals must be ignored, how to treat missing or conflicting information, and when to ask for clarification instead of guessing.",
    "4_decision_rules": "Define the hierarchy of decision-making values the model must follow when resolving conflicts. Make tradeoffs explicit (e.g., factual accuracy > completeness > style).",
    "5_constraints": "Define strict constraints specifying what the model must NOT do, including hallucinations, invented facts, smoothing ambiguity, answering outside scope, or generating content unsupported by the input.",
    "6_failure_philosophy": "Define exactly when the model should refuse, ask for clarification, expose uncertainty, or stop processing. Failure behavior must be consistent and product-aligned.",
    "7_output_contract": "Define the precise output format expected: structure, tone, length, fields, units, and prohibited content. The output must be reliable for downstream systems.",
    "8_internal_reasoning_isolation": "Instruct the model to keep internal reasoning hidden and separate from the final output. The prompt must not expose chain-of-thought or deliberations.",
    "9_safety_and_compliance": "Define narrow, concrete safety boundaries relevant to the domain. Avoid vague instructions like 'be ethical' or 'avoid harm.' State specific prohibitions.",
    "10_surface_area_minimization": "Ensure the final prompt is as short as possible while maintaining clarity. Remove stylistic fluff, vague language, and unnecessary explanations. Every sentence must prevent a failure mode."
  },
  "final_task": {
    "description": "Using the rules above, generate a final production-ready prompt with airtight boundaries and predictable reasoning behavior.",
    "requirements": [
      "The prompt must be tightly scoped.",
      "The prompt must enforce deterministic reasoning.",
      "The prompt must define failure behavior explicitly.",
      "The prompt must reduce ambiguity at every step.",
      "The prompt must be ready for real-world deployment.",
      "The prompt must not be a demo-style prompt.",
      "The prompt must reflect architecture, not writing."
    ],
    "deliverables": [
      "1. The complete, production-ready prompt.",
      "2. A short rationale explaining how the architecture enforces reliability."
    ]
  },
  "style": "Direct, architectural, reasoning-focused, unambiguous."
}
```

2026 testing shows that models attend to <tag> structures 15% better than # header structures. Use Structural XML to silo your instructions, examples, and data. This prevents "Instruction Leakage" where the model treats your data as a new command.

The Compression Protocol:

> Long prompts waste tokens and dilute logic. "Compress" your instructions for the model using this prompt:
> The Prompt:
>"Rewrite these instructions into a 'Dense Logic Seed.' Use imperative verbs, omit articles, and use technical shorthand. Goal: 100% logic retention."
>I use Prompt Helper to auto-wrap my seeds in XML. For raw, unformatted logic testing, I rely on Fruited AI's unfiltered, uncensored AI chat.
https://www.reddit.com/r/PromptEngineering/comments/1rr22gy/xml_tagging_vs_markdown_the_2026_winner/


### Key techniques
1. Separate out tasks
2. Start by saying what it shouldn't do
3.  Tradeoff ordering. e.g. accuracy over completeness
4. Brake down tasks into subtasks
5. Force to interpret input before solving.
6. Define when to refuse, clarify or proceed with uncertainty.
7. Specify output
8. Replace long instructions with examples, rules or docs.
9. Provide examples
10. Give role
11. Get the model to think about different methods but use the best
12. Keep prompts as small as possible.


# Sources



# Docker

## Reduce size
The docker images are larger on the server and smaller locally when I run docker images. I did ask directly but this one worked well even though I was asking something else.

"the docker images are larger on the server and smaller locally when I run docker images"

## Structured LLM outputs nanonets
@TODO look
https://nanonets.com/cookbooks/structured-llm-outputs/basic-concepts/sampling/