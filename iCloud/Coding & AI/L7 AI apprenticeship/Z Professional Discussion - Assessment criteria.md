

**Artificial Intelligence Data Specialist — Level 7 Apprenticeship**  
**Learner:** Jesse Karadia  
**Organisation:** HMRC

This journal is organised around the EPA assessment criteria rather than treating every KSB as a separate interview question. Each criterion has a criterion-focused KSB list followed by one substantial STARR answer. The official grading table assesses the KSBs collectively within each theme, so the lists below are a practical evidence map rather than a claim that each criterion is formally marked in isolation.

Use these as speaking notes, not a script. Keep the first-person language, adapt the depth to the question, and be ready to identify supporting artefacts such as test results, decision matrices, GitLab issues, documentation, dashboards, DPIAs, stakeholder feedback, wiki guidance and model experiment records.

## TODO completion list — evidence gaps to fill

Search this file for `TODO:` to return to every gap. Replace each item with short factual notes and, where possible, the name or location of an artefact. Do not add sensitive operational details that cannot be discussed in the EPA.

### Theme 1 TODOs

- [ ] **TODO: Methodologies actually used** — Add any workplace example where I personally used an unsupervised method (for example clustering, PCA or anomaly detection). If I have not used one, keep the current explanation that I considered it but did not select it. Add a machine-vision example only if I genuinely used one; otherwise keep the explanation of why it was not appropriate to Hubble.
- [ ] **TODO: Hubble evaluation figures** — Add the final LinearSVC macro-F1/accuracy, holdout size, number of records, class count, inference/training time and the equivalent SEC-BERT figures. Confirm whether “two percentage points better” is correct and whether the comparison was on the same split.
- [ ] **TODO: Statistical significance wording** — Confirm the exact test, number of folds/runs, assumptions checked, p-value/confidence interval and effect size for the model comparisons. Five cross-validation folds may not support a strong significance claim, so record the limitation precisely.
- [ ] **TODO: Acceptance and usability evidence** — Add dates or approximate period, number/types of users, how feedback was collected, the agreed acceptance criteria and the artefacts that show the resulting blank-description, dimensional-data and dashboard changes.
- [ ] **TODO: Simulation evidence** — Add a genuine scientific simulation example if I used one at work. If not, retain the narrower statement that controlled model/hyperparameter experiments compared alternative pipeline scenarios and do not claim a separate simulation project.
- [ ] **TODO: Architecture classification** — Confirm which Hubble/DAP components count as enterprise, private-cloud and public-cloud resources in HMRC terminology, and add the names of any approved architecture or security documents I can mention.
- [ ] **TODO: Scale and performance** — Confirm the ODC core count, typical document volume, before/after runtime, Solr scale/resilience evidence, and whether “approximately 128 returns concurrently” is accurate.
- [ ] **TODO: API evidence** — List the exact database drivers/packages, Solr endpoints or query clients, S3/FSx interfaces and datasets I personally connected. Add a REST/API example only if I built or used one; do not describe a normal file copy as an API.
- [ ] **TODO: Long-format impact** — Verify the “days rather than nine months” comparison, identify the before/after process being compared and add an artefact or witness who can corroborate it.
- [ ] **TODO: Calculation-error impact** — Add a non-sensitive description of the material incorrect-figure issue: my precise role, what Hubble extracted, how the recreated calculation was validated and the resulting business action. Confirm whether “very large” can safely be quantified.

### Theme 2 TODOs

- [ ] **TODO: Quantified organisational outcomes** — Verify the 233% increase, 150+ DAP users and “millions of pounds” claim. Record the measurement period, baseline/definition and a safe supporting artefact or witness for each.
- [ ] **TODO: Leadership evidence** — Add one named or anonymised example of someone I mentored, what I did, what they could do afterwards and how that improved organisational practice. Add any feedback received.
- [ ] **TODO: Audience-specific communication** — Add the actual meetings, dashboards, decision paper or presentation used to explain the model choice to technical and non-technical audiences, plus one example of how the explanation changed.
- [ ] **TODO: External dissemination and industry impact** — Add where/how Graffiti was shared, the external audience, approximate reach or feedback, and one concrete change or insight it prompted. Current evidence demonstrates sharing more strongly than proven improvement to industry practice.
- [ ] **TODO: Wider social-context evidence** — Add the particular sources or current issues I critically analysed, when I shared the findings, with whom, and how the findings changed a decision or working practice. Preserve links/titles where they are safe to cite.
- [ ] **TODO: AI-guidance challenge** — Add the approximate date, my precise written feedback, who considered it, what wording/process changed and where the revised guidance can be evidenced.
- [ ] **TODO: Impartial decision records** — Add one specific DAP decision with the stakeholders' conflicting positions, decision criteria, final decision, business benefit and any written record.
- [ ] **TODO: Software-engineering collaboration** — Identify the engineers/contributors by role, how we worked together, the organisation's relevant testing/documentation requirements, test-suite size or coverage if known, and a concrete defect prevented or found.

### Theme 3 TODOs

- [ ] **TODO: Organisation/industry/society impact evidence** — Add a specific example at each level and distinguish demonstrated impact from potential future impact. Confirm which Hubble outcome can be discussed without exposing sensitive tax-risk information.
- [ ] **TODO: Ethical risk assessment details** — Add the main risks recorded in the DPIA, their ratings before/after mitigation, review/approval roles, review date and the artefact I can name. Do not copy sensitive contents into this journal.
- [ ] **TODO: Bias and monitoring** — Add actual per-class findings, any class-weighting or sampling used in the final model, thresholds for intervention, and whether operational drift/performance monitoring was implemented or is still a proposed improvement.
- [ ] **TODO: Trend-to-practice outcome** — Add a measured example of how Graffiti, model evaluation, MLOps guidance or another trend changed colleagues' speed, quality, reproducibility or decision-making.
- [ ] **TODO: Non-compliance requirements** — Name the organisational policies and the specific legal/regulatory requirements relevant to Hubble, plus how compliance was checked. If discussing penalties, verify the current official figure before the EPA rather than relying on memory.

### Theme 4 TODOs

- [ ] **TODO: Lawful basis and governance** — Confirm the lawful basis/purpose, retention expectations, controller/processor responsibilities and relevant HMRC approvals for the actual data used. Add only what I am authorised to discuss.
- [ ] **TODO: Accessibility evidence** — Add the product reviewed, WCAG version/level, issues identified, fixes I personally made, how they were tested and the outcome. For Graffiti, record the alternative installation method and any user feedback confirming it worked.
- [ ] **TODO: Diversity of users** — Add which user groups were consulted, what different needs they raised and one design change made for each relevant need; avoid claiming representative user testing if it did not occur.
- [ ] **TODO: Legal/IP/contract checks** — Add any actual dependency licences, model cards, supplier terms, intellectual-property or data-sharing checks completed. Keep the existing text as general knowledge if no workplace example exists.

### Theme 5 TODOs

- [ ] **TODO: CPD evidence** — Add dates and titles for the strongest papers, books, courses, workshops, community interactions or conferences, what I learned from each and the specific work decision it changed.
- [ ] **TODO: Team development** — Add how I assessed team skills, set or supported development goals, checked progress and gathered feedback. Current evidence is strongest on informal mentoring and guidance, so add formal responsibility only if it happened.
- [ ] **TODO: Final deployed-model status** — Confirm whether TF-IDF plus LinearSVC was fully deployed, recommended for deployment or remained a validated prototype at the relevant time. Use one description consistently throughout the document.
- [ ] **TODO: Final technique-selection evidence** — Add the decision-matrix headings/weights, final scores, approval route, production performance and a link/name for the experiment record, DPIA, model documentation or acceptance record.

