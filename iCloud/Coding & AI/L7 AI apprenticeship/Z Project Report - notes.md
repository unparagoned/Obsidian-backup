# Z Project Report - notes

Source notes:
- [[Z Overall - st0763_artificial-intelligence-ai-data-specialist_l7_ap-for-publication_qm]]
- [[Z Project Report]]
- [[Z Project Report - EPA_Prep_-_Project_Report]]
- [[Z Project Report - Project brief]]
- [[Z Project Report - Draft]]
- [[Z Project Report - Review and to do]]

## Assessment facts

Assessment method 1 is the project report with presentation and supplementary questioning.

- Component 1: 5,000 word project evaluation report, with 10% tolerance.
- Component 2: presentation and supplementary questioning.
- The project must be based on real pre-gateway work carried out in the workplace.
- A project brief is submitted at gateway. The EPAO signs it off and provides the report title.
- After title confirmation, the report must be completed within 6 weeks.
- The presentation is submitted after the report and is delivered to an independent assessor.
- Presentation and questioning lasts around 75 minutes: normally 30 minutes presentation and 45 minutes questions.
- The assessor must ask at least 10 questions.
- The assessment is graded holistically across report, presentation, and answers.
- To pass, all pass descriptors mapped to AM1 must be met.
- To get distinction, all pass criteria and all distinction criteria mapped to AM1 must be met.

## Required report structure

Use the EPA plan structure explicitly. The report should not read like a generic ML write-up; it should show business need, judgement, trade-offs, implementation, and evaluation.

1. Introduction and background.
2. Outline of the issue or opportunity and the business problem to be solved.
3. Methods used and justification.
4. Scope of the project, including KPIs.
5. Data selection, collection, and pre-processing.
6. Survey of potential alternatives.
7. Implementation and performance metrics.
8. Results.
9. Discussion and conclusions/recommendations.
10. Summary of findings.
11. Implications.
12. Caveats and limitations.
13. Appendices.

Appendices should include:

- Code and documentation used for the project.
- Statistical rigour: uncertainty, bias, and error estimates where appropriate.
- Figures, tables, and visualisations.
- Mapping of the project report to AM1 KSBs.
- Employer verification that the report reflects my own involvement and work.

## Project core narrative

Project title: Categorising data in financial documents.

The project is Hubble, an internal HMRC tool that extracts tagged and untagged items from iXBRL financial documents and classifies untagged free-text financial line items into taxonomy concepts using supervised machine learning.

The business problem is that some financial document types are poorly tagged. In some cases only around 30% of figures are tagged, so analysts can reliably use only a minority of the submitted financial data. This limits profiling, policy analysis, and tax risk identification.

The opportunity is that tagged iXBRL figures provide high-quality labels. These can be used as training data to learn the relationship between descriptions, headings, table names, and taxonomy concepts. The model can then classify untagged items and extend analytical coverage.

The main technical challenge is multi-class text classification over hundreds of nominal taxonomy classes with high class imbalance, noisy descriptions, multiple taxonomies, domain-specific terminology, and some irreducible ambiguity where descriptions alone are insufficient.

The selected solution was TF-IDF word n-grams with LinearSVC and balanced class weights. It was chosen because it gave strong macro-F1, very fast CPU inference, interpretable feature weights, lower infrastructure cost, and simpler deployment than transformer alternatives.

## AM1 KSBs

Knowledge:

- K1: AI and ML methodologies such as data mining, supervised/unsupervised ML, NLP, and machine vision to meet business objectives.
- K3: Applying advanced statistical and mathematical methods to commercial projects.
- K5: Designing and deploying effective data analysis and research techniques to meet business and customer needs.
- K6: Delivering data products using iterative, incremental, and project management approaches.
- K13: Compromises and trade-offs when translating theory into workplace practice.
- K14: Business value of a data product delivered to business needs, quality standards, and timescales.
- K23: Performance and accuracy metrics for model validation.
- K26: Scientific method, experiment design, and hypothesis testing.
- K28: Communicating concepts to diverse audiences.

