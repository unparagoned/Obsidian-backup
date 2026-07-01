BCS Level 7
Artificial Intelligence Data Specialist
Apprenticeship

Assessment Method 1
Project Report with Presentation and
Supplementary Questioning

Work-Based Project Sign-Off Document

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

IfATE Standard V1.0

Page 2 of 22

June 2024

Change History

Changes made to this document are recorded below. This includes the latest version
number, date of the amendment, and details of the change. The purpose is to
identify the updates undertaken.

Version Number
& Date
V1.0
October 2021
V1.1
April 2023
V2.0
June 2024

Changes Made

Document created.

‘’Project Title’’ box added, Minor formatting updates.

New template applied.

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 2 of 22

Overview

This mapping document is to help facilitate the timely sign-off for the intended work-
based project for assessment method 1.

The apprentice should complete the following project mapping to clearly explain how
the proposed work-based project will meet all the assessment criteria allocated to this
assessment method.

Apprentices must produce a project report based on a pre-gateway work-based project
during the EPA period, which will be the basis of a presentation to the independent
assessor with supplementary questioning immediately after the presentation.

The  project  report  and  presentation  are  compiled  after  the  apprentice  has  gone
through the gateway process.

The EPAO will review the mapping document and sign it off. If more detail is needed,
the EPAO will provide feedback to request further information.

Top Tip

  Please take the time to fully read and understand the assessment plan for

this assessment method.

We strongly recommend that the mapping document is completed and used. Failure
to do so will likely cause delays in the EPAO being able to sign off the proposed work-
based project.

Please do NOT save this as a pdf as it needs to be annotated by the EPAO.

Add your full name to the start of the filename prior to submission.

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 3 of 22

Assessment method 1, component 1: Project report

Apprentice Details

Name

ULN

Training
Provider

Jesse Karadia

3591334404

QA

Employer

HMRC

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 4 of 22

Project title

Categorising data in financial documents

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 5 of 22

Project brief

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 6 of 22

Financial documents contain a large amount of useful information, that could be used to provide insight for government policy or to identify tax
risk. Company accounts and tax computation are in an iXBRL format(semi-structured), which are (x)html documents where items are tagged
with an iXBRL concepts from a fixed taxonomies. For fully tagged documents, existing workflows should allow us to reliably extract, structure
and analyse the figures. In practice some financial document types are poorly tagged(~30% of the figures are tagged), meaning that most of
the data in these important documents has been unavailable for analysts for profiling, policy insight or identifying tax risks.
I developed a tool, Hubble, which extract data from these documents, both tagged and untagged items, and classifies untagged items into a
taxonomy class using supervised machine learning. It extracts the description for items but there is no fixed taxonomy or specified way that
items must be described. This means items of the same class can have many different descriptions associated with them. Financial documents
use domain-specific terminology, which data analysts might not be familiar with, which can make it very difficult and error prone working with
the raw descriptions. To be able to fully exploit the data, we need to be able to classify it based on extracted features like the description,
heading and table name.

I managed the technical side of the project, and implemented the following stages.

-  Business understanding: Discuss use cases with SME/analysts, how the data would be used for profiling and generating statistics.
Identified constraints, data protection, infrastructure limitations, performance. Agreed measurable success criteria both short term with short
sub-population based outputs to file, and long-term full population ingestion to an Oracle database.
-  Data understanding: The existing tagged figures are high quality labels(iXBRL concepts) that can be used for supervised learning. The
different document types have very different taxonomies so should have different models. Different taxonomies can use different iXBRL
concept names, so it’s best to train just on the main taxonomy used for each document type.

-  Data preparation: Cleaned and normalised text; using placeholders for numbers and dates; removing or masking personal data(names,
addresses and references) in line with the Data Protection Impact Assessment completed and Data Protection Act 2018/UK GDPR. Created
stratified train, test and holdout datasets. Also created square root weighted train distributions due to the high-class imbalance.

-  Modelling: This is a multi-class(nominal) classification problem with high class imbalance. Compared different way to vectorise the features
such as TF-IDF n-grams, SBERT, and other embeddings. Compared different model families, scikit-learn classifiers, neural nets and BERT
based models. Tuned hyperparameters using grid/halving search and optuna. Evaluated with macro-F1 to ensure minority classes are not
ignored. Reviewed confusion matrixes for poor performing classes to identify systematic errors that could be mitigated through better data
preparation or additional features. The chosen pipeline was TF-IDF 1-3 n-grams with LinearSVC with balanced class weights. This

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 7 of 22

