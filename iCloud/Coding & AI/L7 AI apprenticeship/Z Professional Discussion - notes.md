# Z Professional Discussion - notes

Source notes:
- [[Z Overall - st0763_artificial-intelligence-ai-data-specialist_l7_ap-for-publication_qm]]
- [[Z Professional Discussion]]
- [[Z Professional Discussion - EPA_Prep_-_Professional_Discussion]]
- [[Z Professional Discussion - AM2 Professional Discussion - Share with Learners]]
- [[Z Project Report - AM1 Previously Asked Questions in Presentation]]
- [[Z Professional Discussion - from past learners]]
- [[Z Professional Discussion - Journal]]
- [[Z Project Report - notes]]
- [[AI and Data Science Professional Practice Term 2 Theme 5 Legal aspects =]]
- [[AI and Data Science Professional Practice Term 2 Theme 6 Error, bias and uncertainty =]]
- [[AI and Data Science Professional Practice Term 3 Theme 7 =]]
- [[AI and Data Science Professional Practice Term 3 Theme 8 Team working =]]
- [[AI and Data Science Professional Practice Term 4 =]]
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]]
- [[Disruptive Leadership for Sustainable Strategy - Topic 7 - Data strategy]]
- [[Data Science Principles Topic 4 - Statistical testing =]]
- [[Data Science Principles Topic 5 - Working with big data =]]
- [[Data Science Principles Topic 6 - Storing your data]]
- [[Data Science Principles Topic 7 - Data Governance]]
- [[Programming for AI Topic 2 Sklearn]]
- [[Programming for AI Topic 3]]
- [[Programming for AI Topic 4]]
- [[Machine Learning using Cloud Computing Assignment]]

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

## Journal evidence by KSB

Use these as the main answer anchors. Each answer should start with one of these workplace examples, then add the technical explanation, trade-off, risk, and reflection.

### K7: Problem solving and evaluating software solutions

Main evidence: Hubble classification of untagged iXBRL descriptions.

- Situation: tax computations and accounts contain many untagged figures; some documents had only around 30% of figures tagged, so analysts could not profile across the full data population.
- Task: categorise the free-text descriptions into standard iXBRL taxonomy concepts.
- Actions:
  - Researched cosine similarity, scikit-learn classifiers, Naive Bayes, Random Forest, LinearSVC, CNN/MLP/RNN approaches, BERT, SEC-BERT, MPNet/e5 embeddings, and transformer fine-tuning.
  - Compared methods using macro-F1, accuracy, precision, recall, speed, simplicity, maintainability, explainability, cost, and security/provenance.
  - Tested feasibility against infrastructure: BERT/SEC-BERT could perform well but required GPU training and had slower inference on larger datasets.
  - Used test data, stratified splits, cross-validation, holdout evaluation, confusion matrices, per-class metrics, and acceptance/usability feedback from analysts.
- Result: final operational choice should be described as TF-IDF plus LinearSVC because it gave strong quality, CPU-speed inference, explainability through feature coefficients, and lower deployment risk. The journal also records earlier proof-of-concept work where MLP/BERT approaches performed well; discuss those as experimentation that informed the final decision, not the final deployed preference.
- Reflection: the most advanced model is not automatically the best model. The right answer is the model that meets business, governance, reliability, and operational constraints.

### K8: Interpreting organisational AI and data policies

Main evidence: challenging overly broad AI/LLM guidance and completing the Hubble DPIA.

- Situation: new organisational guidance treated all machine learning as if it had the same risk profile as generative AI/LLMs.
- Task: ensure projects followed policy while avoiding unnecessary business blockage.
- Actions:
  - Reviewed the guidance against practical ML workflows.
  - Explained that basic ML classification needed different controls from LLM use, because restricted LLM platforms did not support normal model development, testing, and deployment.
  - Provided specific feedback on why the guidance was not implementable and how it should be changed.
  - Completed a DPIA for Hubble and embedded controls such as secure processing, data minimisation, PII canonicalisation, and human-in-the-loop use.
- Result: guidance was changed in line with the comments; Hubble was designed in a way that aligned with privacy, security, and organisational controls.
- Reflection: policies need interpretation, not blind application. Professional integrity means challenging guidance constructively where it is outdated or technically inaccurate.

### K10: Own role supporting organisational strategy and objectives

Main evidence: Hubble, DAP, ODC, analyst support, and mentoring.

- Situation: HMRC needs to exploit data to identify tax risks and provide evidence to policy/Treasury.
- Task: build data products, platforms, and team capability that improve tax-risk identification and analytical coverage.
- Actions:
  - Lead developer on Hubble, which extracts data from company accounts and uses ML to categorise descriptions.
  - Arranged setup and development of the Data Analytics Platform (DAP), a POSIT platform supporting R and Python.
  - Supported upgrades, access, functionality, and mentoring for analysts.
  - Arranged On Demand Compute (ODC) so large jobs and GPU-heavy experiments can run temporarily and cost-effectively.
- Result:
  - Hubble can extract substantially more data from accounts, recorded in the journal as 233% more data.
  - Analysts use outputs in profiles and the work supports millions of pounds of identified tax risks.
  - DAP grew from one user to over 150 users.
- Reflection: the role is T-shaped: deep iXBRL/domain knowledge plus broad data engineering, ML, R/Python, cloud, and platform knowledge.

### K11: Roles and impact of AI, data science, and data engineering

Main evidence: Hubble as an end-to-end data engineering and ML product.

- Data engineering role: extract, clean, canonicalise, structure, and store iXBRL data so it can be profiled at scale.
- Data science role: investigate the data, understand imbalance and ambiguity, evaluate methods, and quantify performance and uncertainty.
- AI/ML role: classify untagged descriptions where deterministic rules or manual tagging would not scale.
- Organisational impact: analysts can use a larger proportion of submitted financial data, reducing manual grouping and improving consistency.
- Societal impact: better identification of tax risk supports public revenue, which funds public services.
- Industry/society examples to mention if asked broadly: medical imaging, fraud detection, demand forecasting, market prediction, pricing, stock ordering, and risk assessment.
- Risk: if AI outputs are over-trusted, they can create wrong conclusions, unfair outcomes, or reputational damage. Hubble mitigates this by supporting analysts rather than making automatic decisions.

### K16: High-performance computing architectures

Main evidence: Solr, DAP, ODC, Oracle, and future lakehouse/Spark direction.

- Situation: HMRC data includes structured XML, semi-structured iXBRL/XHTML, PDFs and large volumes arriving quickly.
- Actions:
  - Used Apache Solr for fast distributed text search and profiling over document-style data.
  - Used POSIT DAP for R/Python analytical workflows.
  - Arranged ODC to spin up large machines, for example 128 cores or GPU-enabled infrastructure, for intensive extraction or model training.
  - Loaded structured outputs to Oracle for analyst querying.
  - Considered future migration to a lakehouse, SparkR/EMR, and Redshift-style storage for better scale and integration.
- Result: fast search/profiling, cost-effective burst compute, and scalable batch processing without keeping large or GPU infrastructure running permanently.
- Strength: ODC balances performance and cost.
- Weakness: some parallel processing packages split work poorly when documents vary in size, leaving some cores idle. Dynamic work splitting is better.

### K17: Current industry trends in AI and data science

