# Presentation slides: review and speaker notes

Review of `Jesse Karadia Presentation.pptx` as of 31 Aug 15:45. **26 slides**, notes on 24. The deck now matches the report's headline figures everywhere checked: 0.975/0.785 with CIs, 0.99 coverage, 3 days, 2.3pp/28x/220x, 826 to 141, 27 of 141 and eight at zero, 0.934/0.790 and 0.913/0.184, 9.8pp and ~20pp, 0.971/0.998, decision matrix totals against 195. The summary slide (26) ends the deck with the strongest points on screen for questioning, and the Questions line sits on it, so no blank closing slide.

Sources: `[[Z Project Report - Report final]]` for all figures and quotes, `[[Z Project Report - L7_AI_Data_Specialist_AM1-Project_and_Presentation_Guidance_V2.1]]` for the coverage requirements.

## Fixed since the last review

- Slide count 27 → 26; the empty "Any questions?" slide is gone, Questions now on the summary slide.
- Slide 9 notes: "LLMs were created for visual situations" corrected to CNNs.
- Slide 10: notes now open with the zero explanation (weighted points, lower-is-better inverted, worst model gets zero) and carry the full rubric.
- Slide 11: "2/3 days" now "3 days"; security row added, so all six KPIs are shown.
- Slide 13: coefficient walk-through in notes is strong, including the honest "coefficients aren't everything" point.
- Slide 14: table has example column, percentages, and "(should not match)" labels; notes state 13 cases per row, command one case, canonical control.
- Slide 16: slide now says "could be explained by"; SME review and work-with-providers mitigations on the slide.
- Slide 19: GitLab/team notes complete with the five iteration stages.
- Slide 25: duplicate lesson gone; slide-level typos fixed.
- Slide 22/26: tens-of-millions caveat (incomplete spreadsheet, monitoring box arranged) is in slide 22's notes.

## Remaining fixes, in priority order

1. **Slide 12, slide text**: "Only 54 items were classified as CashOnHand" — 54 is the *support* (true count in the holdout); the model predicted it 46 times (33 correct + 13 wrongly attracted). Say "Only 54 items in the holdout are CashOnHand". Notes also still say "Median per-class macro-F1"; the slide correctly says per-class F1 — align the notes.
2. **Slide 8, slide text**: "Paired T-tests were validated over test populations" is garbled. Should be "Paired t-tests over the cross-validation folds helped determine which models to drop."
3. **Slide 22 notes** first line still says "30% of data was easily categorisable and profilable" — the slide's fixed wording is "30% of data was tagged, now over 99% is extracted and classified". Align the note (tagged ≠ categorisable; the 99% is extracted-then-ML-classified at 0.785 macro-F1, which is the follow-up question to expect).
4. **Typos in notes**: slide 23 "thought" → "through", "datils" → "details"; slide 25 "befehand", "stages was"; slide 16 "were were", and the notes still state the agents/software explanation as fact where the slide says "could be" — align.
5. **Slide 17 notes**, garbled sentence: "requires development on ODC rather than existing that don't have a GPU" — suggested replacement in the notes block below.
6. **Slide 20** has almost no notes — full set below.
7. **Slide 14 notes** lack the category definitions — paste block below.

## Running order and timing

26 slides in 30 minutes ≈ 1.1 min each. Budget the heavy ones and claw back on light ones:

| Heavy (1.5–2 min) | Light (≤0.5 min) |
| --- | --- |
| 10 decision matrix (2.0 — do not read the rubric) | 1 title |
| 14 robustness table (1.5) | 24 next steps |
| 7 alternatives table (1.5) | 25 lessons |
| 20 stakeholders table (1.5) | |
| 21 limitations (1.5) | |
| 12 residuals (1.5) | |

That is ~9.5 min on six slides, ~1 min each for the rest. Rehearse 10 and 14 with a timer; they are where overruns happen.

---

# Speaker notes and Q&A ammunition, slide by slide

Notes blocks are plain text, ready to paste over the existing notes. "If asked" bullets are for questioning, not for the talk.