---

# Theme 1: Use and knowledge of computing and statistical foundations of AI and data science

**Theme KSBs:** K7, K16, K18, K19, K22, K25, S1, S16, S19, S20, S26.

**Distinction integration:** The pass answers in this theme also identify the existing norm or assumption, the investigation undertaken, the solution proposed and its impact where that connection is natural. The standalone distinction answer remains the fullest version.

## Describes how to use statistical, AI and machine learning methodologies such as data mining, supervised/unsupervised machine learning, natural language processing and machine vision to meet business objectives

**Relevant KSBs:**

- K19 — principles and properties behind statistical and machine learning methods
- K22 — relationship between mathematical principles and core AI/data science techniques
- K25 — programming languages and modern machine learning libraries
- S26 — selecting and applying appropriate AI and data science techniques

### STARR — selecting methodologies for Hubble

**Situation:** Company accounts and tax computations are submitted as iXBRL, but some tax computations had only about 30% of their figures tagged. Conventional extraction therefore omitted much of the available information. Hubble could extract the untagged descriptions, but the same accounting concept could be expressed in many different ways, making population-level profiling impractical through manually maintained regular expressions.

**Task:** I needed to turn inconsistent, untagged descriptions into standard taxonomy concepts so analysts could profile a much larger proportion of the data and identify tax risk more efficiently. I also needed to decide which statistical, AI and machine-learning methods actually suited this business problem.

**Action:** I treated the work as an NLP classification problem and built an evidence-led comparison rather than selecting a fashionable model. This challenged the established assumption that population analysis had to rely on tagged items or manually maintained matching rules: I investigated whether tagged descriptions could instead provide supervision for classifying untagged content. I used descriptive analysis and data mining to understand concept frequencies, description overlap, ambiguous labels, rare classes and model error patterns. Because tagged items provided labels, supervised learning was the main operational approach. I compared cosine similarity, Naive Bayes, Decision Trees, Random Forest, SVC, LinearSVC, SGDClassifier, neural networks, BERT/SEC-BERT and embedding models such as MPNet and e5. I also considered unsupervised embeddings and clustering for exploring latent groupings and anomalous or rare descriptions, but they did not provide the controlled standard taxonomy output the business needed. Machine vision was not appropriate because the relevant input was extracted text and document structure rather than pixels; using it would have added complexity without supporting the objective. I assessed candidates using macro-F1, accuracy, per-class results, cross-validation, speed, infrastructure, explainability, provenance, maintainability and cost.

**Result:** TF-IDF with LinearSVC was the strongest operational choice. SEC-BERT had about two percentage points better raw macro-F1 in testing, but required GPU infrastructure, was slower, less explainable and introduced package/model provenance concerns. LinearSVC ran on existing CPU infrastructure, produced useful results quickly, and exposed feature coefficients that helped explain classifications. The proposed reuse of tagged data as supervision made previously difficult-to-use untagged descriptions available in consistent categories, reduced dependence on manual matching and contributed to analysts identifying tax risk.

**Reflection:** Method selection must begin with the business objective, label availability, data type and deployment constraints. Supervised NLP was appropriate here; unsupervised methods remained useful for exploration, while machine vision and frontier LLMs were disproportionate. The best technical score alone does not define the best business solution.

### Technical detail / likely follow-up

- **Data mining:** frequency analysis, description overlap, ambiguity analysis, class distributions, rare-class investigation and error-pattern analysis.
- **Supervised learning:** tagged iXBRL concepts acted as labels for predicting concepts for untagged descriptions.
- **Unsupervised learning:** embeddings or clustering could expose groups and anomalies, but cluster identities would still require interpretation and would not guarantee alignment to the official taxonomy.
- **NLP pipeline:** parsing, lower-casing, whitespace/punctuation normalisation, PII canonicalisation, TF-IDF vectorisation and classification.
- **Machine vision:** suitable for image classification, object detection or segmentation, but not justified for already extractable text. If scanned PDFs became a source, OCR/document vision could become relevant.
- **Business objective:** wider analytical coverage, reduced manual grouping, faster profiling and stronger tax-risk identification.

## Explains how to solve problems and evaluate software solutions via analysis of test data and results from research, feasibility, acceptance and usability testing in line with organisational requirements

**Relevant KSBs:**

- K7 — problem solving and evaluation through research, feasibility, acceptance and usability testing
- S26 — selecting and applying the most appropriate technique

### STARR — evaluating the Hubble classification solution

**Situation:** Hubble could extract untagged iXBRL descriptions, but analysts could not practically profile them because descriptions were inconsistent and there were hundreds of taxonomy classes with a long tail of rare examples.

**Task:** I was responsible for defining the problem, researching feasible solutions, testing them objectively, and confirming that the chosen output was usable and met HMRC requirements for security, explainability, infrastructure and analyst adoption.

**Action:** I challenged the common practice of treating the highest headline accuracy or the most advanced model as the answer. I first defined success more broadly: the solution had to classify minority as well as common concepts, run at operational scale, remain explainable, use supportable technology, protect data and be usable by analysts. I researched classical ML, neural-network, transformer and embedding approaches. For feasibility, I assessed CPU/GPU requirements, throughput, cost, provenance, maintainability and whether the model could run on the estate. I created fixed train, test and holdout flags so every model used the same data splits. For scikit-learn models I used stratified cross-validation and HalvingRandomSearchCV; for neural networks and transformers I used Optuna. I compared macro-F1, accuracy, per-class performance, confusion matrices and runtime, and used paired-difference tests as an indicator of whether model differences were meaningful while recognising that five folds limited certainty. I proposed a decision matrix so model quality, operational feasibility and risk were evaluated together.

I then involved users in acceptance and usability testing. Analysts tested outputs and a dashboard. Their feedback exposed predictions being made from blank descriptions using only headings or table names, so I changed the production logic to return no prediction where the description was missing. Users also needed more dimensional data, so I generalised the extraction rather than coding only a narrow subset. The dashboard initially displayed the top five matches and scores, but users found low-quality alternatives and raw scores confusing, so I limited the display to more confident matches and added explanatory text. A remaining request for numeric rather than natural database keys is being treated as a performance question to test across Oracle and SAS, rather than accepting either preference without evidence.

**Result:** The chosen TF-IDF and LinearSVC approach balanced model quality with speed, explainability, supportability and security. Acceptance testing changed both the extraction and prediction behaviour, while usability testing made the dashboard clearer. The investigation changed the team's basis for evaluating solutions—from headline model performance alone to evidence across users, infrastructure and risk—and produced a technically credible solution analysts could use rather than a high-scoring prototype that failed organisational requirements.

**Reflection:** I learned to research established tooling before writing bespoke evaluation code; Optuna automated comparison and visualisation that I had partly built myself. I also learned that training, test and production preprocessing need a single controlled implementation so rules such as blank-description handling cannot diverge. In future I would agree acceptance criteria and test cases earlier, automate more pipeline parity checks, and retain a traceable risk/decision log.