combination of vectorisation and model was quick, can run on a CPU and has good performance. TF-IDF works well over the domain specific
vocabulary.

-  Evaluation: I used unseen data to evaluate the model and determined that it performed sufficiently well to be deployed.

-  Deployment: The python ML was integrated into a R pipeline using reticulate, with outputs being stored in an Oracle database. Collaborated
with DevOps around deployment approaches and infrastructure. Created on demand compute(ODC) so a separate EC2 instance is fired up
with larger compute resource just to run the daily population and then shuts down. This allows processing a large amount of data within
specified timescale without negatively impacting users on existing platforms.

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 8 of 22

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 9 of 22

Project checklist table

The purpose of this table is to cross-check that the project work completed by the apprentice meets the KSBs required by this assessment
method.

Write a short and clear explanation in the ‘Project Mapping’ column how each assessment criterion below will be met through the proposed
project report and presentation. This project should have been carried out as part of your regular work prior to the EPA gateway. The EPAO will
then review your document.

Please note, performing a skill does not demonstrate that you have the required knowledge and understanding; it is, therefore, essential that you
provide justification for your actions and choices and clearly explain the thinking behind these.

NOTE:
‘OK’ only indicates that the supplied mapping has the potential to meet the requirements of the criterion specified.
DISTINCTION criteria mapping will be noted but we will not provide any direct feedback.

Remember, where you have selected a tool or technique, justify why it has been chosen.

Pass and distinction criteria

Awareness of the opportunities of AI and data science to create business value and growth
(K13, K14)
Pass grading descriptors
AI and data science solution
developed within the project
addresses a business need in line
with quality standards and
timescales. The business value of a
data product / solution and any

Project mapping
I developed a tool Hubble, which extract and categorises untagged items from
iXBRL financial documents. Before analysts could only reliably use tagged
figures, which consists of only 30% of the figures in some types of documents.
Hubble helped us meet our quality standards, like completeness since for most
documents we can extract all of the figures and the ML classes provide
consistency across the data.

EPAO feedback
OK

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 10 of 22

constraints making trade-offs
accordingly have been considered.

The business value is that it reduces manual effort, allows us to better create
statistics that informs and drives government policy and better identify risks.
Performance was balanced by infrastructure/costs, where selecting faster
models that could run quickly on a CPU were prioritised allowing development
on existing infrastructure.

Distinction grading descriptors
Articulates a commercial awareness
of organisational priorities. Explains
how the practical trade-offs in
implementing an AI or data science
solution for the particular business
context have been addressed and
shape the solution accordingly to
optimise outcomes.

Mapping noted but no
feedback given on
distinction criteria.

I designed a solution around HMRC’s priorities of maintainability, reliability,
cost control, data protection, AI safeguards, security and ability to scale to
millions of records quickly.
I chose LinearSVC over transformer based models, trading marginal
performance gains(2.3pp) for a solution that is simpler(more maintainable),
more explainable(feature coefficients), quicker(13x), allows development on
existing infrastructure, with the ability to scale cost effectively.
Separate models for every taxonomy would give the best raw performance, but
I used a single taxonomy for each document type, resulting in consistent class
names, to increase analyst usability.
To scale we would need additional infrastructure, but to be cost effective we
setup on-demand-compute, which allows us to fire up an EC2 instance just for
a job and close it when finished.

Underpinning assessment criteria
K13: How to identify the compromises and trade-offs which must be made when translating theory into practice in the workplace

K14: The business value of a data product that can deliver the solution in line with business needs, quality standards and timescales

Critically evaluate the effectiveness and performance of proposed AI and data science solutions
Pass grading descriptors
Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Project mapping

EPAO feedback

Page 11 of 22

Critically evaluates the performance
of developed AI and machine
models and the steps taken to
mitigate sources of error and bias.