## Slide 2. HMRC and iXBRL documents

Existing notes are good (viewer left, HTML right, name attribute present/absent). Keep.

**If asked — what is a taxonomy?** A fixed dictionary of concepts (single CamelCase names like `TurnoverRevenue`) published by the FRC. The FRC suite (FRS 101, FRS 102, UK IFRS, Charities) shares a common core, so `TurnoverRevenue` is the same element across them; the genuinely different concepts are module-specific ones like the charity concepts (`IncomeFromCharitableActivities`, `CharityFunds`). Old UK GAAP (pre-2015) used different names entirely (`TurnoverGrossOperatingRevenue`), and US GAAP / international IFRS use `us-gaap:Revenues` / `ifrs-full:Revenue` — a mapping layer, not retraining, would be the route to serve those.

## Slide 3. Business problem

Notes fine. **If asked where "billions" comes from**: millions of documents per year, each with many figures, accumulated over years of filings; the report states it as the scale analysts could not access.

## Slide 4. The ML problem

Notes good (boat/animal example, royalties "advances" miss, Ferrari→MotorCars).

**If asked — problem type**: multi-class text classification, 141 nominal classes, strong imbalance, short inputs (median 2 words, max 15 after preprocessing). Not multi-label: one concept per item.

## Slide 5. EDA

```
iXBRL accounts submitted to Companies House were selected: same format as those submitted to HMRC, public, so free exploration without exposing customer data. One month, 298,461 accounts, 2.8 million rows. SMEs noted year-end clustering (31 Dec, 31 Mar) so not perfectly representative, but unlikely to materially affect the analysis.
956 concepts; the 75 most common cover 95% of items; the Pareto chart shows the long tail, closer to lognormal than power-law. That imbalance is why macro-F1 is the primary metric.
Descriptions are 1-9 words, mode 2, mixed types: nominal text, dates, names, numbers.
Descriptions and concepts are many-to-many: "Taxation and social security costs" maps to similar concepts, but "total" maps to 12 dissimilar ones.
Some concepts are more specific than the description can support, which puts a real upper limit on any description-only model.
```

**If asked — how would you compute that ceiling?** The best any string-only model can do is return the most common concept per distinct description; that majority-vote oracle is a hard upper bound. (Private note, not for slides or report: computed after the fact, the model reaches ~99.7% of the accuracy ceiling and ~98.3% of the macro-F1 ceiling on canonical descriptions — 99.6%/96.8% on cleaned — assuming canonicalisation is right. Do not volunteer numbers; the lesson on slide 25 is that it was not established beforehand.)

## Slide 6. Preprocessing

Notes good (DPIA/UK GDPR, forward-slash surprise, 350 threshold).

**If asked — the 956 → 826 split**: filtering invalid descriptions (blank, <2 chars, >15 words) removed 89 concepts that had no valid rows left; canonicalising names, dates, numbers and postcodes into five placeholder labels (`HubbleName`, `HubbleDate`, `HubbleNumber`, `HubbleCompanyName`, `HubblePostcode`) absorbed a net 41 more. 257 source concepts feed a placeholder, but most survive as labels because canonicalisation is per-row: a concept becomes `HubbleDate` where its description is a date and keeps its own label otherwise.
**If asked — why placeholders rather than dropping**: SMEs advised a bare placeholder is not enough to categorise, but knowing an item is a name/date is itself useful; also GDPR data minimisation, and it treats less common ethnic names the same as common ones.
**If asked — why 350?** Ensured enough examples per class even in the 1% training population used for cheap experiments. If anything it may have been too small at 1% (~3 examples per class).

## Slide 7. Survey of alternatives

Notes good. Keep the unsupervised rejection grounded on **cosine similarity** (that is what the report says); silhouette scores were a separate embedding comparison, not the rejection evidence.

**If asked — LLM security**: HMRC policy prevented sending taxpayer data through an external API; also excessive for short phrases, cost at daily-population scale, and no feature-level interpretability.
**If asked — regex detail**: it also would not cover the long tail, and when SME time was available the outputs were still incomplete (the royalties/advances example on slide 4).