### Technical detail / likely follow-up

- **Research:** model documentation, literature and tests across classical ML, embeddings, neural networks and transformers.
- **Feasibility:** technical, operational, security, maintenance and cost constraints; GPU availability; model provenance.
- **Test-data analysis:** fixed splits, stratification, cross-validation, holdout testing, macro-F1, per-class measures, confusion matrices and runtime.
- **Acceptance testing:** analysts checked whether extracted dimensions and classifications met the use case.
- **Usability testing:** dashboard feedback changed the number of alternatives shown and the explanation of scores.
- **Risk assessment:** class imbalance, misleading metrics, missing descriptions, unassured models, pipeline divergence and over-reliance on predictions.

## Describes the relationship between mathematical principles and core techniques in AI and data science within the organisational context

**Relevant KSBs:**

- K19 — statistical and machine-learning principles
- K22 — mathematics underpinning core techniques in organisational context

### STARR — the mathematics behind the Hubble model choice

**Situation:** Hubble needed to classify short, inconsistent accounting descriptions into a large and imbalanced set of standard concepts. Stakeholders needed both reliable outputs and an explanation of how the method worked.

**Task:** I needed to select and explain a technique whose mathematical properties suited sparse text, unequal class frequencies and HMRC's need for fast, supportable and interpretable processing.

**Action:** I represented each description as a numeric vector using TF-IDF. Term frequency captures how strongly a word occurs in a description, while inverse document frequency uses a logarithmic weighting to reduce the influence of words appearing throughout the corpus. This creates a high-dimensional sparse matrix. LinearSVC then uses vector geometry and optimisation to find separating hyperplanes between classes; an L1 penalty with `dual=False` was appropriate for the sparse feature space and drove many feature weights to zero, supporting both efficiency and interpretability. I also challenged the stakeholder preference for accuracy as the headline measure. My investigation showed that accuracy could hide poor treatment of rare concepts, so I proposed macro-F1, where each class contributes equally through its precision and recall. Stratified splits maintained class proportions, cross-validation estimated generalisation, and inferential tests helped judge whether apparent model differences were likely meaningful. In separate agent-risk work, I used an F-test to identify unequal variances and then Welch's t-test for two independent, approximately normal groups with unknown population variance.

**Result:** The mathematics supported an organisationally appropriate choice: TF-IDF and LinearSVC were fast on existing CPUs, explainable through feature coefficients and better aligned to minority concepts than selection on accuracy alone. Reframing evaluation around macro-F1 made rare-class performance visible and gave stakeholders a more impartial basis for comparison. The agent-risk analysis also replaced a qualitative suspicion with quantitative evidence at a 99% confidence level.

**Reflection:** Mathematical principles are not an abstract add-on; they explain why a technique behaves as it does and whether its output is suitable for a decision. I would not present a p-value or model metric as certainty. Sample size, assumptions, class representation, practical effect size and business consequences must all be considered alongside statistical significance.

### Technical detail / likely follow-up

- **Linear algebra:** documents become vectors; coefficients and dot products contribute to class scores; neural networks and transformers rely on matrix operations.
- **Calculus and optimisation:** neural networks learn weights through gradients and backpropagation; SVM training optimises a margin-based objective.
- **Probability and statistics:** sampling, confidence, hypothesis testing, precision/recall, generalisation estimates and uncertainty.
- **Regularisation:** controls overfitting; L1 can create sparse coefficients and improve interpretability.
- **Organisational relevance:** macro-F1 represents reliability across rare and common concepts; CPU speed lowers deployment cost; coefficients support explanations and governance.

## Explains how they have used programming languages and modern machine learning libraries for commercially beneficial scientific analysis, simulation and data engineering to meet business needs

**Relevant KSBs:**

- K18 — programming languages and techniques applicable to data engineering
- K25 — programming languages and modern ML libraries for scientific analysis and simulation
- S26 — technique selection and application

### STARR — using R, Python and SQL as one Hubble pipeline

**Situation:** Company returns in XML and accounts in iXBRL/XHTML contained valuable structured and semi-structured data. The analysts who would maintain and use the extraction primarily worked in R, while the strongest documented ML ecosystem for the classification experiments was in Python.

**Task:** I needed to select languages and libraries for extraction, cleaning, model experimentation and data delivery without forcing the whole pipeline into one language or creating an unsupported workflow. This meant challenging the norm that a project should remain in the language in which it started, while preserving a maintainable experience for its users.

**Action:** I investigated package maturity, team capability, platform support and long-term maintenance rather than choosing a language by preference. I built the extraction in R because its XML/HTML parsing packages were strong and it matched the team's skills. I cleaned and canonicalised the text by lower-casing, normalising spacing and punctuation, and replacing variable information such as names, companies, dates, postcodes and numbers with typed placeholder tokens. I tested preprocessing choices rather than assuming they helped; replacing forward slashes with spaces reduced classification performance, so I did not retain that transformation. For ML I proposed a hybrid design using Python because scikit-learn, TensorFlow/Keras, PyTorch and Hugging Face were more mature and better documented for the work. I used `reticulate` so the R-first workflow could call Python functions without forcing analysts to abandon their supported workflow. I compared scikit-learn classifiers, Hugging Face/`transformers`/`torch` BERT models, and CNN, MLP and RNN experiments in Keras/TensorFlow, using Optuna and MLflow-style experiment discipline. SQL created the Oracle output structures, while `dbplyr` translated familiar tidyverse operations into lazy SQL executed by the database.

**Result:** The proposed mixed-language architecture combined the strongest suitable tools while retaining an R-first interface for analysts. It extracted and transformed semi-structured data, classified descriptions, and delivered controlled Oracle tables that analysts could query without abandoning their existing workflows. This widened usable analytical coverage, reduced manual preparation and demonstrated that supportability and user adoption were more valuable than enforcing a single-language norm.

**Reflection:** The correct language is contextual: data format, library maturity, user capability, deployment platform, supportability and long-term maintenance all matter. Python support is growing in HMRC's AWS lakehouse, so I would reassess the boundary over time, but I would migrate only where the business and maintenance benefit outweigh disruption.

### Technical detail / likely follow-up

- **R:** iXBRL/XML/HTML parsing, transformation, analyst-facing workflow and orchestration.
- **Python:** Polars-style filtering, scikit-learn, TensorFlow/Keras, PyTorch, Hugging Face, Optuna and model experimentation.
- **SQL/Oracle:** structured output, joins, access control and query pushdown.
- **`reticulate`:** allowed mature Python ML code to be called from the supported R workflow.
- **Scientific analysis/simulation:** controlled candidate-model and hyperparameter experiments simulated alternative pipeline choices against fixed splits; the work did not require a separate physical-process simulation.

## Uses applied research and data modelling to design and refine the infrastructure and architectures to deliver secure, stable and scalable data products, including enterprise, private and public cloud resources and services

**Relevant KSBs:**

- K16 — high-performance computer architectures
- S1 — applied research and data modelling for secure, stable and scalable data products
- S16 — requirements and implementation of data management infrastructure
- S19 — scalable infrastructure and service management

### STARR — refining Hubble's data-product architecture

**Situation:** Hubble processed high-volume, varied data including XML, iXBRL/XHTML and PDFs. The normal POSIT Data Analytics Platform was suitable for development but not for extracting the full volume, and outputs needed to remain secure, stable and accessible to analysts.