Skills:

- S2: Analyse test data, interpret results, and evaluate solution suitability.
- S3: Critically evaluate arguments, assumptions, abstract concepts, and incomplete data to make recommendations.
- S4/S5: Communicate and manage stakeholder expectations.
- S7: Work autonomously and in multidisciplinary teams.
- S9/S10: Manipulate, analyse, visualise, and select complex datasets and methodologies.
- S11: Apply advanced maths and statistics to deliver business outcomes.
- S15: Identify, develop, build, and maintain AI/data services and platforms.
- S17: Implement data curation and data quality controls.
- S18: Develop visualisations for monitoring and performance.
- S22: Apply scientific methods through experiment design, EDA, and hypothesis testing.
- S24: Apply research methodology and project management techniques.
- S25: Select programming languages/tools and follow software development practices.
- S27: Analyse information, frame questions, and use SMEs to scope requirements.

Behaviours:

- B2: Reliable, objective, capable of independent and team working.
- B6: Comfortable with technical and non-technical people; presents data truthfully and appropriately.

## Theme 1: Business value and growth

KSBs: K13, K14.

Pass evidence needs to show:

- The AI/data science solution addresses a real business need.
- The solution was delivered in line with quality standards and timescales.
- Business value was considered.
- Constraints and trade-offs were considered.

Project evidence:

- Hubble addresses the gap where untagged financial figures were unavailable for automated analysis.
- It improves analytical coverage from the tagged minority toward the full population of extracted figures.
- Business value includes reduced manual effort, more complete profiling, better policy evidence, and better identification of tax risks.
- Quality standards include reliable extraction, consistent taxonomy labels, reproducible modelling, documented experiments, and human-in-the-loop usage.
- Timescale and operational needs shaped the model choice: CPU-friendly, fast inference, maintainable by the team, deployable within existing HMRC infrastructure.

Distinction evidence:

- HMRC priorities shaped the solution: maintainability, reliability, cost control, data protection, security, AI safeguards, and scaling to millions of records.
- LinearSVC was selected over transformer models because transformer gains were marginal or absent while infrastructure, cost, latency, and maintainability were worse.
- A single main taxonomy per document type was preferred over too many bespoke taxonomy mappings because standardised labels are more usable for analysts.
- On-demand compute balances scaling and cost by using larger EC2 resources only when needed for daily batch work.

## Theme 2: Evaluation, robustness, error, bias, and data quality

KSBs: K23, S3, S17.

Pass evidence needs to show:

- Critical evaluation of developed AI/ML model performance.
- Steps taken to mitigate error and bias.
- Selection of principles, techniques, and solutions to improve robustness.
- Business-focused recommendations based on arguments, assumptions, concepts, and data.
- Data curation and quality controls aligned with organisational and regulatory requirements.

Project evidence:

- Baseline DummyClassifier gave a performance floor.
- Multiple model families were compared: scikit-learn classifiers, CNN, transformer models such as SEC-BERT, and embedding approaches.
- Macro-F1 was the primary metric because the label distribution is highly imbalanced and accuracy alone would over-reward common classes.
- Accuracy was still monitored because common-class performance matters operationally.
- Confusion matrices and per-class results were used to identify systematic error patterns.
- Raw descriptions alone were noisy. Canonicalisation and extra features improved performance.
- Names, dates, numbers, postcodes, and companies were replaced with canonical tokens.
- Date 31 March 1982 was treated separately because it has specific tax significance.
- Stratified train/test/holdout splits kept all classes represented.
- Sqrt-weighted training populations and balanced class weights reduced majority-class bias.
- Population-size validation showed smaller training subsets were reliable for experimentation, reducing compute without losing model-ranking confidence.
- Data quality controls included dropping or handling low-quality ambiguous descriptions, PII masking, label engineering, and documenting limitations.

Good phrasing:

"The main bias risk in this project is not demographic fairness in the usual consumer-facing sense; it is class imbalance and representation bias across taxonomy concepts, document types, and preparation practices. I mitigated this through macro-F1, stratified sampling, balanced class weights, sqrt-weighted sampling, and per-class performance reporting."