## Slide 8. Traditional supervised ML

```
Comparing every model and hyperparameter over the full data was not feasible, so I first validated that small populations are representative: Pearson correlation to the full population 0.971 at 1% and 0.998 at 10%, and models not significantly worse at 1% were also not significantly worse at 100%. So small samples filter, 10% is reliable.
DummyClassifier floor (stratified baseline 0.007 macro-F1) to ensure real performance.
HalvingRandomSearchCV over 10,000 candidates narrowed models and hyperparameters.
Visualising hyperparameters against score and fit time showed two clusters: min_df=1 was both faster and better than min_df=2, which was surprising on speed, and narrowed later search ranges.
Stratified five-fold cross-validation reduced variance and allowed paired t-tests at the 5% level; where models could not be separated by macro-F1, train time decided, e.g. max_iter=10000 kept when 20,000 gave no significant gain.
```

**If asked — why is min_df=1 faster?** With rare but highly discriminative n-grams kept, the L1 solver converges in fewer iterations; sparse high-dimensional input is not itself slow for a linear SVM.
**If asked — paired t-test validity**: fold results share training rows so variance is understated; that is the 5x2cv limitation on slide 21. For the final comparison the right tool is paired bootstrap resampling on the fixed holdout, which is the other slide 21 point.

## Slide 9. Conventional and transformer NNs

Notes good (Optuna, sqrt weighting best, CNN surprise, SEC-BERT rationale).

**If asked — why does a CNN work on text?** The integer token IDs are arbitrary — ID 6 is no closer to 7 than to 412 — so they are used only as row indices into a learned embedding table (vocab 3,871 × 518 dims). Each word becomes the same learned vector every time it appears. A Conv1D filter is a 3-position × 518-channel weight block slid along the sequence: a learned detector for a 3-word pattern, scored at every position. Global max-pooling keeps each filter's best match wherever it occurred, so "cash at bank and in hand" and "total cash at bank" light up the same detector: position invariance (not word-order invariance — "trade debtors" and "debtors, trade" are different windows). 236 filters give 236 pattern scores which the dense layers map to 141 classes. With median 2-word descriptions, local n-gram patterns are essentially the whole signal, which is why it competes with transformers here (same insight as Kim 2014 — note: Kim is not in the report's reference list, so make the point without the citation).
**If asked — input representation**: the CNN does NOT use TF-IDF. TF-IDF sparse vectors feed LinearSVC only. The CNN path is TextVectorization to integer IDs → dense learned embeddings. SEC-BERT uses its own subword tokenizer and contextual embeddings.
**If asked — per-architecture scores**: deliberately not reported; the trial budget across architectures was uneven so ranking them by score would be misleading. CNN won its family and went forward; families were then compared properly in the decision matrix.

## Slide 10. Selecting the final model

Notes structure is right: zero explanation FIRST, then the bullets; rubric present but never read aloud. Say the zero line before anyone reads the table:

```
Cells are weighted points: each criterion's share times its weight, 195 total weight. Lower-is-better metrics are inverted, so the worst model scores zero — that is why SEC-BERT shows three zeros on time and size. A reciprocal normalisation would have been better; covered in limitations.
```

**If asked — where do these performance numbers come from?** All three models trained on the 10% square-root-weighted population and evaluated on the same holdout subset with bootstrap CIs (report B32): LinearSVC 0.800, CNN 0.808, SEC-BERT 0.823 macro-F1, hence 2.3pp. The 0.785 on the KPI slide is a different measurement: 100% unweighted training, full holdout. The transformer-search numbers (SEC-BERT 0.754 vs RoBERTa 0.743, MPNet 0.714, MiniLM 0.681) are from the Optuna comparison on its own split — three bases, deliberately not mixed.
**If asked — the 0.35 confidence factor**: where a model's CI overlapped the best model's, its score was multiplied by 0.35 so uncertain differences would not dominate. Limitation (slide 21): the better method is paired bootstrap resampling — resample the same test rows for both models, difference the metric per resample, read the CI of the difference; paired differencing removes the shared-rows variance that makes independent CIs overlap.
**If asked — how were subjective scores set?** A 1–5 rubric per criterion with a written narrative per model (report A6.2.5 and B31), including a Cost rubric (5 = fast to train, cheap to run on CPU, lightweight to store; 3 = needs GPU support).
**If asked — would a different weighting change the winner?** LinearSVC wins on 11 of 15 criteria; SEC-BERT leads only the four performance shares by tiny margins. The gap (37.2% vs 15.3%) is not weight-sensitive.

