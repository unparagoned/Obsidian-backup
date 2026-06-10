# Z Professional Discussion - notes

Source notes:
- [[Z Overall - st0763_artificial-intelligence-ai-data-specialist_l7_ap-for-publication_qm]]
- [[Z Professional Discussion]]
- [[Z Professional Discussion - EPA_Prep_-_Professional_Discussion]]
- [[Z Professional Discussion - AM2 Professional Discussion - Share with Learners]]
- [[Z Professional Discussion - AM1 Previously Asked Questions in Presentation]]
- [[Z Professional Discussion - from past learners]]
- [[Z Journal]]

## Assessment facts

Assessment method 2 is the professional discussion.

- One-to-one discussion with an independent assessor.
- 60 minutes, with possible 10% extension to complete the final answer.
- Minimum of 10 open questions.
- Questions come from the EPAO question bank and assessor follow-ups.
- It focuses on KSBs that are less likely to occur naturally in the project report, presentation, or technical test.
- The discussion can draw on broader workplace experience, not only the project.
- Use first person: "I did", "I decided", "I learned", "I influenced".
- To pass, all AM2 pass descriptors must be met.
- To get distinction, all pass descriptors and all AM2 distinction descriptors must be met.

## Response structure

Use a structured answer so each response proves competence rather than becoming a technical ramble.

STAR:

- Situation: context and why it mattered.
- Task: what I was responsible for.
- Action: what I personally did and why.
- Result: business/technical outcome, evidence, and learning.

For distinction-level answers, add:

- Trade-off: alternative options and why I chose one.
- Risk: what could go wrong and how I managed it.
- Reflection: what changed in my practice or in the organisation.

Useful closing sentence:

"The key judgement was balancing technical performance with business risk, governance, cost, maintainability, and stakeholder adoption."

## AM2 KSBs

Knowledge:

- K7: Solving problems and evaluating software solutions through test data, research, feasibility, acceptance, and usability testing.
- K8: Interpreting organisational policies, standards, and guidelines for AI/data.
- K10: How my role supports organisational strategy and objectives.
- K11: Roles and impact of AI, data science, and data engineering in industry and society.
- K16: High-performance computing architectures.
- K17: Current industry trends across AI and data science.
- K18: Programming languages and techniques for data engineering.
- K19: Principles behind statistical and ML methods.
- K21: How AI/data science techniques support the analytical team.
- K22: Relationship between mathematics and AI/data science techniques in organisational context.
- K25: Programming languages and modern ML libraries for commercial scientific analysis/simulation.
- K29: Accessibility and diversity of user needs.

Skills:

- S1: Applied research/data modelling to design secure, stable, scalable data products.
- S6: Direction and technical guidance on AI/data science opportunities.
- S8: Coordinate and manage diverse stakeholders with conflicting priorities.
- S12: Consider legal, ethical, regulatory, and governance issues throughout the data process.
- S14: Work with software engineers on testing and documentation.
- S16: Define requirements for data management infrastructure.
- S19: Use scalable infrastructure and services to generate business solutions.
- S20: Design efficient algorithms/APIs for large data access and analysis.
- S23: Disseminate AI/data science practice and best practice.
- S26: Select and apply appropriate AI/data science techniques to complex business problems.
- S28: Independent, impartial decision-making in complex, changing circumstances.

Behaviours:

- B1: Strong work ethic and commitment to required standards.
- B3: Ethical, legal, regulatory integrity; protect personal data, safety, and security.
- B4: Initiative and responsibility to overcome challenges and own solutions.
- B5: Continuous professional development.
- B7: Participates and shares best practice in organisation and wider community.
- B8: Maintains awareness of trends and innovations through literature, online sources, community interaction, conferences, and other methods.

## Theme 1: Computing and statistical foundations

KSBs: K7, K16, K18, K19, K22, K25, S1, S16, S19, S20, S26.

Pass criteria:

- Describe how to use statistical, AI, and ML methodologies such as data mining, supervised/unsupervised ML, NLP, and machine vision to meet business objectives.
- Explain how to solve problems and evaluate software solutions through test data, research, feasibility, acceptance, and usability testing.
- Describe the relationship between mathematics and core AI/data science techniques in organisational context.
- Explain use of programming languages and ML libraries for commercial analysis, simulation, and data engineering.
- Explain use of applied research and data modelling to design/refine secure, stable, scalable infrastructure.
- Explain how to design algorithms/APIs for accessing and analysing large data.

Distinction criterion:

- Explain when I challenged the norm by investigating and proposing a solution, and the impact this had.

Project evidence:

- Used supervised ML because tagged iXBRL concepts provided labels for untagged text classification.
- Used NLP/text classification methods: cleaning, canonicalisation, TF-IDF n-grams, embeddings, CNN, transformers.
- Used statistical evaluation: macro-F1, accuracy, precision, recall, stratified cross-validation, holdout testing, paired t-tests, population-size correlation analysis.
- Used data mining/EDA to identify class imbalance, ambiguous descriptions, label distribution, and taxonomy issues.
- Used Python libraries: scikit-learn, TensorFlow/Keras, HuggingFace Transformers, Optuna, MLflow.
- Used R for extraction/pre-processing because it fits HMRC analyst workflows and HTML parsing.
- Used reticulate to integrate Python ML into R.
- Designed scalable processing by choosing CPU-friendly LinearSVC and on-demand compute instead of a GPU-heavy transformer pipeline.
- Designed efficient access and analysis through structured outputs to Oracle and documented pipelines.

Mathematics to explain:

- TF-IDF: term frequency weighted by inverse document frequency; useful because rare discriminative financial phrases matter.
- LinearSVC/SVM: finds separating hyperplanes in high-dimensional feature space; works well with sparse text matrices.
- Regularisation: limits overfitting; L1 encourages sparsity and can improve speed/explainability.
- Macro-F1: arithmetic mean of per-class F1, so minority classes matter equally.
- Cross-validation: estimates generalisation and reduces dependence on one split.
- Paired t-test: checks whether performance differences are likely meaningful rather than random variation.
- Class weighting: increases penalty for errors in minority classes.

Challenge-the-norm answer:

"The norm would have been to rely on tagged iXBRL data only, or to use manually maintained matching rules for untagged descriptions. I challenged that by showing that tagged items could be reused as supervision for a supervised ML classifier. The impact was a reusable method that extended analytical coverage, reduced manual effort, and gave analysts access to data they could not previously exploit at scale."

## Theme 2: Professional practice in a commercial environment

KSBs: K8, K10, S6, S8, S14, S23, S28, B1, B4, B7.

Pass criteria:

- Explain how I developed professional working practices and leadership techniques in AI/data science and improved organisational practice.
- Justify technique choice, explaining risks/benefits and alternatives to technical and non-technical audiences.
- Explain how I shared AI/data science practices across the organisation to improve practice.
- Explain how I made independent impartial decisions while respecting others' views in complex circumstances.
- Explain how I worked with software engineers to implement testing and documentation processes.

Distinction criterion:

- Critically analyse wider social context, current issues, and trends; apply findings with justification and share them with the wider community.

Project evidence:

- Used GitLab issues, templates, epics, milestones, and documentation to improve traceability and team working.
- Used Kanban because the team was small and needed visibility without heavy ceremony.
- Gave analysts practical guidance on when ML categories are reliable and when to inspect raw descriptions.
- Shared best practice through README, setup scripts, project documentation, demos, and discussions.
- Worked with DevOps/software engineers on deployment, testing, documentation, synthetic/anonymised test fixtures, and infrastructure.
- Made impartial model selection using a decision matrix: performance, latency, cost, explainability, maintainability, governance, and scalability.
- Respected SME input where it contradicted initial assumptions, such as taxonomy differences and date/name handling.

Commercial context:

- HMRC priorities: reliable services, cost control, data protection, explainability, security, auditability, and operational scalability.
- Business value: better policy evidence, more complete risk identification, reduced manual analyst effort, reusable methodology for other document types.
- Risk management: human-in-the-loop, no automated decisions from ML category alone, PII masking, DPIA, per-class performance warnings.