Main evidence: iXBRL/LLM monitoring, Graffiti, transformer research, and MLOps awareness.

- Actions:
  - Follow iXBRL International and other industry sources.
  - Reviewed examples where passing a whole HTML document to an LLM performed poorly, while extracting iXBRL first and passing structured context worked better.
  - Created the Graffiti iXBRL viewer to extract iXBRL and pass relevant data plus a query to an LLM.
  - Monitored trends such as LLMs, tool use/MCP, model cards, MLOps, drift detection, explainable AI, responsible AI, and privacy-enhancing techniques.
- Result: Graffiti gives more accurate account-analysis answers because it grounds the LLM in extracted iXBRL rather than raw noisy HTML.
- Reflection: trends are useful only when applied with evidence. LLMs create opportunities, but they also introduce hallucination, prompt injection, data leakage, cost, and governance risks.

### K18: Programming languages and data engineering techniques

Main evidence: Java, R, Python, SQL, reticulate, dbplyr, S3, Solr, Oracle.

- Java: moves data from original stores into S3 buckets and extracts iXBRL/XML into Apache Solr.
- R: main Hubble extraction language because R packages are strong for HTML/XML parsing and analysts in the area use R.
- Python: used for ML because scikit-learn, TensorFlow/Keras, Hugging Face, datasets, transformers, torch, Optuna and MLflow are more mature and better documented.
- reticulate: allows R code to call Python ML functions so analysts can keep an R-first workflow while using Python ML.
- SQL/Oracle: stores extracted outputs in relational tables for querying.
- dbplyr: lets R/tidyverse code interact with database tables and translates operations to SQL.
- Core data engineering pattern: extract, transform, canonicalise, validate, load, document, and monitor.
- Reflection: choose language and tooling by task, team skill, package maturity, deployment environment, and maintainability.

### K19: Principles behind statistical and ML methods

Main evidence: risk comparison using Welch's t-test, plus model evaluation.

- Statistical testing example:
  - Situation: agent-level data needed quantitative comparison.
  - Hypothesis: null hypothesis was that the agent had the same risk as others.
  - Data: two independent groups, ratio data, normally distributed, n > 30, population standard deviation unknown.
  - F-test showed unequal variances, so Welch's t-test was more appropriate than Student's t-test.
  - Result: with 99% confidence, the null hypothesis could be rejected.
- ML principles to explain:
  - Supervised classification learns a function from labelled examples to unseen descriptions.
  - Text is converted to numeric features using TF-IDF or embeddings.
  - LinearSVC learns separating hyperplanes in high-dimensional sparse feature space.
  - Neural networks learn weights through loss, gradients, backpropagation, and optimisation.
  - Transformers use self-attention to model relationships between tokens.
  - Regularisation controls overfitting.
  - Macro-F1, stratification and per-class metrics manage imbalance.
- Reflection: statistical and ML methods are not just coding techniques; they provide a disciplined way to decide whether differences are meaningful and whether a model generalises.

### K21: How AI/data science supports analytical teams

Main evidence: analysts using Hubble and DAP.

- Situation: analysts were manually grouping inconsistent financial descriptions.
- Actions:
  - Built the classifier around familiar iXBRL taxonomy concepts.
  - Engaged analysts and SMEs during testing through calls, examples, confusion matrices, and feedback.
  - Provided DAP support so analysts could use R/Python tools and create dashboards or connect to other systems.
- Result: analysts can profile more data faster, with more consistent categorisation, while SMEs focus on higher-value review rather than repetitive manual grouping.
- Limit: model categories should be treated as analytical suggestions, not ground truth.

### K22: Mathematics and core AI/data science techniques in organisational context

Main evidence: TF-IDF, embeddings, LinearSVC, class weighting, and evaluation metrics.

- TF-IDF: term frequency times inverse document frequency turns text into a sparse numeric vector. It worked because accounting descriptions contain specific terms and phrases.
- Embeddings: dense vectors can capture semantic similarity, but generic embeddings did not always understand specialist accountancy language.
- LinearSVC: uses optimisation to find class-separating hyperplanes; with sparse TF-IDF and L1 penalty many features can become zero, improving speed and interpretability.
- Macro-F1: averages class-level F1 so rare taxonomy concepts matter equally.
- Paired tests: compare model runs on the same splits to assess whether differences are likely meaningful.
- Organisational context: HMRC needed a model that was accurate enough, explainable, cheap to run, secure, maintainable, and usable by analysts.

### K25: Programming languages and modern ML libraries

Main evidence: scikit-learn, TensorFlow/Keras, Hugging Face, torch, datasets, Optuna, MLflow.

- scikit-learn: cosine similarity, Naive Bayes, Random Forest, LinearSVC, TF-IDF, train/test split, cross-validation, metrics.
- TensorFlow/Keras: MLP, CNN, RNN/LSTM experiments and custom network layers.
- Hugging Face/datasets/transformers/torch: BERT and SEC-BERT experiments and fine-tuning.
- Optuna: hyperparameter optimisation.
- MLflow: experiment tracking, comparison, reproducibility, and model artefact/version discipline.
- Commercial benefit: faster analyst workflows, reusable methodology, lower manual effort, better risk identification, and stronger analytical coverage.
- Key answer point: describe the final model and the experimental alternatives; do not imply every prototype was production-ready.

### K29: Accessibility and diversity of user needs

Main evidence: Graffiti bookmarklet guidance, WCAG expert input, and analyst documentation.

- Situation: tools need to be usable by people with different technical skill levels and accessibility needs.
- Actions:
  - Engaged a WCAG expert on one project.
  - Started fixing accessibility gaps.
  - For the Graffiti bookmarklet, created alternative guidance for users who could not drag it to the bookmarks bar.
  - Made documentation and dashboards clearer for analysts, SMEs, managers, DevOps and governance reviewers.
- Result: more users can run and understand the tools.
- Reflection: accessibility is easier when designed in from the start. In this context, accessibility is not only screen-reader UI work; it includes usable documentation, clear outputs, and communication matched to different users.

### S1: Applied research and data modelling for secure, stable, scalable data products

- Applied research: compared model families and literature/documents around transformers, BERT, TF-IDF, SVMs, neural networks, and text classification.
- Data modelling: transformed unstructured/semi-structured iXBRL text into structured records with descriptions, context, labels, predictions, and metadata.
- Security/stability: processed data inside HMRC estate, used DPIA controls, avoided unassured niche models for production, and kept outputs in controlled systems.
- Scalability: used CPU-friendly models, ODC for burst processing, Solr for distributed search, and Oracle/database outputs for querying.

### S6: Direction and technical guidance

- Owns/supports the DAP platform where AI/data science work happens.
- Provides guidance on virtual environments, data access, GPU-enabled machines, project setup, and ML use cases.
- Mentors analysts and project teams.
- Runs or supports regular discussions about ML opportunities.
- Maintains wiki guidance so good practice is reusable.

### S8: Stakeholder coordination and conflicting priorities

- Stakeholders: analysts, SMEs, DevOps/software engineers, managers/budget holders, internal platform teams, external suppliers.
- Conflicts:
  - Users wanted GPU functionality and more data connections.
  - Budget holders needed cost justification and licence control.
  - External stakeholders suggested data transfer rather than direct database connections.
  - Some users wanted S3 write patterns where existing database access was safer or simpler.
  - Some non-technical stakeholders preferred accuracy; technical evaluation showed macro-F1 was more appropriate for imbalance.