## Slide 11. KPIs

```
All six KPIs met. Accuracy 0.975 against 0.7; macro-F1 0.785 against 0.6 — the DummyClassifier baseline is 0.007, so the model is three orders of magnitude above chance-with-priors. Coverage over 99% against 95%. Three days against a week. Interpretable via feature coefficients. Security: well-established open-source packages, no external API, CPU-only estate — the SEC-BERT provenance concern is exactly what this KPI screens.
Accuracy is far above macro-F1 because the imbalance means common, easy classes dominate accuracy; macro-F1 weights all 141 classes equally, so the 27 weak rare classes pull it down. That is why macro-F1 is the primary metric.
The decision matrix score is not definitive: security or interpretability failures would override any score. If SEC-BERT had been materially superior, the route would be training our own BERT-based model in-house rather than using one with limited provenance.
```

## Slide 12. Residual analysis

Fix the 54 wording (see fixes). Notes otherwise good — keep "issue with the data rather than the model", but say "compute the performance ceiling" rather than "clean the data", which can sound like filtering the test set to raise the score.

**If asked — CashOnHand vs CashBankOnHand**: same FRC taxonomy, different specificity: `CashOnHand` (54 holdout items) is physical cash only, sibling of `CashBankOnHand` (7,791). With "cash at bank and in hand" tagged to both (5,670 vs 21), the model takes the majority; the minority tags surface as errors. By volume, 94% of holdout records fall in concepts scoring above 0.9.

## Slide 13. Interpretability and explainability

Notes are strong (coefficients read directly; "cost of" negative for TurnoverRevenue; "goods" negative for CostSales but positive under SEC-BERT). Keep the distinction crisp: **interpretable** = the model's own parameters explain it (coefficients); **explainable** = post-hoc approximation (LIME/SHAP) — helpful, but an approximation, and Rudin's argument is to prefer interpretable models where stakes matter.

**If asked — how does LIME work here?** Perturbs the input description (dropping words), watches the prediction change, fits a small local linear model; its weights say which words drove this one prediction.

## Slide 14. Robustness (eval data)

Add category definitions to notes:

```
13 hand-written cases per row, one per concept; command has a single case. Canonical is the control: both models 100%, so every other row is a drop from a working baseline.
canonical: the standard wording. synonym: accepted alternative term, e.g. Cost of goods sold. abbreviation: accountant's shorthand, e.g. COGS. variation: same words, different grammar, e.g. Costs of sale. contextual: plain-English definition with none of the key terms. long context: the concept buried in a full narrative sentence. typo: keyboard errors, e.g. Cost of salse. ocr: scanner substitutions, zero for o, one for l, e.g. C0st of sa1es. unicode: Cyrillic look-alike letters, looks identical, different bytes. adversarial: shares words with the concept but means something else, e.g. Sales commission - correct means it does NOT match. command: prompt-injection instruction in the description - correct means it does NOT follow it.
LinearSVC equalled or beat SEC-BERT on 10 of 11. Unicode is the one loss: TF-IDF has never seen the Cyrillic token; a subword model partially recovers. Note abbreviation and unicode are poor for BOTH models, and typo is identical at 31% each - training-data limitations, not architecture, and they undercut the assumption that a subword transformer handles misspellings better.
These perturbations are hand-constructed; the follow-up is measuring which actually occur in production data, at what rate.
```

