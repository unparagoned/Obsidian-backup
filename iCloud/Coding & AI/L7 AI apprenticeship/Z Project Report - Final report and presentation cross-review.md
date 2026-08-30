# Final report and presentation cross-review

Reviewed 29 August 2026. Speed-claim clarification updated 30 August 2026.

## Scope

Compared:

- `Jesse Karadia Presentation.pptx` (26 slides, including the title and closing summary)
- `[[Z Project Report - Report final]]`
- all other files in this folder whose names start `Z Project Report`, treating the BCS guidance and signed-off project mapping as authoritative, the current final report and PowerPoint as the current deliverables, and older drafts/notes as supporting evidence or warnings rather than current facts

No source file was edited.

## Bottom line

The report and presentation tell the same core story and cover all seven presentation areas required by the BCS guide: summary, context and implications, research, practical application, business recommendations, follow-on outcomes, and next steps. The strongest material is the model-selection trade-off, the honest per-class and production-data qualification of the headline result, the practical production system, and the evidence of stakeholder adaptation.

The constraints in the request are reversed in the official guide:

- The **project report** is 5,000 words with a tolerance of ±10%, so the permitted range is 4,500–5,500 words. Appendices, references and diagrams are excluded.
- The **presentation** must be designed to last 30 minutes. The guide does not set it a 5,500-word limit.

A cleaned visible-text count of report Sections 1–12 is approximately **5,447 words**, leaving only about 53 words below the maximum. Different Markdown/export counting methods have previously produced estimates between roughly 5,406 and 5,499. The count that matters is the final submitted Word/PDF count, so this remains amber until the exported submission is checked.

The PowerPoint contains approximately **1,890 visible words** and **3,213 words in speaker notes**. Visible text plus notes is about 5,103 words, although that is not a meaningful speaking count because the notes repeat slide content. At 110 words per minute the notes alone take about 29 minutes; slide 20 has no notes, and transitions, pauses and chart explanation add time. A timed rehearsal is essential.

## How to use this review

Each issue below should identify:

1. **Where** the change is needed.
2. **What** is currently unclear, missing or inaccurate.
3. **Suggested change**: the specific action to take.
4. **Example wording**: text that can be used directly or adapted.

The example wording is intended to remove ambiguity about the recommendation; it is not mandatory wording where the user's own phrasing would be more natural.

## Highest-priority actions before submission

### 1. Appendix E is empty

`[[Z Project Report - Report final#Appendix E. Employer verification that the report reflects my own involvement and work.|Appendix E]]` contains only its heading. The BCS guide lists employer verification as a minimum required appendix. If verification is supplied as a separate signed document, Appendix E should clearly point to it in the final submission. If it is not supplied separately, this is a submission blocker.

**Suggested change:** insert the signed employer verification in Appendix E, or add a clear cross-reference if it is submitted separately.

**Example wording if separate:** “Employer verification is supplied as a separate signed document accompanying this project report.”

### 2. Correct and standardise the train/inference speed claims

The three ratios answer different questions and must not be used interchangeably:

| Figure | Calculation | Correct meaning | Example sentence |
| --- | --- | --- | --- |
| **13x** | 51,587.97s / 4,023.40s = 12.82x | Training SEC-BERT on the 10% square-root-weighted population was about 13x faster than the earlier full-population SEC-BERT run. This is a within-SEC-BERT sampling result, not a LinearSVC-versus-SEC-BERT result. | “Using the 10% square-root-weighted training population reduced SEC-BERT training time from 14.33 hours to 1.12 hours, approximately 13x faster than the full-population SEC-BERT run.” |
| **About 28x** | 4,023s / 144s = 27.94x | On the common 10% square-root-weighted training population, the recorded comparison time for LinearSVC was about 28x shorter than SEC-BERT. Because the times were logged through different frameworks and the LinearSVC/CNN values were manually entered into the comparison record, describe these as recorded comparison-run times rather than a controlled hardware benchmark. | “On the common 10% square-root-weighted training population, the recorded comparison times were 144 seconds for LinearSVC and 4,023 seconds for SEC-BERT, approximately 28x.” |
| **About 220x** | 143.107s / 0.6406s = 223.38x | LinearSVC inference was about 223x faster than SEC-BERT over the same 243,990-row test workload. Rounding to “about 220x” is reasonable. The displayed figures are total workload times, not per-sample seconds. | “On the same 243,990-row test workload, LinearSVC inference took 0.64 seconds versus 143.11 seconds for SEC-BERT, approximately 223x faster.” |

