
# 1. Introduction and background.

HMRC receive millions of financial documents such as company accounts and tax computations that contain a large amount of information used to provide insight for operational/government policy and to identify tax risk. They are iXBRL documents; semi-structured (x)HTML documents where key items are tagged with concepts from fixed taxonomies. 

For fully tagged documents, previous workflows allows us to reliably extract, structure and analyse the data in those documents. Initial analysis showed that some document classes only have approximately 30% of the figures tagged, which means that existing workflows can't utilise 70% of the figures. There are various reasons for this, ranging from limitations in software used to create the documents to people deliberately leaving items they don't want HMRC to review untagged. 

The previous workflows to extract iXBRL data, require complex and long schema updates to processes new taxonomies every year. The wide database format is also hitting the column limits of the Oracle database complicating things further. It can take up to 9 months for the updates, but HMRC only have 12 months to open an enquiry, leaving little time for profiling and opening an enquiry in time. 

Hubble is a tool I developed that extracts both tagged and untagged items; and uses supervised multi-class text classification to categorise the untagged items. The system scales with workload and uses a long format for the Oracle database, allowing it to deal with any taxonomy, resulting in data being ingested within days of receipt. 

I initially worked on Hubble myself, writing the vast majority of the code and doing all the ML elements myself, but as the project became bigger and more important to HMRC I arranged for more resource and lead a virtual team working on the project.

# 2. Outline of the issue or opportunity and the business problem to be solved.

The business problem was that a significant amount of data submitted to HMRC couldn't be used in bulk analysis, since previous workflows didn't extract untagged data. So bulk numerical analysis was restricted the tagged figures, which could be missing 70% of the numerical data in those documents. This means profiles using such data don't have the data to properly identify high tax risk returns limiting compliance yield HMRC can bring in. Also we were unable to provide accurate data or statistics for the department/government to make informed decisions. This combined with the 9 month taxonomy lag was creating serious operational issues. 

The initial requirements just included extracting the raw data such as descriptions, but  items can be described in lots of different ways with no fixed taxonomy. Analysis of the descriptions showed that some classes had a large variety of descriptions, some with over 23,000 unique descriptions, and SME highlighted that many are domain-specific technical terms that not all analysts would be familiar with. Graphs and stats showed a very long tail, beyond anything that could practically be investigated in depth. 

Initial usage required lots of complex regular expressions and working with SME due to the domain-specific terminology, which was error prone, incomplete and time-consuming. I considered ways to systemise a rule-based system which would help with some of the issues but it would be too resource intensive, especially of the SME time, while still failing on the long tail. It wasn't a feasible business solution, so I investigated alternatives. 

While 70% of items may be untagged, 30% of figures are tagged, and they are tagged by software or accountants so should be good quality training data for supervised learning that could then be applied to the 70%. So, I recommended creating a supervised multi-class text classification ML model to classify the descriptions. 

# 3. Methods used and justification.

## 3.1. Project management