## Slide 15. Features

Notes good ("Total" example; heading + table name → number of employees). Always say **on production data** for the 9.8pp, since slide 6's ~20pp is on evaluation data and an assessor may try to add them.

## Slide 16. Bias and fairness (production data)

Fix "were were" and align notes to the slide's "could be explained by". Add the what-did-you-do line:

```
The gap is real and I investigated it rather than explaining it away. Residual analysis showed many differences are between very similar concepts without enough information to separate them - the evaluation's specificity, a data issue, not a model treating small companies unfairly. But labels are the training proxy, so provider tagging quality matters: mitigations are per-class performance in the dashboard, human in the loop, SME evaluation stage, the simplified-taxonomy recommendation, and working with providers on tagging consistency. Careful not to overclaim in either direction.
```

**If asked — why do the subgroup figures (0.934/0.790) both beat the whole-population 0.741?** Macro-F1 is not an average of subgroup macro-F1s: the whole population's class set is the union, including rare classes absent from each subgroup, and those score low.

## Slide 17. Productionising

Replace the garbled ODC sentence:

```
To process the volume I worked with DevOps to set up on-demand-compute: an EC2 instance running POSIT starts per job and shuts down after, cheaper than a continuously running machine. CPU-only instances were cheaper and more available than GPU - AWS GPU availability was spotty - and with 128 cores ODC gave over a 20x speed-up. This is also the cost story: a model that needs only CPUs makes this architecture possible.
Automated daily process; analysts just query the database.
Long format rather than wide: every taxonomy has different concepts and new ones keep adding more, so a column per concept hits Oracle's 1,000-column limit and breaks on schema updates; long format handles any taxonomy without structural change.
Data available in SAS and POSIT.
```

## Slide 18. Guidance and Governance

Notes fine. **If asked — data quality framework**: DAMA UK dimensions: completeness (untagged data now extracted), consistency (tagged and untagged structured the same, same ML categories), timeliness (long format allows extraction within days for any taxonomy), validity/accuracy (invalid descriptions removed). Plus DPIA, DPA 2018, UK GDPR, restricted access.

## Slide 19. Agile, Kanban, CRISP-DM, GitLab

Notes good (five iteration stages, templates, test-per-issue policy, branch video).

**If asked — why Kanban not Scrum**: small team, competing business demands, fixed sprint commitments inappropriate; Kanban updates kept progress visible. **Why CRISP-DM not TDSP**: solo ML work, so team-oriented TDSP disproportionate; CRISP-DM matches the cyclical nature and each stage leaves documented artefacts.

## Slide 20. Working with stakeholders

Notes to add (the table carries the content, notes nearly empty):

```
Communication evolved from stakeholder reactions: PowerPoint, markdown guides, meetings, workshops. Early technical detail was too much for some audiences.
Managers: benefits, outcomes, funding, blockers, timeframes; cost-benefit memos on faster ingestion and coverage secured additional developers and infrastructure funding.
General: Problem-Solution-Outcome; visual examples - the 2D SVM decision boundary, confusion matrices with error examples, a worked weighted-vs-macro example instead of formulas.
Analysts: outcomes over mechanics. Repeated questions led to the interactive dashboard: test the model, see per-concept performance. Top-5 confused users with poor matches, so I cut it to plausible matches only; as understanding grew, so did use.
SMEs: taxonomy and accountancy questions - the 31 March 1982 date, placeholder-alone-not-enough advice, taxonomy naming differences leading to main-taxonomy-only training.
DevOps: benchmarks, memory, future requirements, EC2 cost-benefit; outcome was ODC funded and built.
```

## Slide 21. Limitations

Notes mostly good. Keep the two decision-matrix caveats exactly as phrased ("consistent normalisation baseline"; "bootstrap resampling paired differences" instead of the CI discount). One reconciliation line worth adding:

```
Scaling on the selection slide means inference volume on CPU; here it means training time growing with dataset size and label count. Going 10% to 100% train gained only 0.3pp macro-F1, so bigger data is not where improvement lies - preprocessing and taxonomy are.
```