The 10% square-root-weighted population contained 195,192 training rows. It was used to compare LinearSVC, CNN and SEC-BERT consistently in Appendix B32. After model selection, the final LinearSVC was trained on the 100% training population and evaluated on the full holdout in Appendix B38. The 10% comparison and the final full-data LinearSVC evaluation therefore serve different purposes.

#### Exact PowerPoint change

**Slide 10, “Selecting final model”**

- Replace **“220x faster operation”** with **“About 220x faster inference on the same 243,990-row test workload (0.64s vs 143.11s)”**.
- If training speed is mentioned visibly or in the notes, use: **“On the same 10% square-root-weighted training population, the recorded comparison times were 144s for LinearSVC and 4,023s for SEC-BERT (about 28x).”**
- Add to the notes/Q&A explanation: **“The earlier 13x figure compared full-data SEC-BERT with 10% square-root-weighted SEC-BERT; it did not compare LinearSVC with SEC-BERT.”**
- Do not use “operation”, because that merges training and inference into one unsupported generic speed claim.

#### Exact report changes

| Report location | Current wording/problem | Suggested change | Example replacement wording |
| --- | --- | --- | --- |
| Section 7.5, model selection | “220x faster operation” merges training and inference and gives no denominator. | Describe inference only and identify the common workload. If training is discussed, give it as a separate recorded comparison. | “While SEC-BERT had the highest macro-F1, I selected LinearSVC because it was simpler to maintain and explain, and its inference was approximately 223x faster on the same 243,990-row test workload (0.64 seconds versus 143.11 seconds).” |
| Appendix A6.1, `metric_config` | “Inference time per sample in seconds.” The values are totals, not per-sample times. | Change the metric description to the total common-workload time. | `"description": "Total inference time in seconds for the common 243,990-row test workload."` |
| Appendix B32 introduction | It implies one evaluation workload but does not distinguish the 10,000-row performance holdout from the 243,990-row inference test workload. | State the two evaluation bases separately. | “All three models trained on the 195,192-row 10% square-root-weighted training population. Performance metrics use the same 10,000-row holdout; inference times use the same separate 243,990-row test workload.” |
| Appendix B32 row labels | “Train time (s)” and “Inference time (s)” do not state their denominators. | Retain the raw values but make the row labels explicit. | “Recorded training time, 195,192-row 10% sqrt subset (s)” and “Inference time, 243,990-row test workload (s)”. |
| Appendix B33, inference-time description | “Inference time per sample in seconds.” | Define it as total workload time and retain the lower-is-better direction. | “Total inference time for the common 243,990-row test workload; lower is better.” |
| Appendix D, K13 mapping | “220 times faster inference” lacks its denominator. | Add the workload qualifier. | “I selected LinearSVC partly because its inference was approximately 223x faster than SEC-BERT on the same 243,990-row test workload.” |

The B32 raw figures themselves do not need changing: training 144 / 2,640 / 4,023 seconds and inference 0.64 / 23.87 / 143.11 seconds. What needs correcting is the description, denominator and distinction between training and inference.

Recommended standard wording:

> On the common 243,990-row test workload, LinearSVC inference took 0.64 seconds versus 143.11 seconds for SEC-BERT, about 223x faster (reported as about 220x). On the common 195,192-row 10% square-root-weighted training population, the recorded comparison times were 144 seconds versus 4,023 seconds, about 28x. The separate 13x result measured the reduction from full-data to sampled SEC-BERT training.

### 3. Correct the bias explanation in the presentation

