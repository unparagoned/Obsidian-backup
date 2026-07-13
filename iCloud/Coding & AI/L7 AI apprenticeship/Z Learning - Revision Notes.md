

# Data Science

Data science is about improving decision making by insights extracted from large data sets.

Data science includes a set of principals, problems definitions, algorithms, and processes for extracting non-obvious and useful patterns from large data sets.

Data science includes ML and data mining, and also includes stuff like capturing, leaning and transforming data.

Data science allows for customer segmentation/clustering.

Or association rule minding, identify products that are brought together.

Or anomaly or outlier detection.

Classification/prediction. - predicting a missing value or attribute, rather than what will happen in the future. e.g. predict if an email is spam.


Hierarchy of needs, aggregate and explore might be dependent on each other

![[623b64ef5c4cbd767e53d7477e4e8b97_MD5.png]]


## Skills of a Data scientist

- Communication
- Domain expertise
- Data ethic and regulations
- Data wrangling and databases
- Computer science and HPC
- Data visualisation
- Statistic & probability
- Machine learning


![[d1bc52d3bd081303094e5ea7637bbddc_MD5.png]]


Data engineer. Create and maintain the architectures including databases and large scale data processing systems.

Expertise in SQL, NoSQL, Hadoop/Spark

Java, Scala, Python

Architecture design and how to build robust data pipelines

Problem solving skills related to data quantity, quality and processing speed.

- How have data-driven decisions have influenced strategic initiatives?

Extractions, categorisation of data provides insight into companies which helps inform government policy.

- Are there areas where data science has led to cost savings, improved efficiencies, or better customer relationships?

# Data

Transactional data includes event information such as the sale of an item, etc.

Relational databases store data as one row per instance and one column per attribute.

Big data is defined in terms of the three Vs, volume of data, variety of data, and velocity it must be processed.

Resulted in the development of NoSQL databases - simpler data models than traditional relational databases.

Big data is also about processing data quickly, e.g. MapReduce in Hadoop. Queries are processed on multiple servers then reduce(merged) together.

## Create a dataset
- Collect data
- Data cleaning
- Transformation
- Integration. If from different data sources, i.e. match formats, etc.
- Formatting, SQL, JSON, CSV.

## Relationships

- Must involve two entities, although it could be with itself
- Can't be more than two entities

If data needs to be stored about the relationship then it's an entity.

A data model describes how data is represented within a system

## Conceptual model

Identifies what concepts(entities) the data model is about

Describes how the concepts relate to each other

## Logical data model

Identifies what information will be stored about each entity

Labels the relationships

So stuff like data types, key attributes, etc.

## Physical data model

Precisely describes how the data will be stored and their types

May introduce additional constraints

Includes selecting a database

Entities become tables

Attributes become columns

Primary and foreign keys specified

How to develop a data model

- Top down from business requirements
- Bottom up, from example data



## DIKW pyramid

WISDON - applied knowledge, how to make practical and ethical decision

KNOWLEDGE - organised information, can answer "how"

INFORMATION - linked elements, processed and structured

DATA - abstracted elements - raw data


![[956c8212974b360097693252a1347838_MD5.png]]


## Data types

### Structured 

SQL

### Semi-structured
XML or JSON
If there is a flexible format then it's semi-structured, so json/xml can be semi-structured but also structured
If the json always meets a schema then it's structured.

### Quasi-structured

Some structure but doesn't fit into a relational database e.g. emails

### Unstructured

text. images video

Raw data are direct abstractions like weight or height.

### Raw data


### Derived data 

is like a BMI

### Captured data 

are direction measurements,

### Exhaust data 

are biproducts, like metadata.

Attributes are either numerical(continuous or discrete) or categorical(ordinal[e.g. poor to good] or nominal[e.g. colours])

Satisfaction scores (ordinal data) meadia or mode scores

Sales data(numerical data) time series to predict future.

Employee categorisation(categorical data) Analysis may use bar charts to display distribution.


### Numeric data

#### Continuous 

#### Discrete

#### Interval

Like a date, where difference makes sense but not multiplication, no zero origin.

#### Ratio

Has a true zero origin, so Kelvin not C

### Categorical
#### Nominal

Like names or sex. 

#### Ordinal

Can be ordered, good, ok or bad


## Big Data

- Volume. Amount of data generated and stored.
- Variety. Wide range of data sources and formats, structured, semi-structured(JSON) and unstructured(pdfs) and binary(images, audio, vidoe)
- Velocity. Speed data is generated and processed.
- Veracity. Accuracy and reliability of data.
- Value. How useful and relevant the data is.


# Architecture

Data governance. Data architecture must comply is rule and policies.

Data security standards. Prevent unauthorised or malicious access, modifications nor disclosure.

Oversight of pipelines.

Storage capacity. The data architecture must consider how much storage is need by different systems.

Reduced latency.

Scalability

Data architecture and data analysis.

Data architecture is a blueprint or a plan for how to use data.

Include rules, policies, standards and governance.


![[88a2278734e8285003780f398ba4da67_MD5.png]]

- Relational data warehouse
- Data lake. Just storage no compute, but there are many compute engines that work with a data lake. e.g. Hadoop Distributed File System(HDFS). Can be hard to query or use the data in a lake. 
- Modern data warehouse. Uses a lake for storage and ML, and data warehouse for normal querying.
- Data Fabric. A large fabric of systems that can ingest any sort of data.
- Data lakehouse. Gets rid of the relational data warehouse and just uses on repository a data lake. All data goes into the data lake, and all queries are done from the data lake. A delta lake runs on top of the data lake and works more like a relational database. e.g. Delta Lake, Apache Iceberg, Apache Hudi.
- Data Mesh. Data is kept within domains, and they are connected.

## Data lake architecture

1. Ingestion layer. Collecting and importing data. Supports multiple data ingestion methods, including match processing, real-time streaming, and API-based data collection.e.g. Apache Kafka, Apache Nifi, AWS Kinesis, Azure Event Hubs.
2. Storage layer. Where raw data is stored. Scalable and cost-effective storage that can handle structured, semi-structured and unstructured data. Distributed file system or object storage systems like Dadoop Distributed File system(HDFS), Amazon S3, Azure Blob Storage, Google Cloud Storage.
3. Processing layer. Transform, cleaning and analysis of data stored in the data lake. Supports a variety of data processing frameworks and tools for batch and real-time processing. e.g. Apache Spark, Aparche Fink, Presto, AWS Glue, Azure Data Factory.
4. Data catalogue and metadata management. Ensures users can find, understand and trust the data in the lake. Comprehensive view of the data including its lineage, quality and usage. e.g. Apache Atlas, AWS Glue Data Catalogue, Azure Data Catalogue.
5. Security and governance layer. Ensures that data in the lake is secure and complies with regulatory requirements. Includes control, encryption, auditing and monitoring to protect sensitive data. e.g. Apache Ranger, SWS Lake Formation, Microsoft Purview.
6.  Consumption layer. Allows users to access and analyse data stored in the lake. Supports varies access methods including, SWL, ML models and data visualisation tools. e.g. Tabeau, Power BI, Jupyter Notebooks.

Key features of a data lake

- Scalability.
- Flexibility. Can store all data types in their native formats. Including structured data from databases, semi-structured data like JSON and SML and unstructured data like text, images, video.
- Cost-effectiveness. Leveraging cloud storage data lakes offer a cost-effective way to store large amounts of data. Pay-as-you-go pricing.
- Accessibility: Multiple data access methods, such as SQL or ML workflows, or big data processing frameworks.
- Integration and interoperability. Works seamlessly with a variety of data processing and analytics tools.
- Data governance and security. Ensure daata security and governance is citical. Access control, encryption and auditing.
- Real--time data processing:

### Risks of data lakes

- Data governance challenges. Without proper governance they can be swamps of used and disorganised data. Robust metadata management, data catalogues and governance frameworks help maintain data quality and compliance.
- Security and privacy concerns. Employing strong encryption, access controls, regular security audits is essential.
- Complexity in data integration. Integrating data could result in issues with data consistency and integrity.
- Use Extract, Transform, Load(ETL) tools and establish clear data integration process.
- Performance issues. Leverage data partitioning, indexing and appropriate data processing frameworks to enhance performance.
- Skill requirements. Invest in training and hiring skilled professions.

### How to build a data lake

1. Define objective and requirements. e.g. improve data analytics, support ML. Identify types of data.
2. Choose the right platform. AWS, Azure, Google Cloud offer scalable and cost-effective solutions. In-prem provide more control but can be more expensive and complex to manage. Select the right storage solution, S3, Blob, etc.
3. Design the architecture. Ingestion layer, storage, processing framework, data catalogue, security.
4. Data ingestion. Data sources, ingestion tools that ingest data in its native format.
5. Data processing and transformation. Clean and prepare data, transform data.
6. Implement data governance. Update and manage metadata so data can be easily discovered and understood. Implement data quality checks and validation. Ensure data lake complies with regulations and standards such as GDPR.
7. Enable data access and analytics. Provide tools such as SWL query engines(e.g. Presto AWS Athena), data visualisation tools(Tableau, Power BI), ML platforms(AWS SageMaker, Azure ML). Train users on how to access and utilise the data lake effectively.
8. Monitor and optimise. Continuously monitor the performance to identify and address bottlenecks. Optimise the data lake's architecture and processes to ensure it remains efficient and cost-effective. e.g. adjusting storage config, refining data ingestion process or upgrading processing frameworks.