Distinction evidence:

- Communication practice changed after stakeholder feedback: less abstract metric-heavy explanation for analysts; more examples, confusion matrices, and concrete error cases.
- Technical stakeholders received deeper detail on benchmark design, model selection, and infrastructure impact.
- Recommendations should include a monitoring dashboard, per-class reliability warnings, retraining triggers, and human review for decisions.

## Theme 3: Systematic methodology and project management

KSBs: S2, S9, S10, S22, S25.

Pass evidence needs to show:

- Selection and use of datasets, programming languages, tools, and scientific methodologies.
- Clear justification for each selection.
- Analysis of test data and proposed solutions against current and future business requirements.
- Manipulation and analysis of complex datasets.
- Critical evaluation of assumptions and incomplete data to make recommendations.

Project evidence:

- CRISP-DM structured the ML work: business understanding, data understanding, data preparation, modelling, evaluation, and deployment.
- R was used for extraction/pre-processing because it is an organisational default and maintainable by analysts.
- Python was used for ML because the ecosystem is stronger for text classification, hyperparameter search, transformers, and experiment tracking.
- Reticulate integrated Python ML into an R pipeline.
- MLflow tracked experiment parameters, metrics, and artefacts.
- GitLab issues, epics, tasks, and milestones supported planning, traceability, and handover.
- Data was split 80/10/10 using stratified sampling.
- Model development used controlled experiments, cross-validation, hyperparameter search, and statistical testing.
- Future requirements included scaling to millions of records, CPU deployment, fast inference, and minimal disruption to analysts.

Useful contrast:

- Rule-based matching: explainable but brittle, high SME maintenance, poor long-tail coverage.
- Transformer model: powerful but expensive, slower, more complex, harder to govern.
- TF-IDF + LinearSVC: strong domain fit, interpretable, fast, simple, scalable.

## Theme 4: AI project and development management

KSBs: K6, S24.

Pass evidence needs to show:

- Correct selection and application of development, research, and project management techniques.
- Engagement with customers/users.
- Solving the business problem being addressed.

Project evidence:

- CRISP-DM was selected because the project was an applied data mining/ML problem requiring iteration between data preparation, modelling, and evaluation.
- Kanban was selected over Scrum because the team was small and needed lightweight work tracking with minimal ceremony.
- GitLab gave visibility, auditability, and a durable record of decisions and tasks.
- Stakeholder engagement included analysts, SMEs, ML experts, DevOps, and managers.
- Analysts helped validate usefulness and outputs.
- SMEs clarified taxonomy edge cases, ambiguous descriptions, date handling, and whether names should be removed or tokenised.
- DevOps helped shape deployment and infrastructure.

Distinction evidence:

- Explain the impact of selecting these methods on working practice: transparent progress, reusable documentation, easier handover, more systematic experimentation.
- Explain continuity risks if tools were not used: knowledge trapped in notebooks or one person's memory, weak audit trail, hard onboarding, harder governance.

## Theme 5: Communication and influencing across teams

KSBs: K28, S4, S5, S7, S27, B2, B6.

Pass evidence needs to show:

- Working with technical and non-technical stakeholders.
- Adapting communication to different needs.
- Knowing when to work independently and collaboratively.
- Using questioning and discussions with SMEs to scope requirements.
- Clear written and verbal communication.
- Working with software engineers to ensure testing and documentation.

Project evidence:

- Analysts: focus on examples, confusion matrices, where the model works, where it fails, and how to use outputs responsibly.
- Managers: focus on benefits, cost, timeframes, risks, resourcing, and funding requirements.
- DevOps: focus on benchmarks, memory, CPU/GPU needs, latency, deployment, and operational stability.
- SMEs: focus on taxonomy meaning, ambiguous concepts, domain-specific terminology, and data quality decisions.
- ML experts: discuss model design, metrics, hyperparameters, and evaluation.
- GitLab issue templates improved clarity: steps to reproduce, expected vs actual, proposed fix.
- README and setup scripts helped analysts use the tool without direct support.
- Unit/integration tests and synthetic/anonymised fixtures supported safe testing.