Slide 16 states as fact that larger companies spend more on agents and use more expensive software. The report is appropriately more cautious: cheaper software is a **possible explanation** for the observed company-size gap, labels are a proxy, and some errors are taxonomy or source-data issues. Present the company-size and software-provider differences as an observed association plus a hypothesis requiring investigation, not a causal conclusion.

The slide should also state the mitigations already evidenced elsewhere: per-class performance dashboard, human in the loop, no automated decisions, subject-matter-expert review, work with software providers, and possible taxonomy simplification.

**Suggested change:** replace the causal explanation with an observed result, a possible explanation and the mitigation.

**Example wording:** “Performance differed by company size and software provider. One possible explanation is variation in tagging quality or preparation practices, but this analysis does not establish the cause. I mitigated the risk through per-class monitoring, subject-matter-expert review and keeping a human in the loop.”

### 4. Fix the visual overflow and closing slide

Automated slide-boundary testing found content outside the slide canvas on:

- Slide 9, “Conventional and transformer based NNs”
- Slide 19, “Agile process, kanban, CRISP-DM, and GitLab”

In both cases the title is above the slide boundary. Slide 26 also renders with the closing “Questions?” text clipped at the bottom and is too dense for a final slide. These are visible presentation defects even though the content is correct.

**Suggested changes:**

- **Slide 9:** move the title fully inside the slide canvas and enlarge or crop the workflow so the audience can read the part being discussed.
- **Slide 19:** move the title fully inside the slide canvas; shorten it if necessary, for example **“Delivery approach: Agile, CRISP-DM and GitLab”**.
- **Slide 26:** remove secondary detail and retain only the problem, solution, selected model/trade-off, qualified headline result and business outcome. Move “Questions?” upward so it is fully visible.

### 5. Rehearse to 28–29 minutes, not exactly 30

The notes are close to a 30-minute script but uneven:

- Slide 10 has about 418 note words, around 3.5–4 minutes on its own.
- Slide 21 has about 228 note words.
- Slide 20, the stakeholder slide, has no speaker notes despite carrying important distinction evidence.
- Slide 11 has only about 52 note words even though the contrast between the headline score and weak minority classes needs careful explanation.

Aim to finish the rehearsed talk in 28–29 minutes to allow for slide changes, pauses and recovery. The current deck averages only about 69 seconds per slide.

**Suggested change:** use the notes as prompts rather than reading every visible line. Reduce slide 10 to approximately 2–2.5 minutes, add a 45–60 second stakeholder example to slide 20, and add a short explanation to slide 11 about why strong overall accuracy coexists with weak minority classes.

### 6. Remove or cite the orphan reference

The report has 43 reference-list entries but only 42 are cited in Sections 1–12. **Kim (2014)** is currently uncited. Either cite it in Section 6 where CNNs for sentence classification are introduced, or remove it from the reference list.

**Example citation sentence if retained:** “CNNs were also considered because convolutional architectures can capture informative local word patterns in sentence-classification tasks (Kim, 2014).”

## Material in the report that is missing or underplayed in the presentation

Not every report detail belongs in a 30-minute talk. The items below matter because they map directly to assessment criteria or likely supplementary questions. Most can be handled in speaker notes or backup slides rather than adding more visible text.