I selected an agile approach for the overall project(https://agilemanifesto.org/principles.html). I didn't strictly adhere to a specific framework, selecting features that were appropriate("Teams tailor Agile practices to their needs, blending frameworks like Scrum and Kanban for optimal results" https://www.atlassian.com/agile), with it being more Kanban focused since the project team was small and the overhead of SCRUM wouldn't be appropriate. The competing business demands on the team meant that fixed sprints weren't appropriate but regular Kanban updates ensured progress on this project while other business needs were accommodated. 

The agile approach allowed us to iterate quickly delivering usable pieces of work, with basic raw data initially delivered on file, then in additional steps more data, iXBRL information, ML categories, improved architectures and database. Regular meetings and a workshop with stakeholders helped get feedback such as the issues dealing with raw descriptions; validate business understanding and planned approaches. With each step evaluated for feasibility, benefits and risks. The customer requirements at the beginning wouldn't have foreseen the way the project developed, highlighting the benefit of an agile approach opposed to a more fixed waterfall approach. 

## 3.2 CRISP-DM

I used CRISP-DM since accommodates the cyclical nature of ML and provides a clear intuitive structure. Since I working on the ML aspect myself CRISP-DM is more appropriate than larger more complex methodologies like TDSP. Each stage produced documented artefacts, allowing evidence backed decisions in other steps. The iterative improved macro-f1 from under 0.50 to 0.787. 

## 3.3 Languages and Tools

### 3.3.1 Gitlab

While using GitLab to manage project isn't common in HMRC, I decided that the advantages of transparency, audibility and documentation outweighed the costs of learning a new tool. 
- The issues board worked well as the Kanban board helping us track issues and tasks. 
- The epics were useful for working with management who were focused on longer term timelines. 
- I created templates for issues, tasks and PR, which ensured they were completed to a consistent level by all team members. Covering details such as details of every step required to recreate the issue, expected vs actual and proposed fixes.
- Team members were encouraged to document issues in detail on GitLab, to update project markdown documents, and guided that code comments should be why code does what it does rather than just describing what it does. 
- Version control, branches and independent review of PR helped ensure changes were of sufficient quality and limit issues. This required training the team how to use branches, which I videoed for reference. 

### 3.3.2 Languages and packages

I used R due to its powerful packages and it is the default coding language used by analysts, so has much greater support and maintainability.  Packages such as rvest, xml2 were good for the html extraction work;  "parallel" to allow processing hundreds of documents in parallel; dbplyr for Oracle database access using familiar syntax; testthat for testing.

I used python for the ML aspects since the classification packages are more mature and have more support. The reticulate package in R allows importing python function into a R workflow, which made integrating it work well. The python ML packages used included MLflow to track tracks data version, model version, performance and various other metrics; sci-kit learn for traditional ML models; TensorFlow/Keras to build and train NN; HuggingFace Transformers to utilise pre-trained transformer based models; and Optuna to fine tune parameters and hyperparameters. The exploratory work was done in Jupyter notebooks to allow for detailed narrative alongside the code.  

SQL was also used for setting up and managing the Oracle database and tables.

## 3.4 Testing

While working with others to review the code base, we discussed the scope, coverage and implementation of unit, integration and system testing. Constraints such as that the tests shouldn’t contain any customer data, so to use synthetic or anonymised fixtures instead. For new issues I decided we should create tests for new issues and bugs, to make it easier to investigate and fix those bugs in the future. While a single command runs all the the tests, I would like to also add a CI pipeline in the future. 

With user acceptance testing, it highlighted that users might prefer numeric primary keys for joining rather than natural keys for join performance reasons. They also suggested structuring data in a way they are more familiar with. 

## 3.5 Scientific method and statistical analysis

I used hypothesis formulation; controlled experimentation including DummyClassifier baselines; stratified cross validation with paired t-tests at the 95% confidence level to determine if models were statistically different from the top model. Challenges included class imbalance which required using score like macro-f1 which gives equal weighting to each class, stopping common classes from dominating the scores. On the modelling side different approaches were tested such as balanced weights and/or square-root weighted training samples.

# 4. The scope of the project (including key performance indicators).

The project scope evolved over time, from pure extraction of core data like descriptions and values to file; to extracting and formatting other relevant data such as headings, table names, structural data(table number, row number, column number) and iXBRL data(concept, dimensional data); adding ML capabilities; and an automated pipeline extracting to Oracle database. 

Working with stakeholders success criteria were established. 
- Macro-F1 > 0.6, primary performance metric. 
- Accuracy > 0.7, a secondary metric metric that is more intuitive and easier top understand by stakeholders.
- Automated extraction coverage > 95%, data automatically extracted and classified
- Timely extraction < 1 week from date of receipt. 

Secondary KPIs used were precision; recall, train time, inference time, interpretability, explainability, maintainability, reliability, cost control, data protection, AI safeguards, security, logging, and ability to scale to millions of records quickly.

# 5. Data selection, collection and pre-processing.


## 5.1 Data selection

HMRC's systems are locked down, without any readily available GPU access making it difficult to do exploratory work with complex models,  so exploratory work was done using a standalone device with a GPU over 298,461 publicly available iXBRL accounts submitted to Companies House in November 2025. A  month of data makes it more representative, although many companies select specific dates like 31 December or 31 March, so the data might not be completely representative but that shouldn't have any material impact for my analysis. For the implementation phase the company accounts and tax computations submitted to HMRC were used. This resulted in 2.8m lines of data with 956 concepts(labels).

## 5.2 Exploratory Data Analysis(EDA)

Rank frequency plots of both description and concept had a long tail. With a Pareto chart showing that the most used 75 concepts cover 95% of items; with a distribution closer to a lognormal fit than power-law. Motivating the use of macro-F1 over accuracy so that common classes don't dominate the metrics. 

The main feature is a description that has various types, from nominal text, dates(temporal), names(nominal) and figures(numeric ratio). 

The xbrl concept(label) is a categorical nominal label from a fixed taxonomy. It's a single CammelCase word, but splitting into words make it human readable with similar concepts have similar wording. 

The descriptions are many-to-many with cosine similarity analysis, identifying situations where some descriptions like "Taxation and social security costs" were used for very similar concepts, but other descriptions such as pure dates were used for lots of different concepts. It also highlighted that taxonomy goes into a great deal of specificity, beyond what is generally required or could be predicted based on the human readable data in the accounts. Creating a real upper limit to any model. 


## 5.3 Preprocessing

The text features like description were normalised, lowercasing and replacing special characters with spaces. Not all preprocessing was effective, for example replacing forward slashes with spaces actually reduced performance, so it was dropped. 

I canonicalised the description, so most dates were replaced by a placeholder "hubble_date", except for 31 March 1982, which subject matter experts explained has a special meaning for tax so that was replaced with "hubble_date_1982_03_31". 

Similarly company names, individual names, postcodes and numbers were identified using regular expressions and labels replaced by placeholders. This helps avoid overfitting and makes the model more generalisable; improves model performance since it reduces a lot of the noise;  preserves privacy; enhances data security through data minimisation. It is more ethical since it would treat less common ethnic names the same as more commonly used names. 

SME advised that where there was a placeholder by itself, then that would not be enough information to categorise it, so we agreed to do label engineering and changing them to similar placeholders like HubbleName. So while we can't predict the actual concept the placeholder is related to, know it relates to a name can be useful in analysis. 

Systems and outputs were restricted to specific users limiting data access. 

I implemented data quality controls aligned with HMRC expectation and broadly in line with DAMA UK’s quality dimensions(https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework)(https://www.dama-uk.org/resources/the-six-primary-dimensions-for-data-quality-assessment).
- Completeness improved since untagged data was now extracted. 
- Consistency because the untagged data and iXBRL tagged data was structured and formatted in similar ways on the same tables. 
- Timeliness, since the data was structured in a way and the architecture allowed extraction and categorised within days. 
- Validity and accuracy were addressed by removing descriptions less than 2 characters, missing; low-quality; or longer than 16 words which analysis showed weren't valid descriptions. 

These measures and preprocessing improved model macro-F1 scores from under 0.5 to over 0.7, and ensured I was complying with both HMRC and regulatory requirements; DPIAs; and Data Protection Act 2018/UK GDPR. 

Because the data was going to be used over various model architectures and packages, I created stratified splits upfront, 80/10/10, test, train, holdout plus sub splits and square-root weighted splits.

The work on preprocessing significantly improved the performance of the model going form a macro-f1 of 50% to over 70%.

# 6. Survey of potential alternatives.


Various approaches were used to embed the words, from TF word and character ngrams, all-mpnet-base-v2 and infloat/e5-large-v2. The silhouette score was used to see how well the models embedded the descriptions for each concept. MPNET has the best silhouette score, suggesting it's able to capture the different descriptions which have the similar meaning better than just TF. 

The tagged concepts go into a great deal of specificity beyond what is required, so unsupervised methods were considered, about whether they could group similar concepts together. The cosine similarity highlighted a limit to unsupervised methods. 

I initially used theory to limit the solutions to those that would work well with supervised classification of text.

The primary feature is a free text "description". So this is text classification problem. While most figures are untagged, 30% of figures are tagged and due to the volume of the total data, this means that we can train the model on the 30% of tagged data, so it is a supervised multi-class classification problem.  

The descriptions are normally just a word or a short phrase, but  have domain-specific terminology. There were two main methods used to embed the descriptions, TFIDF and dense vector embeddings. TFIDF extracts character and word n-grams, this can work well since it captures domain specific terminology and phrasing well and works well with a variety of models with good speeds and performance. Dense vector embeddings capture more of the semantic meaning of phrases so should capture phrases that have similar meaning even if the words are different, which should improve classification especially on unseen descriptions. 

There are a range of possible models that deal with text such as using traditional ML such as Naive Bayes and SVM; training a deep neural network from scratch; fine tuning a larger transformer based model locally; using a frontier LLM and fine tuning it via an API. 

Traditional ML models can perform well with classifying short simple text, especially since descriptions in the accounts will normally have less variety than generic free text.

A deep neural network can be trained to categorise descriptions, and has the advantage of being able to learn patterns beyond that of a fixed algorithm used in transitional ML. 

There are a number of BERT based models. These models have been pre-trained, so have a lot of semantic understanding baked in. But many BERT models are trained on generic text,  SEC-BERT is a model that was trained on SEC filing(financial filings), so should have better semantic understanding of accountancy terms and concepts, which is very appropriate here.

It is expected that a frontier LLM would have the best semantic understanding, but it is likely to be excessive for this use case. A LLM would be good at understanding lots of text, but we just have short phrases and small sentences at most. There are additional technical, data security and governance issues around using an API. So a LLM based approach was not used.

The existing approach of using regex's could could be systemised, creating a repository of concepts and the associated regular expressions that could be used to identify them from the description. This would be a very labour intensive approach, that would require large input from SME, would be incomplete and error prone. So this approach wasn't used. 

Exploratory analysis showed that unsupervised methods around the words used would be insufficient. 

The primary feature is a free text "description". So this is text classification problem. While most figures are untagged, 30% of figures are tagged and due to the volume of the total data, this means that we can train the model on the 30% of tagged data, so it is a supervised multi-class classification problem.  

The descriptions are normally just a word or a short phrase, but are have domain-specific terminology. There were two main methods used to embed the descriptions, TFIDF and dense vector embeddings. TFIDF extracts character and word n-grams, this can work well since it captures domain specific terminology and phrasing well and works well with a variety of models with good speeds and performance. Vector embeddings capture more of the semantic meaning of phrases so should capture phrases that have similar meaning even if the words are different, which should improve classification especially on unseen descriptions. 

There are a range of possible models that deal with text such as using traditional ML such as Naive Bayes and SVM; training a deep neural network from scratch; fine tuning a larger transformer based model locally; using a frontier LLM and fine tuning it via an API. 



It wasn't possible to test every model and hyperparameter over the full train dataset. So initially I tested a few smaller models over 1%, 10% and 100% train populations, to see if results using the smaller populations were representative of larger populations. I checked the Pearson correlation of the f1-macro scores for those models to the various populations. The 1% population had a fairly high score of 0.971 and 10% had a very high scores of 0.998. Using a paired T-test models that weren't not significantly worse over the 1% population were the same at 100% population. So this meant that it was reasonable to filter out models and hyperparameters using a smaller populations, and that the 10% train population was large enough for reliable results. 

To narrow down the initial models and hyperparameters I used HalvingRandomSearchCV, which let's me cover many models and hyperparameters in an efficient way. Robustness was improved through stratified cross validation which reduced variance. Since there were cross validation scores, I used this with a paired t-test to show which models were not significantly worse at the 95% level. This narrowed down the models to LinearSVC, SVC(linear) and PassiveAggressiveClassifier. 

To get a better handle of the hyperparameters I plotted them against against scores, this helped narrow down the ranges to use in more in the next iteration using the full train population size.  A 2D graph using colour showed that min_df 1 had clusters with better speed and scores over min_df 2. 

I focused on macro-f1 scores since it provides a single value that that takes into various factors and is appropriate for the high-class imbalance  to ensure the model worked well on the business requirement that it works well on as many classes as possible, even minority classes.

Here LinearSVC had the best f1-macro score and was significantly better than the other models at the 95% confidence level. 

I then tried different embeddings, such as mpnet, e5, various tfidf word and character embeddings. Complex tfidf with a complicated combination of word and character ngrams, performed significantly better than a simple tfidf word embedding,  the difference was very small ~0.003 and it took 2.46 times longer than simpler word only embeddings. mpnet also was significantly better but also by only 0.003 but took 76 times as long. So the choice was to stick with a simpler tfidf word only embeddings, which would be faster, easier to maintain and would make it easier to interpret models over the them.  



Traditional ML models can perform well with classifying short simple text, especially since descriptions in the accounts will normally have less variety than generic free text. 

A deep neural network can be trained to categorise descriptions, and has the advantage of being able to learn patterns beyond that of a fixed algorithm used in transitional ML. 

There are a number of BERT based models. These models have been pre-trained, so have a lot of semantic understanding baked in. But many BERT models are trained on generic text,  SEC-BERT is a model that was trained on SEC filing(financial filings), so should have better semantic understanding of accountancy terms and concepts, which is very appropriate here in this use case where we are classifying descriptions in financial documents. 

It is expected that a frontier LLM would have the best semantic understanding, but it is likely to be excessive for this use case. A LLM would be good at understanding lots of text, but we just have short phrases and small sentences at most. There are additional technical, data security and governance issues around using an API. So a LLM based approach was not used.


# 7. Implementation - performance metrics.

Samples were selected to balance statistical power with processing time, ensuring conclusion were robust without delaying delivery.

The final pipelines used TFIDF(1-3 word ngrasms, min_df 1, norm l2) with LinearSVC(penalty l1, C 2.8, loss squared_hinge, dual False, class_weight balanced, max_iter 10000) from scikit-learn. 

There was a range of similar performance for C, but a lower C was selected to prevent overfitting and enhance model generalisability. 


I calculated confidence intervals using a bootstrap method. 

The model was trained across a 1%, 10%, 100% train population plus also 10% square root weighted population. The 10% sqrt weighted train population resulted in 1.3pp better f1-macro score but 0.0573pp lower accuracy, compared to 10% population. But training on the full 100% population resulted in the best f1-macro and accuracy, and would have the simplest pipeline. 

To deal with the class imbalance and reduce systematic bias towards majority classes, I used class weighting.


Optuna was used with NN and transformer based models. This has the benefit over the fairly manual approach used with scikit-learn. Optuna has built in visualisation around hyper parameters and automatically tuns the hyperparameters. In the future I will also use Optuna with sci-kit learn models. 

DNN, LSTM, GRU, CNN, BI neural networks were tested, with CNN doing best. With dropout hyperparameters used as regularisation technique. 

Various transformer based models were tested, roberta-base, nlpaueb/sec-bert-base, sentence-transformers/all-mpnet-base-v2, and sentence-transformers/all-MiniLM-L6-v2. Various combinations of using weighted models, sqrt weighted training data and random oversampling were tried. Using sqrt weighted training data has the best f1-macro score. 

I worked autonomously when deep focus was required, such as during core modelling phases, building models and analysing metrics. I would then demo my current approach and get feedback in meetings with ML experts. When evaluating the outputs I would collaborate with SME who had a deeper understanding of the taxonomies, and the issues of lumping them together.

I would often work collaboratively on tasks assigned to other team members, partially to share knowledge and also upskill them.

I would work collaboratively with DevOps since they had knowledge, expertise and control over infrastructure that I did not have.


GitLab was used to document all key aspects, with documents covering data structures and types, guide to setup Oracle tables and create developer credentials, details of key decisions and the reason why they were made. The task list and issues were moved to the dedicated GitLab page.   

The selection of TF-IDF and LinearSVC was selected due to performance, computational efficiency, explainability, scalability and suitability for HMRC working environment. The short domain-specific descriptions led itself well to TF-IDF(1-3 n-grams) with discriminatory vocabulary captured as their own feature. LinearSVC works well with sparse matrices like those created by TF-IDF and using L1 regularisation which removes irrelevant features, resulted in even sparser matrices, allowing inner products to be done very efficiently. This allowed me to test and develop the model using existing infrastructure without disturbing other users.
# 8. Results.

Sensitivity analysis and model robustness was tested over various categories, abbreviations, adversarial(So phrased to be misleading), scenario planning, command(command to inject LLM), contextual(semantically the same), long context, ocr issues, synonyms, typos, unicode and variations. 

Overall LinearSVC outperformed SEC-BERT in robustness testing, which was unexpected since I would have expected the domain specific training and better semantic meaning would it would have done better overall. Also the areas where LinearSVC did worse like typos and variations would be rare over real data, since accountancy documents are primarily generated by computers, rather than people typing every description. 

Looking at the coefficients of the LinearSVC helps interpreting how the model arrived at what it did, but it's not possible to do anything similar with SEC-BERT. 

But there are tools like LIME and SHAP which do work on SEC-BERT and help with the explainability with both CNN and FFSEC-BERT but also LinearSVC. They can provide insights beyond the coefficients alone. 

Residual analysis, confusion matrix is useful to see what kinds of mistakes the model is making for the different concepts.  Many issues relate to there not being enough distinguishing information in the description, so it would classify based on the most common concept associated with that description, but the testing dataset has example of that description being associated with different concepts. So this isn't a limit of the model. In some situations it means the description alone isn't enough data to categorise the item, so in later iterations additional features of the table name and heading were also included which improved f1-macro from x to y. 

Performance was balanced by infrastructure/costs, where selecting faster models that could run quickly on a CPU were prioritised allowing development on existing infrastructure.

SME also provided input explaining how that in some cases there simply isn't enough information at all in the accounts to predict the specific concept used. 

To compare the model architectures a decision matrix was used. This covered 8 objective measures such as f1-macro and train time and 6 subjective measures such as interpretability and deployment simplicity. Each measure was weighted and adjustments were made if there were overlapping confidence intervals. With a rubric setting the standard/scores for the the subjective scores with an accompanying narrative. So factors like simplicity, interpretability, maintenance burden, deployment simplicity, model size, train time outweighed pure f1-macro scores. 

The various options were evaluated not just in terms of performance but also explainability, operational risk, security, infrastructure constraints and long-term maintainability.

Some models had marginally better performance, but are black boxes, which poses a risk, so I went with a model that is explainable.

Future requirements include scaling to millions of documents with fast inference speeds(2.7ms), on low cost infrastructure. This ruled out the larger transformer based models that would need to be run on expensive GPUs(for performance reasons), and still be significantly slower to train and run. SVM based models that can be developed on existing CPU based infrastructure, have good performance and are very fast.

On demand compute will help with scaling, and CPU EC2 instances are cheaper and have better availability ensuring reliability.

Performance was balanced by infrastructure/costs, where selecting faster models that could run quickly on a CPU were prioritised allowing development on existing infrastructure.

I chose LinearSVC over transformer based models, trading marginal performance gains(2.3pp) for a solution that is simpler(more maintainable), more explainable(feature coefficients), quicker(13x), allows development on existing infrastructure, with the ability to scale cost effectively.

The model has high accuracy 97%, but high class imbalance means that it underperforms on minority classes, with some classes performing very poorly. Summaries of poorly performing classes have been created for analysts so that they are aware of when they might need to do more bespoke and complex description matches rather than using the ML category. I recommended and created an an interactive dashboard which has this data in it, this transparency helps people determine how well the model works and can see statistics on it's performance on certain categories, which is much more user friendly than just having a large dataset they would have to review themselves. Often the errors are misclassifying very similar categories and the features don’t have enough information to differentiate between those categories. Requesting feedback after each step. 

The dashboard had a top-k, but some of those were very poor matches and the scores were confusing, so on feedback I just showed the top-k that were better actual possible matches. 

The ML category can be wrong, so should not be used for any automated decisions, so the process requires a human in the loop, who should review the actual description.

The result is a dataset that reduces manual effort 
# 9. Discussion and conclusions/recommendations.

Separate models for every taxonomy would give the best raw performance, but I used a single taxonomy for each document type, resulting in consistent class names, to increase analyst usability.

The source iXBRL documents were complex with inconsistent HTML structures, iXBRL data and multiple taxonomies. I initially thought best to train over a large random sample, but different taxonomies had conflicting naming. A bespoke model for each taxonomy would give the best raw scores, but it would be confusing to analysts, so it was recommended to train only using the main taxonomy and use those classes over all taxonomies.

I asked SME about errors where the predicted class was what I expected but the iXBRL concept was slightly different, they explained that some concept names differ between the different taxonomies, which meant that each model should have training data limited to a single taxonomy, but it would be good to use the main taxonomy to classify across all the documents since that would provide standardised labels.

To scale we would need additional infrastructure, I worked dev-ops to setup on-demand-compute, which allows us to fire up an EC2 instance just for a job and close it when finished, which is much more cost effective than having a large machine running all the time. 

My communication approach evolved based on how stakeholders reacted to early explanations. Initial technical descriptions were too detailed for some audiences, so I shifted towards a visual and example-based explanations. So very simple visual decision trees showing what attribute was split on, or graphed SVM 2D decision boundary.
A simple example helped illustrate the difference between weighted and macro scores.

For more technical stakeholders rather than just stating what I did I started to give more detailed explanations for why certain choices were made and linking theory to the experimental results.

I recommended that communications should have the headline figures and results, with a section that explains any technical terms with illustrations and examples, and an appendix with the technical details.

Worked closely with analysts where I focused on outcomes, showing confusion matrices for good and poor quality classes and looking at examples, so they understood where it would be good, situations where it would make mistakes and the kind of mistake they should expect.

With DevOps I focused on benchmarks, memory usage and future requirements, cost/benefit of specific EC2 instances. 

With managers I focused on the kinds of information they needed like business level topics like timeframes, resource requirements, funding, blockers they could help with.

With managers I focused less on the technical development and focused on the business level, so benefits and outcomes, timeframes for improvements, and the benefits of more people working on the project, which resulted in work being reallocated for someone to focus on development. Memos were drafted with cost benefit analysis requesting more funding for infrastructure, this resulted in additional funding for infrastructure.

The project readme utilises markdown to provide clear headings and sections, with instructions, links and code blocks, which has been successfully used by many analysts to setup the tool. When users have issues or questions, I updated the docs to be clearer or cover such issues. 
I created a setup script and detailed readme to allow other users to setup and use the tool. This means many analysts are now running the tool allowing me to focus on development.

Changed to using Oracle database. 

Bias was investigated both against size of companies and software provider. So large companies had a f1-macro score of 0.9343 vs 0.789835 for small companies. Which could be explained by smaller companies using cheaper software, with some software providers having a score of 0.184061 vs 0.913292. On residual analysis often the misclassifications were for very similar classes and not enough information to differentiate between them. This highlights an issues one that maybe the specificity of the model and testing to too high. Also it's highlighting just differences in how the software tags items, but it's a training proxy, and such issues wouldn't apply to untagged items, if we had human labelled classes this issue wouldn't show up. But the ML category could be used in a variety of ways, including trying to detect 

Regularly updating the features, model, etc.  

Monitoring drift of inputs, are there new taxonomies. Drift on outputs is detected for both accuracy and f1-macro, using a 2pp drop and for there to be non-overlapping confidence intervals, over two consecutive days. 

Moving to a core data source used widely, meeting with reliant data sources, discussing how formal data contracts will need to be created to ensure reliability in the service. 

Cost benefit analysis, significant benefits already seen both in timeliness of existing data and also extracting new untagged data. So funding had been provided to expand and increase capability and reliability of the system.
# 10. Summary of findings.
# 11. Implications.

Hubble helped us meet our quality standards, such as completeness and consistency since we can extract all of the figures and have consistent ML classes.

The business value is that it reduces manual effort, allows us to better create statistics that informs and drives government policy and better identify risks. It's been used in projects where hundreds of billions of pounds of incorrect figures in returns have been identified. 

I explained how the ML category worked and gave examples to analysts explaining when it works well or not, using confusion matrices and examples. With greater understanding of the ML category analysts started using the ML category more when profiling, with Hubble being widely used in by multiple teams

Presentations to non-technical audiences roughly follows the Problem-Solution-Outcome structure. Trying to explain complex concepts even step by step was still confusing for non-technical audiences, so I moved over to using simple concepts like confusion matrixes with examples. The solution is at a very high level without going into the technical detail, with the focus on the outcomes each slide focused on a separate benefit/functionality with clear examples they could understand explaining what it does without going into unnecessary detail. 

Manual spreadsheet to record benefits showed tens of millions in estimated benefits, but completion was incomplete so I arranged for the central management system to have built in functionality to monitor benefits. 

I investigated and implemented a solution that extracted additional data and used ML to categorise items increasing consistency so that analysts could more easily and robustly use the data.
# 12. Caveats and limitations.

Analysts were educated that the ML category can be wrong and shouldn’t be used for automated decisions. There should always be a human in the loop before any action on it happens. This would include a person looking at the actual descriptions.

The model and evaluation were all based on tagged data. But the main use case would be on untagged data, and there is a risk that the untagged data could be different than the tagged data. e.g. An item might have been left untagged since there aren't any relevant taxonomy concepts for that item. Ideally untagged data would be human tagged by SME, but it requires tax trained experts, who have other much higher priority work to focus on. 

LinearSVC has very good performance on smaller dataset sizes but doesn't scale as well on larger datasets, so it's not practical to train it on larger datasets. But going from 10% train data set to 100% saw only a 0.4pp increase in f1-macro, so much larger datasets are unlikely to increase performance significantly. 

Increasing data set size while keeping a fixed numeric cutoff, results in more labels, so model performance actually decreased, also different document types had different distributions in labels, also resulting in different performance, making comparison across different document types and sources difficult. 

The integration of R and python while working well, does add more complexity to setting up the project and other teams have had issues with the reticulate package. With the the long term look to a lakehouse, it seems like python has more support for the ETL stake where Hubble would fit, and with higher python use in HMRC now, it might be worth considering porting in the future. 



# 13. Appendices.
## Code and documentation used for the project.
## Statistical rigour: uncertainty, bias, and error estimates where appropriate.
## Figures, tables, and visualisations.
## Mapping of the project report to AM1 KSBs.
## Employer verification that the report reflects my own involvement and work.