### What is a data warehouse?

A data warehouse, is a central repository to store, manage and analyse data. It is structured providing efficient querying and analysis, unlike a data lake.

![[db024e253a37b7754553ca8c2c820b2c_MD5.png]]

Key features

1. Subject-orientated, so all data relating to a real-world object or event is linked
2. Data from different sources are integrated to provide a single source of truth
3. Data in a SW is non-volatile, real-only and doesn't change.
4. SW are time-variant, allowing for analysis of historical data to show differences over time.

#### Data warehouse schemas

Stored using a star schema. Using primary and foreign keys.

![[0945cd4e633c6bd308e40afed23414ec_MD5.png]]

Can also have child tables

![[4c183891a77920dfc500b7acba831584_MD5.png]]

### Data Lakehouse

Combines data lake and data warehouse.

Desirable features

- Schema enforcement and governance
- Transaction support
- Business Intelligence support
- Storage decoupled from compute to enable scalability
- Openness - open storage formats allow any data to be stored and accessed.
- APIs for access to data sets
- Support for both structured and unstructured data
- Support for diverse workloads
- End-to-end streaming
- Catalogue system for discoverability

### Data cubes

DW use online analytical processing(OLAP) to provide multidimensional analysis of the data. OLAP systems use data cubes to create multidimensional datasets.

![[15ed1518b49bedccf7e1959d03f43ab0_MD5.png]]


### Data vaults

Business keys are separated out and held in entiity-descrete tables called hubs. Attribute data is held in other tables called satellites which are linked to the hubs.

- Hub:: Represents core business entities such as customers, products, orders. Each hub contains a unique list of keys which are stable identifiers for the entities. Also contain metadata.
- Links: Links capture the relationships between hubs. e.g. link between customers and orders. Also contain metadata
- Satellites: Store data the descriptive attributes and contextual information related to hubs and links. Attached to specific hub or link. Allow for tracking changes over time without modifying the core structure of hubs and links.

![[b8164ad5d993731067e0524afe6c96c7_MD5.png]]

Data volts are better able to accommodate changes and integrate systems. There is no data cleansing.

Principles of a data vault

- Scalable. Handle large volumes of data. Lots of data and new data sources and changes.
- Flexible. Allows integration of disparate data sources.
- Supports agile development.
- Robust audit trail. Since data is traceable to its source.


### Data mesh