| Topic | What the report contains | Current presentation gap | Suggested change | Example wording/action |
| --- | --- | --- | --- | --- |
| Own role and contribution | The report states that Jesse wrote the vast majority of the code, all the machine learning, then led a virtual team. Appendix D distinguishes autonomous work from collaboration. | The deck uses first person but never gives a clean statement of personal ownership, leadership, autonomous work and where specialists were needed. | Add one explicit ownership sentence near the start or on slide 19/20. | “I developed all of the machine-learning work and the vast majority of the code, then led a virtual team to integrate and operationalise the wider service, working with specialists where infrastructure or domain input was required.” |
| Dataset selection | Public Companies House data was used for exploration to minimise customer-data access; restricted HMRC data was used for production evaluation. | The deck labels evaluation and production data but does not explain why two sources were selected or why their results are not directly comparable. | Add one sentence to slide 5 or 16 narration explaining the purpose of each source. | “I used public Companies House accounts for safe experimentation and restricted HMRC data for production evaluation; because the populations differ, their performance figures should not be treated as directly comparable.” |
| Scope and exclusions | Section 4 defines included extraction/classification/pipeline work and excludes profiling, human labelling and automated decisions. | KPIs are shown, but scope and exclusions are not stated together. | Add one spoken scope sentence near the start. | “My scope covered extraction, classification and the production pipeline; downstream profiling, new manual labelling and automated decisions were deliberately out of scope.” |
| Data protection and quality governance | Names and personal information are replaced, access is controlled, a DPIA is referenced, and Data Protection Act/UK GDPR requirements are discussed. | Slide 6 mentions removing personal identifiers; slide 18 covers operational governance, but the legal/organisational controls and traceability are absent. | Add one governance sentence to slide 6 or 18 notes. | “Personal identifiers were removed or replaced, access was controlled under the DPIA and UK data-protection requirements, and outputs retained whether a value came from customer tagging or an ML prediction.” |
| Scientific method and software testing | Explicit hypotheses, `DummyClassifier` baseline, stratified splits, paired tests, bootstrap confidence intervals, unit/integration/system tests and synthetic/anonymised fixtures. | Population-size tests and confidence intervals appear, but the systematic method, baseline and software-quality testing are not joined into a coherent point. | Add a concise method sentence to slide 8 or 19 narration. | “I tested explicit hypotheses against a DummyClassifier baseline, used stratified validation and confidence intervals for model evidence, and used unit, integration and system tests for the production pipeline.” |
| Class-imbalance treatment | Balanced class weights, square-root-weighted populations and oversampling experiments, including cases where weighting hurt neural networks. | The deck explains why macro-F1 matters but does not explain how imbalance was mitigated. | Add one sentence to slide 8 or 10 notes. | “To reduce majority-class bias, I tested balanced model weights, square-root-weighted training samples and oversampling, retaining the treatment that worked best for each model family.” |
| Production versus public-holdout results | Holdout: 0.975 accuracy / 0.785 macro-F1. One HMRC production population: 0.853 / 0.741. | The production figures appear only on the crowded limitations slide and are absent from the KPI/results narrative. | State the lower production result immediately after the headline holdout result and explain the population difference. | “The public holdout achieved 0.975 accuracy and 0.785 macro-F1; on one HMRC production population this reduced to 0.853 and 0.741, showing that the public holdout is an optimistic proxy rather than a guarantee of production performance.” |
| Feedback changed practice | Report: repeated questions led to the dashboard; showing a top five confused users, so it was reduced to plausible matches. | Slide 20 lists approaches and outcomes but omits this strong, specific example of adapting after feedback. It also has no notes. | Use this as the main 45–60 second stakeholder-adaptation example rather than reading every table cell. | “Repeated questions led me to build an interactive performance dashboard. It initially showed the top five predictions, but poor matches confused users, so I changed it to show only plausible alternatives.” |
| Research provenance | The report has 42 cited sources and justifies CRISP-DM, metrics, algorithms, statistical tests and governance. | The deck visibly cites only Dietterich and Gama and has no references/backup source slide. | Add short source entries in speaker notes and one unpresented reference slide. | Add a final backup slide titled **“Selected research and standards”** listing the key sources used for CRISP-DM, metrics, model comparison, explainability and governance. |
| Q&A evidence | Appendices B31–B40 contain the decision matrix, final metrics, architecture, per-class results and residual analysis. | The deck has no backup slides after the summary. | Add unpresented evidence slides for likely questions. | Add five backup slides: raw decision-matrix values; full pipeline; per-class results; bias/group split; and public-holdout versus production results. |

## Material in the presentation that is missing or weaker in the report

There is very little important presentation content absent from the report. Most slide claims trace to Sections 1–12 or Appendices A/B. The exceptions are mainly caveats or wording differences:

### Robustness cases are hand-built/theoretical