- Approach: gather views, explain trade-offs, document options, choose the best business-wide solution rather than simply following the loudest request.
- Result: DAP grew to over 150 users, ODC was delivered, licences were managed, and POSIT/SAS interoperability improved.

### S12 and B3: Regulatory, legal, ethical and governance issues

- DPIA completed before Hubble work.
- Data minimisation: names, references, companies, dates, numbers and other high-cardinality identifiers replaced or removed where appropriate.
- Secure processing: work stayed within HMRC estate and controlled AWS/VPC/S3/Oracle environments.
- Model selection included security and provenance: SEC-BERT was niche and less assured, so it carried a supply-chain/model-provenance risk.
- Human-in-the-loop: predicted categories are advisory and should not drive automatic tax decisions.
- Explainability: LinearSVC and TF-IDF feature coefficients are easier to explain than transformer decisions.
- Non-compliance risks: GDPR breach, legal challenge, reputational damage, loss of public trust, invalid decisions, operational rollback, and financial penalties.

### S14: Work with software engineers on testing and documentation

- Hubble is complex and has multiple users/developers.
- Principle: changes should be backed by tests; if a function has no test, create one before changing it.
- Tests should pass before pushing to main.
- Documentation includes README setup, `.md` docs, project choices, and usage guidance.
- Unit tests cover functions; integration-style tests cover complex varied input cases.
- Reflection: tests take effort but reduce risk, speed future change, and help new contributors understand expected behaviour.

### S16: Data management infrastructure

- Example: controlled access to S3 data through a proxy and a distribution list.
- Result: only users who needed access had access.
- Trade-off: proxy added reliability and performance issues.
- Future improvement: lakehouse access controls should offer more user-level permissions, reducing the need for slower proxy workarounds.
- Link to Hubble: requirements include secure storage, scalable compute, controlled access, database outputs, and integration with enterprise/private/public cloud resources.

### S19: Scalable infrastructure and services

- Native AWS scalable services can be easier to set up and back up, but may be expensive and opaque even with low usage.
- For smaller projects, fixed-price systems or EC2 can be more predictable.
- ODC is better for large burst jobs: spin up 128-core or GPU resources, process the backlog, then shut down.
- Dynamic parallel work allocation matters because iXBRL documents vary in size; static splitting can leave cores idle.
- Answer frame: scalability includes technical throughput and financial sustainability.

### S20: Efficient algorithms/APIs for large data access and analysis

- Hubble processes large volumes of iXBRL documents with parallel processing.
- ODC allows many documents/returns to be processed in parallel without affecting the main platform.
- Outputs are stored in a database rather than loose files, making them easier to query and join.
- dbplyr allows tidyverse-style R analysis while pushing work to SQL/database systems.
- Efficient design is not only algorithmic complexity; it includes data locality, database access, batching, parallelism, and avoiding repeated manual file movement.

### S23 and B7: Disseminating practice and sharing best practice

- Shares AI/data science practice through wikis, Teams channels, direct mentoring, demos, documentation, setup scripts, and project guidance.
- Shares iXBRL/LLM learning externally through Graffiti and engagement with leading iXBRL experts.
- Best-practice themes: environment setup, secure data access, model limitations, human-in-the-loop use, reproducibility, testing, documentation, and responsible AI.
- Reflection: AI best practice changes quickly; document principles and update guidance when tools or risks change.

### S26: Selecting and applying appropriate AI/data science techniques

- Started with simple baselines such as cosine similarity and Naive Bayes.
- Compared classical ML, neural networks, transformer embeddings, and fine-tuned models.
- Chose final technique using performance, cost, speed, explainability, maintainability, security, infrastructure fit, and business need.
- Important distinction:
  - Experimental learning: MLP/BERT/CNN/RNN work helped test what was possible.
  - Operational recommendation: TF-IDF plus LinearSVC is the stronger professional-discussion answer because it is explainable, CPU-friendly, and meets governance/maintenance constraints.

### S28: Independent and impartial decision-making

- Situation: different stakeholders preferred different models and metrics; accuracy and transformer models were attractive but incomplete decision criteria.
- Actions:
  - Listened to analysts, SMEs, technical colleagues and managers.
  - Set objective comparison criteria before selecting the model.
  - Used macro-F1 for imbalanced taxonomy classes while still monitoring accuracy.
  - Compared speed, explainability, security, maintainability, cost and infrastructure.
- Result: selected the model that fit HMRC use, not the most fashionable model.
- Reflection: impartiality is easier when the decision matrix and evidence are agreed before results are known.

### B1: Work ethic and standards

- Completed QA material, workshop preparation, notes and optional reading.
- Investigated topics beyond surface level when confused, such as how quantum computing speed-up depends on specific algorithms like quantum Fourier transform, not vague "parallelism".
- Assessment result recorded in the journal: last assessment was 80%.
- Answer angle: standards are met through preparation, curiosity, evidence, documentation, testing, and honest limitation-setting.

### B4: Initiative and ownership

- No off-the-shelf solution existed for tagging unstructured iXBRL data.
- Took ownership of the technical direction, built proof-of-concepts, handled extraction, cleaning, training, validation and reporting.
- Troubleshot GPU/compute limitations and reconfigured workflows for available infrastructure.
- Produced a validated proof of concept and business case for ML in data profiling.
- Answer angle: ownership means seeing the problem through, not just contributing code.

### B5: Continuous professional development

- Uses QA material, optional recommended books, documentation, papers, online sources, and practical experimentation.
- Prioritises learning because not every recommended source can be read at once.
- Applies learning directly: scikit-learn, TensorFlow/Keras, Hugging Face, Optuna, MLflow, MLOps, legal/ethical issues, bias/uncertainty, DataOps and cloud ML.
- Converts learning into team practice through documentation, demos, setup scripts, wiki guidance, and mentoring.

### B8: Awareness of trends and innovation

- Reviewed transformer literature such as Vaswani et al. and Rothman.
- Studied Hugging Face documentation and GitHub repositories for practical fine-tuning.
- Tracks iXBRL, LLM, MCP/tool-use, MLOps, drift detection, model monitoring, explainability, responsible AI, and governance trends.
- Strategic point: staying current is not academic decoration; it makes model choices defensible and helps avoid obsolete practice.

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

## Ready-to-say answer prompts

Use these as rehearsable outlines. Do not memorise word-for-word; keep the first-person evidence and the judgement.

### Tell me about a complex AI/data science problem you solved

- Situation: iXBRL accounts/tax computations contain many untagged financial figures, so analysts could not profile the full data population.
- Task: I needed to classify inconsistent free-text descriptions into standard taxonomy concepts.
- Action: I built the extraction and modelling pipeline, compared baselines, classical ML, neural networks and transformer approaches, cleaned/canonicalised the data, handled class imbalance, and evaluated with macro-F1, accuracy, per-class metrics, confusion matrices, speed, cost and explainability.
- Result: Hubble expanded usable analytical coverage, reduced manual grouping, and gave analysts more consistent categories for profiling and risk analysis.
- Reflection: the key judgement was choosing a model that was good enough technically and fit HMRC governance, cost, infrastructure and maintainability constraints.

