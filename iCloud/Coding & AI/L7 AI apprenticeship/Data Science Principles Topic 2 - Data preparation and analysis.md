
This topic covers the following five learning objectives. After completing the reading and activities you will be able to do the following:

2.1 Describe the types of data preparation that may be needed before data analysis can begin

2.2 Explain the principles for creating good visualisations

2.3 Discuss various graphics and techniques used in data visualisation

2.4 Demonstrate use of Power BI to carry out data transformations

2.5 Use Power BI for data preparation

You will also explore the following subtopics:

- Preparing your data
- Analysing your data
- Visualising your data
- More Power BI
- Loading data into Power BI

From <[https://app.qa.com/resource/topic-2-data-preparation-and-analysis-1698/?context_id=14505&context_resource=lp](https://app.qa.com/resource/topic-2-data-preparation-and-analysis-1698/?context_id=14505&context_resource=lp)>

[Boehnert, J. (2016) Data Visualisation Does Political Things . DRS2016: Design Research Society: Future-Focused Thinking](https://westminsterresearch.westminster.ac.uk/download/ca109c03787d3730c041791d71d6ca5db0de14e7c22057b73d56b1faf860540b/6726771/Data_Visualisation_Does_Political_Things_-_DRS_2016_BOEHNERT_FINAL-April.pdf). University of Brighton 27 - 30 Jun 2016 Design Research Society. Article links to an external site.

The paper argues that the use of data visualisations can be politically motivated.

[Lakin, S. (2011) How to use statistics](https://www.vlebooks.com/Product/Index/304059) (opens in a new tab) - Section 1 (Introductory Statistics), Chapters 1-2 (Introduction to Statistics and Data, Presentation of Data) 

From <[https://app.qa.com/resource/topic-2-data-preparation-and-analysis-1698/?context_id=14505&context_resource=lp](https://app.qa.com/resource/topic-2-data-preparation-and-analysis-1698/?context_id=14505&context_resource=lp)>

## Data Visualisation Does Political Things, Boehnert, J.

What data was collected, what does the data illustrate, how to illustrate it.

Data visualisations don't show everything, but often they are treated as a neutral point of view.

It's a powerful and flawed tool of oppression.

Purely quantitative approaches often fail to capture power relations, ideologies, attitudes, motivations and behaviours that cannot be reduced to a number.

Datawash uses data visualisation to conceal or obscures knowledge

Darkdata would be the data that isn't collected like police killings of black people.

Data - pure facts

Information - structured data

Knowledge - ability to use information

Wisdom - capacity to choose objective consistent with values

Climate discourse: climate science, climate justice, climate contrarian, neoliberalism and ecological modernisation.

[Lakin, S. (2011) How to use statistics](https://www.vlebooks.com/Product/Index/304059) 

Branches of stats, data collection, descriptive statistics and inferential statistics,

Aim of stats is to present the data in an understandable way

Inferential statistics about making a conclusions from the data. e.g. is the speed limit to high resulting in accidents.

## Notes

Extract, Transform, load (ETL)  - For getting data into a data warehouse

Data wrangling used to transform data often for data science.

Extraction should ensure data integrity

Transform - data cleansing, normalisation and standardisation, discretisation(transform continuous data into categorical data), feature engineering(create new data points from existing data)

Loading, can be done in batches or real time.

As part of the CRISP-DM model, ETL is mainly part of data preparation.

Tools like snowflake and AWS glue are used for ETL.

Data transformation

Different sources, might have different formats

Incomplete data, how to fill in gaps or remove records

Duplication of data

Process

Data cleaning

Normalisation and standardisation

Data from multiple sources might be combined

Feature engineering, where new attributes are made from existing

Power BI

Filter & sort

Merge and append

Pivot and unpivot

Custom columns

Discretisation

This can help handle outliers and reduce the sensitivity of the outcome to slight variations. Can enhance the robustness of stats or ML.

- Reduce complexity
- Make models easier to interpret
- Certain algorithms can perform better
- Control outliers

There are various binning methods

- Equal width binning
- Equal frequency binning
- Custom binning.

Missing data

- Missing completely at random(MCAR) e.g. survey lost in mail
- Missing at random(MAR) - Missing relating to the observed data but not unobserved data. e.g. students at night might be less likely to complete a questionnaire.
- Missing not at random(MNAR) - Missingness related to the variable itself. e.g. Online shopping survey, customers who spend lots are less likely to answer, so the missingness relates to the variable(spending amount) - that is if spending is not measured.


Listwise deletion, removes all data for a case that has one or more missing values, useful for MCAR

Pairwise deletion, analyses cases where the variables of interest are present. Useful for MCAR but may have issues otherwise.

Imputation, fill missing values with estimates.

Understand the context, test different methods, document choices.

Imputation

Mean/media/mode imputation, useful for MCAR

Constant value imputation, useful when it's important to distinguish missing data and observed zeroes.

K-nearest neighbours(KNN), takes an average of nearest neighbours

Regression imputation, use regression models to predict the missing values

Multiple imputation, uses multiple models, and then combines outputs

Multivariate(Multiple) Imputation by Chained Equations(MICE), Multiple iterations over each missing entry. Uses regression models to estimate the missing values, then updates the estimates as more data becomes available. Useful when it's not MCAR, as it allows for uncertainty about imputations.

Outliers

Three standard deviations from the mean

Could be errors or might provide valuable insight.

Univariate outlier, e.g. age of someone is 150

Multivariate outliers, in respect to the combination of variables it's an outlier.

Can view them using

Box plots, scatter plots, histograms, z-score plot(above or below 3/-3)

Other methods

Standard deviation +-3

Interquartile range(IQR) method. Below Q1 - 1.5/QR or above Q3 + 1.5/QR

Z-score method, highest or lowest scores are outliers

Treatment

- Remove from data set
- Transformations like using log can limit their impact
- Set a threshold - winsorising
- Robus stats method that are less sensitive to outliers

Normalisation

Feature scaling improves the performance

- Enhancing model convergence, e.g. gradient descent converge faster when features are scaled
- Improving accuracy. K-nearest neighbours(KNN) and support vector machines(SVM) perform better when features have similar scales.
- Avoiding dominance, prevents features with large ranges from dominating those with smaller ranges

Normalisation

(X-Xmin)/(Xmax - Xmin)

When to use normalisation

- When the distribution is not gaussian/normal
- To preserve relationships between data points

Advantages

- Maintaines relationship
- Scales data to a fixed range

Disadvantages

- Sensitive to outliers.

Standardisation

(x - u)/o

![](data:image/png;base64,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)

U - mean

O - standard deviation

When to use

When the data is approximately normally distributed

When the algorithms assumes normally distributed features, e.g. linear regression, logistic regression, neural networks

Advantages

- Reduces the effect of outliers compared to normalisation
- Centres data around zero, which can be beneficial for some algorithms

Disadvantages

- Soes not bound the transformed features.

Aggregation

e.g. sum, average, count, min, max, median.

Cleaning

Remove duplicates

Correct data entry errors, typos incorrect formats

Standardise formats, e.g. dates

Apply domain knowledge

Contextual validation, is everything in the right range, e.g. age

Derived indicators e.g. high risk

Segmentation and classification e.g. products by type

Anomaly detection.

Framing data question

Descriptive - what?

Diagnostic - how, why?

Predictive - forecasts

Prescriptive - recommends based on forecast

What - what are the averages sales, Bar charts, line graphs, pie charts

How - how as customer satisfaction changed. Line charts and area charts

Why - why did sales increase in Q1. Heatmaps, scatter plots, annotated charts

Where - Geographical maps and heatmaps

Who - who are out top customers by revenue. Pareto charts and pie charts

When - time series charts and Gantt charts

You can download a [chart comparison PDF resource](https://app.qa.com/download/dam/e77e520a-e860-4580-b19a-6ae289fa44d2) which provides a comparison of different chart types

From <[https://app.qa.com/course/analysing-and-visualising-your-data-ai-1698/choosing-chart/?context_id=14505&context_resource=lp](https://app.qa.com/course/analysing-and-visualising-your-data-ai-1698/choosing-chart/?context_id=14505&context_resource=lp)>

[DAPAID72_Topic 2_Chart comparison resource_v0.2 (Final)](file:///C:/Users/unpar/OneDrive/Documents/Learning/L7%20AI/DSP/DAPAID72_Topic%202_Chart%20comparison%20resource_v0.2%20\(Final\).docx)

Comparison over items or time. Bar chart or line chart

Relationship charts. Show the relationship between data. Scatter chart, bubble chart

Distribution charts. So distribution of a dataset. Histogram. Scatter chart

Composition charts. Show composition of data. Either composition over time or composition is static. Stacked column chart or stacked area chart

Visualisation must be trustworthy, accessible and elegant.

Check accuracy

Consider the audience

Maintain consistent style

Use space appropriately

Keep things simple

Check that the main message comes through

Explanatory visuals inform by providing an annotation to explain the graphics

Exhibitory visuals leave it to the user to work out insights.

Exploratory visuals allows the users to explore, including interactive elements

Project

Formulating a brief

Working with the data

Establishing editorial thinking

Developing a design solution

Dashboards

Displays various visual data in one place.

Include multiple elements

Controls for filtering and drilling down

Designed with an audience journey in mind

Show real time or near real time data

Aggregate data from different systems

Enable goal tracking(KPI)

Customisable and shareable

Interactivity

Filtering enables users to specify which data they wish to include or exclude from a chart

Highlighting,

Participating, lets users add data to customise the chart, allows users to change or add values to see a different display

Annotating, Headings, intros, user guides, reader guides, legends, chart apparatus and references, chart labelling and captions, footnotes and methods

Animating, could show data over time

Navigating, Could let users explore in greater detail. e.g. select part of one graph and another one shows more detail.

If you can't communicate the message in five seconds the design is too complex.

Power BI

Data Analytis Expressions(DAX)

Aggregations - sum, average, min, max, count

Measure is a custom calculation not part of a table

Report is where the visuals are

Column charts are the standard for comparing series to each other

Visual refers to charts and graphs

Legend - color

Axis - shape

Values - calculatable data

Publish to power BI service

Get customs stuff from App source

New query using New Source

Raw Data -> Power Pivot(DAX Engine/Brain) -> Visuals(dashboards, pivots, Power view, power Map) -> Power BI

Raw Data -> Power Query(data transformation) ^

Data profiling, understand structure of data, identify errors, outliers, improve performance, etc.

Cardinality - low distinct and unique, how cardinality is lots of distinct and unique items

Probably don't want high cardinality so think about if we can remove it.

Common errors, invalid values, null, conversion errors

Column charts show the shape of the data

## Reflect

2.1 Describe the types of data preparation that may be needed before data analysis can begin

ETL, extract translate load

Cleaning

Incomplete data - fill in gaps or remove

Deduplication

Formatting

Structuring

Normalisation and standardisation

Combine data

Feature engineering

For accounts need to extract data, clean and standardise data,

2.2 Explain the principles for creating good visualisations

Visualisation must be trustworthy, accessible and elegant.

Check accuracy

Consider the audience

Maintain consistent style

Use space appropriately

Keep things simple

Check that the main message comes through

Dashboards at work can be used to inform users

2.3 Discuss various graphics and techniques used in data visualisation

Filtering enables users to specify which data they wish to include or exclude from a chart

Highlighting,

Participating, lets users add data to customise the chart, allows users to change or add values to see a different display

Annotating, Headings, intros, user guides, reader guides, legends, chart apparatus and references, chart labelling and captions, footnotes and methods

Animating, could show data over time

Navigating, Could let users explore in greater detail. e.g. select part of one graph and another one shows more detail.

Scroll to adjust timframe data is shown by

2.4 Demonstrate use of Power BI to carry out data transformations

2.5 Use Power BI for data preparation

From <[https://app.qa.com/course/reflect-and-explore-ai-1698/reflect-26062024163113/?context_id=14505&context_resource=lp](https://app.qa.com/course/reflect-and-explore-ai-1698/reflect-26062024163113/?context_id=14505&context_resource=lp)>