Slide 14’s notes acknowledge that the perturbations are theoretical and may not reflect realistic frequency or form in the data. The report lists the robustness result but does not make this limitation explicit. This is a useful caveat for Section 12 or, if the word limit prevents it, something to volunteer in the talk and questioning.

**Suggested change:** add one limitation sentence to Section 12 if the word count permits; otherwise add it to slide 14’s spoken explanation.

**Example wording:** “The robustness cases were hand-built perturbations designed to test specific failure modes; they do not establish how frequently those perturbations occur in production.”

### The presentation overstates “data rather than model”

Slide 12 says, “This is an issue with the data rather than the model.” The report correctly says **some** apparent errors arise because descriptions do not contain enough information. Keep the qualified wording: some errors are data/taxonomy ambiguity; others are genuine model errors.

**Suggested replacement:** “Some apparent errors are caused by ambiguous descriptions or inconsistent labels; others remain genuine model errors.”

### The model-selection table is transformed scoring, not raw performance

Slide 10 shows weighted decision points such as 2.33 for accuracy and 2.88 for macro-F1. Without a label, these look like impossible raw metrics. The report’s B32 has the actual values and B33/B34 explain the scoring. Label the slide table “weighted decision-matrix points” and be ready to open a backup slide with raw values.

The percentages in the total row (37.2%, 25.8%, 15.3%) do not sum to 100% because they are percentages of the maximum available weighted score, not shares of the three models. State that visibly or remove the percentages.

**Suggested changes:**

- Change the table heading to **“Weighted decision-matrix points”**.
- Add a small note: **“Percentages show achievement against the maximum possible weighted score; they are not shares and do not sum to 100%.”**
- Alternatively, remove the percentages and retain only the point totals.

### Lessons learned are partly stronger in the deck

The deck explicitly says a non-interpretable model may still be explainable and that robustness cases may not be realistic. The report discusses explainability and limitations separately but does not frame these as lessons. This is not a report gap that must be filled, but the presentation wording should remain precise: interpretability and post-hoc explainability are related but not interchangeable.

**Suggested wording:** “LinearSVC is directly interpretable through its feature coefficients; neural and transformer models require post-hoc explanations, which can help explain individual predictions but do not provide the same level of inherent interpretability.”

## Presentation content and wording issues by slide

### High impact

| Slide | Problem | Suggested change | Example wording/action |
| --- | --- | --- | --- |
| **8** | “T-tests were validated over test populations” is unclear. | State what was validated: the small-sample filtering conclusion held on the full population. | “Models that were not significantly worse on the smaller samples also remained competitive on the full training population, supporting the use of samples to narrow the search.” |
| **10** | “220x faster operation” merges training and inference; the table looks like raw metrics. | Use the qualified inference statement, keep training separate and label the table as weighted points. | “LinearSVC inference was approximately 223x faster on the same 243,990-row test workload.” Add **“Weighted decision-matrix points”** above the table. |
| **12** | “This is an issue with the data rather than the model” is too absolute. | Qualify the claim. | “Some apparent errors are caused by ambiguous descriptions or inconsistent labels; others remain genuine model errors.” |
| **14** | The chart denominator and the meaning of high adversarial/command scores are unclear. | State the number of cases and explain that refusal is correct for false-match tests. | “Each category contains 13 cases, except command with one case. For adversarial and command tests, a high score means the model correctly refused the false match.” |
| **16** | The slide implies a causal explanation for group-performance differences. | Present the result as an association, identify possible explanations and state mitigations. | “Performance differed by company size and software provider. Tagging quality and preparation practices may contribute, but the analysis does not establish causation.” |
| **20** | Reading the table alone misses the strongest evidence that feedback changed the product. | Add a 45–60 second example about the dashboard and identify personal versus collaborative work. | “Repeated questions led me to build a dashboard. When its top-five output confused users, I changed it to show only plausible matches. I led the ML work and collaborated with analysts, subject-matter experts and DevOps on adoption and deployment.” |
| **21** | The main tagged-to-untagged limitation and the limit of automated drift checks are underexplained. | State that monitoring the same proxy labels cannot replace manual evaluation. | “Because evaluation uses tagged items as a proxy for untagged items, automated drift checks inherit the same limitation and must be supplemented by periodic manually reviewed production samples.” |
| **26** | The closing slide is crowded and “Questions?” is clipped. | Retain five points only and move “Questions?” upward. | Keep: **problem; Hubble solution; selected LinearSVC trade-off; qualified holdout result; business outcome**. Remove secondary technical detail already covered earlier. |