Distinction evidence:

- Adaptation influenced decisions and working practices: managers reallocated development effort, funding was secured for infrastructure, analysts used the ML category more effectively, and team work became more transparent through GitLab/Kanban.
- Be explicit that outputs should not be used for automated tax decisions; the human-in-the-loop control is part of truthful, appropriate communication.

## Theme 6: Application of technical knowledge

KSBs: K1, K3, K5, K26, S11, S15, S18.

Pass evidence needs to show:

- Application of scientific and technological methods for ML, AI, data science solutions, services, and platforms.
- Business outcomes.
- Successes and challenges.

Project evidence:

- Supervised ML is appropriate because tagged iXBRL concepts provide labels.
- The task is nominal multi-class text classification with high class imbalance.
- TF-IDF works well because the text is short and domain-specific vocabulary is highly discriminative.
- LinearSVC works well with sparse high-dimensional TF-IDF matrices.
- L1 regularisation creates sparsity, reducing irrelevant features and improving efficient inference.
- Macro-F1 aligns with the business need to perform well across minority classes, not only common ones.
- Confusion matrices and feature weights provide explainability.
- Dashboards/per-class reports help analysts judge when to trust classifications.

Distinction evidence:

- Rationale for selecting LinearSVC must include scientific benefit and working-practice fit.
- Appraise alternatives and risks: rule-based brittleness, transformer cost/complexity, CNN opacity, minority class underperformance, taxonomy drift, extraction edge cases, PII handling edge cases.
- Explain mitigations: monitoring, retraining, human review, DPIA, PII canonicalisation, documentation, per-class metrics, and performance dashboards.

## Presentation notes

Presentation must cover:

- High-level summary of report.
- Context, implications, and recommendations.
- Research undertaken.
- Practical application of KSBs.
- Business recommendations.
- Follow-on outcomes.
- Actions and next steps.

Suggested 30-minute structure:

1. Problem and value: why untagged iXBRL data matters.
2. Data and labels: how tagged figures provide training signal.
3. Methodology: CRISP-DM, Kanban, datasets, tools.
4. Model comparison: baseline, TF-IDF/LinearSVC, CNN, SEC-BERT.
5. Evaluation: macro-F1, accuracy, confusion matrices, per-class issues.
6. Trade-offs: performance vs cost, explainability, maintainability, infrastructure.
7. Governance: PII, DPIA, human-in-the-loop, monitoring.
8. Business impact: expanded analytical coverage, adoption by teams.
9. Limitations: minority classes, ambiguous descriptions, taxonomy drift, extraction edge cases.
10. Recommendations and next steps.

## Presentation question bank and answer prompts

General answering advice:

- Use a 3-part answer: direct answer, project evidence, and business implication.
- Anchor answers in Hubble, not generic ML theory.
- Mention trade-offs explicitly: performance, cost, explainability, maintainability, governance, and timescale.
- Where possible, use the project numbers: around 30% tagged coverage in affected documents, 826 final classes, macro-F1 0.787, accuracy 97.1%, 2.7 microseconds per record inference, 14.3 hours GPU training for full SEC-BERT.
- If asked about a weakness, state the limitation clearly and then give the mitigation.
- If the question is broad, link the answer back to AM1 themes: business value, methodology, evaluation, robustness, communication, and governance.

### Previously asked presentation questions

#### How did you arrive at using this model? Why not another model?

Assessor intent: model selection, critical comparison, trade-offs, scientific method.

Strong answer:

- I did not start with LinearSVC as an assumption; I compared rule-based approaches, classical ML models, a CNN, and transformer models.
- The final model was selected using agreed criteria: macro-F1, accuracy, inference speed, training cost, explainability, deployment complexity, and maintainability.
- TF-IDF plus LinearSVC was best overall for this task because the descriptions are short and domain-specific, so n-gram vocabulary is highly predictive.
- LinearSVC achieved macro-F1 0.787 and accuracy 97.1%, with 2.7 microseconds per record inference on CPU.
- SEC-BERT was considered because it is domain-pretrained, but it required GPU training, took 14.3 hours on the full dataset, had slower inference, and did not improve macro-F1.
- The decision was therefore not just "best metric"; it was the best operational fit for HMRC scale, governance, and maintenance.