**Task:** I needed to define and refine an architecture that could burst for large extraction jobs, protect access to sensitive data, recover reliably, provide queryable outputs and remain financially sustainable.

**Action:** I challenged two established assumptions: that each annual taxonomy needed another manually mapped wide table, and that scalable cloud architecture automatically meant continuously available auto-scaling services. I investigated taxonomy change, Oracle width limits, workload shape, user needs and real cloud costs. I proposed a long-form data model that stored descriptions, contexts, concepts, predictions and document metadata without rebuilding wide tables for each new taxonomy. I worked with platform engineers to establish On-Demand Compute: temporary EC2 capacity, including roughly 128-core or GPU configurations when justified, spun up for a job and shut down afterwards. I used dynamic work allocation because documents varied greatly in size and static splitting left some cores idle. Apache Solr provided distributed fast text search and resilience across servers, while Oracle held structured outputs for analyst querying. Controlled S3 and a proxy/distribution-list arrangement restricted cloud data access. The DPIA, processing within controlled environments and rejection of unassured production models supported security and governance. I also compared native AWS auto-scaling services with fixed-price/self-hosted options and found that serverless convenience could have unpredictable or disproportionate cost at small project scale.

**Result:** The proposed architecture separated large jobs from the main platform, scaled compute only when needed, provided fast search and structured analyst access, and reduced the risk of uncontrolled data access. The long-form model was taxonomy-independent and removed the previous need to maintain extremely wide annual mappings. It supported access to new submissions within days rather than the previous ingestion delay of around nine months, while temporary compute challenged the assumption that scale required paying for permanent capacity.

**Reflection:** Scalability includes cost, operability and governance, not just maximum throughput. The proxy protected access but introduced reliability and performance overhead; a future lakehouse should provide user-level permissions directly. I would also address long-running parallel-job token refresh centrally rather than sharing refreshed S3 credentials between workers through a file. Longer term, Spark/EMR and Redshift or lakehouse-native storage may integrate the processing more effectively, subject to benchmarking and access-control assurance.

### Technical detail / likely follow-up

- **Enterprise/private resources:** HMRC POSIT DAP, Oracle, Solr and controlled internal services.
- **Public-cloud resources:** AWS EC2/ODC and S3 within organisational controls.
- **Security:** DPIA, data minimisation, estate-contained processing, distribution-list access and controlled outputs.
- **Stability:** distributed Solr, tests, controlled database outputs and isolation of burst workloads.
- **Scalability:** on-demand compute, parallel processing, dynamic scheduling and taxonomy-independent long-form data.
- **Financial feasibility:** compare serverless/autoscaling convenience with fixed or temporary compute using real usage profiles.

## Explains how to design algorithms for accessing and analysing large amounts of data, including Application Programming Interfaces (API) to different databases and data sets

**Relevant KSBs:**

- K16 — effective use of high-performance architectures
- S20 — efficient algorithms and APIs for large-scale data access and analysis
- S19 — scalable services and infrastructure

### STARR — moving Hubble from files to scalable data access

**Situation:** The first Hubble workflow saved extracted results to files and users often exported them as CSV or Excel. Runs were slow and usually limited to selected populations, while repeated file movement made large-scale querying, joins and reuse difficult.

**Task:** I needed to redesign access and processing so Hubble could handle large document populations without saturating the main platform and could expose results through data stores analysts already used.

**Action:** I challenged the established file-based workflow, under which Hubble results were repeatedly saved and exchanged as CSV or Excel and runs were restricted to selected populations. I investigated where time and manual effort were being lost, then proposed document-level parallel processing and queryable shared storage. I worked with DevOps to provision ODC and used dynamic parallel scheduling so approximately 128 returns could be processed concurrently without the long-tail inefficiency caused by static batches of differently sized documents. I moved structured outputs into Oracle rather than loose files. R's database interface and `dbplyr` provide the programmatic API layer: analysts write familiar tidyverse operations, which are lazily translated to SQL and executed close to the data rather than downloading everything into memory. Where an attempted SAS-writing package was unreliable, I used a shared FSx route with Parquet for interoperable columnar output. Solr supported fast distributed text retrieval, while the S3 proxy controlled access to object data. I considered data locality, batching, query pushdown, parallelism, storage format and the cost of repeated serialisation, not merely the complexity of an individual function.

**Result:** Large extraction jobs could run on isolated temporary capacity without degrading the shared analytics platform. Replacing the file-first norm with database and Parquet outputs made results easier to query, join and reuse, while existing R analysts could continue using familiar syntax and let the database perform the heavy work.

**Reflection:** An efficient algorithm is part of a wider data-access design. Parallelism helps only if work is balanced, credentials remain valid and output avoids new bottlenecks. I would benchmark natural versus numeric database keys on the actual Oracle and SAS join workloads, and I would expose stable service interfaces only where they improve reuse rather than adding a REST API for its own sake.

### Technical detail / likely follow-up

- **Interfaces/APIs used:** R database drivers, `dbplyr`-to-SQL translation, Solr query interface, S3 access via a controlled proxy and file/service interfaces for Parquet.
- **Large-volume techniques:** lazy execution, query pushdown, batching, dynamic parallelism, columnar Parquet and data locality.
- **Database types:** Oracle relational storage for structured queries; Solr distributed document storage for fast text search; S3/FSx for object/shared-file exchange.
- **Possible extension:** an LLM could generate Solr queries only after receiving controlled schema information, with validation and authorisation before execution.

## Distinction — Explains when they have challenged the norm through investigating and proposing a solution and the impact this had

**Relevant KSBs:**

- K7 — research and evaluation
- S1 — applied research and data modelling
- S20 — large-scale data access and analysis
- S26 — selecting and applying an appropriate solution

### STARR — challenging fixed, tagged-only iXBRL ingestion

**Situation:** The established approach relied on tagged iXBRL data and transformed annual taxonomies into wide Oracle tables. New taxonomies required manual mapping, the tables approached Oracle width limits, and ingestion could take more than nine months. HMRC normally needs to open enquiries within a year, so that delay left little time for profiling and case action. Untagged values and useful free-text descriptions were largely unavailable at scale.

**Task:** Although Hubble's initial requirement focused on extracting untagged content, I believed effective profiling required tagged and untagged information together. I needed to investigate whether a different data model and classification approach could remove the annual bottleneck without making the result unusable for analysts.

**Action:** I challenged the assumption that the output needed to be a manually mapped wide table and that only explicitly tagged items were dependable enough for automated extraction. I profiled the source, investigated taxonomy change and database limitations, and proposed a long-form, taxonomy-independent representation. I consulted analysts to confirm they could work with long data. I also proposed reusing correctly tagged descriptions as supervised training labels so a classifier could map untagged descriptions to standard concepts. I researched and compared candidate models and selected TF-IDF with LinearSVC using performance, speed, explainability, security and maintainability rather than raw score alone. I extracted contextual details such as headings, table names and column positions so the data could support investigations beyond the original narrow requirement.

**Result:** New taxonomies could be ingested without annual structural remapping, and analysts could begin profiling submissions within days rather than waiting around nine months. The broader extraction also meant Hubble already held the contextual features needed when a material calculation problem involving very large incorrect figures was identified; analysts could recreate calculations at a scale that manual work and tagged-only data could not support.