Wider social/current trends:

- Increased use of AI in public sector decisions requires transparency, accountability, and proportionate governance.
- Foundation models are powerful but not always the right answer; smaller interpretable models may be better where data is structured, language is domain-specific, and governance matters.
- AI misuse and over-automation can reduce trust, so professional practice must include honest communication of limitations.

## Theme 3: Current and future impact of AI/data science

KSBs: K11, K17, K21.

Pass criteria:

- Describe how AI/data science roles and impact affect my organisation, industry, and society.
- Explain how I assessed and addressed ethical issues, selected procedures/methods, and unintended business consequences.
- Describe how I applied solutions and showed awareness of trends that enhanced working practices.
- Explain impact, consequences, and risks of non-compliance.

Project evidence:

- AI/data science helps HMRC make better use of submitted data for policy, profiling, and tax risk analysis.
- Data engineering makes the data usable at scale; ML adds classification where labels are missing.
- Analytical teams benefit because Hubble standardises descriptions into taxonomy concepts.
- Unintended consequences include analysts over-trusting predictions, minority classes being less reliable, or PII leaking into training data.
- Mitigations include documentation, per-class performance dashboard, human review, PII tokenisation, and clear warnings against automated decisions.
- Non-compliance risks include privacy breach, reputational damage, invalid decisions, legal challenge, loss of public trust, and operational rollback.

Trends to mention:

- MLOps, model monitoring, drift detection, model cards, AI assurance, explainable AI, data governance, privacy-enhancing technologies, and responsible AI.
- For LLMs/foundation models: useful for some tasks, but risks include hallucination, prompt injection, data leakage, cost, and weaker explainability.

## Theme 4: Ethical, legal, regulatory, governance, accessibility

KSBs: K29, S12, B3.

Pass criterion:

- Evaluate regulatory, ethical, and legal requirements affecting implementation, including accessibility for all users and diversity of user needs.

Project evidence:

- Company officer names and other personal data can appear in financial documents, so GDPR/Data Protection Act concerns exist even where some data is public.
- DPIA and data protection controls shaped preprocessing.
- PII was replaced with canonical placeholders where possible.
- Sensitive data should not be placed in unit tests; use synthetic or anonymised fixtures.
- The model output should not be used for automated decisions; it supports analysis and requires human interpretation.
- Accessibility in this context includes making documentation and dashboards usable by analysts with different technical backgrounds, not only end-user UI accessibility.
- Diversity of user needs includes analysts, SMEs, DevOps, managers, and governance reviewers needing different levels of detail.

Good answer:

"I treated governance as part of the design, not something added after modelling. For example, PII canonicalisation improved both compliance and model quality because high-cardinality names and addresses were not useful predictive signal and increased privacy risk."

## Theme 5: Continuous professional development

KSBs: B5, B8.

Pass criteria:

- Analyse how I take responsibility for my own and my team's knowledge, skills, professional growth, and personal development.
- Explain how I selected and applied the most appropriate AI/data science techniques to solve a complex business problem in line with organisational and regulatory requirements.

Evidence ideas:

- Learned and applied scikit-learn, Optuna, MLflow, HuggingFace, TensorFlow/Keras, and experiment-tracking practices.
- Used course materials on data science, legal/ethical issues, error/bias/uncertainty, DataOps/MLOps, and cloud ML.
- Read documentation and papers to compare TF-IDF, SBERT/embeddings, BERT-like models, CNNs, and SVMs.
- Shared learning through documentation, demos, setup scripts, GitLab issues, and analyst guidance.
- Took feedback from SMEs, ML experts, analysts, DevOps, and managers to improve practice.
- Maintained awareness of model drift, MLOps, explainability, responsible AI, and governance trends.

Good answer:

"My CPD was not only personal learning. I converted learning into working practice by documenting the pipeline, creating setup scripts, explaining model limitations to analysts, and introducing more systematic experiment tracking and project management."

## Evidence bank: Hubble examples

Use these as examples across multiple questions.

### Model selection

