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

## Likely supplementary questions

- Why was macro-F1 chosen over accuracy?
- How did you know the model was better than a baseline?
- Why did you select LinearSVC rather than BERT?
- What were the main sources of error?
- What bias exists in the project and how did you mitigate it?
- How did you handle PII and GDPR?
- How did you involve stakeholders?
- What would you do differently with more time?
- How would the model be monitored in production?
- How would you explain the model to a non-technical stakeholder?
- What is the risk if an analyst uses the ML category incorrectly?
- How does your solution create business value?

## Remaining improvement points to check

- Confirm notebook 06 has a complete final model decision matrix.
- Add or reference per-class error analysis for the worst-performing classes.
- Make PII handling explicit, especially edge cases such as directors' names.
- State whether the final LinearSVC vs transformer difference is statistically significant.
- Explain deployment architecture, retraining triggers, drift/performance monitoring, and rollback.
- Explain any dataset version differences, such as v13 vs v16.
- Explain any constants, such as maximum word length filtering.