I evaluated many models starting from a baseline(DummyClassifier), and then
compared families such as SVMs, decision trees, random forests, NN, BERT,
using accuracy, recall, precision and f1. I focused on macro-f1 scores since it
provides a single value that that takes into various factors and is appropriate
for the high-class imbalance.
Reviewing the errors highlighted issues around ambiguous descriptions, dates,
names, numeric values, incorrect extractions which provided confusing training
data to the model. So latter iterations removed them or used placeholders,
increasing the macro-f1 from under 50% to over 70%.
To deal with the class imbalance and reduce systematic bias towards majority
classes, I used class weighting and/or sqrt weighting balance training set.
Sometimes the description did not have enough information to predict the
category, so latter models also included table name and heading as features.

OK, but final report
should show the
class-level results
clearly, especially
where minority
classes perform less
well and need analyst
review.

Considers and selects from a range
of appropriate principles, techniques
and solutions to enhance the
robustness of decisions at all
stages.

OK

I used CRISP-DM ensuring that each stage produced documented evidence
back decisions.
A Kanban based agile approach with regular meeting with end users allowed
me to validate business understanding, planned approaches and feedback on
progress.
Robustness was improved through stratified cross validation which reduced
variance and ensured minority classes were represented. I used
HalvingRandomSearch to filter a range of scikit-learn models and
hyperparameters, then GridSearchCV was used to optimise the
hyperparameters. I also calculated t statistics to see if various runs were
statistically different from the top scoring run. I compared different way to
vectorise the features such as TF-IDF n-grams, SBERT, and other
embeddings. The embeddings were significantly better than TF-IDF, but it was
only be 0.3pp and the models ran much slower.  I evaluated different ways to

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 12 of 22

Critically evaluates the arguments,
assumptions, abstract concepts and
data to make business focused
recommendations.

Demonstrates how, from the range
of possible solutions presented, they
contributed to identifying the optimal
solution.

Explains how they implement data
curation and data quality controls in
line with organisational and
regulatory requirements.

deal with class imbalance, weighting and sqrt weighted population sampling,
and used macro-f1 when evaluating models.

I evaluated whether building a ML classifier was justified from a business
perspective. I extracted all the descriptions for key classes and then worked
with SME to go over some key terms used and all the possible variations that
could be used. Some classes, had a large variety of words or phrases that
could be used(some had over 23,000 unique descriptions), including domain-
specific technical terms that not all analysts would be aware of. To manually
use the descriptions, would be difficult, time consuming and error prone. So, I
recommended to create a ML model to classify the descriptions.
I initially used theory to limit the solutions to those that would work well with
supervised classification of text. I evaluated multiple possible solutions, through
experimentation and recording advantages and disadvantages. I looked at
performance scores such as macro-f1, accuracy, training time, inference
latency, cost, complexity and scalability.
Transformer based models had good performance but would require GPUs to
run at required speeds, and after reviewing significant increased costs decided
it wasn’t justified by the extremely minor performance gains.
I selected LinearSVC with TF-IDF(1-3 n-grams) since they worked well on the
domain-specific terminology to give good performance, cost, scalability and
interpretability.
I implemented data quality controls aligned with HMRC expectation and
broadly in line with DAMA UK’s quality dimensions. Missing or low-quality and
ambiguous descriptions were identified were dropped rather than poisoning the
ML model. Personally identifiable(names/addresses) were identified both by
using regular expressions and labels and were replaced with placeholders

OK

OK

OK

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 13 of 22

Distinction grading descriptors
Critically evaluates and adapts
practice making recommendations
for communicating technical
methodology.

allowing the model to work with placeholders while preserving privacy and
compliance with the Data Protection Act 2018/UK GDPR.
These controls improved model reliability and ensured the dataset met both
HMRC and regulatory requirements.

My communication approach evolved based on how stakeholders reacted to
early explanations. Initial technical descriptions were too detailed for some
audiences, so I shifted towards a visual and example-based explanations. So
very simple visual decision trees showing what attribute was split on, or
graphed SVM 2D decision boundary.
A simple example helped illustrate the difference between weighted and macro
scores.
For more technical stakeholders rather than just stating what I did I started to
give more detailed explanations for why certain choices were made and linking
theory to the experimental results.
I recommended that communications should have the headline figures and
results, with a section that explains any technical terms with illustrations and
examples, and an appendix with the technical details.

Mapping noted but no
feedback given on
distinction criteria.

Explains when they have effectively
communicated technical information
in a team context which has
influenced others and impacted
positively on decisions or working
practices.