### Visible wording/formatting

| Slide | Current issue | Suggested replacement/action |
| --- | --- | --- |
| **7** | “Transformers (locally run)” wraps awkwardly. | Widen the cell or shorten to **“Locally run transformers”**. |
| **9** | Title overflows and the workflow is too small. | Move the title inside the canvas and enlarge/crop the workflow to the stages discussed. |
| **13** | “coefficients which explains”. | Change to **“coefficients which explain”**. |
| **15** | Missing spaces before parentheses. | Use **“heading (2025 Number)”** and **“table name (Employees)”**. |
| **17** | “setup” is used as a verb; “Structure data as, long vs wide” is malformed. | Use **“set up”** and **“Structure data in long or wide format”**. |
| **18** | “performance, how it works” repeats the same idea. | Use **“performance and model behaviour”**. |
| **19** | Title overflows. | Move it inside the canvas or shorten to **“Delivery approach: Agile, CRISP-DM and GitLab”**. |
| **21** | “Humans to feed into another manual evaluation stage” is a fragment; “R and Python” has a leading space. | Use **“Use human-reviewed samples for a further manual evaluation stage”** and remove the stray space. |
| **23** | “fully supported by DevOps” is grammatically incomplete in context. | Use **“Move to a fully DevOps-supported service”**. |
| **24** | “Better integration of MLflow…” has lost its bullet/indent. | Restore it as a separate bullet aligned with the other next steps. |
| **25** | “stages were … still has” disagrees; `befehand` is misspelled. | Use **“Although earlier stages were completed, the project still has…”** and change to **“beforehand”**. |
| **26** | “for others factors”; malformed `C I0.780`; clipped final line. | Use **“for other factors”**, format as **“95% CI: 0.780–0.788”**, and move/shorten the final line so it fits. |

### Readability

The deck’s large body type is generally readable, but several embedded figures are not. Apply the following changes where the audience needs to read the detail:

| Slide | Figure | Suggested change |
| --- | --- | --- |
| **5** | Pareto chart labels | Crop to the most important classes or add an enlarged backup version; narrate the long-tail conclusion rather than expecting every label to be read. |
| **9** | Model-selection workflow | Enlarge the central selection path and move secondary branches to a backup slide. |
| **12** | Confusion-matrix labels | Crop to the two or three cells being explained, or provide an enlarged backup slide. |
| **15** | Source-document example | Highlight and enlarge only the description, heading and table-name fields used by the model. |
| **17** | Architecture diagram | Simplify to the extraction → feature preparation → classification → output path; keep implementation detail in a backup slide. |

## Report-specific feedback

### Submission blockers/risks

| Risk | Suggested change/action | Example wording/check |
| --- | --- | --- |
| Appendix E is empty. | Insert employer verification or point clearly to the separately submitted signed document. | “Employer verification is supplied as a separate signed document accompanying this report.” |
| The body is too close to the 5,500-word maximum. | Export the final Word/PDF and use that application's word count for Sections 1–12 only. Cut at least 50–100 words if the count is not comfortably below 5,500. | Record the final declared count on the title page if required. |
| Obsidian links, images, code and cross-references may not survive export. | Open the final Word/PDF and test every contents link, appendix link and figure; check that no `[[...]]` syntax or missing-image placeholders remain. | Search the export for `[[`, `]]`, `.png`, `.svg`, `#A` and `#B` to find likely conversion failures. |
| Submission metadata may be incomplete. | Check the EPAO template and add all required front-page metadata. | Confirm: approved title, apprentice, employer, standard/version, submission date and declared word count. |
| Generative-AI use is not currently disclosed. | Add a short disclosure naming each AI tool and explaining the extent of its use. BCS's *Using AI in Assessments* policy V1.1 (February 2026) requires full disclosure and clear references for AI use in project work. | State what the tool assisted with, what remained the apprentice's own work, and how outputs and cited sources were verified. Do not alter the official work-based project declaration form; add a separate AI-use statement. |