The idea was introduced by Zhamak Dehghani in 2019, and in addition to the content here, you can also read about this by following this link to [Dehghani's article on Data Meshs](https://martinfowler.com/articles/data-monolith-to-mesh.html).

From [[https://app.qa.com/course/big-data-architectures-ai-1698/data-mesh/?context_id=14499&context_resource=lp](https://app.qa.com/course/big-data-architectures-ai-1698/data-mesh/?context_id=14499&context_resource=lp)](app://obsidian.md/%5Bhttps://app.qa.com/course/big-data-architectures-ai-1698/data-mesh/?context_id=14499&context_resource=lp%5D\(https://app.qa.com/course/big-data-architectures-ai-1698/data-mesh/?context_id=14499&context_resource=lp\))

Rather than central system it's distributed. With each owner responsible for their data. So areas of expertise are responsible for their data rather than a central team.

### Data fabric

Like Denodo

The term first emerged in 2013 when Forrester introduced the idea of Information Fabric. You can read about this on the [Forrester website](https://www.forrester.com/blogs/13-08-15-information_fabric_30_delivers_the_next_generation_of_data_virtualization/). Since then, the idea has been further developed. It is not the same as data mesh which you learnt about in the previous unit. Data fabric is focused more on automation. According to Gartner, data fabric is '[a design concept that serves as an integrated layer (fabric) of data and connecting processes](https://www.gartner.com/smarterwithgartner/data-fabric-architecture-is-key-to-modernizing-data-management-and-integration)'

From [[https://app.qa.com/course/big-data-architectures-ai-1698/data-fabric/?context_id=14499&context_resource=lp](https://app.qa.com/course/big-data-architectures-ai-1698/data-fabric/?context_id=14499&context_resource=lp)](app://obsidian.md/%5Bhttps://app.qa.com/course/big-data-architectures-ai-1698/data-fabric/?context_id=14499&context_resource=lp%5D\(https://app.qa.com/course/big-data-architectures-ai-1698/data-fabric/?context_id=14499&context_resource=lp\))

A integration layer over distributed data.

Data virtualisation: Data remains distributed but is integrated as an abstraction layer.

Augmented data catalogue: Provides metadata to provide context.

Knowledge graph: Show relationships between data

Metadata activation: Automated services to help with metadata

Recommendation engine: AI/ML will continuously analyse, learn and make predictions on data integration and the management ecosystem based on the active metadata.

Data preparation and ingestion: Much is automated

Data Ops: Teams work together for continuous integration and delivery.

e.g. Microsoft Fabric has a virtualisation layer. Snowflake AI data cloud, AWS sagemaker





## Schema on write
Like a relational database

## Schema on read
Like a Data lake


## Relational modelling

1NF: One value per cell
2NF: No dependency on part of a composite key.  Must depend on full key
3NF: No dependency on non-key column

Denormalisation: when redundant copies of data are in multiple tables

## Data Vault

Hubs - business entities, like customers or products

Link - relationships between hubs, typically as a separate table. A link table contains a set of foreign keys that reference the primary keys of the related hubs.

Satellites - Store descriptive attributes about a hub or a link.

Complex

Data duplication, since data is stored at the atomic level.

Performance, can be slow and more complex queries.

Lack of standardisation.

#### Kimball and Inmon Data Warehousing Methodologies

Top down Inmon

![[880596cb718606ef195729328d5db404_MD5.png]]

Kimball bottom up

![[8171807f73953824e9f479aa870729e3_MD5.png]]


## Hadoop

Based on Google paper on MapReduce

- Distributed storage
- Distributed processing
- Resilience: If a node fails it can recover. Offers a single view of the data as if it was on a single file system
- Parallel processing. Implements Hadoop MapReduce which can split data into chunks and run the chunks in parallel

- Mapreduce: Processing using different languages
- Hive & Drill: Analytical SQL on Haooop
- Mahout & Spark Mlib: Machine learning
- PIG: Scripting
- Hbase: NoSQL database
- Zookeeper & Ambari: Management and coordination
- Spark: In-memory, data flow engine
- Kafka & Storm: streaming
- Solar & Lucene: Searching and indexing
- Ooxie: Scheduling
- YARN: Resource management
- Storage: Hadoop Distributed File System (HDFS)



# Statistics

## Types
### Data collection, e.g. make sure collection of sample is representative

### Descriptive statistics

Present data numerically or visually

Measures of central tendency, e.g. 

## Process

### Statistical investigations

- Formulate question or hypothesis
- Designing the study
- Collecting the data
- Analysing data
- Interpreting results
- Presenting findings

### Sample, Explore, Modify, Model, Assess(SEMMA)
Sample - data collection, sampling techniques, data partitioning(train test)
Explore - Descriptive stats, data visualisation, correlation analysis
Modify - Data cleaning, data transformation, feature engineering
Model - Modelling selection, model training, hyperparameter tuning
Assess - Model validation, performance metrics(accuracy, precision, recall, f1, ROC-AUC), model comparison

### Mean
Uses all data but sensitive to outliers

### Median
Middle or mean of two middle values. Not sensitive to outliers.

### Mode
Most common, good for categorical data 

Measure of dispersion, range, variance, standard deviation

Measures of position, percentiles, quartiles
### Inferential statistics

Making conclusions from the data

Inferential statistics, make predictions or inferences about a population based on a sample of data.


## Distributions

Statistics is the practice of collecting and analysing data to make findings or predications.


![[b820ed0301bdb4af999353f1f095aee3_MD5.png]]

### Zscore - turns a distribution into a normal distribution

![[f0ecf546c9f88967183c0590d2bda673_MD5.png]]

### Coefficient of variation  - help determine how spread out distributions are

![[a18ab638630cc0d0ba1ed9f6aee575a7_MD5.png]]

### Central Limit Theorem

If the population is not normal, but you take sample size greater than 30, the sample mean will be roughly normal. 

The standard deviation equals the population sd divided by the square root of n

![[33ce4ba31c9bbfb0c2bdaefa1be38617_MD5.png]]

Less than 30 samples use a T-distribution, which has a fatter tail for more uncertainty and variance.
### Confidence interval


![[276812759316c210b4fd69d3a5c14bef_MD5.png]]



## Means
### Geometric mean

(A x b x c)^1/3

This would be better for say finance where the return is a multiplication of values, so better than arithmetic mean

### Harmonic mean

3/(1/3 + 1/5 + 1/6)

e.g .average speed of 35mph and 20mph


## Hypothesis testing

Forming a null(H0) and alternative(H1) hypotheses

Null is that there is no pattern or evidence.

Determine the likelihood that the sample data supports the null hypothesis

P-value is chance of it happening if there was no pattern. Usually want it to be less than 5%

Factors in creating null hypothesis

1. Objective of research
2. Directionality. Non-directional(two tailed). Expect a difference but don't predict the direction. Directional(one-tailed) predict direction of difference, suitable when theories suggest an outcome.
3. Simplicity and clarity. The null hypothesis should offer a simple contradiction to the alternative hypothesis.
4. Feasibility. Can it actually be tested


### Type I error

Type I error is when you reject the null hypothesis, but it's actually true. False positives.

### Type II error

Type II error is when you do not reject the null hypothesis, but it's false. False negative.


### Significance tests

Chi-squared is used for nominal data, while t-tests and ANOVA are suitable for interval and ratio data

Comparing means: Use T-tests or ANOVA

Assessing relationships: Use correlational or regression analysis to examine the relationship between variables

Testing Associations: Use chi-squared tests to explore associations between categorical variables

Parametric tests such as t-tests and ANOVA assume normality and homogeneity of variance, if these assumptions are violated, non-parametric tests like Mann-Whitney U Test or Kruskal-Wallis Tests may be more appropriate

Independent groups: Use independent t-tests or one-way ANOVA

Paired samples: Use paired t-tests or Wilcoxon signed-rank test

Repeated Measures: Use repeated measures ANOVA

Sample size

Larger samples let us assume normality

Smaller samples sizes non-parametric tests are often preferred.

Level of measurement

Continuous variables: T-tests, ANOVA, regression

Categorical: chi-squar5ed or fisher's extract test.
#### Pearson's correlation coefficient for linear relationships

- Pearson’s Correlation Coefficient: Measures the linear relationship between two continuous variables.

![[85ec6366fe711a17e69f833282195a05_MD5.png]]

t-statistics for Pearson correlation coefficient.

![[1fa4d753ebc35c941c03fc5b646a4835_MD5.png]]

#### Linear regression

![[bf7bc4f05f530fcaff7b1d6d59a0f44f_MD5.png]]

![[248687aa791a42400405a13908bbbb69_MD5.png]]

![[b156b3fd5d08fe81ab87f562ca863df6_MD5.png]]

 y = dependant variable, a = y intercept function, b = slope of the regression line, x = independent variable, r = Pearson’s correlation coefficient, S_y= standard deviation of y, S_x = standard deviation of x, y ̅ = mean of y sample and x ̅ = mean of x

#### Z test

n > 30

If we known the variance and it's a normal distribution.

Where the population variance is known?

If x is normally distributed with mean mu and sd

![[5ddefd7b4b9e80ad25bd6ec35ee248aa_MD5.png]]

A sample has a variance of the population variance/n

So a z test statistic for a sample is

![[95bcd66f7bd6672d935e4606efe1a688_MD5.png]]

The second is about sample means, so you get a factor of square root n. 
So if the sample is the population, the standard deviation of the means is zero, n is high
If the sample population is say 1, then it's the same as normal. 
If the sample population is 2, then you create the means of all pairs of numbers, then work out the standard deviation of those means.

Then compare to critical value.

95% confidence is "testing at the 5% level"

Comparing two groups

![[5fd5188573ae4d856b4571f9c31b310e_MD5.png]]

X is the mean of a sample of size n from a normal distribution with mean mu

We don't know the mu means are but the null hypothesis says mu1 = mu2, so it cancels out.

#### T-tests 


- Independent samples T-Test: Compares the means of two independent groups.
- Paired samples T-Test: Compares the means of the same group at different times.
- One-sample T-Test: Compares the mean of a single group to a known value.

Where the population variance is not known.

So we estimate it from the sample sd, where we use n-1 factor.

![[fa389ad86328a15432b9db4c6a156155_MD5.png]]

If the population is large enough say 30, then we can use a z-test

![[29b5079df4d050fdb0257a3c53b69b1e_MD5.png]]

We use students t-distribution with n-1 degrees of freedom.

(2.55 -2.5)/0.1*20^0.5 = 2.2361

Paired t-test

Subtract values from one group from the other and use the differences

With the null mu = 0

2.1/(1.96921/10^0.5)=3.37231

Df = 10 -1

Unpaired t--test

Pooled sd, just calculated as the average of the variances

![[3dcb2343a8a0ea4c25cda2c6a3e40ac6_MD5.png]]

(12.2-13.1)/(2.7722/(8/2)^0.5)=-0.6493

The n is just for a single group.

Df = 2n -2 =  14

Unpaired with unequal size

![[d5e7fcf38ce5edbc1d98c1a605522a78_MD5.png]]

![[e8e0d7dfc1e4757134815c79f28d3fdf_MD5.png]]


#### ANOVA(Analytics of variance) 
- One-Way ANOVA: Tests for differences in means across multiple groups.
- Two-Way ANOVA: Tests for the influence of two different categorical independent variables on a continuous dependent variable.

e.g. comparing the test scores of students from different teaching methods to see if the teaching method affects performance. One-way ANOVA is used since there is one independent variable(the teaching method) and one dependent variables(test scores)

#### Chi-squared tests.  
Asses relationships between categorical variables(nominal)

- Chi-Square Test of Independence: Determines whether there is an association between two categorical variables.
- Chi-Square Goodness of Fit Test: Determines whether a sample matches an expected distribution.

Does the data fall into various classes as expected.

![[14e0817eedddf9d5e1419f2b65ac3df0_MD5.png]]

O is observed frequencies, E is expected frequencies

It's always a one tailed test, since the value can never be negative.

Degrees of freedom is number of categories -1

The null hypothesis is that chi-squared = 0, with alternative being >0

Compare to both 0.05 and 0.01. So it might be that there is some evidence to reject the null but not strong evidence and so on.

Two criteria

If you had a table of peppers by size and colour, that creates a table. So when trying to work out if there is a correlation between size and colour you can use chi-squared test as well.

Degrees of freedom are (m-1)(n-1)

Expected is the table col sum * row sum / table sum

Then do chi-squared for the whole table.

#### F-tests

Compare two variances to see if they are significantly different. Commonly used in the context of ANOVA. The test evaluates whether the variability within the groups is less than the variability between groups.

![[60ed47a569c9d980512b8ef9130b5f62_MD5.png]]

F-test statistic = Var1/var2

Look up degrees of freedom the right way around, which is? Should be higher variance is column and denominator is the row.

### Non-parametric testing

Don't require any assumptions about the distribution of the data. So useful when using ordinal data, skewed distributions or small sample sizes. They often use ranks rather than actual data values, which makes them more robust against outliers and non-normality. Includes Mann-Whitney U test and Kruskal-Wallis test

#### Mann-Whitney U Test
Compares differences between two independent groups when the dependent variable is either ordinal or continuous but not normally distributed. Used when assumptions of T-test are not met.

e.g. compare the recovery times of patients using two different treatments, where data is no normally distributed.
#### Wilcoxon Signed-Rank Test
The Wilcoxon Signed-Rank Test is a non-parametric test for comparing two related samples or repeated measurements on a single sample. Alternative to paired sample T-test when the data does not meet assumptions of T-test

e.g. comparing pain levels in patients before and after treatment where the data does not follow a normal distribution.

#### Kruskal-Wallis Test

Non-parametric test that is used to compare three or more independent groups when the dependent variable is either ordinal or continuous but not normally distributed. Alternative to one-way ANOVA when assumptions are not met. It evaluates whether the medians of the groups differ significantly.

e.g. Assessing the effectiveness of three different diets on weight loss where the distribution is not normal.

#### Regression analysis: 
Model the relationship between dependent and independent variables to predict outcomes

- μ (mu): Represents the population mean. It’s the average value of a variable in the entire population.
- σ (sigma): Denotes the population standard deviation. It measures the spread or variability of data points in the population.
- x̄ (x bar): Refers to the sample mean. It’s the average value of a variable in a sample.
- s: Represents the sample standard deviation. Like σ but calculated from a sample.
- n: Stands for the sample size. It indicates how many observations are in a sample.
- p-value: An important concept in hypothesis testing.
- Z-score (z): Measures how many standard deviations a data point is from the mean.




# Processes
## CRISP-DM


![[31e2aa0c553a645a6ec120871be4fddb_MD5.png]]


Business understanding: Getting to know the needs of the business in the context of the problem and ensuring the project goals align with business objectives. This can include a business plan. The data science problem can be framed here in terms of form of input and form of desired output.

Data understanding: Establish data availability, collecting data, describing data, exploring data and verifying data quality.

Data preparation: Selecting data, cleaning data, constructing data(feature engineering), linking data, transforming data, formatting data. The final data set will be created here.

Modelling: Selecting the ML techniques to explore, building the models, fitting the models and collecting results

Evaluation: Assessing overall results and determining if the goals of the project have been met. Decide whether to deploy model or not. Bias detection.

Deployment: Liaise with technical teams to put the deployment into production. Including production pipelines, storage structures, setting up process for regular review, monitoring and planning training for users. Might want feedback from users to see if it meets their needs.


![[c1b039565ff390fe2950b67eb457903f_MD5.png]]


## Team Data Science Project(TDSP)

TDSP is a data science methodology launched by Microsoft in 2016. It combines software engineering, agile processes, and core data science life cycle. It is useful for large projects, so different teams can work on different parts.

![[4783940f7a73187a95b40f389caf78ff_MD5.png]]

Starts with Business problem, then data acquisition and understanding(domain knowledge, exploratory data analysis, data cleaning, data pipelines) and modelling(feature engineering, model training, model evaluation and hyperparameter tuning). Then Model deployment and presentation(integration into a larger application, performance monitoring, dashboards, or reports). Ends with stakeholder acceptance.

TDSP has four key components

1. Data science life cycle definition
2. Standardised project structure
3. Recommendations for infrastructure and resources
4. Tools which support responsible AI

## Knowledge Discovery in Datasets(KDD)

Is a systematic method for extracting useful information from large amounts of data. Focuses on pattern discovery or data mining.

![[399e06cab3738784498733115a0f2d3c_MD5.png]]

Selection(stored data), preprocessing(selected data), transformation(prepared data), data mining(transformed data), evaluation(pattern discovered and new knew knowledge).

## SEMMA(Sample, Explore, Modify, Model and Assess)

Was developed by SAS as their recommended process for data mining.

![[f529fa591e3ed3908aa1f38c41da3d73_MD5.png]]

1. Sample - Samply yes/no
2. Explore - Data visualisation, clustering, associations
3. Modify - Variable selection, creation, data transformation
4. Model - Neural networks, tree-based models, logistic models, other stats models.
5. Asses - Model assessment


## Waterfall

![[a11d2f62106af464d273f120ca009f40_MD5.png]]

![[b5e524f22d62f9a5ef7fe8b98ebb152e_MD5.png]]

## Agile

Main tenets:

- Put individuals and interactions before process and tools
- Put working software before comprehensive documentation.
- Put customer collaboration before contract negotiation.
- Put responding to change before following a plan

Best practices

- Flexibility
- Work breakdown
- Strong teamwork
- Iterative improvements
- Cooperation with a client.

Not perfect for all project. E.g. with regulatory requirements a more structure approach might be ideal.

Agile is a philosophy. Two methods are Kanban and Scrum

## Kanban

Is a visual management system to see work in progress, manage workflow and optimise efficiency. It does not have a defined process, so offers flexibility, but can also cause confusion over the process, and extra work deciding the process.

![[53f63b36d998b0f68d63dd1ec4f445d9_MD5.png]]

## Scrum

Roles

- Product Owner
- Scrum Team
- Scrum Master

![[502aae97345e8b6ef52856d4ccf879f0_MD5.png]]

- Product owner creates a backlog
- Scrum team conducts a sprint planning session, where the backlog are converted into logical tasks, which can be completed in short sprints
- Team decides time duration for every sprint, usually 2 week, but could be 1-4 weeks.
- Team gets together every data for Scrum meeting - daily standup
- Scrum master guides the team, making sure they have everything they need and keeping them motivated
- Stakeholders and product owner conduct a review at the end of each sprint.
- Team reflects on the sprint and identifies lessons learnt

- Sprint
- Sprint Planning
- Daily Standup
- Sprint Review
- Sprint Retrospective

Scrum artifacts are:

- Product backlog
- Sprint backlog
- Product Increment: Set of items delivered in the sprint

Methods to achieve them can be flexible

- User stories.
- Story pointing - Developers estimate effort needed to satisfy a user story
- Burndown Charts - Amount of work that has been completed in a sprint and the total work remaining
- Scrum of Scrums - Used for complex projects where multiple teams need to work together.

### Is agile suitable to Data science

Agile is flexible so it can be suitable.

Kanban has no process, so CRISP-DM could be superimposed.

The short nature of sprints in Scrum, might not suit the highly explorative and experimental nature of data science. Scrum emphasises iterative delivery small, concrete features, doesn't align that well to that.

## Data Driven Scrum(DDS)

Combines Scrum with Kanban. DDS has unknown and varying length iterations.

A DDS iteration might include whole process like, data collection, data exploration, data preparation, analysis, evaluation

![[fbf710ddd3fa1b1bae10ee87026ab5ee_MD5.png]]

[https://www.datascience-pm.com/data-driven-scrum/](https://www.datascience-pm.com/data-driven-scrum/)

- Brainstorm explore questions, data, success criteria
- Prioritise: collectively agree on questions to answer
- Create/refine: artifacts to answer the questions
- Observe artefacts and analyse those observations

Key roles

- Product Owner
- Process Expert - like scrum master
- DDS Team members

Artifacts

- Product Owner backlog
- DDS team backlog
- Item breakdown board
- Task board(Kanban-like board)

## Domino

Combines Agile with data science, acknowledging the multiple team roles of a data science project.

Principles

- Expect and embrace iterations, but prevent iterations from meaningfully delaying projects, or distracting from the goal at hand
- Enable compounding collaboration by creating components that are reusable in other projects
- Anticipate auditability needs and preserve all relevant artifacts associated with the development and deployment of a model.

Six stages

1. Ideation
2. Data acquisition and exploration
3. Research and development
4. Validation
5. Delivery
6. Monitoring

Stages are similar to CRISP-DM

Within the stages, board-based agile principals, like teams, collaboration, short iterative deliveries, close stakeholder management, product backlog

## Project Management Body of Knowledge

The Project Management Institute(PMI) product a book called Project Management Book of Knowledge(PMBOK)

It's generic knowledge.

[https://www.projectmanager.com/blog/history-of-pmi](https://www.projectmanager.com/blog/history-of-pmi)

## Critical Path Method(CPM)

Build a project in terms of activities listed as a work breakdown structure. Specify duration of each task and dependencies between tasks.

The analysis shows the longest sequence of tasks to finish the project. That becomes the critical path.

## Critical Chain Path Method(CCPM)

Extends CPM by focusing on resources needed to complete the project.

Three main parts of the critical chain

1. The critical path - the longest sequence of tasks that needs to happen
2. The feeding chain - the tasks that run alongside the critical path and merge with it eventually
3. Resource buffers - Extra resources, set aside to be pulled in if needed

[https://asana.com/resources/critical-chain-project-management](https://asana.com/resources/critical-chain-project-management)

## Extreme Programming(XP)

Focus on

- Pair programming
- Weekly cycles
- Highly energised cross-function teams
- High engagement from the customer
- Continuous integration

[https://www.agilealliance.org/glossary/xp/](https://www.agilealliance.org/glossary/xp/)

## Lean Methodology

Eliminating waste from key processes to continuously improve the value steam

Optimising separate technologies, assets and verticals.

Used by Ford and Toyota.

## Six Sigma

Introduced at Motorola

Identifies quality by what is not working.

It applies management based on statistics.

Six sigma, meas six standard deviations away from a mean of 0. So a failure rate of only 0.00034%.

## PRINCE2

Projects in Controlled Environments, originally created by the UK gov or IT projects.

Seven principles

1. Continued business justification
2. Learn from experience
3. Define role and responsibilities
4. Manage by stages
5. Manage by exception
6. Focos on products
7. Tailor to suit the project

Six variables to control a project

1. Timescales
2. Costs
3. Quality
4. Scope
5. Benefits
6. Risk

[https://www.projectmanager.com/blog/prince2-methodology](https://www.projectmanager.com/blog/prince2-methodology)

## Extreme Project Management(XPM)

For projects that are uncertain, complex and fast changing. Focus on adaptive, iterative process. Customers are given priority.

Teams can self-organise and adapt to project changes.

[https://activecollab.com/blog/project-management/extreme-project-management-xpm](https://activecollab.com/blog/project-management/extreme-project-management-xpm)

## Research

Primary research involves collecting original data

Secondary research uses data that has already been collected

Quantitative data - numeric

Qualitative data - words

Qualitative research

Not as precise or deterministic as quantitative

Through surveys, interviews, etc.

Qualitative Data Analysis(QDA) is used to make sense of the collected data. QDA is the process of interpreting and understanding non-numeric data to identify patterns and themes. Involves coding segments according sentiments expressed. Analysing code frequencies across the data for themes to emerge. Thematic analysis.

Quantitative research, hypothesis testing through statistical significance testing. Show result is significance 95% or 99% confidence level.

Type 1 error(false positives) rejects a null hypothesis that is actually true

Type 2 error(false negative) fails to reject a null hypothesis that is actually false

[https://machinelearningmastery.com/what-is-a-hypothesis-in-machine-learning/](https://machinelearningmastery.com/what-is-a-hypothesis-in-machine-learning/)

A scientific hypothesis is a provisional explanation for observations that is falsifiable.

A statistical hypothesis is an explanation about the relationship between data populations that is interpreted probabilistically.

A machine learning hypothesis is a candidate model that approximates a target function for mapping inputs to outputs.

In supervised machine learning the model itself is the hypothesis. Statistical hypothesis testing can be used to select the best machine learning model from a number of candidate models based on performance.

[https://machinelearningmastery.com/statistical-significance-tests-for-comparing-machine-learning-algorithms/](https://machinelearningmastery.com/statistical-significance-tests-for-comparing-machine-learning-algorithms/)

"Model X has better performance than model Y" or "there is no difference in performance between model X and model Y".

A model that approximates the target function and maps inputs to outputs is called a hypothesis.

Learning involves navigating the space of hypothesis to approximate the target function.

When an acceptable level of loss is reached, you have the hypothesis. The developed models is called a hypothesis because it is an approximation function.

h(hypothesis): a single hypothesis e.g. a candidate model

H(hypothesis set): A space of possible hypotheses for mapping inputs to outputs. Constrained by the choice of framing the problem, the choice of model an choice of model configuration.

For regression problems, the model or hypothesis will be the form of an equations. It is possible test a regression equations for statistical significance but can complex and impractical due to the number of features and size of the dataset.

Depending on the software it might not be possible to extract the model. It's not common to do statistical significance of ML models.

For classification the outputs is a distribution of possible outcomes, this differs for each input making statistical significance testing irrelevant.

For ML models we often use metrics like mean squared error or accuracy.

Scientific method

![[3fcab1db2a315a910cc6bbd5fcdbd98a_MD5.png]]

[https://www.sciencebuddies.org/science-fair-projects/science-fair/steps-of-the-scientific-method](https://www.sciencebuddies.org/science-fair-projects/science-fair/steps-of-the-scientific-method)

Data science method

Ask a question

Do background research

Collect and prepare data

Train and validate a model to form a hypothesis

Check the results

Optimise or test the model

![[dfbfd4c7169bd56c391ae5607a8f47f1_MD5.png]]

[https://www.aha.io/roadmapping/guide/agile/development-methodologies](https://www.aha.io/roadmapping/guide/agile/development-methodologies)

Agile

![[007284ef2f40a665c649cd92c9ea25df_MD5.png]]

We are uncovering better ways of developing software by doing it and helping others do it.

Through this work we have come to value:

1. Individuals and interactions over processes and tools
2. Working software over comprehensive documentation
3. Customer collaboration over contract negotiation
4. Responding to change over following a plan

That is, while there is value in the items on the right, we value the items on the left more.

We follow these principles:

1. Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.
2. Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage.
3. Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.
4. Business people and developers must work together daily throughout the project.
5. Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done.
6. The most efficient and effective method of conveying information to and within the development team is face-to-face conversation.
7. Working software is the primary measure of progress.
8. Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.
9. Continuous attention to technical excellence and good design enhances agility.
10. Simplicity — the art of maximizing the amount of work not done — is essential.
11. The best architectures, requirements, and designs emerge from self-organizing teams.
12. At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.”

![[5496164c91101ae53a5890c2671e131a_MD5.png]]

![[ed71db30242ebd70e4024df7fd62351b_MD5.png]]

|   |   |
|---|---|
|Agile methodologies and frameworks||
|The Aha! Framework|[The Aha! Framework](https://www.aha.io/roadmapping/guide/the-aha-framework/the-aha-framework-for-product-development) was developed by Aha! and released publicly in 2024. It is the engine that has powered our company's success and the development of our [software suite](https://www.aha.io/suite-overview). The Aha! Framework is unique in that it ensures strategic alignment while supporting ongoing sprints with continuous deployment. It is organized around the [phases of product development](https://www.aha.io/roadmapping/guide/stages-of-product-development), with discrete activities within each that support rapid value delivery. The activities begin with biannual strategy-setting and include ongoing sprints.<br><br>Related:<br><br>- [The activities in The Aha! Framework](https://www.aha.io/roadmapping/guide/the-aha-framework/what-are-the-activities-in-the-aha-framework)<br>- [How to adopt The Aha! Framework](https://www.aha.io/roadmapping/guide/how-to-adopt-the-aha-framework)<br>- [Frameworks functionality in Aha! software](https://www.aha.io/support/roadmaps/strategic-roadmaps/knowledge/frameworks)|
|Adaptive Software Development (ASD)|ASD is built on the principles of RAD. ASD follows a continuous cycle of "speculate, collaborate, and learn" to adapt as work progresses. Its key characteristics include being mission-focused, feature-based, iterative, time-boxed, risk-driven, and tolerant of changes throughout the development process.|
|Agnostic agile|Agnostic agile practitioners might balk at being included in a list of agile frameworks, given one of the key principles is not to adhere to the specifics of any one framework. This approach is about leading with agile principles and then choosing any framework that best serves the specific organization's needs.|
|Crystal|Crystal is a collection of agile software development approaches. With all, the focus is on customization. Crystal practices iterative and incremental development, active user involvement, and delivering on commitments. Agile teams are encouraged to define the most effective way of collaborating, based on details like the number of team members and the specific type of project you are working on. Developers have the autonomy to adjust processes and optimize workflows as needed. Agile pioneer Alastair Cockburn [wrote a book](https://www.amazon.com/Crystal-Clear-Human-Powered-Methodology-Small/dp/0201699478) about crystal methods in 2004.|
|Dynamic Systems Development Method (DSDM)|Dynamic systems development methodology (DSDM) combines the principles of time-boxing and collaboration with an emphasis on goals and business impact. It lays out four distinct phases for tackling projects: feasibility and business study, functional model or prototype, design and build iteration, and implementation. DSDM is typically selected by larger organizations and governments with the budget to cover overhead and implementation.|
|Extreme Programming (XP)|[XP](http://www.extremeprogramming.org/rules.html) is all about collaboration and transparency. It espouses five key values: communication, simplicity, feedback, courage, and respect. Characteristics include sitting together, pair programming, test-first programming, continuous integration, collective ownership, and incremental design. The approach is intended for small teams that are co-located and close-knit.|
|Fluid Adaptive Scaling Technology (FAST)|[FAST](https://fluid.scaling.tech/home) puts an emphasis on self-organizing teams (or "tribes") who form, change, dismantle, and reform dynamically over value cycles as short as two days. FAST self-describes as product-centric, with equal weight given to product discovery as product delivery.|
|Feature-Driven Development (FDD)|FDD is a model-driven methodology intended for larger teams working on a project using object-oriented technology. It defines five processes: develop the overall model, build the feature list, plan by feature, design by feature, and build by feature. The goal is to deliver more features that customers want. Work moves quickly — developers typically build each feature in two weeks. FDD can be useful for companies with a more rigid or hierarchical structure where lead developers make decisions that impact the rest of the team.|
|Kanban|[Kanban](https://www.aha.io/roadmapping/guide/agile/what-is-kanban) is a tricky one, even though it is incredibly popular with many types of agile development teams (as well as product and project teams). Tricky because it is not technically a methodology or framework — it is a workflow management system with an emphasis on continuous delivery. The core principles of kanban are to visualize what you do today, limit the amount of work in process, and optimize flow. Teams visualize work on a [kanban board](https://www.aha.io/roadmapping/guide/agile/how-to-set-up-kanban-board) and follow a pull-based approach, grabbing a new task as they have bandwidth. Progress across the board is monitored until work is completed according to the team's [definition of done](https://aha-gatsby-staging.netlify.app/roadmapping/guide/agile/agile-dictionary).<br><br>Related:<br><br>- [How is kanban used by product managers?](https://www.aha.io/roadmapping/guide/product-development-methodologies/kanban-product-management)<br>- [How development teams implement kanban](https://www.aha.io/roadmapping/guide/agile/how-development-teams-implement-kanban)<br>- [Best practices for configuring Aha! Develop to support kanban](https://www.aha.io/support/develop/develop/best-practices/best-practices-configure-aha-develop-for-kanban)|
|Large-Scale Scrum (LeSS)|[LeSS](https://less.works/) defines 10 principles for deploying and maintaining scrum across an entire company. It was created to support organizations with multiple scrum teams. There are two configurations: one for two to eight scrum teams, and one for more than eight scrum teams. LeSS co-creators Craig Larman and Bas Vodde [co-wrote a book](https://www.amazon.com/Large-Scale-Scrum-More-Addison-Wesley-Signature/dp/0321985710) that outlines how teams can adopt the principles.|
|Lean Software Development (LSD)|[LSD](https://www.aha.io/roadmapping/guide/agile/agile-vs-lean) applies lean manufacturing principles and practices to software development. It promotes a minimalist approach — the key principles are to eliminate waste, ensure quality, create knowledge, defer commitment, deliver fast, respect people, and optimize the whole. Lean teams collaborate to deliver a [Minimum Viable Product](https://www.aha.io/roadmapping/guide/plans/what-is-a-minimum-viable-product) (MVP). Once that product is released, the team gathers customer feedback and then applies those insights to new product iterations.|
|Nexus|The [Nexus framework](https://www.scrum.org/resources/online-nexus-guide) was created by Ken Schwaber, one of the co-creators of scrum. It is an agile model that is used in tandem with scrum. Nexus adds an integration team composed of a product owner, [scrum master](https://www.aha.io/roadmapping/guide/agile/what-is-a-scrum-master), and integration team members. The team focuses on facilitating dependencies and other issues across teams.|
|Rapid Application Development (RAD)|RAD emphasizes speed and flexibility. Developers build prototypes, collect user feedback, and iterate often. RAD is ideal for highly skilled teams that need to develop a product quickly (within a few months) and are able to collaborate with customers during the process.|
|Scaled Agile Framework® (SAFe®)|[SAFe](https://www.aha.io/roadmapping/guide/agile/scaled-agile-framework) is a set of principles, guidelines, and prescribed levels for implementing agile and lean principles at scale. The core principles of SAFe include taking an economic view, applying systems thinking, assuming variability and preserving options, building incrementally, basing milestones on objective evaluation, making value flow without interruption, planning and delivering across a portfolio in a synchronized cadence, unlocking the intrinsic motivation of knowledge workers, decentralizing decision making, and organizing around value. <br><br>Related:<br><br>- [What is the role of a SAFe product manager?](https://www.aha.io/roadmapping/guide/product-development-methodologies/what-is-the-role-of-pm-in-safe)<br>- [Best practices for configuring Aha! software to support SAFe](https://www.aha.io/support/roadmaps/strategic-roadmaps/best-practices/best-practices-for-configuring-aha-to-support-safe)<br>- [How to run SAFe PI planning with Aha! Whiteboards](https://www.aha.io/support/whiteboards/whiteboards/how-to/run-safe-pi-planning-whiteboards)|
|Scrum|[Scrum](https://www.aha.io/roadmapping/guide/agile/what-is-scrum) is an iterative and incremental agile software development framework. Scrum teams operate from core pillars of transparency, inspection, and adaptation. There are defined roles, including [scrum master](https://www.aha.io/roadmapping/guide/agile/what-is-a-scrum-master) and product owner. Teams work in time-boxed [sprints](https://www.aha.io/roadmapping/guide/agile/what-is-a-sprint) of two to four weeks and follow scrum ceremonies — such as [sprint planning](https://www.aha.io/roadmapping/guide/agile/what-is-a-sprint-planning-meeting), daily scrum, sprint review, and sprint [retrospectives](https://www.aha.io/roadmapping/guide/agile/what-is-an-agile-retrospective). These ceremonies facilitate the continuous improvement and tight alignment that allow scrum teams to deliver value at a sustainable pace. Scrum is well suited to teams that are nimble, cohesive, and willing to pivot often based on stakeholder feedback.<br><br>Related:<br><br>- [What is the role of a product manager in scrum?](https://www.aha.io/roadmapping/guide/product-development-methodologies/scrum)<br>- [How to implement scrum](https://www.aha.io/roadmapping/guide/agile/how-to-implement-scrum)<br>- [Best practices for configuring Aha! Develop to support scrum](https://www.aha.io/support/develop/develop/best-practices/best-practices-configure-aha-develop-for-scrum)|
|Scrumban|[Scrumban](https://www.aha.io/roadmapping/guide/agile/agile-dictionary) is a hybrid of scrum and kanban. It was initially developed as a way for teams to transition from scrum to kanban or vice versa. But over time, it gained traction as a standalone methodology, not just as a stopgap. The scrum part of scrumban gives teams defined guidelines for roles, planning, and running sprints effectively. The kanban part of scrumban offers a way to balance work against resources with the pull system, plus visualizations of work in progress.|

- Motivated teams: Agile requires intrinsically motivated individuals who are driven by problem-solving, are able to accept and incorporate feedback, and thrive when working independently and as a collective. Many frameworks encourage self-organizing teams, which requires high commitment and performance to be successful. 
- Backlog prioritization: Creating and [maintaining a healthy backlog](https://www.aha.io/roadmapping/guide/release-management/product-backlog-refinement) is critical to agile success. Having an up-to-date, prioritized list of features ensures the team can move quickly when ready to begin work. In many agile frameworks, backlog health is a team performance metric.
- Incremental development: Agile hinges on iteration. Iterative cycles require that developers break down large projects into smaller, more manageable units of work. Each batch of work builds on previous increments and early feedback received, which means your product is constantly being improved. 
- Frequent communication: Agile teams transmit information daily. From standups to real-time conversations, core development teams communicate about capacity, work status, and any issues that need to be addressed. Alignment across the entire [product development team](https://www.aha.io/roadmapping/guide/product-management/what-makes-up-the-product-team) is just as important. Regularly connecting with cross-functional teammates minimizes costly rework. 
- Cross-training: Development slows when there is only one teammate who can perform a particular task. Agile teams display an "all-hands" approach in that teammates should be able to pick up, contribute to, or peer review work in progress as needed. Cross-training increases team adaptability and, ultimately, team velocity.
- Retrospectives: Team members check in with one another at regular intervals (typically after an iteration) to reflect on how to improve processes going forward. [Agile retrospectives](https://www.aha.io/roadmapping/guide/agile/what-is-an-agile-retrospective) facilitate the kind of transparent, open communication that encourages teams to constantly evolve for the better.

CRISP-DM with DDS to track progress. CRISP-DM is an ideal process for ML, but need a flexible agile method to track progress. The tasks can be varying length so the kanban with variable tasks is more ideal

## Reflection

### Kolb's Model of Reflection


![[ee609c1f458e9dd3598a667227c41410_MD5.png]]

# Ethics and bias

## Issues

- Fake news and deepfakes.
- Privacy and transparency. Facebook's Beacon programme breached customer privacy(advertising).
- Black box problem - don't know why AI made the decision it did.
- Trust and accountability.
- Bias.
- Security and hacking.



## Error, bias and uncertainty

### Random error
e.g. misreading weight, or natural phenomena causing fluctuation in measurements

### Systematic error 
Systematic error is a consistent or proportion difference. e.g. miscalibrated scales.



## Accuracy
	- Errors in data can cause errors in outputs
	- Appropriate algorithm, hyper params, poor training
## Bias
	- Data could capture bias or not be representative
	- Historical bias - migth select males for jobs
	- Sample bias - sample must be representative. Must be truly randomised
		- self selection bias. 
	- survival bias
	- Aggregation bias. e.g. if results are calculated at the county level, then those are averaged, that might not be right, since it doesn't account for the number of people or weightings. e.g. if county 1 has average income of £1m and pop of 10k and county 2 has average income of £2m and pop of 100, you can't just averages £1m and £2m it needs to be a weighted average.
	- Confirmation bias. When researchers select data that confirms their beliefs.
	- Measurement bias, faulty measurement equipment

### Mitigating bias

- Awareness and training
- Diverse data sources
- Robust sampling techniques
- Rigorous data cleaning
- Blind analysis, where analyst don't know the hypothesis or expected outcome

Good data governance ensure data is consistent, trustworthy and isn't misused

An organisation should have a data controller and data processor

Data architecture are the models, policies, rules and standard for how data is collected, stored, integrated and used.

Data analysis is the applying statistical and logical techniques to describe, and evaluate data.

Data governance allows for good data architecture, which allows for good data analysis, which confirms the trustworthiness of the data and validates governance and architecture frameworks.


## Fairness tests

- Select representative data of the whole population
- Check results for bias
- Apply fairness tests
- Monitor ML systems continuously
- Fairness through unawareness
- Fairness through awareness
- Counterfactual fairness
- Causal fairness
- Fairness testing
- Data testing, feature bias, label bias, selection bias

## Uncertainty
### Aleatoric uncertainty

Aleatoric uncertainty is inherent uncertainty and is always there. e.g. flipping a coin
Noisy data is aleatoric
### Epistemic uncertainty
Epistemic uncertainty lack of knowledge about the system. 
Incomplete coverage is epistemic
### Ontological uncertainty
Ontological uncertainty - the degree of conceptual understanding of the world

### Structural uncertainty
Structural uncertainty relates to simplification we have to make

### Deep uncertainty
Deep uncertainty derives from the extent to which we can anticipate the nature of the problem space

### Standard error and confidence intervals

Standard error and confidence intervals can quantify uncertainty.

Standard error of mean = sd/(number of observations)^0.5



## Privacy and ownership
Data could be sold legitimately or illegitimately


## Code of Conduct


![[3ed8c17a0206f8864275e47af2e9023b_MD5.png]]

### Data Science Associate Code of Conduct Rules

1. Terminology
2. Competence
3. Abide by client decisions
4. No criminal or fraudulent activity
5. Communication with clients
6. Confidential information
7. Conflicts of interest
8. Duties to prospective clients
9. Data science evidence, quality of data and quality of evidence
10. Misconduct
11. Do not engage in conduct that is prejudicial to method of science
12. Do not misuse data science results to communicate false reality or promote an illusion of understanding


## Frameworks

- Asilomar AI Principles.
- OECD AI Principles.
- Understanding artificial intelligence ethics and safety (UK Government).
- Data Ethics Framework (UK Government).
- Ethical Guidelines for Trustworthy AI (EU).

### Asilomar AI Principles

Research issues

- Research goal - should be a beneficial intelligence
- Research funding - should cover ethics and other issues as well
- Science-Policy Link - constructor exchange between the two
- Research culture - Culture of cooperation, trust and transparency
- Race avoidance: Should work cooperatively to avoid corner-cutting on safety standards

Ethics and values

- Safety - should be safe and secure
- Failure transparency - if AI causes harm, it should be possible to determine why
- Judicial transparency - decisions should be explainable
- Responsibility:
- Value alignment:
- Human values:
- Personal Privacy.
- Liberty and privacy
- Shared benefit
- Shared prosperity
- Human control.
- Non-subversion
- AI Arms Race. In respect to actual weapons.

Longer-term issues

- Capability caution. Avoid assumption on upper limits on future AI capabilities
- Importance. Massive change
- Risks - Could be catastrophic.
- Recursive self-improvement
- Common good.

Shared prosperity, Common good, safety

### OECD

Section 1: Principles for responsible stewardship of trustworthy AI

- Inclusive growth, sustainable development and well being
- Respect for the rule of law, human right  and democratic values, including fairness and privacy.
- Transparency and explainability
- Robustness, security and safety
- Accountability

Section 2: National policies and international co-operation for trustworthy AI:

- Investing in AI research and development
- Fostering an inclusive AI-enabling ecosystem
- Shaping an enabling interoperable governance and policy environment for AI
- Building human capacity and preparing for labour market transformation
- International cooperation for trustworthy AI.

How the government should help and foster AI development

### UK ethics

AI ethics is a set of values, principles and techniques

Projects must be

- Ethically permissible
- Fair and non-discriminatory
- Worthy of public trust
- Justifiable

Governance

- A framework of ethical values
- A set of actionable principles
- A Process-based governance framework

Ethical values framework

- Respect the dignity of individuals
- Connect with each other sincerely, openly and inclusively
- Care for the wellbeing of all
- Protect the priorities of social values, justice and public interest

Actionable FAST principles

- Fairness
- Accountability
- Sustainability
- Transparency


## FAST

- Fairness
- Accountability
- Sustainability
- Transparency

### Data fairness
- Trained on representative, relevant, accurate and generalisable datasets
- Have model architectures that do not include target variables, features, processes or analytical structures, which are unreasonable, morally objectionable, unjustifiable

### Implementation fairness
- Are deployed by users sufficiently trained to implement them responsibly and without bias 

### Outcome fairness

- Do not have discriminatory or inequitable impacts

### Dataset Factsheet
you should initiate the creation of a Dataset Factsheet at the alpha stage of your project. This factsheet should be maintained diligently throughout the design and implementation lifecycle in order to secure optimal data quality, deliberate bias-mitigation aware practices, and optimal auditability. It should include a comprehensive record of data provenance, procurement, pre-processing, lineage, storage, and security as well as qualitative input from team members about determinations made with regard to data representativeness, data sufficiency, source integrity, data timeliness, data relevance, training/testing/validating splits, and unforeseen data issues encountered across the workflow.

### Discriminatory Non-Harm Self-Assessment

Step 1: Identify the fairness and bias mitigation dimensions that apply to the specific stage under consideration (for example, at the data pre-processing stage, dimensions of data fairness, design fairness, and outcome fairness may be at issue).

Step 2: Scrutinise how your particular AI project might pose risks or have unintended vulnerabilities in each of these areas.

Step 3: Take action to correct any existing problems that have been identified, strengthen areas of weakness that have possible discriminatory consequences, and take proactive bias-prevention measures in areas that have been identified to pose potential future risks.

### AI Transparency map

![[d9e7b33d873367007e28f96d7559d9be_MD5.png]]

### Explanatory Strategies

![[4798dbb7aeac3fc4cf5b4f58dfcb43e4_MD5.png]]


### Data Ethics Framework


- Transparency - 0 not public - 5 widely available
- Accountability - 0 not established - 5 public scrutiny build into project cycle
- Fairness - 0 risk of harm or discrimination - 5 project promotes just and equitable outcomes

[https://assets.publishing.service.gov.uk/media/5f74a4958fa8f5188dad0e99/Data_Ethics_Framework_2020.pdf](https://assets.publishing.service.gov.uk/media/5f74a4958fa8f5188dad0e99/Data_Ethics_Framework_2020.pdf)

1. Define and understand public benefits and needs
2. Involve diverse expertise
3. Comply with the law
4. Review the quality and limitations of the data
5. Evaluate and consider wider policy implementation

Rating 0 to 5. Less than 3 requires change and looking at

### Ethical guidelines for trustworthy AI(EU)

[https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai)

- Lawful
- Ethical
- Robus

- Human agency and oversight
- Technical robustness and safety
- Privacy and data governance
- Transparency
- Diversity
- Societal and environmental wellbeing
- accountability

Trustworthy AI(ALTAI)


## Legal

### OECD Guidelines

UK Data Protection Act 2018 is compliant with EU GDPR

Supervisory organisations

European Data Protection Board(EDPR) EU and

Information Commissioner's Office(ICO) UK

Controller:  Natural or legal person, public authority, agency or other body that alone or jointly with others, determines the purposes of means of processing of personal data.

Processor: A natural or legal person, public authority, agency or other body that processes personal data on behalf of the controller.

The controller is responsible for complying with GDPR.

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/controllers-and-processors/controllers-and-processors/what-are-controllers-and-processors/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/controllers-and-processors/controllers-and-processors/what-are-controllers-and-processors/)

Key principles

1. Lawfulness, fairness and transparency
2. Purpose limitation
3. Data minimisation
4. Accuracy
5. Storage limitation
6. Integrity and confidentiality
7. Accountability.

[https://ico.org.uk/](https://ico.org.uk/)

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/)

Legitimate purpose

- Consent
- Contract
- Legal obligation
- Vital interests
- Public task
- Legitimate interests

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/)

Special Category data

- Personal data revealing racial or ethnic origin
- Personal data revealing political opinions
- Personal data revealing religious or philosophical beliefs
- Personal data revealing trade union membership
- Genetic data
- Biometric data
- Data concerning health
- Data concerning a person's sex life
- Data concerning a person's sexual orientation

To process special category data you need lawful basis and a separate condition for processing. The condition must be documented.  Conditions like, explicit consent, employment, social security and social protection law, vital interest, etc.

A Data protection impact assessment(DPIA) is needed for any type of processing which is likely to be high risk.

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/lawful-basis-for-processing/special-category-data/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/lawful-basis-for-processing/special-category-data/)

Legitimate interest

- Identify legitimate interest
- Show that the processing is necessary to achieve it.
- Balance it against the individual's interest, rights and freedoms

Legitimate interest might be marketing, fraud prevention, security, etc.

### Accountability

Appropriate measures and records must be in place.

### Article 22

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/rights-related-to-automated-decision-making-including-profiling/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/rights-related-to-automated-decision-making-including-profiling/)

You can only carry out automated decision making if

- Necessary for the entry into or performance of a contract
- Authorised by domestic law applicable to the controller
- Based on the individuals explicit consent.

UK GDPR doesn't not allow solely automated decision making that have legal or similarly significant effect on individuals

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/rights-related-to-automated-decision-making-including-profiling/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/rights-related-to-automated-decision-making-including-profiling/)

### Transfer of data outside the UK

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/)

Can't transfer outside the UK unless there are appropriate safeguards in place. But it's OK if it's transferred to the same company/entity.

### Adequacy regulations

Can be transferred to somewhere covered by "adequacy regulations". So agreements with

EEA

EU or EEA

Gibraltar

Republic of Korea

Countries covered by European Commissions adequacy decisions.

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/)

Partial adequacy for

Cananda only data subject to Personal Information and Electronic Documents Act

Japan - Protection of Personal information

USA - subject to UK Extension to the EU-US Data Privacy framework

### Appropriate safeguards

If it doesn't meet adequacy regulations you can see if it meets "appropriate safegaurds".

Do a transfer risk assessment, which will consider Article 46 mechanisms.

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-data-transfer-agreement-and-guidance/international-data-transfer-agreement-and-guidance/transfer-risk-assessments/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-data-transfer-agreement-and-guidance/international-data-transfer-agreement-and-guidance/transfer-risk-assessments/)

Article 46

1. A legally binding and enforceable instruments between public authorities or bodies
2. UK binding corporate rules(UK BCR)
3. A contractually binding data protection clauses.
4. An ICO-approved code of conduct
5. Certification under ICO-approved certification scheme
6. Contractual clauses authorised by ICO
7. ICO-authorised administration arrangements between public authorities or bodies

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/)

### Exceptions

Where you are allowed to transfer outside the UK

1. Explicit consent
2. Contract with the person the data is about, need to transfer the data to meet contract
3. Required to enter into a contract that benefits the person the data transferring is about
4. Public interest
5. For a legal claim or defence
6. To protect someone's vital interests. - The person it's about must be physically or legally incapable of giving consent.
7. Public register
8. One-off transfer necessary to meet your compelling legitimate interests.

[https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/#:~:text=Exceptions%202%2C%203%2C%204%2C,of%20achieving%20a%20specific%20purpose](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/international-transfers-a-guide/#:~:text=Exceptions%202%2C%203%2C%204%2C,of%20achieving%20a%20specific%20purpose).

## The Equality Act(UK)

[https://www.legislation.gov.uk/ukpga/2010/15/contents/](https://www.legislation.gov.uk/ukpga/2010/15/contents/)

Protect

1. Age
2. Disability
3. Gender reassignment
4. Marriage and civil partnership
5. Pregnancy and maternity
6. Race
7. Religion or belief
8. Sex
9. Sexual orientation

Bias in lending algorithm

[https://edition.cnn.com/2019/11/10/business/goldman-sachs-apple-card-discrimination/index.html?utm_source=fbCNN&utm_medium=social&utm_content=2019-11-10T22%3A00%3A04&utm_term=link](https://edition.cnn.com/2019/11/10/business/goldman-sachs-apple-card-discrimination/index.html?utm_source=fbCNN&utm_medium=social&utm_content=2019-11-10T22%3A00%3A04&utm_term=link)

[https://www.trustscience.com/resource/blog/archive/the-role-of-protected-attributes-in-ai-fairness](https://www.trustscience.com/resource/blog/archive/the-role-of-protected-attributes-in-ai-fairness)

## The Human Rights Act(UK)

- Article 2: Right to life
- 3: Freedom from torture and inhumane or degrading treatment
- 4: Freedom from slavery and forced labour
- 5: Right to liberty and security
- 6: Right to a fair trial
- 7: No punishment without law
- 8: Respect for your private and family life, home and correspondence
- 9: Freedom of thought, belief and religion
- 10: Freedom of expression
- 11: Freedom of assembly and association
- 12: Right to marry and start a family
- 14: Protection from discrimination in respect of these rights and freedoms

## The Artificial Intelligence Act(EU)

The higher the risk the stricter the rules.

Exemptions for military and research purposes

[https://www.consilium.europa.eu/en/press/press-releases/2024/05/21/artificial-intelligence-ai-act-council-gives-final-green-light-to-the-first-worldwide-rules-on-ai/?utm_source=brevo&utm_campaign=AUTOMATED%20-%20Alert%20-%20Newsletter&utm_medium=email&utm_id=320](https://www.consilium.europa.eu/en/press/press-releases/2024/05/21/artificial-intelligence-ai-act-council-gives-final-green-light-to-the-first-worldwide-rules-on-ai/?utm_source=brevo&utm_campaign=AUTOMATED%20-%20Alert%20-%20Newsletter&utm_medium=email&utm_id=320)

Cognitive behavioural manipulation and social scoring will be banned.

Unacceptable risk: banned

High Risk: Registration in EU database, detailed documentation, risk assessment and mitigation, activity logging, human oversight, robustness obligations

Limited risk: transparency obligations

Minimal risk: free use

# Concerns and issues

- Cybercrime
- Cyberbullying
- Misinformation
- Loss of privacy
- Mental health issues
	- Social media makes mental health issue worse
	- Compare to what they see online
- Society media safety
	- Remove illegal content quickly or prevent it from appearing in the first place
	- Prevent children from accessing harmful or age inappropriate content
	- Enforce age limits
	- Ensure risks and dangers to children are more transparent and publish risk assessments
	- Provide parents and children clear and accessible ways to report problems online.
- Job loss
- Carbon footprint
	- Water
	- CO2
	- e-waste
- Digital divide
	- Affordability
	- Availability
	- Skills

## Accessibility and AI

- Visual assistance from AI
- AI for live transcription
- AI for mobility issues. AI with cameras can help people with visual impairment. They can navigate the real world.

AI could identify people with disabilities and treat them differently which could be a risk.

# Team working

## The big five

Teamwork can be broken down into five components

- Team leadership. Directs and coordinates
- Performance monitoring.
- Backup behaviour. Anticipate the other team member need, shift workloads where required
- Adaptability. Adjust strategy based on information gathered from backup behaviour and reallocate team resources.
- Team orientation. Prioritise team goals over individual members' goals.


![[2e7d7e19d0d328d532779f0ff86c2849_MD5.png]]


## Data science project teams

Table 1: Data science roles and expertise – adapted from Saltz (2024) 

|   |   |   |   |
|---|---|---|---|
||Level of expertise|||
|Role|Domain expertise|Technical knowledge|Quantitative skills|
|Data scientist|Medium|Medium|High|
|Data engineer|Low|High|Medium|
|Data science architect|Low|High|Low|
|Data science developer|Low|High|Medium|
|Product owner|Medium|Low|Low|
|Data/business analyst|Medium|Medium|Medium|
|Process master|Low|Low|Low|
|Subject matter expert|High|Low|Low|

## Building a data science capability

- The data science team. Concentrates on machine learning algorithms and discovering models
- The data engineering team. This team creates data pipelines and manages data storage and organisation at scale.
- The operation team. Looks after the infrastructure and makes sure everything keeps running.


# Projects

## AI and Digital Innovation

# Models

### RNN


 A![[193f34f86a1f431e3166bfd9411524f7_MD5.png]]

Vanishing gradient problem, RNN forgets stuff over time

### LSTM

LSTM uses gating mechanism to hand over more information


## Transformer



![[05350c2747594a20f8587786ac9b94dc_MD5.png]]


Attention finds out how each word is related to all other words in a sequence including itself.
To increase performance eight attention mechanisms are run in parallel. Multi-head attention
So attention replaced recurrence.

Positional encoding is done using sin and cosine, not just added, but adding in a specific way


Split each d=512 of each word into 8 dk=64 dimensions.

It uses Q, K and V to project it into 8 heads, so it's not just split, but linearly projected into a lower-dimensional space, unique to each head.

- Query (Q): Represents what we’re looking for — it’s the "question" the model is asking.
- Key (K): Represents what each word offers — like a label or identifier.
- Value (V): Contains the actual content or information of the word.


![[b71d5071f5e9d75763f12d809d7465b1_MD5.png]]



There are many layer normalization methods.

![[400630b4742589c31583f40c0eb710fd_MD5.png]]


The input and output of the FFN layers is d=512 but the inner layer is larger with dff=2048

FFN can be viewed as performing two kernel size 1 convolutions

![[d85b07b8667c84cb2980658a637c0e95_MD5.png]]

### The decoder stack

![[f140f1678778ffa7d889dcdf296679b2_MD5.png]]

So linear is like a score, softmax makes it a probability. Might be at the level of layers.

### Bidirectional Encoder Representation from Transformers(BERT). BERT only uses the encoders and does not use the decoder stack.

Doesn't mask future tokens but masks a random token, and sometimes nothing, and sometimes with the wrong token.

Can do sentence embeddings, and learns positional encodings.

BERT uses both unsupervised and supervised learning. 

### GPT

GPT is more self supervised, since it predicts words. 

1. Fine-tuning
2. Few-Shot(FS) - Model is trained, then shown demonstrations of the task to complete. This is called conditioning and replaces weight updating.
3. One-shot(1S) - Only one demonstration is presented
4. Zero-shot(ZS) - No demonstration is given to the model of the task to be performed.

### Vision Transformers 

1. Split the image into patches
2. Linear projection of the flattened images
3. Hybrid embedding transformer encoder

### Contrastive Language-Image Pre-Training(CLiP)

It trains on image pairs and captions.

### Prompting

Act like an expert.
Chain of though
Describe otuputs
Few/One/No shot

Issues

Direct injection - ignore previous commands
Obfuscated input 
Encoded payload
Data poisoning
Prompt smuggling
System prompt leakage
Jailbreaking
Nested prompts
## Evaluating models

### Accuracy
Accuracy = Correct/Total

### Precision
Precision = TP / (TP + FP)

### Recall
Recall = TP / (TP + FN)

### F1
F1 = 2 xPrecision x Recall/(Precision + Recall)

### Matthews Correlation Coefficient(MCC)

![[9cc1a3346124abc04967ead584ead671_MD5.png]]

Works even if the sizes of the classes are different

### GLUE(General Language Understanding Evolution) SuperGlue

Some tasks to test natural language understanding(NLU)

1. CoPA - multiple choice
2. BoolQ - yes no
3. Commitment bank - Examine a hypothesis and premise, then label the hypothesis as neutral, an entailment(logically follows) or contradiction.
4. Multi-Sentence Reading Comprehension (Multi-RC) - multiple choice
5. Recognising Textual Entailment (RTE) 
6. Words in Context (WiC) - Must work out if the same word has the same meaning in different sentences
7. The Winograd Schema Challenge (WSC) Is the pronoun right, in a sentence with a occupation, participant and pronoun.  "I poured water from the bottle into the cup until it was full.", Does it refer to the bottle or the cup


### Bilingual Evaluation Understudy Score(BLEU) compares the candidate sentence(C) to a reference sentence® or several reference sentences.

For machine translation
C(N) number of correct tokens

![[e52ac0bc56eac0c54e64e3888530faf7_MD5.png]]


# Coding languages

## AutoML
AutoML translation service, will train a custom model for a specific domain

## Tensorflow
Google Brain developed Tensor2Tensor T2T, an TensorFlow extension that contains a library of deep learning models, that contain many transformer examples.

# Trax
Google brain then produced Trax, an end-to-end deep learning library. Uses TensorFlow and JAX under the hood.

Trax has lots of methods that can be applied to get it running properly