I explained how the ML category worked and gave examples to analysts
explaining when it works well or not, using confusion matrices and examples.
With greater understanding of the ML category analysts started using the ML
category more when profiling, with Hubble being widely used in by multiple
teams.

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 14 of 22

Underpinning assessment criteria
K23: The use of different performance and accuracy metrics for model validation in AI projects

S3: Critically evaluate arguments, assumptions, abstract concepts and data (that may be incomplete), to make recommendations and to
enable a business solution or range of solutions to be achieved

S17: Consistently implement data curation and data quality controls

Apply systematic methodology and project management principles in the delivery of innovative, stable and
robust solutions

Pass grading descriptors
Selects and uses datasets,
programming languages, tools and
scientific methodologies to research
business problems, providing a
clear justification for their selection.

Project mapping
The main extraction and analysis was done in R(organisation default), since it
has good libraries at parsing html and is maintainable by more analysts. But
python was chosen for ML since the libraries are more mature for text
classification and model evaluation than in R.
Samples were selected to balance statistical power with processing time,
ensuring conclusion were robust without delaying delivery.
This was used to show that while some documents had good tagging levels
average of 70% other documents had very poor tagging levels average of 30%.
Graphs were useful, showing that there was a large variety of terms used for
each class.

EPAO feedback
OK

Analyses and critically evaluates
test data and proposed solutions,
considering current and future
business requirements.

The test data was very imbalanced, so it was important to use balanced
weighting and/or sqrt weighted training populations to ensure the model
worked well on the business requirement that it works well on as many classes
as possible, even minority classes.
Future requirements include scaling to millions of documents with fast
inference speeds(2.7s), on low cost infrastructure. This ruled out the larger

OK

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 15 of 22

transformer based models that would need to be run on expensive GPUs(for
performance reasons), and still be significantly slower to train and run. SVM
based models that can be developed on existing CPU based infrastructure,
have good performance and are very fast.

Manipulates and analyses complex
datasets and critically evaluates
arguments, assumptions, abstract
concepts and data (that may be
incomplete) to make
recommendations and to enable a
business solution or range of
solutions to be achieved.

The source iXBRL documents were complex with inconsistent HTML
structures, iXBRL data and multiple taxonomies. I initially thought best to train
over a large random sample, but different taxonomies had conflicting naming.
A bespoke model for each taxonomy would give the best raw scores, but it
would be confusing to analysts, so it was recommended to train only using the
main taxonomy and use those classes over all taxonomies.
It was assumed that the description would be enough to categorise the data,
but when reviewing where the model didn’t do so well it was clear the
description wasn’t enough, so latter models also used the heading and table
name.

OK

Underpinning assessment criteria
S2: Independently analyse test data, interpret results and evaluate the suitability of proposed solutions, considering current and future
business requirements

S9: Manipulate, analyse and visualise complex datasets

S10: Select datasets and methodologies most appropriate to the business problem

S22: Apply scientific methods in a systematic process through experimental design, exploratory data analysis and hypothesis testing to
facilitate business decision making

S25: Select and use programming languages and tools, and follow appropriate software development practices

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 16 of 22

AI Project and Development Management
Pass grading descriptors
Correctly selects and applies
development, research methodology
and project management techniques
to engage with customers and solve
the business problem being
addressed.

Project mapping
I used CRISP-DM to structure the technical work and used Kanban to manage
delivery using GitLab epics, issues, tasks, and milestones to deliver in iterative
increments. This also provided visibility of progress and timeframes to
management.
I engaged stakeholders regularly, analysts provided feedback about the
outputs, suggesting changes around ambiguous descriptions. Workshops
validated the need, uses the benefits of the data.
These methods ensured regular engagement with customer groups, so the
solution stayed aligned with their needs, directly solving the original problem of
untagged figures, and evolving to solve new problems.

EPAO feedback
OK

Distinction grading descriptors
Can evidence suitable methodology
and tools have been selected with
understanding of the impact of this
choice on working practice, along
with the risks to continuity of
working practice that may arise if
such solutions are not utilised.

An agile approach lets us iterate quickly while keeping stakeholders in the loop.
I chose Kanban since the project team was very small and the overhead of an
approach like SCRUM wouldn’t be appropriate.
CRISP-DM works well on small ML projects like this providing a clear structure.
The use of GitLab for manage projects is not common in HMRC, so there was
a learning curve, but the advantages of transparency, auditability and
documentation outweigh the costs of learning a new tool. Without GitLab it
would make handover difficult.