Useful phrase:

"The transformer route was technically plausible, but in this project the simpler model was both more effective and more deployable. The extra complexity did not buy a measurable improvement."

#### What if your model goes badly wrong one day? How would you fix it?

Assessor intent: monitoring, risk management, governance, incident response.

Strong answer:

- First, contain the risk: the model output should support analysts, not make automated tax decisions.
- Detect the problem through monitoring: macro-F1 against a fixed holdout set, per-class performance, prediction distribution drift, taxonomy changes, and analyst feedback.
- Diagnose whether the issue is data drift, extraction failure, taxonomy update, preprocessing bug, or model degradation.
- Roll back to a previous model/version if needed because experiments and artefacts are tracked.
- Retrain or adjust preprocessing if the issue comes from changed descriptions, new taxonomy concepts, or poor extraction.
- Communicate limitations clearly to users and managers, especially if specific classes should not be relied on.

Hubble-specific evidence:

- Use MLflow, versioned notebooks, GitLab issues, documented model comparison, per-class dashboards, human-in-the-loop use, and retraining triggers.

#### What is the bias in your project? How did you mitigate it?

Assessor intent: bias understanding beyond demographics, robustness, data quality.

Strong answer:

- The main bias risk is not demographic fairness; it is representation bias and class imbalance across taxonomy concepts, document types, and preparer practices.
- Common concepts have far more examples than rare concepts, so a naive model could perform well overall while failing minority classes.
- I mitigated this through macro-F1, stratified train/test/holdout splits, balanced class weights, sqrt-weighted training populations, per-class evaluation, and confusion matrix review.
- There is also selection bias because training labels come from tagged items; if tagged and untagged items differ systematically, performance may vary on the untagged population.
- The mitigation is to monitor real use, compare prediction distributions, use analyst feedback, and keep humans in the loop for material decisions.

Useful phrase:

"In this project, bias mainly means unequal model reliability across concepts and document-preparation styles, so the mitigations are metric choice, sampling design, class weighting, per-class reporting, and responsible use."

#### What is the ROI of your project?

Assessor intent: business value, measurable benefit, cost awareness.

Strong answer:

- ROI should be framed as improved analytical coverage, reduced manual review, better consistency, and more complete evidence for profiling, policy, and compliance risk work.
- Affected documents had only around 30% tagged figures, so analysts were limited to a minority of available financial data.
- Hubble extends coverage toward the full extracted population and reduces the need for manual classification of free-text descriptions.
- The model is cheap to run because it uses CPU inference and on-demand compute rather than permanent GPU infrastructure.
- Benefits include analyst time saved, more complete population analysis, reusable methodology for other document types, and better identification of tax risk.

Careful wording:

- Do not invent a cash saving unless it is evidenced.
- Say: "The business value is strongest as capability uplift and avoided manual effort. A precise cash ROI would need measured analyst time saved and compliance yield attribution."

#### How will you handle project scope extension in the future?

Assessor intent: scalability, future requirements, project control.

Strong answer:

- Extend in controlled increments rather than trying to generalise everything at once.
- Prioritise document types by business value, tagging gap, data volume, and taxonomy stability.
- Reuse the established pipeline: extraction, EDA, preprocessing, model training, evaluation, per-class dashboard, and deployment.
- Revalidate assumptions for each new document type because taxonomies, HTML structure, and description styles differ.
- Manage scope through GitLab epics/issues, acceptance criteria, stakeholder review, and clear KPIs.

Hubble-specific risks:

- New document types may need new extraction logic, taxonomy mapping, retraining, and updated PII checks.

#### How does your project impact people's day-to-day life and work?