**Reflection:** Challenging the norm is most effective when it is based on evidence and user validation, not novelty. The long format traded some immediate human readability for adaptability and scale, so consulting analysts was essential. I would retain benchmark evidence, user acceptance records and before/after timings to make the impact readily defensible in the EPA.

---

# Theme 2: Professional practice in a commercial environment

**Theme KSBs:** K8, K10, S6, S8, S14, S23, S28, B1, B4, B7.

**Distinction integration:** The pass answers in this theme also consider the wider public-sector/social context and current AI trends, explain how those findings affected the chosen practice, justify the application and identify how learning was shared. The standalone distinction answer remains the fullest version.

## Explains how they have developed their professional working practices and leadership techniques in regard to AI and data science and how this has improved organisational practice

**Relevant KSBs:**

- K10 — own role supporting organisational strategy and objectives
- S6 — direction and technical guidance
- B1 — work ethic and commitment to standards
- B4 — initiative, responsibility and ownership

### STARR — developing from technical contributor to platform and practice leader

**Situation:** The Data Analytics Platform began with one user and needed to support a growing number of analysts using R, Python, data engineering and ML. Hubble also grew into a complex product requiring technical direction, support and safe ways for others to contribute.

**Task:** I needed to do more than write code: I had to provide direction, keep the platform useful and funded, establish working standards, mentor others and connect technical work to HMRC's objective of using data to identify tax risk and support policy evidence.

**Action:** I took ownership of Hubble's technical direction and the DAP service. I arranged platform capability and upgrades, worked with engineers on ODC and GPU access, supported users directly, mentored project teams and ran discussions about ML opportunities. Because public-sector AI can affect trust, privacy, fairness and accountability, I treated professional practice as more than enabling the latest technology. I critically reviewed new internal guidance that treated conventional ML like generative AI, explained why that was disproportionate and proposed more usable wording; the guidance was changed. I applied the underlying responsible-AI findings through secure access, reproducible workflows, explainability and human oversight, then shared them through wiki guidance, Teams discussions and mentoring. On Hubble I introduced tests-before-change, main-branch quality gates, GitLab issues, templates, epics, milestones and a lightweight Kanban process appropriate to a small team. I tailored my leadership: detailed technical guidance for developers, examples and limitations for analysts, and business value, social impact, cost and risk for decision-makers.

**Result:** DAP grew from one user to more than 150 and supported teams building new analytical and ML tools. Hubble extracted 233% more data from relevant documents than the previous approach, and its outputs were used in profiles associated with millions of pounds of identified tax risk. Documentation and mentoring enabled users to develop tools and integrations themselves rather than relying on me for every change, while the revised guidance supported a more proportionate balance between innovation and public-sector accountability.

**Reflection:** Leadership in data science is partly creating conditions in which others can deliver safely. I have developed from solving the immediate technical problem to establishing shared practices, capability and governance. I would improve this further with more formal measures of user outcomes, structured succession planning and regular review of guidance as tools and risks change.

## Justifies their choice of techniques, explaining the risks and benefits and offers an alternative to technical and non-technical audiences

**Relevant KSBs:**

- K8 — interpreting organisational AI/data policy
- S6 — technical guidance
- S8 — stakeholder coordination and expectation management
- S28 — independent and impartial decisions

### STARR — communicating the LinearSVC decision

**Situation:** Hubble stakeholders had different preferences. Some wanted accuracy as the headline measure, analysts suggested models such as Random Forest, and transformer models attracted interest because they were current and powerful.

**Task:** I needed to make an impartial recommendation, explain the benefits and risks, provide credible alternatives and communicate the same decision appropriately to technical and non-technical audiences.

**Action:** I first consulted stakeholders and converted their concerns into an agreed comparison: macro-F1 and per-class reliability, accuracy, speed, compute cost, explainability, security/provenance, maintainability and deployment fit. I compared TF-IDF plus LinearSVC with alternatives including Naive Bayes, Random Forest, neural networks, BERT/SEC-BERT and embeddings. I critically considered the wider public-sector context: a marginally better score did not automatically outweigh opacity, security/provenance risk, energy and infrastructure cost, or the risk that users would over-trust a complex model. To technical audiences I explained sparse TF-IDF vectors, regularisation, class imbalance, cross-validation, coefficients, latency and CPU/GPU constraints. To non-technical audiences I described macro-F1 as reliability across rare as well as common concepts, CPU inference as lower cost and easier deployment, and coefficients as a way to understand the words influencing a result. I was explicit that SEC-BERT's higher raw score was a benefit, but its GPU need, throughput, support/provenance and explainability created material risks. I offered SEC-BERT or a separately assured domain model as alternatives if future business value justified the infrastructure and governance work. I documented and shared the rationale so others could reuse the proportional model-selection approach rather than treating complexity as progress.

**Result:** TF-IDF with LinearSVC was selected because it provided good quality, fast CPU processing, clearer explanations and lower operational risk. Stakeholders could see that their views had been considered and that the decision was based on transparent criteria rather than personal preference.

**Reflection:** Communicating alternatives strengthens a recommendation because it shows the choice is deliberate. The wider lesson I shared was that accountable public-sector AI requires proportionality and transparency as well as model performance. In future I would agree metric definitions and social/technical risk tolerances even earlier and keep a short decision record containing both a technical comparison and a plain-English version.

## Explains how they share and disseminate AI and data science practices across organisations to improve industry practice

**Relevant KSBs:**

- S23 — disseminating AI/data science practice across departments and industry
- B7 — participating and sharing best practice internally and with the wider community

### STARR — sharing iXBRL and AI practice through guidance and Graffiti

**Situation:** Interest in applying ML and LLMs to iXBRL existed both inside HMRC and in the wider iXBRL community, but techniques, limitations and governance were evolving quickly.

**Task:** I needed to make useful practice reusable inside the organisation and contribute learning externally without exposing sensitive HMRC data or presenting experimental approaches as settled best practice.

**Action:** I did not share new AI techniques as unqualified best practice. I critically assessed current LLM trends against the wider risks of hallucination, prompt injection, data leakage, opacity, cost, over-automation and loss of trust. Internally, I converted that analysis into guidance shared through Teams channels, direct mentoring, demonstrations and a maintained wiki. The guidance covered environment setup, virtual environments, secure data access, reproducibility, testing, model limitations, human-in-the-loop use and proportionate model selection. I documented Hubble with a full README and detailed Markdown design notes so contributors could understand not only how to run it but why choices were made. Externally, I applied sector evidence through Graffiti, an LLM-over-iXBRL tool using public data, and shared developments with leading iXBRL experts. It demonstrated a generalisable grounded-LLM practice: extract and structure the iXBRL first, then provide the relevant context to an LLM, rather than passing a noisy full HTML document.

**Result:** DAP users gained practical, reusable guidance and mentoring; contributors could adopt safer and more reproducible workflows. Graffiti applied the critical analysis in a safe public-data example, increased understanding of how structured iXBRL context can improve LLM analysis and provided a vehicle for sharing the benefits, limitations and responsible-use pattern with the wider professional community.

**Reflection:** Dissemination is not a one-off presentation. Fast-moving AI guidance needs versioning, review and honest statements of evidence and limitations. I would strengthen the impact evidence by tracking wiki use, training feedback, reuse by other teams and external responses to Graffiti.