### How did you select the most appropriate AI or ML technique?

- I did not start with a preferred model. I compared rule-like/simple similarity, Naive Bayes, Random Forest, LinearSVC, neural networks, embeddings, BERT and SEC-BERT.
- I used a decision matrix: macro-F1, accuracy, per-class behaviour, inference speed, training cost, explainability, maintainability, security/provenance and deployment complexity.
- SEC-BERT was attractive because it used financial language, but it needed GPU training, was slower, harder to explain, and had provenance concerns.
- TF-IDF plus LinearSVC was a stronger operational fit because descriptions were short/domain-specific, inference was CPU-fast, feature coefficients were explainable, and performance was strong.
- Closing judgement: "The best model was not the most advanced model; it was the model that met the business objective safely and sustainably."

### How did you evaluate whether the solution was successful?

- Technical: macro-F1, accuracy, precision, recall, confusion matrices, per-class metrics, stratified splits, holdout testing and cross-validation.
- Operational: inference speed, training cost, CPU/GPU requirements, integration with R/Python workflow, and ability to run on ODC.
- Governance: DPIA, PII canonicalisation, secure processing, model provenance, explainability and human-in-the-loop guidance.
- User acceptance: analyst feedback, SME review of ambiguous taxonomy cases, and whether outputs could be used in profiles.
- Limitation: I would not claim the metric alone proves success; success is performance plus usable, governed deployment.

### How did you handle uncertainty, error and bias?

- Error: checked extraction issues, ambiguous descriptions, generic labels, and taxonomy inconsistencies.
- Bias: main risk was class imbalance and representation bias, not demographic bias. Common concepts had many examples and rare concepts had few.
- Mitigation: macro-F1, stratified evaluation, class weighting, per-class dashboards, confusion matrices, SME review and human-in-the-loop use.
- Uncertainty: some descriptions are intrinsically ambiguous without surrounding context; I would communicate low-reliability classes and avoid automated decisions.
- Reflection: uncertainty should be surfaced to users rather than hidden behind a single metric.

### How did you work with technical and non-technical stakeholders?

- Analysts: concrete examples, error cases, confusion matrices, how to interpret outputs.
- SMEs: taxonomy meaning, ambiguous descriptions, date/name handling, and domain edge cases.
- DevOps/software engineers: compute, deployment, dependencies, tests, documentation, ODC and data access.
- Managers: business value, cost, risk, timescales and decisions needed.
- Governance: DPIA, data minimisation, security, access controls and human oversight.
- Result: stakeholder input changed both the technical design and the communication approach.

### How did you adapt your communication style?

- I changed the level of abstraction by audience.
- For managers, I translated macro-F1 into "reliability across rare as well as common concepts" and CPU inference into "lower cost and easier deployment".
- For analysts, I used examples and limitations rather than model equations.
- For DevOps, I focused on reproducibility, dependencies, scheduling and infrastructure.
- For external audiences, I would remove sensitive HMRC architecture, volumes, and tax-risk use cases, using public or synthetic examples.

### How did you manage conflicting priorities?

- Conflict examples:
  - Accuracy versus macro-F1.
  - Transformer performance versus cost/explainability.
  - User demand for new data paths versus secure existing database access.
  - Scalable cloud services versus predictable cost.
  - Speed of delivery versus testing/documentation.
- Approach: gathered views, defined criteria, compared evidence, explained trade-offs and documented the decision.
- Result: selected solutions that balanced user need, business value, risk and maintainability.
- Reflection: respecting views does not mean accepting every request; it means making the decision transparently and impartially.

### How does your role support organisational objectives?

- HMRC objective: improve use of data to identify tax risks, support policy evidence and make better analytical decisions.
- Hubble: extracts and categorises more financial data, including untagged data that was previously hard to use.
- DAP: gives analysts modern R/Python capability and grew from one user to over 150 users.
- ODC: supports large-scale processing and ML experiments cost-effectively.
- Mentoring/documentation: increases team capability and reuse.
- Outcome: better analytical coverage, reduced manual effort and stronger risk identification.

### How did you ensure legal, ethical and regulatory compliance?

- Completed a DPIA before Hubble work.
- Processed data within HMRC-controlled environments.
- Applied data minimisation and PII canonicalisation for names, references, companies, dates and numbers where appropriate.
- Avoided unassured niche models for production because provenance and security mattered.
- Documented that predictions are advisory, with humans in the loop for material decisions.
- Used explainability as a model-selection criterion.
- Consequence of non-compliance: privacy breach, legal challenge, reputational damage, loss of trust, invalid decisions and operational rollback.

### Tell me about a time you challenged the norm

- Norm: rely only on tagged iXBRL data or manually maintained matching rules for untagged descriptions.
- Challenge: I proposed using tagged data as supervised labels to classify untagged descriptions at scale.
- Investigation: compared multiple methods and evaluated performance, cost, explainability and deployment constraints.
- Impact: reusable pipeline, more data available to analysts, reduced manual grouping, and a more evidence-based model-selection culture.
- Another example: challenged overly restrictive AI guidance that treated all ML like LLMs; provided detailed feedback and the guidance was changed.

### How have you shared best practice?

- Created wiki guidance for DAP users on environments, access and workflows.
- Shared project documentation, README setup, demos and analyst guidance.
- Used Teams channels and mentoring to spread AI/data science practice.
- Shared iXBRL/LLM learning externally through Graffiti and engagement with iXBRL experts.
- Best-practice topics: secure data access, reproducibility, testing, model limitations, human-in-the-loop use, and choosing appropriate models.

### How do you keep your AI/data science knowledge current?

- QA materials and optional recommended reading.
- Papers and books, including transformer literature and BERT/fine-tuning sources.
- Hugging Face, scikit-learn, TensorFlow/Keras and other documentation.
- iXBRL International and sector sources.
- Practical experimentation with BERT, SEC-BERT, embeddings, CNN/MLP/RNN, LinearSVC, Optuna and MLflow.
- I convert learning into practice through docs, demos, wiki pages and project decisions.

### What are the risks of non-compliance in your work?

- GDPR/Data Protection Act breach.
- Loss of public trust.
- Legal challenge or invalid analytical/operational decisions.
- Reputational damage to HMRC.
- Security incident if data leaves controlled environments or unassured models are used.
- Operational rollback and wasted delivery effort.
- Possible financial penalties in broader organisational contexts.

### How do mathematical principles underpin the methods you used?

- TF-IDF uses frequency and logarithmic inverse document frequency to weight terms.
- LinearSVC uses vector geometry and optimisation to find separating hyperplanes.
- Macro-F1 uses precision and recall to avoid majority-class dominance.
- Cross-validation uses sampling logic to estimate generalisation.
- Paired t-tests and Welch's t-test use inferential statistics to test whether observed differences are likely meaningful.
- Neural networks use linear algebra, activation functions, calculus, gradients and backpropagation.
- Transformers use matrix operations and attention to model token relationships.

### How did you ensure suitable testing and documentation?

- Principle: changes should have tests; if no test exists, create one before changing the function.
- Run tests before pushing to main.
- Use unit tests for functions and integration-style tests for complex varied documents.
- Maintain README setup and `.md` project documentation.
- Use GitLab issues, epics, milestones and templates for traceability.
- Use MLflow and versioned artefacts for model experiments.
- Result: easier onboarding, safer change, and better auditability.