Assessor intent: user impact, adoption, ethics, practical usefulness.

Strong answer:

- Analysts can work with a much larger proportion of financial data rather than only tagged figures.
- It reduces repetitive manual interpretation of free-text descriptions and makes outputs more consistent across analysts.
- SMEs are still needed for edge cases and validation, but their effort moves from manual categorisation to higher-value review.
- Managers get better evidence for policy and risk prioritisation.
- The impact must be managed responsibly: outputs should include confidence/per-class reliability context and should not be used as automatic tax decisions.

#### How do you communicate with higher management?

Assessor intent: audience adaptation, stakeholder management, business communication.

Strong answer:

- With senior managers, focus on business problem, value, risk, cost, timescale, and decisions needed.
- Avoid deep technical detail unless it affects a decision.
- Translate metrics into consequences: macro-F1 means reliability across rare as well as common concepts; inference speed means daily batch feasibility; CPU deployment means lower operational cost.
- Use concise written summaries, decision papers, risk logs, and clear recommendations.
- Be transparent about limitations and mitigations.

Useful contrast:

- Managers: value, risk, funding, delivery.
- Analysts: examples, limitations, how to use outputs.
- DevOps: infrastructure, memory, latency, scheduling.
- SMEs: taxonomy meaning and ambiguous cases.

#### Would you present the same content to an external audience, customer, or competitor?

Assessor intent: communication adaptation, confidentiality, governance.

Strong answer:

- No, the content would be adapted to audience, purpose, and confidentiality.
- For an external audience, remove sensitive HMRC data, internal architecture details, security controls, tax risk use cases, and operational volumes where inappropriate.
- Use public or synthetic data examples and focus on methodology, governance, and high-level outcomes.
- For a competitor or supplier, share only approved non-sensitive information and avoid anything that reveals operational capability or risk-identification methods.
- The core message may stay the same, but the evidence, examples, and level of detail would change.

#### How did this project initiate? Where did it come from?

Assessor intent: business need, stakeholder pull, problem framing.

Strong answer:

- The project came from a real analytical gap in HMRC's use of iXBRL financial documents.
- Some important document types had poor tagging, with only around 30% of figures tagged.
- Analysts either ignored the untagged majority or manually interpreted descriptions, which was slow and inconsistent.
- The opportunity was identified because tagged items already provide labelled examples, making supervised learning viable.
- Initial stakeholder work with analysts and SMEs confirmed the business need, feasibility, and success criteria.

#### What is your data pipeline like?

Assessor intent: end-to-end understanding, implementation, deployment.

Strong answer:

- Input: iXBRL documents processed from HMRC systems.
- Extraction: R pipeline parses tagged and untagged financial items, descriptions, headings, table names, and taxonomy concepts.
- Preprocessing: clean text, canonicalise dates, names, companies, numbers, and other PII/noise.
- Labelling: use tagged items as supervised labels; engineer canonical labels where the description reduces to a name/date/number.
- Modelling: Python/scikit-learn model called from R through reticulate.
- Evaluation: stratified splits, cross-validation, holdout testing, macro-F1, accuracy, confusion matrices, per-class metrics.
- Deployment: batch processing with on-demand compute and outputs loaded into Oracle for analyst use.

#### Where is the data coming from? Same resource or different resources?

Assessor intent: data provenance, label quality, data selection.

Strong answer:

- The training data comes from iXBRL financial documents already submitted to HMRC.
- Tagged figures provide labels because each tagged item has an iXBRL taxonomy concept assigned by the preparer.
- The documents can use different taxonomies and structures, so the modelling approach was scoped by document type and main taxonomy.
- Public Companies House data can demonstrate the method in notebooks, but production data and operational deployment are internal.
- Data provenance and handling are governed through HMRC controls, DPIA, PII canonicalisation, and documented preprocessing.

#### What trade-offs did you make?

Assessor intent: professional judgement, K13, practical constraints.

Strong answer:

- Model complexity vs deployability: chose LinearSVC over SEC-BERT because performance was comparable or better and operational cost was much lower.
- Accuracy vs minority-class fairness: used macro-F1 and balanced approaches rather than optimising only for overall accuracy.
- Standard taxonomy labels vs full taxonomy precision: used a main taxonomy per document type for analytical consistency.
- PII preservation vs model signal: canonicalised names and companies to protect privacy and improve generalisation, accepting that some fine-grained signal is removed.
- Speed/cost vs exhaustive experimentation: validated smaller training subsets to run efficient hyperparameter search.
- Automation vs responsible use: classification supports analysts but does not replace human judgement for material decisions.

#### What lessons did you learn?

Assessor intent: reflection, continuous improvement, professional maturity.

Strong answer:

- Start with the business problem and decision criteria, not with a preferred algorithm.
- Simple models can outperform more complex models when the feature representation fits the problem.
- Data preparation and label design had more impact than model architecture.
- Macro metrics, per-class review, and confusion matrices are essential for imbalanced multi-class problems.
- Stakeholder communication matters: analysts needed concrete examples and error cases, not just aggregate scores.
- Governance should be designed into the pipeline early, especially PII handling, documentation, and human-in-the-loop controls.

#### What is your current granularity, and how would you handle requests for more granular results?

Assessor intent: requirements change, scope, model limits. This was originally asked about forecasting, but for Hubble translate it to taxonomy/detail granularity.

Strong answer:

- Current granularity is taxonomy-concept classification for extracted financial line items within the selected document type.
- If stakeholders wanted more granular outputs, I would first clarify the business question: more granular by taxonomy concept, document section, subpopulation, time period, company segment, or confidence band.
- Then I would check whether the data supports that granularity and whether performance remains reliable at that level.
- More granular classes usually mean fewer examples per class, so minority-class performance and ambiguity risks increase.
- I would prototype on a subset, define new KPIs, review per-class metrics, and only extend scope where the output is reliable enough for the intended use.

### Additional likely supplementary questions

#### Why was macro-F1 chosen over accuracy?

Assessor intent: metric selection and class imbalance.

Strong answer:

- The class distribution is highly imbalanced: common concepts dominate the data and rare concepts still matter analytically.
- Accuracy can look strong if the model predicts common classes well, even if it performs poorly on minority classes.
- Macro-F1 gives each class equal weight, so it tests whether the model works across the taxonomy rather than only on frequent concepts.
- Accuracy was still monitored because common-class performance matters operationally, but macro-F1 was the primary KPI.

#### How did you know the model was better than a baseline?

Assessor intent: scientific method, evaluation validity.

Strong answer:

- I used DummyClassifier baselines to establish a performance floor.
- I used stratified train/test/holdout splits and cross-validation to reduce evaluation variance.
- I compared multiple model families under controlled conditions and tracked runs in MLflow.
- The final model exceeded the macro-F1 KPI and performed far above the baseline.
- Confusion matrices and per-class metrics showed where performance was strong and where limitations remained.

#### What were the main sources of error?

Assessor intent: error analysis, limitations, mitigations.

Strong answer:

- Main errors came from semantically similar concepts, generic descriptions such as "total" or "additions", minority classes with limited training examples, taxonomy drift, and extraction edge cases.
- Some ambiguity is irreducible if the description alone is insufficient.
- I mitigated this by adding contextual features such as heading and table name, using per-class performance dashboards, reviewing confusion matrices, and keeping analysts aware of low-reliability concepts.

#### How did you handle PII and GDPR?

Assessor intent: legal/regulatory awareness, data governance.

Strong answer:

- Work involving PII was covered by a DPIA and organisational data controls.
- Personal names, company names, addresses, postcodes, dates, and numbers were canonicalised where appropriate.
- PII canonicalisation reduced privacy risk and improved model generalisation by removing high-cardinality noise.
- Edge cases remain, such as names without common prefixes, so these are documented and should be monitored in future iterations.
- Public demonstration notebooks use non-sensitive public data while preserving the production methodology.

#### How would you explain the model to a non-technical stakeholder?

Assessor intent: communication across audiences.

Strong answer:

- "The model learns from examples where a financial line item has already been tagged. It learns which words and context usually correspond to each financial category, then uses that pattern to suggest categories for untagged line items."
- Avoid talking first about support vectors or sparse matrices.
- Use an example such as "share premium account" or "deferred consideration" mapping to a taxonomy concept.
- Explain limitations in plain terms: if the wording is too generic, the model may need human review.

#### What is the risk if an analyst uses the ML category incorrectly?

Assessor intent: responsible AI, downstream risk.

Strong answer:

- The risk is that an analyst treats a predicted category as ground truth and makes an incorrect analytical conclusion.
- This could affect profiling, policy evidence, or risk prioritisation.
- Mitigations are per-class reliability reporting, clear labelling of predicted versus tagged values, analyst guidance, human review for material decisions, and avoiding automated tax decisions.

#### How would the model be monitored in production?

Assessor intent: lifecycle management, robustness.

Strong answer:

- Monitor prediction distributions, extraction volumes, class frequencies, per-class performance where labels are available, data drift, taxonomy changes, and user feedback.
- Re-run performance checks against a fixed holdout set after code or taxonomy changes.
- Define retraining triggers such as material macro-F1 drop, new taxonomy concepts, changed document formats, or repeated analyst-reported misclassifications.
- Use versioning so results can be traced to model, data, and preprocessing versions.

#### What would you do differently with more time?

Assessor intent: reflective evaluation and prioritisation.

Strong answer:

- Strengthen production monitoring and retraining automation.
- Add richer contextual features from surrounding rows or document sections to reduce ambiguity.
- Improve PII detection edge cases.
- Expand active learning for low-performing classes.
- Extend the pipeline to additional document types only after validating taxonomy and extraction assumptions.

#### How does the project meet organisational quality standards?

Assessor intent: quality, governance, maintainability.

Strong answer:

- Reproducible experiments, GitLab traceability, MLflow tracking, documented notebooks, tested pipeline components, DPIA controls, PII canonicalisation, model comparison, and per-class evaluation.
- The model choice also supports quality because it is interpretable, cheap to run, and maintainable by the team.

#### How did stakeholders influence the project?

Assessor intent: collaboration, requirements, communication.

Strong answer:

- Analysts helped define usefulness, outputs, and how results would be consumed.
- SMEs clarified taxonomy meanings, ambiguous descriptions, date handling, and whether some names or entities should be canonicalised.
- DevOps shaped the deployment architecture, compute constraints, and batch scheduling.
- Managers shaped business priorities, timescales, and funding decisions.
- Stakeholder feedback changed the communication approach: more examples and concrete error cases for analysts, more cost/risk framing for managers.

#### Why use existing tagged data as labels? Are labels always correct?

Assessor intent: label quality and assumptions.

Strong answer:

- Tagged data is valuable because it provides labels at scale without new manual annotation.
- However, labels are not perfect: preparers may tag inconsistently, taxonomies vary, and tagged items may not fully represent untagged items.
- I treated labels as a strong but imperfect supervision signal and mitigated risk through data cleaning, SME consultation, error analysis, and monitoring.

#### What are the biggest limitations of the project?

Assessor intent: balanced evaluation.

Strong answer:

- Minority-class performance is weaker where training examples are scarce.
- Some descriptions are intrinsically ambiguous without richer context.
- Taxonomy and document-format changes require monitoring and retraining.
- PII detection has edge cases.
- Extraction is harder for non-standard HTML structures.
- These limitations do not invalidate the solution, but they define where human review, monitoring, and future development are needed.

## Remaining improvement points to check

- Confirm notebook 06 has a complete final model decision matrix.
- Add or reference per-class error analysis for the worst-performing classes.
- Make PII handling explicit, especially edge cases such as directors' names.
- State whether the final LinearSVC vs transformer difference is statistically significant.
- Explain deployment architecture, retraining triggers, drift/performance monitoring, and rollback.
- Explain any dataset version differences, such as v13 vs v16.
- Explain any constants, such as maximum word length filtering.