## Distinction — Critically analyses the wider social context and current issues and trends, applying the findings with justification and shares these with the wider community

**Relevant KSBs:**

- K8 — interpreting and challenging organisational AI guidance
- S23 — applying and disseminating practice
- B7 — sharing with the organisation and wider community

### STARR — proportionate use of LLMs in a public-sector context

**Situation:** Foundation models and LLMs created strong interest in automating document analysis. In a public-sector tax context, however, hallucination, prompt injection, data leakage, opacity, bias, cost and over-automation could damage public trust or lead to unfair and indefensible decisions. New internal guidance initially treated all machine learning as if it had the same risk profile as generative AI.

**Task:** I needed to analyse the trend in its social and organisational context, apply it where justified, challenge guidance where it was disproportionate and share a safer working pattern with internal and external communities.

**Action:** I compared the promise of LLMs—natural-language access, faster exploration and broader usability—with their current limitations and the accountability expected of HMRC. I reviewed industry-specific evidence showing that sending complete HTML documents to an LLM performed poorly, while extracting structured iXBRL context first improved grounding. I applied that finding in Graffiti using public filings, structured extraction and a user query. I kept the tool analytical rather than an automated decision-maker and communicated the need for human review. Separately, I reviewed internal AI guidance and demonstrated that its LLM-oriented restrictions would block ordinary ML work without reducing the same risks. I supplied detailed, implementable feedback and the guidance was changed. I shared learning through Graffiti, expert engagement, Teams, mentoring and wiki material.

**Result:** The organisation gained more proportionate guidance, while Graffiti demonstrated a practical grounded-LLM pattern to the wider iXBRL community. The approach captured the productivity benefit without suggesting that model output should replace professional judgement.

**Reflection:** The social licence for public-sector AI depends on transparency, accountability, proportionality and accessible challenge, not simply accuracy. As MCP/tool use expands, capability and risk both rise because models can act across more systems. I would continue to use public/synthetic data for external demonstrations, keep human oversight explicit, and update guidance as evidence, regulation and public expectations change.

## Explains how they have made independent impartial decisions respecting the opinions and views of others in complex, unpredictable and changing circumstances to benefit the business

**Relevant KSBs:**

- S8 — coordinating stakeholders with conflicting priorities
- S28 — independent, impartial decision-making
- B4 — initiative and ownership

### STARR — balancing conflicting DAP and model requirements

**Situation:** As DAP owner and Hubble lead, I faced competing requests from analysts, SMEs, DevOps, budget holders, internal platforms and suppliers. Examples included demand for GPU access, requests for a new S3 data path instead of an existing controlled database route, pressure to prioritise accuracy over macro-F1, and preferences for fashionable transformer models.

**Task:** I needed to respect those perspectives while making decisions for the organisation as a whole under changing technology, funding, security and timescale constraints.

**Action:** I gathered the need behind each request rather than treating the proposed implementation as the requirement. I also considered the wider context behind the decision: public-sector AI and data access require accountability, data protection, sustainable cost and the ability to explain why one group or model was favoured. For licences and GPU-enabled ODC, I collected demand and business justification and worked with budget holders and engineers to provide time-limited scalable capacity. For the proposed direct S3 path, I explained the security and maintenance implications and recommended the existing database route where it already met the need. For model selection, I explained why class imbalance made macro-F1 more informative than accuracy alone and compared stakeholder-suggested models through pre-agreed criteria. I documented trade-offs, shared the reasoning through guidance and stakeholder discussions, and remained prepared to change my initial position when stakeholders, suppliers or new industry evidence presented a better option.

**Result:** DAP grew beyond 150 users with appropriate licences, ODC delivered large/GPU instances cost-effectively, and the platform gained additional data connections including SAS-on-Cloud interoperability. Hubble selected a maintainable and explainable model rather than the loudest stakeholder preference. Avoiding unnecessary new data paths also limited security, support and delivery overhead.

**Reflection:** Respecting opinions does not mean implementing every suggestion. Impartiality comes from clarifying the underlying need, critically considering technical and social consequences, agreeing evidence and decision criteria, recording trade-offs and communicating the outcome. Sharing the reasoning is important because it allows others to challenge or reuse the decision as technology and expectations change. I would improve by making these short decision records routine.

## Explains how they have worked with software engineers to ensure suitable testing and documentation processes are implemented in line with organisational requirements

**Relevant KSBs:**

- S14 — collaboration with software engineers on testing and documentation
- B1 — commitment to required standards

### STARR — engineering controls for Hubble

**Situation:** Hubble became a complex tool with varied real-world documents, several contributors and many users. A small change to parsing or preprocessing could silently affect extraction, model inputs or downstream analyst outputs.

**Task:** I needed to work with engineers and contributors to establish proportionate testing, change control and documentation that supported safe delivery without imposing an unnecessarily heavy process on a small team.

**Action:** I established the principle that changes require tests: if a function had no test, a test was written before modifying it, and the suite had to pass before merging to main. I used unit tests for individual functions and integration-style cases for complex documents because input variation could not be covered by isolated tests alone. I connected this to the wider responsible-AI trend toward reproducibility, traceability and accountability: in a public-sector context, undocumented behaviour or an unrepeatable result can undermine trust even where a model metric appears strong. I applied that finding through GitLab issues, templates, epics and milestones for traceability and a lightweight Kanban board for planning. I wrote a full README for the multi-system setup and maintained detailed Markdown documentation covering architecture, APIs/workflows, limitations and the reasons behind important decisions. I collaborated with platform/DevOps engineers on ODC, data paths and environment constraints, turning operational findings into tests or documentation where possible, and shared the resulting practices through the project documentation, wiki and mentoring.

**Result:** New users could set up the project from the README, contributors could change tested functions with greater confidence, and issues/milestones provided an audit trail from requirement through implementation. The approach reduced regression and onboarding risk while remaining workable for the team size.

**Reflection:** Up-front tests and documentation take time, but they reduce future change cost and dependency on individual knowledge. They also make AI work more open to review, which matters in a public body. This answer naturally covers applying and sharing responsible practice internally; I would use the Graffiti example, rather than over-claiming from Hubble engineering, to evidence sharing with the wider external community. The largest remaining risk is the diversity of source documents, so I would expand a versioned representative corpus, automate integration tests in the merge pipeline, and link requirements, tests and release notes more explicitly.

---

# Theme 3: Awareness of the current and future impact of AI and data science for industry and society

**Theme KSBs:** K11, K17, K21.

## Describes how the potential roles and impact of AI and data science could affect own organisation, industry and society

**Relevant KSBs:**

- K11 — roles and impact of AI, data science and data engineering in industry and society

### STARR — Hubble's organisational and societal impact

**Situation:** Incomplete tagging made large parts of company accounts and tax computations difficult to analyse systematically. Manual interpretation did not scale, and inconsistent descriptions limited the value of otherwise available data.

**Task:** I needed to combine data engineering, data science and AI so analysts could exploit more of the information, while considering what wider impact this kind of automation could have.

**Action:** I used data engineering to extract, clean, canonicalise and structure iXBRL; data science to analyse quality, class balance and performance; and supervised NLP to categorise descriptions. I delivered results to controlled data stores and worked with analysts so the model supported their judgement. I considered the role of similar methods beyond HMRC in fraud detection, medical imaging, demand forecasting, pricing and stock management. I also considered the societal risks: over-trusted outputs, opaque decisions, privacy loss, under-representation of rare classes, deskilling and resistance from staff whose work changes.