### Accuracy and consistency

| Location/topic | Suggested change | Example wording |
| --- | --- | --- |
| Speed claims | Apply Highest-priority action 2 consistently: 13x is within-SEC-BERT sampling, ~28x is the recorded training comparison and ~220x is common-workload inference. | Use the standard paragraph under Highest-priority action 2. |
| Section 9 and slide 16 bias explanation | Describe an association and possible explanations, not a proven cause. | “Performance differed by company size and software provider, but this analysis does not establish why; tagging quality and preparation practices require further investigation.” |
| Robustness limitation | Add the hand-built-test caveat to Section 12 or slide 14 notes. | “These perturbations test selected failure modes but do not show how frequently they occur in production.” |
| Section 7.6 grammar | Correct “on-demand-compute resulting in over a 20x speed-up”. | “On-demand compute resulted in a speed-up of more than 20x.” |
| Recommendation 2 grammar | Replace “using a fully supported by DevOps”. | “Move to a service fully supported by DevOps.” |
| LinearSVC non-convergence | Keep the disclosure and prepare a concise spoken answer explaining the evidence for retaining the model. | “LinearSVC did not fully converge, but performance was stable from 5,000 to 20,000 iterations; I retained 10,000 because the larger setting added runtime without a significant score improvement.” |

### Referencing

| Issue | Suggested change | Example/check |
| --- | --- | --- |
| Kim (2014) is uncited. | Cite it in the CNN discussion or remove it from the reference list. | “CNNs can capture informative local word patterns in sentence classification (Kim, 2014).” |
| The Ribeiro *et al.* (2020) and Mehrabi *et al.* (2021) links contain a year in parentheses inside an already parenthesised citation. This is a punctuation issue, not an author-count issue. | Change the link aliases so the non-integral citations render as `(Ribeiro et al., 2020)` and `(Mehrabi et al., 2021)`. Alternatively, make the author part of the sentence and remove the outer parentheses. | Keep the separate LIME citation as `(Ribeiro, Singh and Guestrin, 2016)`: the QA Harvard guide lists all two or three authors and uses *et al.* only for four or more. |
| The UK GDPR entry uses the official regulation number, title, legislation.gov.uk URL and access date, but the QA Harvard guide does not provide an EU-regulation example. | Treat the existing entry as adequate unless QA has issued a specific legal-citation rule. If strict EU-law formatting is requested, add the *Official Journal of the European Union*, L119, pp. 1–88 rather than leaving this as an undefined check. | Do not describe this as an uncompleted general reference check; it is a narrow style choice not covered by the supplied QA guide. |

## Coverage against the BCS presentation requirements

| Required area | Coverage | Comment | Suggested change |
| --- | --- | --- | --- |
| High-level summary | Strong | Slides 2–4 and 26. | Simplify slide 26 to the five-point closing summary described above. |
| Context, implications and recommendations | Strong | Slides 2–4 and 22–23. | No additional content required; retain the business problem and recommendation link. |
| Research undertaken | Good | Slides 5–10, but provenance/citations and dataset-selection rationale are underplayed. | Add selected sources in notes/a backup slide and use the dataset-selection sentence provided above. |
| Practical application of KSBs | Good, with gaps | Strong technical application; own role, testing, data protection and autonomous/collaborative choices need clearer narration. | Add the ownership, testing, governance and stakeholder-adaptation sentences from the missing-material table. |
| Business recommendations | Strong | Slide 23 is actionable, especially when drift thresholds in notes are included. | Retain the drift thresholds in narration and correct the DevOps wording. |
| Follow-on outcomes | Strong | Slide 22 covers adoption, policy use and estimated benefits; retain the caveat that benefits recording was incomplete. | Add: “Recorded benefits are incomplete, so the estimate should be treated as indicative rather than a fully realised total.” |
| Actions and next steps | Strong | Slide 24, but clarify ownership and fix bullet formatting. | Restore the MLflow bullet and state an owner or responsible team for each next step where known. |