### How would you handle model drift or declining performance?

- Contain: remind users that predictions are advisory.
- Detect: monitor prediction distribution, class frequencies, extraction volume, taxonomy changes, holdout macro-F1, per-class metrics and analyst feedback.
- Diagnose: distinguish data drift, concept drift, taxonomy drift, extraction failure, preprocessing bug or model degradation.
- Act: roll back if needed, fix extraction/preprocessing, retrain, update labels, or adjust guidance for low-reliability classes.
- Communicate: warn analysts/managers about affected outputs and limitations.

### What are the social impacts of AI adoption in your organisation?

- Positive: better use of submitted data, improved tax-risk identification, reduced manual effort, more consistent analysis, and stronger public revenue evidence.
- Risks: over-automation, reduced trust, privacy breaches, opaque decisions, bias against underrepresented groups/classes, and staff resistance.
- Mitigation: transparency, human oversight, clear limitations, accessible guidance, governance, monitoring and proportional model choice.
- Wider point: in public sector AI, technical performance is not enough; fairness, accountability and explainability are central to legitimacy.

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

## Formula-level technical answer bank

This section is for questions where the assessor asks "what does that mean?", "why did you use it?", or "what are the strengths and weaknesses?". Use a plain-English explanation first, then the formula if useful.

### Confusion matrix terms

For one class treated as positive:

- True Positive (TP): model predicted the class and it was correct.
- False Positive (FP): model predicted the class but the true class was different.
- False Negative (FN): true class was this class but the model missed it.
- True Negative (TN): model correctly predicted something else.

In a multi-class problem like iXBRL taxonomy classification, calculate these per class by treating that class as positive and all other classes as negative.

### Accuracy

Formula:

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

What it is:

- The proportion of all predictions that are correct.

When to use it:

- Useful when classes are reasonably balanced and every type of error has similar cost.
- Still useful as a secondary operational measure because common-class performance matters.

Strengths:

- Simple to explain to non-technical stakeholders.
- Gives a quick overall view of performance.

Weaknesses:

- Misleading with class imbalance. A model can get high accuracy by predicting common classes and failing rare but important classes.
- In Hubble, common taxonomy concepts dominate, so accuracy alone would hide poor performance on minority concepts.

Hubble answer:

"I monitored accuracy, but I did not use it as the main model-selection metric because the taxonomy labels were highly imbalanced. Accuracy would reward the model for doing well on common concepts even if it failed on rare concepts."

### Precision

Formula:

```text
Precision = TP / (TP + FP)
```

What it is:

- Of everything predicted as a class, how many were actually that class?

When to use it:

- Use when false positives are expensive.
- Example: if a predicted tax-risk category triggers analyst review, low precision wastes analyst time.

Strengths:

- Measures trustworthiness of positive predictions.
- Good for prioritisation when resource is limited.

Weaknesses:

- Can be high while recall is poor. The model may be very cautious and miss many true cases.

Hubble answer:

"Precision tells analysts how much they can trust predictions for a concept. If precision is low for a concept, I would flag that the model often over-predicts it and analysts should review those cases more carefully."

### Recall

Formula:

```text
Recall = TP / (TP + FN)
```

What it is:

- Of all real examples of a class, how many did the model find?

When to use it:

- Use when false negatives are expensive.
- Examples: medical screening, fraud detection, or missing a rare but important financial concept.

Strengths:

- Shows whether the model misses important cases.
- Useful for risk-identification work where missing a class may matter more than generating extra review cases.

Weaknesses:

- Can be high while precision is poor. The model may find most true cases but also produce many false positives.

Hubble answer:

"Recall matters where the business wants to avoid missing relevant concepts, but I would balance it with precision so analysts are not overwhelmed by false positives."

### F1 score

Formula:

```text
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

What it is:

- The harmonic mean of precision and recall.

Why harmonic mean matters:

- It penalises extreme imbalance. If precision is high but recall is near zero, F1 stays low.

When to use it:

- Use when both false positives and false negatives matter.
- Good for classification problems where accuracy is not enough.

Strengths:

- Balances precision and recall in one metric.
- More informative than accuracy on imbalanced classification.

Weaknesses:

- Does not show whether the issue is precision or recall, so still inspect both.
- Does not include TN, so it is not a complete picture for every problem.

Hubble answer:

"F1 helped me compare whether a model was both finding concepts and avoiding over-predicting them. I still reviewed per-class precision and recall to understand the failure mode."

### Macro-F1

Formula:

```text
F1_k = 2 * (Precision_k * Recall_k) / (Precision_k + Recall_k)
Macro-F1 = (1 / K) * sum(F1_k for k = 1 to K)
```

Where:

- `K` is the number of classes.
- `F1_k` is the F1 score for class `k`.

What it is:

- Calculate F1 separately for each class, then take the arithmetic mean.
- Every class has equal weight, regardless of how many examples it has.

When to use it:

- Use for imbalanced multi-class classification where minority classes still matter.
- This is why it fits Hubble: rare iXBRL concepts may still be analytically important.

Strengths:

- Prevents common classes from dominating the metric.
- Forces attention on performance across the taxonomy, not only the largest labels.
- Aligns with fairness/robustness concerns in non-demographic imbalance.

Weaknesses:

- Can look harsh if many rare classes have very little training data.
- Can overweight classes that are too rare to evaluate reliably.
- Needs support counts and per-class metrics alongside it.

Hubble answer:

"I used macro-F1 because Hubble had hundreds of taxonomy concepts with a long tail of rare classes. Accuracy would mostly tell me about common concepts; macro-F1 told me whether the model worked across the taxonomy."

### Micro-F1 and weighted-F1

Micro-F1:

```text
Micro-F1 = F1 calculated after summing TP, FP and FN across all classes
```

- Good for overall instance-level performance.
- Weakness: dominated by frequent classes.

Weighted-F1:

```text
Weighted-F1 = sum((support_k / N) * F1_k for k = 1 to K)
```

- Weights each class by its number of examples.
- More balanced than accuracy but still gives more influence to common classes.

Hubble answer:

"I would report micro or weighted F1 as secondary metrics, but macro-F1 was better for model selection because rare taxonomy concepts should not disappear from the evaluation."

### TF-IDF

Formulas:

```text
TF(t, d) = count of term t in document d / total terms in document d
IDF(t) = log(N / df(t))
TF-IDF(t, d) = TF(t, d) * IDF(t)
```

Where:

- `t` is a term.
- `d` is a document or description.
- `N` is the total number of documents/descriptions.
- `df(t)` is the number of documents containing term `t`.

What it is:

- A way to convert text into numeric features.
- Common words get lower weight; rarer discriminative terms get higher weight.

When to use it:

- Short text classification.
- Search and information retrieval.
- Domain-specific text where specific words or phrases carry strong signal.

Strengths:

- Fast and CPU-friendly.
- Interpretable: you can inspect important words/ngrams.
- Works well with sparse linear models such as LinearSVC.
- Good where domain terms such as accountancy descriptions are distinctive.

Weaknesses:

- Does not understand word order beyond chosen n-grams.
- Does not truly understand synonyms or context.
- Vocabulary can drift if new terminology appears.
- Rare misspellings or inconsistent descriptions can create noisy features.

Hubble answer:

"TF-IDF was suitable because many financial descriptions are short and domain-specific. Words and phrases such as accounting terms are strong signals. Its interpretability also helped because I could explain which terms drove classifications."

### N-grams

Formula idea:

```text
Unigram = one token: "interest"
Bigram = two tokens: "interest receivable"
Trigram = three tokens: "interest receivable income"
```

When to use:

- Use when phrase meaning matters.
- In Hubble, concepts may depend on multi-word descriptions rather than single words.

Strengths:

- Captures phrases that unigrams miss.
- Still simple and interpretable.

Weaknesses:

- Increases feature count and sparsity.
- Can overfit rare phrases if not regularised.

### LinearSVC / linear SVM

Decision function:

```text
score_c(x) = w_c . x + b_c
predicted class = argmax_c(score_c(x))
```

Hinge-loss objective, simplified:

```text
minimise: 0.5 * ||w||^2 + C * sum(max(0, 1 - y_i * (w . x_i + b)))
```

What it is:

- A support vector machine finds a decision boundary that separates classes with the largest margin.
- LinearSVC uses a linear boundary and is optimised for large sparse datasets, especially text classification.

When to use it:

- High-dimensional sparse text data.
- Multi-class classification where a linear boundary is adequate.
- Situations needing speed, repeatability, and some interpretability.

Strengths:

- Performs well with TF-IDF.
- Fast inference on CPU.
- Handles high-dimensional sparse features.
- Coefficients can show which terms push a prediction toward a class.
- Easier to govern and maintain than a large transformer.

Weaknesses:

- Linear boundary may miss complex non-linear relationships.
- Not naturally probabilistic; calibrated probabilities require extra work.
- Can struggle if synonym/context understanding is needed.
- Hyperparameters such as `C`, penalty and class weights matter.

Hubble answer:

"LinearSVC was the best operational fit because it worked well with sparse TF-IDF features, had strong macro-F1, ran quickly on CPU, and was much easier to explain and maintain than a transformer."

### SVM kernel trick

Idea:

```text
Original features -> transformed higher-dimensional feature space -> linear separation there
```

What it is:

- A kernel lets SVM learn non-linear boundaries by comparing points as if they were in a higher-dimensional space.

When to use it:

- Use RBF or polynomial kernels when the relationship is non-linear and the dataset is not too large.

Strengths:

- Powerful for complex boundaries.

Weaknesses:

- Slower and less scalable than LinearSVC.
- Kernel and gamma choices can cause overfitting or underfitting.
- Less suitable for very large sparse text datasets.

Hubble answer:

"I focused on LinearSVC rather than kernel SVM because Hubble had high-dimensional sparse text features and needed scalable training and fast inference."

### Regularisation

L1:

```text
Loss + lambda * sum(|w_j|)
```

L2:

```text
Loss + lambda * sum(w_j^2)
```

What it is:

- Regularisation penalises overly complex models to reduce overfitting.

When to use it:

- Use whenever the model has many features or overfitting risk.
- Especially relevant for TF-IDF because the feature space can be very large.

Strengths:

- Improves generalisation.
- L1 can drive coefficients to zero, acting like feature selection.
- L2 shrinks weights smoothly and is often stable.

Weaknesses:

- Too much regularisation underfits.
- Too little regularisation overfits.

Hubble answer:

"Regularisation mattered because TF-IDF creates many sparse features. L1 regularisation helped by setting unhelpful features to zero, improving simplicity and interpretability."

### Class weighting

Typical idea:

```text
weight_k = N / (K * n_k)
```

Where:

- `N` is total examples.
- `K` is number of classes.
- `n_k` is examples in class `k`.

What it is:

- Increase the penalty for mistakes on rare classes.

When to use it:

- Imbalanced classification.

Strengths:

- Helps minority classes influence training.
- Easy to implement in scikit-learn.

Weaknesses:

- Can reduce performance on common classes.
- Can make the model over-sensitive to noisy rare labels.

Hubble answer:

"I used class weighting because the taxonomy had dominant classes and a long tail. It helped stop the model from optimising only for common concepts."

### Cross-validation

K-fold process:

```text
Split data into K folds
For each fold:
  train on K-1 folds
  validate on the remaining fold