- Situation: Need to classify untagged iXBRL financial descriptions into taxonomy concepts.
- Action: Compared baselines, TF-IDF/scikit-learn, CNN, SEC-BERT/transformers, embeddings.
- Trade-off: Transformer complexity and GPU cost vs small performance difference; LinearSVC had strong macro-F1, explainability, and CPU speed.
- Result: LinearSVC with TF-IDF selected and deployed/integrated.

### Class imbalance

- Situation: 826 classes, top concepts dominate, long tail of rare classes.
- Action: Used macro-F1, stratified splits, balanced class weights, sqrt-weighted samples, per-class performance review.
- Result: Model evaluation aligned with business need to avoid ignoring minority classes.

### PII and data quality

- Situation: Descriptions can contain names, addresses, company names, dates, numbers.
- Action: Replaced with typed canonical tokens, handled 31 March 1982 separately, documented edge cases.
- Result: Reduced vocabulary noise and improved compliance.

### Stakeholder communication

- Situation: Different groups needed different detail.
- Action: Analysts got examples/confusion matrices; managers got benefits/costs/timeframes; DevOps got benchmarks/infrastructure; SMEs got taxonomy error cases.
- Result: Better adoption, funding/support, and more appropriate use of model outputs.

### Independent decision-making

- Situation: There was a temptation to choose more advanced models.
- Action: Used evidence-based decision matrix across performance, cost, latency, explainability, governance, and maintainability.
- Result: Selected the model that best fit HMRC working practice rather than the most fashionable approach.

## Likely professional discussion questions

- Tell me about a complex AI/data science problem you solved.
- How did you select the most appropriate AI or ML technique?
- How did you evaluate whether the solution was successful?
- How did you handle uncertainty, error, and bias?
- How did you work with technical and non-technical stakeholders?
- How did you adapt your communication style?
- How did you manage conflicting priorities?
- How does your role support organisational objectives?
- How did you ensure legal, ethical, and regulatory compliance?
- Tell me about a time you challenged the norm.
- How have you shared best practice?
- How do you keep your AI/data science knowledge current?
- What are the risks of non-compliance in your work?
- How do mathematical principles underpin the methods you used?
- How did you ensure suitable testing and documentation?
- How would you handle model drift or declining performance?
- What are the social impacts of AI adoption in your organisation?

## Short technical refreshers

### Supervised learning

Learns from labelled examples to predict labels for new cases. Hubble uses tagged iXBRL concepts as labels and predicts concepts for untagged descriptions.

### Unsupervised learning

Finds structure without labels, such as clustering similar descriptions or detecting anomalies. Useful for EDA, taxonomy exploration, or identifying unusual documents.

### NLP

Processes text data. In Hubble this includes tokenisation, normalisation, canonicalisation, TF-IDF vectorisation, embeddings, and text classification.

### Data mining

Discovers patterns in large datasets. In Hubble this includes frequency analysis, ambiguity analysis, concept distribution, description overlap, and model error patterns.

### Model drift

Performance degradation because data, taxonomy, document preparation, or real-world behaviour changes. Monitor data distributions, per-class F1, confidence/calibration, and analyst feedback. Retrain when thresholds are breached.

### Data quality dimensions

Accuracy, completeness, consistency, validity, timeliness, uniqueness, lineage, and relevance.

### Common metrics

- Accuracy: overall proportion correct; can hide minority-class failure.
- Precision: of predicted positives, how many were correct.
- Recall: of actual positives, how many were found.
- F1: harmonic mean of precision and recall.
- Macro-F1: average F1 across classes; useful for imbalance.
- Confusion matrix: shows which classes are confused with each other.

## Final preparation checklist

- Have at least one STAR example for every AM2 theme.
- Practise saying "I" rather than "we".
- Include a result or impact in every answer.
- Name a trade-off in every substantial technical answer.
- Mention governance, monitoring, and limitations without being prompted.
- Use Hubble examples, but also draw on wider workplace/course learning where AM2 asks broader professional practice.
- Do not overclaim model reliability. Explain where it fails and how users should handle that.