## Prepared-question gaps

The deck and `[[Z Project Report - presentation draft]]` cover model choice, failure response, bias, ROI, scope extension, trade-offs, metrics and lessons. Rehearse the following answers explicitly:

| Likely question | Answer should cover | Example opening |
| --- | --- | --- |
| How did the project start and where did it come from? | The original business problem, who raised it, the inability to use untagged figures and how the scope/KPIs were agreed. | “The project began because analysts could reliably use tagged figures but most figures in some document types were untagged and therefore unavailable for analysis.” |
| What is the end-to-end pipeline, and are there one or several data sources? | Public Companies House experimentation data, restricted HMRC production data, extraction, preprocessing, classification, integration and storage. | “There were two evidence sources serving different purposes: public Companies House data for development and restricted HMRC data for production evaluation.” |
| How does the project affect day-to-day work? | Reduced manual classification, more usable data, dashboard/reliability checks and the retained need for analyst judgement. | “Analysts receive more structured data without manually classifying every item, but they still check per-class reliability before using ML-derived categories.” |
| How is the message changed for senior management or an external audience? | Benefits, risks, costs, timeframes and decisions for managers; plain-language Problem-Solution-Outcome and minimal sensitive detail externally. | “For senior management I focus on outcomes, funding, risks and blockers; for an external audience I remove unnecessary technical and sensitive detail and use a simple Problem-Solution-Outcome structure.” |
| Why did 13x appear in the gateway mapping? | It was the full-versus-sampled SEC-BERT training ratio and was incorrectly carried into a cross-model sentence. Distinguish it from ~28x training and ~220x inference. | “The 13x figure measured the benefit of sampling within SEC-BERT; it was not the final LinearSVC-versus-SEC-BERT inference comparison.” |
| Why does SEC-BERT score zero on some decision-matrix measures? | These are transformed points, not raw model metrics; the slowest/largest model receives zero after normalisation for lower-is-better criteria. | “Zero is a decision-matrix score after normalisation, not zero predictive performance.” |
| How can median per-class F1 be 0.966 while macro-F1 is 0.785? | The median describes the middle class; macro-F1 averages every class, so a minority of very weak/zero-scoring classes pulls the mean down. | “Most classes perform strongly, but macro-F1 is reduced by the long tail of weak classes, including eight with zero F1.” |
| Why is production performance lower than the public holdout? | Population/domain shift, tagged data as a proxy, differing software/preparation practices and no claim of direct comparability. | “The public holdout and production data are different populations, so the lower production result indicates transfer risk rather than a contradiction.” |
| What does the non-convergence warning mean, and why retain LinearSVC? | The optimiser had not reached its formal stopping criterion, but scores were stable across 5,000–20,000 iterations and more runtime produced no significant gain. | “The warning means the optimiser did not meet its numerical stopping criterion; it does not mean the model failed, and the validation evidence showed stable performance.” |
| What would establish whether tagged-data performance transfers to untagged items? | A manually labelled representative sample of untagged production items, blinded evaluation and repeated monitoring over time/providers/company groups. | “The key next evidence is a representative, manually labelled sample of previously untagged production items evaluated independently of the training labels.” |

## Suggested order of work

1. Resolve Appendix E and the final export/word count.
2. Apply the train/inference corrections listed in Highest-priority action 2 to slide 10 and the five identified report locations.
3. Fix slides 9, 16, 19, 24, 25 and 26.
4. Add or rehearse the missing KSB narrative: own role, dataset choice, testing, data protection, imbalance mitigation and stakeholder adaptation.
5. Add unpresented evidence slides for the 45-minute questioning period.
6. Rehearse twice: once for content, once strictly timed to 28–29 minutes.