Mapping noted but no
feedback given on
distinction criteria.

Underpinning assessment criteria
K6: How data products can be delivered to engage the customer, organise information or solve a business problem using a range of
methodologies, including iterative and incremental development and project management approaches

S24: Apply research methodology and project management techniques appropriate to the organisation and products

Use of communication and influencing skills across teams
Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 17 of 22

Pass grading descriptors
Describes how they have worked
with a range of technical and non-
technical stakeholders adapting
their approach successfully to meet
their diverse needs.

Project mapping
Worked closely with analysts where I focused on outcomes, showing confusion
matrices for good and poor quality classes and looking at examples, so they
understood where it would be good, situations where it would make mistakes
and the kind of mistake they should expect.
With DevOps I focused on benchmarks, memory usage and future
requirements.
With managers I focused on the kinds of information they needed like business
level topics like timeframes, resource requirements, funding, blockers they
could help with.

EPAO feedback
OK

Explains how to work autonomously
and collaboratively with
multidisciplinary teams indicating
when each would be appropriate.

I worked autonomously when deep focus was required, such as during core
modelling phases, building models and analysing metrics. I would then demo
my current approach and get feedback in meetings with ML experts. When
evaluating the outputs I would collaborate with SME who had a deeper
understanding of the taxonomies, and the issues of lumping them together.
I would often work collaboratively on tasks assigned to other team members,
partially to share knowledge and also upskill them.
I would work collaboratively with DevOps since they had knowledge, expertise
and control over infrastructure that I did not have.

OK

Describes how they have analysed
information and data, using
questioning and discussions with
subject matter experts to scope new
AI and data science requirements.

I asked SME about errors where the predicted class was what I expected but
the iXBRL concept was slightly different, they explained that some concept
names differ between the different taxonomies, which meant that each model
should have training data limited to a single taxonomy, but it would be good to

OK

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 18 of 22

Written and verbal communication is
clear, structured and appropriate for
the audience.

Explains how to work with software
engineers to ensure suitable testing
and documentation processes are
implemented.

use the main taxonomy to classify across all the documents since that would
provide standardised labels.
I asked about names and dates, whether replacing them with placeholders or
removing them. They noted that pure names can be related to multiple classes,
so best to remove them. For dates they noted that there are some specific
dates like 31 March 1982 that have a specific meaning, but most of them have
no meaning.

OK

For issues on GitLab, I created a template which integrates into GitLab which
ensured that issues were clear with details of every step required to recreate
the issue, expected vs actual and proposed fixes.
The project readme utilises markdown to provide clear headings and sections,
with instructions, links and code blocks, which has been successfully used by
many analysts to setup the tool.
Presentations to non-technical audiences roughly follows the Problem-
Solution-Outcome structure. The solution is at a very high level without going
into the technical detail, with the focus on the outcomes each slide focused on
a separate benefit/functionality with clear examples they could understand
explaining what it does without going into unnecessary detail.

I had the codebase reviewed. We reviewed the unit test which covered key
functions and integration tests to cover the end to end process. This was under
the constraint that the unit tests shouldn’t contain any customer data, so used
synthetic or anonymised fixtures instead.
GitLab was used to document all key aspects, with documents covering data
structures and types, guide to setup Oracle tables and create developer
credentials, details of key decisions and the reason why they were made. The
task list and issues were moved to the dedicated GitLab page.

OK

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 19 of 22

Mapping noted but no
feedback given on
distinction criteria.

Distinction grading descriptors
Explains how they adapted their
approach with a range of technical
and non-technical stakeholders and
in different situations in order to
achieve the best outcome for the
business.

Evaluates solutions and explains the
risks and implications of the AI data
science requirements and
alternative approaches and ways to
address them.