**Result:** Hubble reduced repetitive manual grouping, expanded analytical coverage and supported profiles that identified tax risk. Organisationally, this improved HMRC's use of submitted data; at industry level it demonstrated how semi-structured reporting can be made more useful; societally, stronger tax-risk evidence supports public revenue and services.

**Reflection:** A narrow technical pipeline can have material social consequences. Positive impact depends on human oversight, transparent limitations, secure processing and monitoring. I would resist describing AI as replacing analysts: its most defensible role here is augmenting them so they spend more time on expert review and less on repetitive categorisation.

## Explains how they have assessed and addressed the potential business impact of ethical issues relating to AI and data science, the way procedures and methods are selected, and the unintended consequences to the business when they are applied

**Relevant KSBs:**

- K11 — impact of AI/data science on the organisation and society
- K17 — current responsible-AI issues and trends
- Cross-reference: S12 and B3 in Theme 4

### STARR — ethical impact assessment for Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information. A classifier used in a tax-risk context could create privacy, bias, transparency and accountability risks if its categories were treated as fact or used outside their intended purpose.

**Task:** I needed to assess those ethical issues before and during development, choose proportionate procedures and methods, and reduce the likelihood that unintended model behaviour would cause legal, operational or reputational harm.

**Action:** I completed a DPIA before work began and reviewed it as the design evolved. I applied data minimisation and canonicalised names, companies, dates, postcodes and numbers so irrelevant identifiers did not become predictive signal or leak into training. Processing of HMRC data remained inside controlled environments. I assessed representation bias through class distributions, macro-F1, per-class measures and confusion matrices rather than relying on overall accuracy. I selected an explainable TF-IDF/LinearSVC pipeline partly so feature influence could be inspected and rejected an unassured niche model for production despite better raw performance. I documented predictions as advisory and retained a human in the loop. Acceptance testing identified an unintended consequence—blank descriptions receiving poor classifications from surrounding context—so I stopped predictions where the core description was absent. I also changed a confusing top-five dashboard display after usability feedback.

**Result:** Privacy and security risks were reduced before modelling, minority-class failures were more visible, and users received clearer limits on appropriate use. The model remained a decision-support tool rather than an automated determinant, reducing the risk of unfair action, legal challenge, invalid analysis and loss of trust.

**Reflection:** Ethical assessment must cover the complete sociotechnical process: data, labels, metrics, model, interface, users and downstream decisions. A technically explainable model can still be misused, so future improvements should include monitoring, enforced workflow controls, periodic DPIA review and clearer warnings for low-reliability classes.

## Describes how they have applied solutions, demonstrated awareness and explained the changes and trends that have led to enhancement of working practices within their organisation and other members of the team

**Relevant KSBs:**

- K17 — identifying and applying current industry trends
- K21 — supporting and enhancing the work of analytical colleagues

### STARR — applying grounded LLM and modern ML practice

**Situation:** AI techniques, especially transformers, LLMs, tool use and MLOps, were changing quickly. Analysts wanted easier ways to work with iXBRL, but following a trend without evidence could introduce hallucination, data leakage, cost and governance problems.

**Task:** I needed to remain current, test relevant developments, explain their significance and turn useful findings into better practice for analysts and developers.

**Action:** I followed iXBRL International, research literature, technical documentation and practical communities. I tested classical ML, embeddings, BERT/SEC-BERT and neural networks rather than assuming a transformer would be best. That evidence led to a simpler operational Hubble model. For LLMs, I applied sector findings that structured iXBRL context works better than sending an entire noisy HTML document by building Graffiti: it extracts the iXBRL first, then combines relevant structured data with the question. I explained risks and limitations through demonstrations, Teams, mentoring, README/design documents and wiki guidance. I also introduced or promoted more systematic experiment tracking, repeatable environments, tests, human-in-the-loop practice and per-class evaluation.

**Result:** Analysts gained faster, more consistent categorisation through Hubble and a clearer route to interrogating public filings through Graffiti. Team practice improved through reusable guidance, more reproducible testing and a stronger habit of matching model complexity to evidence, governance and business need.

**Reflection:** Trend awareness only creates value when converted into a justified change in practice. I would continue monitoring LLM tool use/MCP, drift detection, explainability, privacy-enhancing methods and responsible-AI guidance, but adopt them only after a controlled test and explicit risk assessment.

## Explains the impact, consequences and risks of non-compliance to the business

**Relevant KSBs:**

- K11 — organisational and societal impact
- K17 — awareness of changing regulation and responsible-AI practice
- Cross-reference: S12 and B3 in Theme 4

### STARR — designing to prevent non-compliance in Hubble

**Situation:** Hubble used sensitive organisational data in a regulated public-sector environment. Non-compliance could arise through excessive data collection, personal-data leakage, weak access controls, unassured technology, opaque model use or decisions made without appropriate human review.

**Task:** I needed to understand the impact of those failures and build preventive controls into the pipeline so the product remained legally, ethically and organisationally defensible.

**Action:** I used the DPIA to identify data-protection and governance risks, minimised and canonicalised personal information, kept processing in controlled environments, restricted S3 and Oracle access, considered provenance in model selection, documented lineage and design choices, and retained human review. I treated compliance as an operational requirement during model and infrastructure selection rather than a final approval step. I also communicated that classifications were suggestions and that model output must not become the defining factor in action.

**Result:** The work avoided a known privacy or security incident and could proceed with proportionate controls. These controls reduced the likelihood of regulatory investigation, legal challenge, invalid decisions, operational rollback, financial loss, wasted development effort, reputational damage and loss of public trust.

**Reflection:** The largest consequence for a public body may be loss of legitimacy and trust, even where a financial penalty is not the immediate outcome. Compliance evidence must remain current as data, users, models and infrastructure change. I would schedule formal DPIA/control reviews and link them to model or pipeline releases.

### Technical detail / likely follow-up

- **Operational impact:** service interruption, rollback, remediation and delayed analytical work.
- **Legal/regulatory impact:** investigation, enforcement, legal challenge and potentially invalid use of results.
- **Financial impact:** remediation cost, wasted investment and penalties where applicable.
- **Reputational/social impact:** reduced stakeholder and public trust, resistance to future AI use and harm to affected people.
- **Security impact:** unauthorised access, data leakage, vulnerable dependencies and broader scrutiny.

---

# Theme 4: Development of suitable AI and data science solutions with consideration for ethical, legal, regulatory, governance and accessibility issues

**Theme KSBs:** K29, S12, B3.

## Evaluates the regulatory, ethical and legal requirements that affect implementation of solutions, including the need for accessibility for all users and diversity of user needs

**Relevant KSBs:**

- K29 — accessibility and diversity of user needs
- S12 — regulatory, legal, ethical and governance issues at each data-process stage
- B3 — integrity in protecting personal data, safety and security

### STARR — governance and accessibility by design

**Situation:** Hubble and related tools served users with different technical abilities and processed company/tax information that could include personal or sensitive data. A technically effective model would still be unsuitable if it breached data-protection principles, relied on unassured components, excluded users or produced inaccessible and misleading outputs.