**If asked — why would reciprocal normalisation be better?** `max − v` anchors the worst model at zero, so scores depend on who else is in the comparison (dropping a model flips near-ties), and a 216x size difference becomes a 5.03 vs 4.97 near-tie. The reciprocal (1/v, then share) preserves true ratios and is stable when alternatives are added or removed.
**If asked — 5x2cv in one line**: five-fold's folds share 75% of training rows, so luck repeats across folds, agreement looks like certainty, and the t-test calls coin-flips significant; two disjoint halves cannot share the luck, keeping the false-positive rate near the nominal 5% (Dietterich 1998).
**If asked — duplicated descriptions across train and test?** True: 2.8M rows collapse to ~7,800 unique canonicalised strings, so most holdout strings also occur in train. For a string-only model the evaluation still measures the right thing (the mapping is what is deployed), but it is optimistic relative to genuinely novel wording — which is what the robustness suite probes, and part of the tagged-to-untagged gap already recorded.

## Slide 22. Implications

Fix note line 1 (see fixes). Keep the incomplete-spreadsheet caveat in the notes — it is the strongest ROI answer, along with the monitoring box you arranged.

## Slide 23. Recommendations

Typos (see fixes). Denodo is now in the report's recommendations, so it is safe on the slide.

**If asked — why 2pp for drift?** More than twice the holdout CI width (~0.8pp on macro-F1), so it will not false-alarm on sampling noise; two consecutive days plus non-overlapping CIs guards against one-day blips. Automated drift only sees tagged items, hence the SME input.

## Slide 24. Next steps

Notes fine (human evaluation; MLflow version recorded in Oracle for traceability; simplified taxonomy rationale).

## Slide 25. Lessons Learned

Notes typos (see fixes). The ceiling lesson stays as "not established beforehand and should have been" — do not volunteer the after-the-fact figures (kept private above under slide 5).

## Slide 26. Summary

Content matches the report. Fix "macro-F1for" in notes. Stays on screen through questioning — that is the point of it.

---

# Cross-cutting prepared answers

- **"Walk me through your data splits."** Stratified 80/10/10 train/test/holdout created upfront before any modelling, plus sub-splits and square-root-weighted variants, shared across all model families for fair comparison. Holdout only for final evaluation.
- **"What did YOU do versus the team?"** Vast majority of the code and all of the machine learning; led the virtual team as it grew; SMEs advised on taxonomy/accountancy; DevOps built ODC with me; engineers reviewed the codebase.
- **"What would you do differently?"** Slide 25, plus: paired bootstrap instead of the CI discount, reciprocal normalisation, 5x2cv at later selection stages, ceiling first, Optuna from the start and for preprocessing choices.
- **"Is the model fair?"** Slide 16 framing: gap is real, investigated, mostly evaluation specificity and provider tagging; mitigations in place; overclaiming in either direction is the trap.
- **"Cost?"** Decision matrix Cost criterion (weight 20; LinearSVC 9.09 vs 5.45), CPU-only vs GPU estate, 220x inference, ODC pay-per-job, SME time saved (slides 4, 7, 22).
- **"Why not fine-tune an LLM / use ChatGPT?"** Security (no taxpayer data through external APIs), excessive for 1-15 word strings, cost at daily-population scale, interpretability KPI.
- **"How do you know it works on untagged data?"** Honestly: we don't fully — that is the recorded limitation. Proxy evidence: robustness suite, production figures on HMRC data (0.853/0.741), heading/table features +9.8pp, SME manual evaluation stage as the control.

# TODO

- [ ] Apply fixes 1–7 in the pptx (54 wording, slide 8 t-test line, slide 22 note, typos, ODC sentence, slide 20 notes, slide 14 definitions).
- [ ] Re-export the report PDF (13 Appendix D links were repaired after the 15:50 export) and rerun `Code/update_contents.py` if page numbers shift.
- [ ] Rehearse slides 10 and 14 against the timing table.