With managers I focused less on the technical development and focused on
the business level, so benefits and outcomes, timeframes for improvements,
and the benefits of more people working on the project, which resulted in work
being reallocated for someone to focus on development. Memos were drafted
with cost benefit analysis requesting more funding for infrastructure, this
resulted in additional funding for infrastructure.
I created a setup script and detailed readme to allow other users to setup and
use the tool. This means many analysts are now running the tool allowing me
to focus on development.
With the project team I used a more formal Kanban process using GitLab to
track work and progress of team members, which resulted in team members
being more productive.
The various options were evaluated not just in terms of performance but also
explainability, operational risk, security, infrastructure constraints and long-term
maintainability. Analysts were educated that the ML category can be wrong
and shouldn’t be used for automated decisions. There should always be a
human in the loop before any action on it happens. This would include a
person looking at the actual descriptions.
Some models had marginally better performance, but are black boxes, which
poses a risk, so I went with a model that is explainable.

Underpinning assessment criteria
K28: How to communicate concepts and present in a manner appropriate to diverse audiences, adapting communication techniques
accordingly.

S4: Communicate concepts and present in a manner appropriate to diverse audiences, adapting communication techniques accordingly.

S5: Manage expectations and present user research insight, proposed solutions and/or test findings to clients and stakeholders.

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 20 of 22

S27: Analyse information, frame questions and conduct discussions with subject matter experts and assess existing data to scope new AI and
data science requirements.

B2: Reliable, objective and capable of independent and team working.

B6: Is comfortable and confident interacting with people from technical and non-technical backgrounds. Presents data and conclusions in a
truthful and appropriate manner.

Application of technical knowledge
Pass grading descriptors
Describes how they applied
appropriate scientific and
technological methods for machine
learning, AI and data science
solutions, services and platforms to
deliver business outcomes outlining
successes and challenges.

Project mapping
I used hypothesis formulation, controlled experimentation, stratified cross
validation, grid/halving search, optuna, and comparison against
DummyClassifer to ensure real performance gains. Challenges included class
imbalance which required different approaches for different models, balanced
weights and/or sqrt weighted training samples.
Successes are that the LinearSVC with TF-IDF, has good performance, is fast,
can run on a CPU, and has been deployed at larger scales.

Distinction grading descriptors
Explains the rationale for selecting
particular technical solutions,
including the relevant consideration
of scientific benefit and suitability for
working practices .

The selection of TF-IDF and LinearSVC was selected due to performance,
computational efficiency, explainability, scalability and suitability for HMRC
working environment. The short domain-specific descriptions led itself well to
TF-IDF(1-3 n-grams) with discriminatory vocabulary captured as their own
feature. LinearSVC works well with sparse matrices like those created by TF-
IDF and using L1 regularisation which removes irrelevant features, resulted in
even sparser matrices, allowing inner products to be done very efficiently. This
allowed me to test and develop the model using existing infrastructure without
disturbing other users.

EPAO feedback
OK, but final report
should make clear
how the ML category
is governed in
practice, particularly
that it supports analyst
review rather than
automated decisions.

Mapping noted but no
feedback given on
distinction criteria.

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 21 of 22

Appraises AI and/or Data solutions
and explains the risks and
implications of the process,
alternative approaches and ways to
address them.

The model has high accuracy 97%, but high class imbalance means that it
underperforms on minority classes, with some classes performing very poorly.
Summaries of poorly performing classes have been created for analysts so that
they are aware of when they might need to do more bespoke and complex
description matches rather than using the ML category. There is an interactive
dashboard which has this data in it, which can help people determine how well
the model does with certain categories. Often the errors are misclassifying very
similar categories and the features don’t have enough information to
differentiate between those categories.
The ML category can be wrong, so should not be used for any automated
decisions, so the process requires a human in the loop, who should review the
actual description.

Underpinning assessment criteria
K1: How to use AI and machine learning methodologies such as data-mining, supervised/unsupervised machine learning, natural language
processing, machine vision to meet business objectives

K3: How to apply advanced statistical and mathematical methods to commercial projects

K5: How to design and deploy effective techniques of data analysis and research to meet the needs of the business and customers

K26: The scientific method and its application in research and business contexts, including experiment design and hypothesis testing

S11: Apply aspects of advanced maths and statistics relevant to AI and data science that deliver business outcomes

S15: Identify, develop, build and maintain the services and platforms that deliver AI and data science

S18: Develop tools that visualise data systems and structures for monitoring and performance

Copyright © BCS 2024
BCS L7 AI Data Specialist IfATE V1.0 Work-based Project Sign-Off Document V2.0, June 2024

Page 22 of 22