**Task:** I needed to evaluate regulatory, ethical, legal, governance, security and accessibility requirements throughout design and implementation, not bolt them on after modelling.

**Action:** I completed a DPIA covering the end-to-end Hubble process and applied purpose limitation, data minimisation and security safeguards. I removed or replaced identifiers such as names, companies, dates, postcodes, references and numbers before training where they were unnecessary, kept HMRC processing inside controlled environments, used access-controlled S3 and Oracle outputs and considered model provenance before allowing dependencies onto the estate. I chose a more explainable, established model and made classifications advisory with human review. For accessibility, I engaged a WCAG expert on one project, assessed the existing product with them and agreed a remediation plan. For Graffiti, whose bookmarklet was normally installed by dragging it to a bookmarks bar, I wrote an alternative method for users unable to perform that interaction. I also adapted documentation and outputs for analysts, SMEs, managers, engineers and governance reviewers, and changed Hubble's dashboard when raw top-five scores confused users.

**Result:** The solution reduced personal-data leakage and technology-assurance risk, kept access controlled and supported defensible human decision-making. Alternative instructions enabled more users to install Graffiti, while clearer documentation and dashboard behaviour improved usability for diverse audiences.

**Reflection:** Accessibility includes interaction, language, documentation and cognitive clarity as well as screen-reader compatibility. It is cheaper and safer to design governance and accessibility in from the start. I would use an accessibility checklist and representative user testing at discovery, retain evidence of WCAG review, and update the DPIA and threat/risk assessment whenever data, purpose, model or infrastructure changes.

### Technical detail / likely follow-up

- **Regulatory/data protection:** lawful and defined purpose, minimisation, retention, access control, security, accountability and DPIA review.
- **Ethical:** fairness, class representation, transparency, explainability, human oversight and prevention of function creep.
- **Legal/commercial:** dependency/model licences, intellectual property, contracts, data-sharing terms and auditability should be checked for each implementation.
- **Accessibility:** WCAG-informed design, keyboard-compatible alternatives, clear language, non-colour-only cues and testing with diverse users.
- **Diversity of need:** different technical skills, roles, assistive needs and levels of domain knowledge; communicate at the right level for each.

---

# Theme 5: Continuous professional development

**Theme KSBs:** B5, B8.

## Analyses how they take responsibility for their own and their team's currency of knowledge and skills, and their professional and personal growth and development

**Relevant KSBs:**

- B5 — commitment to continuous professional development
- B8 — awareness of trends and innovation using varied sources

### STARR — turning personal CPD into team capability

**Situation:** AI, NLP, cloud platforms and governance change rapidly, while the apprenticeship offered more mandatory and recommended material than could be absorbed passively. DAP users also needed current guidance to work safely and effectively.

**Task:** I needed to take responsibility for prioritising my own development, apply learning to real work and convert it into reusable capability for the wider team rather than keeping it as personal knowledge.

**Action:** I combined structured QA learning with recommended books, academic literature such as transformer research, practical documentation from scikit-learn, TensorFlow/Keras and Hugging Face, GitHub projects, iXBRL International material and interaction with technical communities. I prioritised sources against active problems, then tested the learning through work with TF-IDF, LinearSVC, embeddings, BERT/SEC-BERT, CNN/MLP/RNN models, Optuna, MLflow/MLOps practice, cloud compute and responsible-AI controls. I recorded learning in project documentation, setup scripts and a DAP wiki, demonstrated approaches, mentored teams and explained limitations as well as capabilities. I promoted virtual environments, reproducibility, tests, secure data access, human oversight and appropriate model selection.

**Result:** My knowledge translated into concrete improvements in Hubble, Graffiti, DAP infrastructure and model-evaluation practice. Team members gained guidance and support to build their own tools, while DAP grew from one user to more than 150. My structured study also contributed to an assessment result of 80%.

**Reflection:** CPD is most valuable when it changes decisions and builds capability in others. I cannot read every source before it becomes outdated, so I triangulate authoritative research, current documentation and practical experiments, prioritising relevance and credibility. I would formalise team skills reviews, learning goals and feedback measures so development is less dependent on informal mentoring and page-view counts.

## Explains how they selected and applied the most effective/appropriate AI and data science techniques to solve a complex business problem in line with organisational and regulatory requirements

**Relevant KSBs:**

- B5 — applying current learning to professional practice
- B8 — using trends and evidence appropriately
- Cross-reference: S26 — selecting and applying suitable AI/data science techniques

### STARR — evidence-led selection for a regulated Hubble deployment

**Situation:** Hubble needed to map inconsistent, often untagged account descriptions to around 826 taxonomy concepts. The data was imbalanced and domain-specific, the full population was large, and HMRC required secure, explainable and supportable processing.

**Task:** I needed to choose and apply a technique that solved the business problem at scale while meeting organisational policy, data-protection, security, infrastructure, cost and maintenance requirements.

**Action:** I defined the problem and success criteria before selecting a model. I extracted and cleaned the data, created fixed stratified train/test/holdout partitions and canonicalised unnecessary personal and variable information. I established simple baselines, then evaluated Naive Bayes, tree models, SVC/LinearSVC, SGD, embeddings, BERT/SEC-BERT and CNN/MLP/RNN approaches. I used macro-F1, per-class measures, confusion matrices and cross-validation because accuracy alone hid rare-class performance. I also compared inference speed, training cost, CPU/GPU requirements, explainability, provenance, maintainability and deployment complexity. I completed a DPIA, retained processing on controlled systems and rejected unassured or externally processed options where their marginal benefit did not justify the risk. The decision matrix favoured TF-IDF with LinearSVC; I integrated Python ML into the supported R workflow and used ODC/Oracle for scalable processing and delivery. Analyst acceptance and usability feedback changed missing-description handling, dimensional extraction and dashboard presentation.

**Result:** The selected approach performed well enough across the taxonomy, ran quickly on existing CPU infrastructure, was easier to maintain and explain, and met the operational and governance constraints more convincingly than higher-scoring but slower or less assured alternatives. It turned previously difficult-to-use descriptions into consistent analytical categories and reduced manual effort.

**Reflection:** The most effective technique is the one that meets the complete business and regulatory need, not the model with the highest laboratory score. My CPD allowed me to test modern methods credibly, while judgement led me to a simpler deployment choice. I would next strengthen automated drift monitoring, test/production pipeline parity, representative rare-class evaluation and periodic review of whether changes in infrastructure or assured models alter the decision.

---

# Final evidence and rehearsal checks

- Verify the strongest numerical claims and bring an artefact where possible: 233% more extracted data, DAP growth to 150+ users, days rather than nine months, identified tax risk, model scores and assessment result.
- Be precise about prototype versus production: BERT, SEC-BERT, CNN, MLP and RNN were experiments; TF-IDF with LinearSVC was the operational recommendation/deployment described in the journal.
- Do not imply that Hubble makes tax decisions. It categorises data to support analyst judgement, with a human in the loop.
- When asked about APIs, describe the interfaces actually used—database drivers, `dbplyr`, Solr, S3 proxy and storage interfaces—before suggesting possible future REST or LLM-driven interfaces.
- Where the evidence is mainly technical knowledge rather than a completed workplace action, say so clearly and connect it to the decision made; do not invent a project.
- For each answer, be ready to name: the artefact, another person who saw the work, the business outcome, the principal trade-off, the largest risk and what would be improved next.