Average the validation scores
```

Stratified cross-validation:

- Keeps class proportions similar in each fold.

When to use it:

- Model comparison and hyperparameter tuning.
- Especially useful when one train/test split may be unrepresentative.

Strengths:

- More robust estimate of generalisation.
- Reduces dependence on a lucky or unlucky split.

Weaknesses:

- More computationally expensive.
- Must avoid leakage: preprocessing that learns from data should be fitted inside each training fold.

Hubble answer:

"I used stratified evaluation because the class distribution was imbalanced. That reduced the risk that rare classes disappeared from one split and distorted the metric."

### Paired t-test for model comparison

Formula:

```text
t = mean(d) / (sd(d) / sqrt(n))
```

Where:

- `d` is the paired difference in score between two models on the same folds/runs.
- `n` is the number of paired observations.

What it is:

- Tests whether the mean difference between paired results is likely different from zero.

When to use it:

- Comparing two models evaluated on the same folds or same repeated splits.

Strengths:

- Controls for split-to-split variation because both models are tested on the same data partitions.

Weaknesses:

- Assumes the paired differences are approximately normally distributed.
- Statistical significance may not equal practical significance. A tiny improvement can be statistically significant but not worth extra cost.

Hubble answer:

"Where a model had a tiny metric improvement, I considered whether it was practically meaningful. For example, a very small gain was not worth a 67x slowdown or a GPU dependency."

### Welch's t-test

Formula:

```text
t = (mean_1 - mean_2) / sqrt((s_1^2 / n_1) + (s_2^2 / n_2))
```

What it is:

- Compares two means when variances may be unequal.

When to use it:

- Two independent groups.
- Numeric ratio/interval data.
- Population standard deviation unknown.
- Variances unequal, often checked with an F-test or by inspection.

Strengths:

- Safer than Student's t-test when variances differ.

Weaknesses:

- Still assumes reasonably normal data or large enough samples.
- Sensitive to outliers.

Journal answer:

"For the agent risk comparison, I used Welch's t-test after an F-test indicated unequal variances. That let me test whether the apparent difference was statistically meaningful rather than relying only on qualitative judgement."

### Z-test

Formula:

```text
z = (sample_mean - population_mean) / (sigma / sqrt(n))
```

For two proportions:

```text
z = (p1 - p2) / sqrt(p * (1 - p) * (1/n1 + 1/n2))
```

What it is:

- Compares means or proportions using the normal distribution.

When to use it:

- Large sample size, often n >= 30.
- Population variance/standard deviation known for mean comparison, or proportion comparison with adequate counts.

Strengths:

- Simple and powerful with large samples.

Weaknesses:

- Not appropriate where variance is unknown and samples are small.

### Chi-square test

Formula:

```text
chi-square = sum((observed - expected)^2 / expected)
```

What it is:

- Tests whether categorical variables are associated, or whether observed category frequencies differ from expected frequencies.

When to use it:

- Categorical data.
- Example: association between user type and tool adoption, or comparing observed class distribution to an expected distribution.

Strengths:

- Good for counts and categories.

Weaknesses:

- Needs adequate expected counts.
- Shows association, not causation.

### Naive Bayes

Bayes' theorem:

```text
P(class | features) = P(features | class) * P(class) / P(features)
```

Naive assumption:

```text
P(features | class) = P(feature_1 | class) * P(feature_2 | class) * ... * P(feature_n | class)
```

What it is:

- Probabilistic classifier assuming features are conditionally independent given the class.

When to use it:

- Text classification, spam filtering, small datasets, high-dimensional sparse features.

Strengths:

- Very fast.
- Works surprisingly well for text.
- Good baseline.

Weaknesses:

- Independence assumption is unrealistic.
- Can be poorly calibrated.
- Does not learn interactions between terms.

Hubble answer:

"Naive Bayes was useful as a simple baseline, but the final model needed stronger performance and better handling of the taxonomy classes."

### Logistic regression

Formula:

```text
p = 1 / (1 + e^-z)
z = b + w_1*x_1 + ... + w_n*x_n
```

What it is:

- Classification model that predicts probabilities using the sigmoid function.

When to use it:

- Binary classification, or multi-class using one-vs-rest/softmax variants.
- When interpretability and probability outputs matter.

Strengths:

- Interpretable coefficients.
- Fast and strong baseline.
- Probabilistic output.

Weaknesses:

- Linear decision boundary unless features are engineered.
- Can underfit complex relationships.

### Decision tree

Core idea:

```text
Choose feature splits that reduce impurity
```

Gini impurity:

```text
Gini = 1 - sum(p_k^2)
```

Entropy:

```text
Entropy = -sum(p_k * log2(p_k))
```

What it is:

- A tree of feature-based decisions leading to a class/value.

When to use it:

- Interpretable tabular classification/regression.

Strengths:

- Easy to explain.
- Handles non-linear relationships.
- Little preprocessing required.

Weaknesses:

- Overfits easily.
- Unstable: small data changes can create different trees.
- Less suited to very high-dimensional sparse text than linear models.

### Random Forest

Formula idea:

```text
Prediction = majority vote of many decision trees
```

What it is:

- Ensemble of decision trees trained on bootstrap samples and random feature subsets.

When to use it:

- Strong tabular baseline where interpretability is less critical than a single tree.

Strengths:

- Reduces variance and overfitting compared with one tree.
- Handles non-linear relationships.
- Provides feature importance.

Weaknesses:

- Less interpretable.
- Heavier to train and predict.
- Can be less efficient for sparse text than LinearSVC.

### K-means clustering

Objective:

```text
minimise sum(||x_i - centroid_assigned_to_i||^2)
```

What it is:

- Unsupervised method that partitions points into `K` clusters by nearest centroid.

When to use it:

- Exploring unlabelled data, grouping similar descriptions, customer/document segmentation, anomaly exploration.

Strengths:

- Simple, fast and scalable.

Weaknesses:

- Must choose `K`.
- Sensitive to outliers and initial centroids.
- Assumes roughly spherical clusters of similar size.

Hubble angle:

"K-means could help explore groups of descriptions, but because Hubble had labelled tagged concepts, supervised learning was more appropriate for the final classification task."

### PCA

Core idea:

```text
Find orthogonal directions that explain maximum variance
```

What it is:

- Dimensionality reduction method using linear algebra/eigenvectors/SVD.

When to use it:

- Visualisation, noise reduction, reducing correlated numeric features.

Strengths:

- Reduces dimensionality and can speed later modelling.

Weaknesses:

- Components are not directly interpretable.
- Linear method.
- Sensitive to feature scaling.

### Neural network / MLP

Neuron:

```text
output = activation(w . x + b)
```

Common activations:

```text
ReLU(x) = max(0, x)
Sigmoid(x) = 1 / (1 + e^-x)
Softmax(z_i) = exp(z_i) / sum(exp(z_j))
```

Training:

- Forward pass makes prediction.
- Loss function measures error.
- Backpropagation calculates gradients.
- Optimiser such as SGD or Adam updates weights.

When to use it:

- Complex non-linear relationships, image/text/speech tasks, enough data and compute.

Strengths:

- Flexible and powerful.
- Can learn non-linear interactions.

Weaknesses:

- Harder to explain.
- Needs tuning and more compute.
- Can overfit.
- More operational complexity than LinearSVC.

Hubble answer:

"I built neural-network prototypes to test whether non-linear models would improve classification. They were useful experimentally, but the final operational decision also had to consider explainability, speed, governance and maintainability."

### CNN for text

What it is:

- Convolutional filters slide over sequences and learn local patterns.

When to use it:

- Images, and also text classification where local word patterns are useful.

Strengths:

- Learns phrase-like local features.
- Can be faster than recurrent models.

Weaknesses:

- Less interpretable than TF-IDF coefficients.
- Needs tuning and labelled data.

### RNN and LSTM

What it is:

- RNNs process sequences step by step with a hidden state.
- LSTMs add gates to remember/forget information and reduce vanishing-gradient problems.

When to use it:

- Time series, language modelling, sequential data where order matters.

Strengths:

- Designed for sequence dependence.

Weaknesses:

- Slower than transformers because processing is sequential.
- Harder to train; can still suffer from gradient issues.
- Often unnecessary for short financial descriptions.

### Transformer and BERT

Self-attention idea:

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

What it is:

- Transformer models use self-attention so each token can attend to other tokens.
- BERT is bidirectional and pre-trained using masked language modelling and next-sentence prediction.
- SEC-BERT is domain-pretrained on financial/accounting text.

When to use it:

- NLP tasks needing context, synonym handling, semantics, question answering, named entity recognition, or complex text classification.

Strengths:

- Strong language understanding.
- Handles context better than TF-IDF.
- Domain models may understand specialist terminology better.

Weaknesses:

- Large and slow.
- Often needs GPU for fine-tuning.
- Harder to explain.
- Supply-chain/provenance risk if using niche models.
- More expensive to maintain and deploy.

Hubble answer:

"SEC-BERT was technically attractive because it is trained on financial language, but the operational trade-off was poor: GPU requirement, slower training/inference, weaker explainability, and model-provenance concerns. The extra complexity did not justify the marginal performance difference for HMRC."

### Embeddings

What they are:

- Dense numeric vectors representing semantic meaning.

When to use:

- Similarity search, semantic clustering, retrieval, and classification where synonyms/context matter.

Strengths:

- Can group related phrases even when words differ.

Weaknesses:

- Generic embeddings may miss specialist accountancy meanings.
- Less directly interpretable.
- Can be slower than TF-IDF.

Hubble answer:

"I tested embeddings such as MPNet/e5-style approaches. They can capture semantic similarity, but the practical gain was too small compared with the speed and explainability cost."

### Model drift

Types:

- Data drift: input distribution changes.
- Concept drift: relationship between input and label changes.
- Label/taxonomy drift: taxonomy concepts or tagging practice changes.
- Extraction drift: upstream HTML/iXBRL structure changes.

Monitoring:

- Prediction distribution.
- Class frequency.
- Per-class precision/recall/F1 where labels exist.
- Macro-F1 on fixed holdout set.
- Data-quality checks.
- Analyst feedback.
- Taxonomy/version changes.

Strengths of monitoring:

- Finds degradation before users lose trust.
- Supports accountable model lifecycle.

Weaknesses:

- Needs labelled feedback or delayed ground truth for true performance monitoring.
- Thresholds need business judgement.

Hubble answer:

"If Hubble went wrong, I would first contain the risk because outputs are advisory. Then I would check extraction, taxonomy changes, data drift, prediction distributions, holdout macro-F1, per-class errors and analyst feedback before retraining or rolling back."

### Data quality dimensions

Use these words when discussing testing and acceptance:

- Accuracy: data reflects reality.
- Completeness: required fields are present.
- Consistency: same meaning/format across systems.
- Validity: values fit expected rules.
- Timeliness: data is current enough for use.
- Uniqueness: duplicates are controlled.
- Lineage: source and transformations are known.
- Relevance: data supports the business question.

Hubble examples:

- Canonicalising names/dates/numbers improved consistency.
- Removing PII/noise improved relevance and privacy.
- Tracking document source and taxonomy supports lineage.
- Per-class performance checks reveal where model output is not reliable enough.

### Error, bias and uncertainty

Random error:

- Unpredictable variation, for example noisy extraction or inconsistent wording.

Systematic error:

- Consistent bias, for example a parser repeatedly misreading a table structure.

Bias types:

- Historical bias: past behaviour is embedded in data.
- Sample/selection bias: training data is not representative.
- Label bias: labels are inconsistent or wrong.
- Aggregation bias: group-level assumptions do not hold for subgroups.
- Confirmation bias: analysts look for evidence that supports existing beliefs.

Uncertainty types:

- Aleatoric uncertainty: irreducible noise.
- Epistemic uncertainty: lack of knowledge or data; can reduce with more data.
- Structural uncertainty: simplifications in the model or assumptions.
- Deep uncertainty: unclear future conditions or problem space.

Hubble answer:

"The main Hubble bias risk is not demographic fairness; it is class imbalance and representation bias across concepts, document types and preparer practices. I mitigated it with macro-F1, stratified splits, class weighting, per-class dashboards, confusion matrices, SME review and human-in-the-loop use."

### Data science lifecycle

CRISP-DM:

- Business understanding.
- Data understanding.
- Data preparation.
- Modelling.
- Evaluation.
- Deployment.

SEMMA:

- Sample.
- Explore.
- Modify.
- Model.
- Assess.

Hubble mapping:

- Business understanding: untagged iXBRL limits profiling and risk analysis.
- Data understanding: EDA on descriptions, concepts, imbalance, ambiguous labels, taxonomy coverage.
- Data preparation: extraction, cleaning, PII canonicalisation, label construction.
- Modelling: compare baselines, LinearSVC, neural networks, embeddings, transformers.
- Evaluation: macro-F1, accuracy, precision, recall, confusion matrices, speed, cost, explainability.
- Deployment: R/Python integration, ODC batch processing, Oracle outputs, analyst guidance.

### DataOps and MLOps

DataOps principles to mention:

- Collaboration, automation, reuse, analytics as code, testing, monitoring, short cycles, and data-driven improvement.

MLOps principles to mention:

- Reproducibility: retrain an old model and get comparable results.
- Accountability: trace production output to code, data, model and parameters.
- Collaboration: versioned work and asynchronous review.
- Continuous testing: evaluate through the lifecycle.
- Continuous monitoring: detect drift and degradation.
- Reusable infrastructure: avoid rebuilding every project from scratch.

Hubble application:

- GitLab issues, templates, epics and milestones.
- README and docs.
- Unit/integration tests.
- MLflow experiment tracking.
- Versioned notebooks/scripts.
- Holdout set and per-class metrics.
- Human-in-the-loop and analyst feedback.

### Data architecture options

Relational database / Oracle:

- Strength: structured querying, SQL, governance, joins, mature access control.
- Weakness: can be slower for text search or semi-structured document exploration.
- Hubble use: store structured extracted outputs for analysts.

Apache Solr/document search:

- Strength: fast distributed text search and document profiling.
- Weakness: not a relational analytics warehouse.
- Hubble context: useful for fast searching across document-like data.

Data lake:

- Strength: stores structured, semi-structured and unstructured data in native format; scalable and cost-effective for raw data.
- Weakness: can become a data swamp without governance, metadata and quality controls.

Data lakehouse:

- Strength: combines data-lake flexibility with warehouse-like governance, schema enforcement, transactions, BI support, open formats, decoupled storage/compute and APIs.
- Hubble future: move R/SparkR-style processing to EMR and outputs to Redshift/lakehouse-style architecture.

Data fabric:

- Strength: central layer over distributed data using metadata, semantic knowledge graphs, embedded ML and automation.
- Weakness: complex to implement and requires strong governance.

### Legal and governance quick answers

UK GDPR principles:

- Lawfulness, fairness and transparency.
- Purpose limitation.
- Data minimisation.
- Accuracy.
- Storage limitation.
- Integrity and confidentiality.
- Accountability.

Lawful bases:

- Consent, contract, legal obligation, vital interests, public task, legitimate interests.

Special category data:

- Race/ethnic origin, political opinions, religious/philosophical beliefs, trade union membership, genetic data, biometric data, health, sex life, sexual orientation.

Equality Act protected characteristics:

- Age, disability, gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual orientation.

Article 22:

- UK GDPR restricts solely automated decisions with legal or similarly significant effects unless a valid condition applies.

DPIA:

- Needed where processing is likely to be high risk.
- Hubble relevance: company accounts/tax documents can include names, references and sensitive context, so DPIA and minimisation were appropriate.

EU AI Act:

- Risk-based approach: unacceptable risk banned, high risk regulated, limited risk transparency duties, minimal risk free use.
- HMRC answer: not directly the main UK control, but the principles are useful for thinking about documentation, human oversight, robustness and risk assessment.

### Accessibility answer

What accessibility means here:

- UI accessibility where tools have interfaces.
- Alternative instructions where workflows assume mouse/drag actions.
- Clear documentation for technical and non-technical users.
- Outputs understandable by analysts, SMEs, managers, DevOps and governance reviewers.
- Avoiding hidden barriers caused by jargon, unclear confidence/performance warnings, or inaccessible dashboards.

Hubble/Graffiti answer:

"For Graffiti, the bookmarklet originally assumed users could drag it to the bookmark bar, so I added alternative guidance. More generally, I treat accessibility as designing the tool and documentation so users with different technical skills and needs can actually use the output safely."

### Communication by audience

Senior managers:

- Business problem, value, risk, cost, timescale, decisions needed.
- Translate metrics into consequences.

Analysts:

- Examples, confusion matrices, per-class reliability, how to use outputs, when to review raw descriptions.

SMEs:

- Taxonomy meaning, ambiguous concepts, edge cases, domain correctness.

DevOps/software engineers:

- Infrastructure, dependencies, deployment, memory, runtime, scheduling, tests, monitoring.

Governance reviewers:

- DPIA, data minimisation, security, access controls, model limitations, human oversight, auditability.

## Final preparation checklist

- Have at least one STAR example for every AM2 theme.
- Practise saying "I" rather than "we".
- Include a result or impact in every answer.
- Name a trade-off in every substantial technical answer.
- Mention governance, monitoring, and limitations without being prompted.
- Use Hubble examples, but also draw on wider workplace/course learning where AM2 asks broader professional practice.
- Do not overclaim model reliability. Explain where it fails and how users should handle that.
