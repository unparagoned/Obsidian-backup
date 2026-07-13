Praful Pasarkar

pasarkar@gmail.com

Abstract

This comprehensive document serves as an extensive guide on statistical methods, data mining, machine learning techniques, model evaluation, AI adoption, trends, and associated risks, with a focus on practical applications and interview preparation.

Level 7 AI DS AM2 exam preparation

AM2 Exam Preparation

# Contents

[Statistical Methods [2](#statistical-methods)](#statistical-methods)

[Data Mining [8](#data-mining)](#data-mining)

[Supervised Machine Learning [8](#supervised-machine-learning)](#supervised-machine-learning)

[Neural networks ( architecture, gradient, maths in the nodes, gradient descent, weights) [14](#neural-networks-architecture-gradient-maths-in-the-nodes-gradient-descent-weights)](#neural-networks-architecture-gradient-maths-in-the-nodes-gradient-descent-weights)

[Clustering [23](#clustering)](#clustering)

[Types of Machine Learning [34](#types-of-machine-learning)](#types-of-machine-learning)

[The Machine Learning Pipeline [38](#the-machine-learning-pipeline)](#the-machine-learning-pipeline)

[Model Drift [44](#model-drift)](#model-drift)

[Clean Drift Monitoring Diagram [47](#clean-drift-monitoring-diagram)](#clean-drift-monitoring-diagram)

[How are PSI and Chi‑Square Test Measured? [49](#how-are-psi-and-chisquare-test-measured)](#how-are-psi-and-chisquare-test-measured)

[KPIs for Algorithm Accuracy [52](#kpis-for-algorithm-accuracy)](#kpis-for-algorithm-accuracy)

[Poor Data quality [59](#poor-data-quality)](#poor-data-quality)

[select and apply the most effective/appropriate AI and data science techniques to solve complex business problems [62](#select-and-apply-the-most-effectiveappropriate-ai-and-data-science-techniques-to-solve-complex-business-problems)](#select-and-apply-the-most-effectiveappropriate-ai-and-data-science-techniques-to-solve-complex-business-problems)

[How do you disseminate AI and Data Science practices? [67](#how-do-you-disseminate-ai-and-data-science-practices)](#how-do-you-disseminate-ai-and-data-science-practices)

[How do you identify trends in the current AI landscape? [71](#how-do-you-identify-trends-in-the-current-ai-landscape)](#how-do-you-identify-trends-in-the-current-ai-landscape)

[Common algorithms to know [74](#common-algorithms-to-know)](#common-algorithms-to-know)

[Hyperparameter tuning [79](#hyperparameter-tuning)](#hyperparameter-tuning)

[Definition of SVM (Support Vector Machine) [81](#definition-of-svm-support-vector-machine)](#definition-of-svm-support-vector-machine)

[✅ Activation Functions in Neural Networks [83](#activation-functions-in-neural-networks)](#activation-functions-in-neural-networks)

[What is Softmax? [86](#what-is-softmax)](#what-is-softmax)

[Will AI remove jobs? [88](#will-ai-remove-jobs)](#will-ai-remove-jobs)

[Impact of AI on Industry and Society [91](#impact-of-ai-on-industry-and-society)](#impact-of-ai-on-industry-and-society)

[Why Do We Use Unsupervised Learning? [95](#why-do-we-use-unsupervised-learning)](#why-do-we-use-unsupervised-learning)

# 

# Statistical Methods

Statistical methods are techniques used to **collect, summarize, analyze, and interpret data** to support decision‑making. They are broadly divided into **Descriptive Statistics** and **Inferential Statistics**.

------------------------------------------------------------------------

**1. Descriptive Statistics**

**Purpose:** To **summarize and describe** the main features of a dataset.

- It deals with **organizing, simplifying, and presenting data**.

- It does **not draw conclusions beyond the data itself**.

- Helps understand patterns, trends, and variability.

**Key techniques:**

- **Measures of central tendency:** Mean, Median, Mode

- **Measures of dispersion:** Range, Variance, Standard Deviation

- **Data presentation:** Tables, histograms, bar charts, box plots

**Example:**

Calculating the average test score of a class or showing monthly sales using a bar chart.

------------------------------------------------------------------------

**2. Inferential Statistics**

**Purpose:** To **draw conclusions or make predictions about a population** based on a sample.

- Uses probability theory to make **generalizations**.

- Helps test assumptions and support decision‑making.

- Results are expressed with a **level of confidence**.

**Key techniques:**

- **Hypothesis testing:** t-test, Z-test, Chi-square test, ANOVA

- **Estimation:** Confidence intervals

- **Predictive methods:** Regression analysis, correlation

**Example:**

Using a sample of customers to estimate overall customer satisfaction or testing whether a new process improves performance.

------------------------------------------------------------------------

**Key Difference (Interview-friendly summary)**

- **Descriptive statistics** explain *what the data shows*.

- **Inferential statistics** explain *what the data means for a larger population*.

------------------------------------------------------------------------

**One‑line closing (optional):**

“Descriptive statistics summarize data, while inferential statistics help make data‑driven decisions and predictions.”

------------------------------------------------------------------------

**Real‑World Example of Inferential Statistics**

**Example: Customer Satisfaction Survey**

A company wants to know if a **new mobile app feature improves customer satisfaction**.

- They **survey 200 customers** selected randomly out of **50,000 total users**.

- The sample shows an **average satisfaction score increase of 15%** after the feature launch.

- Using **inferential statistics (e.g., hypothesis testing and confidence intervals)**, the company determines that:

  - The improvement is **statistically significant**

  - With **95% confidence**, the new feature has increased satisfaction across the **entire customer base**, not just the sample

**Why this is inferential statistics:**\
Because conclusions about the **whole population** are made based on a **sample**, using probability and statistical testing.

------------------------------------------------------------------------

**Interview one‑liner:**

“Inferential statistics uses a sample to draw conclusions about a larger population, such as determining whether a new product feature genuinely improves customer satisfaction.”

------------------------------------------------------------------------

**Real‑World Example of Inferential Statistics in IT Operations**

**Example: Reducing IT Incident Resolution Time**

An IT operations team wants to check whether a **new incident management process** has reduced resolution time.

- The organisation handles **10,000+ incidents per month**.

- The team analyses a **random sample of 300 incidents** before and after the process change.

- The sample shows the **average resolution time dropped from 6 hours to 4.8 hours**.

- Using **inferential statistics** (e.g., hypothesis testing and confidence intervals), the team concludes:

  - The reduction is **statistically significant**

  - With **95% confidence**, the new process has improved resolution times **across all incidents**, not just the sample

**Why this is inferential statistics:**\
Because the IT team uses **sample data** to make a **data‑driven conclusion about overall IT operations performance**.

------------------------------------------------------------------------

**Interview one‑liner:**

“In IT operations, inferential statistics helps determine whether process improvements—such as reduced incident resolution time—are genuinely effective across all systems, based on sampled data.”

------------------------------------------------------------------------

**1. t‑test**

**Purpose:** To compare **means** when the **sample size is small** and population standard deviation is unknown.

**When to use:**

- Comparing averages between **one or two groups**

- Data is **numerical** and approximately **normally distributed**

**Common types:**

- **One‑sample t‑test:** Sample mean vs a known value

- **Independent t‑test:** Mean of two separate groups

- **Paired t‑test:** Same group before vs after a change

**Example:**

Comparing average incident resolution time **before and after** a new IT process.

------------------------------------------------------------------------

**2. Z‑test**

**Purpose:** To compare **means** when the **sample size is large (n ≥ 30)** and population standard deviation is known.

**When to use:**

- Large datasets

- Data follows a normal distribution

- Population variance is known

**Example:**

Checking whether the average API response time from a sample of 1,000 requests differs from the SLA target.

**Example: SharePoint and Onedrive shared with externally using 2 proportion Z-test hypothesis**

*Null Hypothesis*: Test proportions are same for external sharing in September

*Alternative Hypothesis*: Test proportions are different for external sharing in September

I am using 2 Proportion Z-test hypothesis test for this comparison. Since I want to make sure that the test results are valid and repeatable. Also, the dataset has approximately normal distribution (bell curve). 2 Proportion Z-test hypotheses is suitable for this dataset since

- Sample size is more than 30

- Data points are independent

- Bell Curve (normal distribution)

- Data is randomly generated and selection randomly from the population

- Sample size, as it is created by me, can be equal

With this information, I decided to use 2 Proportion Z-test since this is the best hypothesis test available for the data set and what I am looking for.

Data sets for the month of September SharePoint: 63 external and 717 internal sharing

Data sets for the month of September OneDrive: 44 external and 2161 internal sharing

*Find Proportions:*

P1=63/(63+717)=0.080=8%

P2=44/(44+2161)=0.0199=2%

*Find overall Sample proportions:*

P=(63+44)/(63+44+717+2161)= 0.0358=3.6%

*Test Statics formula:*

The test statics formula is shown in [Figure 3: Test Statics formula](#_Ref186688410). This formula is provided in the 2 Proportion Z-tests. I am using this formula as it is to proceed.

<figure>
<img src="./media/image2.png" style="width:2.65625in;height:1.14583in" alt="two-proprtion-z-test" />
<figcaption><p><span id="_Ref186688410" class="anchor"></span>Figure 3: Test Statics formula</p></figcaption>
</figure>

Z= (0.08-0.0199)/sqroot(0.0358(1-0.0358)(1/780-1/2205))

Z=0.000321

*2 Proportion Z-tests:*

Confidence level table is shown below

<img src="./media/image3.png" style="width:3.86458in;height:0.84375in" alt="z alpha" />

Figure 4: Confidence level chart

Z-score is associated with alpha/2, so the 5% alpha level is 1.96

Comparing the results of Z with Z-score for 5% alpha

0.000321 \< 1.96

**Accept Null Hypothesis.**

<figure>
<img src="./media/image4.png" style="width:6.26806in;height:3.20903in" alt="A drawing of a mountain Description automatically generated" />
<figcaption><p><span id="_Ref186689749" class="anchor"></span>Figure 5: 2 Proportion Z-test bell curve</p></figcaption>
</figure>

The 2 Proportion Z-test shows that Null Hypothesis is correct. Both SharePoint and OneDrive external sharing is comparable for the month of September. Z from calculation is 0.00032 and the Z score from table is 1.96 which is greater than the Z from calculation. [Figure 5: 2 Proportion Z-test bell curve](#_Ref186689749) shows the position of the comparison point on the bell curve.

**Interview tip:**

Z‑test is similar to t‑test but used for **large samples**.

------------------------------------------------------------------------

**3. Chi‑square (χ²) Test**

**Purpose:** To test the **relationship between categorical variables**.

**When to use:**

- Data is **categorical**, not numerical

- Want to check **association or independence**

**Common uses:**

- Independence test

- Goodness‑of‑fit test

**Example:**

Checking whether **incident priority (High/Low)** is related to **resolution success rate (Resolved/Unresolved)**.

------------------------------------------------------------------------

**4. ANOVA (Analysis of Variance)**

**Purpose:** To compare **means of three or more groups**.

**When to use:**

- One numerical outcome

- One categorical factor with **3+ groups**

**Types:**

- **One‑way ANOVA:** One factor

- **Two‑way ANOVA:** Two factors

**Example:**

Comparing mean system downtime across **three different data centres**.

**Why not multiple t‑tests?**

ANOVA avoids increased **error risk** from repeated comparisons.

------------------------------------------------------------------------

**Quick Interview Summary Table (verbal)**

- **t‑test:** Compare means (small samples)

- **Z‑test:** Compare means (large samples)

- **Chi‑square:** Relationship between categories

- **ANOVA:** Compare means across multiple groups

------------------------------------------------------------------------

**One‑line interview closer:**

“t‑test and Z‑test compare averages, Chi‑square tests relationships between categories, and ANOVA compares means across multiple groups.”

------------------------------------------------------------------------

# Data Mining

------------------------------------------------------------------------

**Purpose:**\
To **discover hidden patterns, trends, and relationships** in large datasets to support decision‑making.

**Techniques:**

- **Clustering:** Groups similar data points together

- **Association Rule Mining:** Finds relationships between variables (e.g., items frequently used together)

- **Anomaly Detection:** Identifies unusual or unexpected data patterns

**Applications:**

- **IT operations:** Detecting abnormal system behaviour or security threats

- **Business intelligence:** Identifying customer behaviour patterns and trends

- **Retail:** Market basket analysis and cross‑selling recommendations

- **Finance:** Fraud detection and risk analysis

- **Healthcare:** Identifying disease patterns and treatment outcomes

------------------------------------------------------------------------

**One‑line interview summary:**

“Data mining is used to analyse large datasets and uncover patterns that help organisations improve performance, reduce risk, and make data‑driven decisions.”

------------------------------------------------------------------------

# Supervised Machine Learning

**Purpose:**\
To **train models on labelled data** so they can make accurate **predictions or classifications** on new, unseen data.

**Techniques:**

- **Linear Regression:** Predicts continuous values

- **Logistic Regression:** Classifies binary outcomes

- **Decision Trees:** Rule‑based decision making

- **Random Forests:** Ensemble of decision trees for higher accuracy

- **Support Vector Machines (SVM):** Separates classes using optimal boundaries

**Applications:**

- **IT operations:** Predicting incident volumes, classifying ticket priority

- **Business:** Customer churn prediction and sales forecasting

- **Finance:** Credit scoring and fraud detection

- **Healthcare:** Disease prediction and diagnosis support

- **Security:** Spam filtering and intrusion detection

------------------------------------------------------------------------

**One‑line interview summary:**

“Supervised machine learning uses labelled data to train models that predict outcomes or classify data accurately in real‑world business and IT scenarios.”

------------------------------------------------------------------------

**1. Linear Regression – Mathematical Foundation**

**Objective**

Model the relationship between input features and a **continuous output** by fitting a straight line (or hyperplane).

**Model equation**

For one feature:

$$
y = \beta_{0} + \beta_{1}x + \varepsilon
$$

For multiple features:

$$
y = \beta_{0} + \beta_{1}x_{1} + \beta_{2}x_{2} + \cdots + \beta_{p}x_{p} + \varepsilon
$$

- $\beta$: model parameters (weights)

- $\varepsilon$: error term

**Cost function (Least Squares)**

Linear regression minimizes the **sum of squared errors**:

$$
J(\beta) = \sum_{i = 1}^{n}(y_{i} - {\widehat{y}}_{i})^{2}
$$

This ensures:

- Errors are penalised heavily when large

- A **convex optimisation problem** (single global minimum)

**Parameter estimation (Normal Equation)**

$$
\widehat{\beta} = (X^{T}X)^{- 1}X^{T}y
$$

Or solved using **gradient descent** for large datasets.

**Key mathematical assumptions**

- Linearity

- Independence of errors

- Constant variance (homoscedasticity)

- Normally distributed errors (for inference)

<img src="./media/image5.png" style="width:3.64583in;height:2.73438in" />

**Intuition (interview‑friendly)**

Linear regression fits a line by minimising squared distances between predicted and actual values.

------------------------------------------------------------------------

**2. Decision Trees – Mathematical Foundation**

**Objective**

Split data into **pure subsets** using a sequence of rules to predict an outcome.

**Core concept: Recursive partitioning**

At each node, choose the feature and split that **maximises information gain**.

------------------------------------------------------------------------

**Impurity measures**

**(a) Gini Impurity (most common) (Continuous)**

$$
G = 1 - \sum_{k = 1}^{K}p_{k}^{2}
$$

- $p_{k}$: proportion of class $k$

- Lower Gini = purer node

**(b) Entropy (Categorical)**

$$
H = - \sum_{k = 1}^{K}p_{k}{\log}_{2}p_{k}
$$

**Information Gain**

$$
IG = H(parent) - \sum_{i = 1}^{n}\frac{N_{i}}{N}H(child_{i})
$$

The split with **highest information gain** is selected.

<img src="./media/image6.png" style="width:4.34028in;height:2.2in" />

------------------------------------------------------------------------

**Regression trees**

Instead of Gini/Entropy, minimise **Mean Squared Error (MSE)**:

$$
MSE = \frac{1}{n}\sum_{i}^{}(y_{i} - \overset{ˉ}{y})^{2}
$$

------------------------------------------------------------------------

**Key mathematical properties**

- Non‑linear

- No distribution assumptions

- Greedy optimisation (local, not global optimum)

**Limitation (math‑driven)**

- High variance

- Small data changes ⇒ different tree

**Intuition**

A decision tree repeatedly splits data to minimise uncertainty in predictions.

------------------------------------------------------------------------

**3. Random Forests – Mathematical Foundation**

**Objective**

Improve decision trees by **reducing variance** through **ensembling**.

<img src="./media/image7.png" style="width:6.16667in;height:4.625in" />

------------------------------------------------------------------------

**Core mathematical ideas**

**(a) Bootstrap Aggregation (Bagging)**

- Draw multiple datasets using **sampling with replacement**

- Train one tree per sample

This lowers variance:

$$
Var(\overset{ˉ}{Y}) = \frac{1}{n}Var(Y)
$$

------------------------------------------------------------------------

**(b) Random feature selection**

At each split:

- Use only a **random subset of features**

- Decorrelates trees

If trees are less correlated:

$$
Var_{forest} \approx \rho\sigma^{2} + \frac{1 - \rho}{T}\sigma^{2}
$$

- $\rho$: correlation between trees

- $T$: number of trees

Lower correlation ⇒ better performance.

------------------------------------------------------------------------

**Prediction**

- **Classification:** Majority vote

$$
\widehat{y} = \text{mode}(h_{1}(x),h_{2}(x),\ldots,h_{T}(x))
$$

- **Regression:** Average prediction

$$
\widehat{y} = \frac{1}{T}\sum_{t = 1}^{T}h_{t}(x)
$$

------------------------------------------------------------------------

**Mathematical advantages**

- Lower variance than a single tree

- Handles non‑linearity and interactions well

- Law of large numbers improves stability

**Trade‑off**

- Less interpretable

- Higher computational cost

**Intuition**

Random forests average many weak, uncorrelated trees to produce a strong, stable model.

------------------------------------------------------------------------

**Comparison Summary (Interview‑Friendly)**

| **Model** | **Core Maths Idea** | **Strength** | **Weakness** |
|----|----|----|----|
| Linear Regression | Least squares optimisation | Simple, interpretable | Assumes linearity |
| Decision Tree | Entropy / Gini minimisation | Non‑linear, intuitive | High variance |
| Random Forest | Variance reduction via averaging | Accurate, robust | Less interpretable |

------------------------------------------------------------------------

**Final one‑liner for interviews**

“Linear regression is based on least‑squares optimisation, decision trees minimise impurity using entropy or Gini, and random forests reduce variance by aggregating many randomly trained trees.”

------------------------------------------------------------------------

# Neural networks ( architecture, gradient, maths in the nodes, gradient descent, weights)

------------------------------------------------------------------------

**1. Neural Network Architecture**

A **neural network** is a layered function approximator.

**Basic structure**

- **Input layer:** Features $x_{1},x_{2},\ldots,x_{n}$

- **Hidden layer(s):** Non‑linear transformations

- **Output layer:** Prediction (regression or classification)

Input → Hidden Layers → Output

Each layer consists of **neurons (nodes)** connected by **weights**.

------------------------------------------------------------------------

**2. Mathematics Inside a Neuron (Node)**

Each neuron performs **two main mathematical steps**:

**(a) Weighted Sum**

$$
z = w_{1}x_{1} + w_{2}x_{2} + \cdots + w_{n}x_{n} + b
$$

- $x_{i}$: input features

- $w_{i}$: weights

- $b$: bias (shifts the function)

------------------------------------------------------------------------

**(b) Activation Function**

$$
a = f(z)
$$

This introduces **non‑linearity**, allowing the network to model complex patterns.

**Common activation functions:**

- **ReLU:** $f(z) = \max(0,z)$

- **Sigmoid:** $\frac{1}{1 + e^{- z}}$

- **Tanh:** $\frac{e^{z} - e^{- z}}{e^{z} + e^{- z}}$

- **Softmax (output layer):**

$$
\text{Softmax}(z_{i}) = \frac{e^{z_{i}}}{\sum_{j}^{}e^{z_{j}}}
$$

**Interview intuition:**

A neuron computes a weighted sum of inputs and passes it through a non‑linear activation.

------------------------------------------------------------------------

**3. Weights and Biases**

- **Weights** determine **importance** of each input

- **Bias** allows output to shift left/right

Mathematically, the network represents a **parameterised function**:

$$
\widehat{y} = f(x;W,b)
$$

Training means **finding optimal values of weights and biases**.

------------------------------------------------------------------------

**4. Loss Function (Error Measurement)**

The network learns by minimising a **loss function**.

**Examples**

- **Regression (MSE):**

$$
L = \frac{1}{n}\sum(y - \widehat{y})^{2}
$$

- **Classification (Cross‑entropy):**

$$
L = - \sum y\log(\widehat{y})
$$

The loss defines **how wrong the prediction is**.

------------------------------------------------------------------------

**5. Gradients and Backpropagation**

**What is a Gradient?**

A **gradient** is the partial derivative of the loss with respect to a parameter:

$$
\frac{\partial L}{\partial w}
$$

It tells:

- **Direction** to change the weight

- **How much** the change affects the loss

------------------------------------------------------------------------

**Backpropagation (Core Idea)**

Backpropagation applies the **chain rule of calculus** to compute gradients efficiently.

For a weight:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}
$$

Where:

- $\frac{\partial a}{\partial z} = f'(z)$(activation derivative)

- $\frac{\partial z}{\partial w} = x$

------------------------------------------------------------------------

**Why backprop works**

- Reuses intermediate derivatives

- Scales to deep networks

**Interview intuition:**

Backpropagation calculates how much each weight contributed to the final error.

**6. Gradient Descent (Learning Process)**

Once gradients are known, weights are updated using **gradient descent**.

**Update rule**

$$
w_{new} = w_{old} - \eta\frac{\partial L}{\partial w}
$$

- $\eta$: learning rate

- Move **opposite** to the gradient (downhill)

------------------------------------------------------------------------

**Variants**

- **Batch Gradient Descent:** Full dataset

- **Stochastic Gradient Descent (SGD):** One sample

- **Mini‑batch GD:** Small batches (most common)

------------------------------------------------------------------------

**Problems & fixes**

- **Too large learning rate:** Divergence

- **Too small:** Slow learning

- **Local minima / saddle points:** Momentum, Adam optimizer

------------------------------------------------------------------------

**7. Putting It All Together (Training Loop)**

1.  Forward pass → compute predictions

2.  Compute loss

3.  Backpropagation → compute gradients

4.  Gradient descent → update weights

5.  Repeat until convergence

------------------------------------------------------------------------

**Interview Comparison Summary**

| **Concept**      | **Mathematical Role**               |
|------------------|-------------------------------------|
| Architecture     | Function composition                |
| Weights          | Learnable parameters                |
| Node             | Weighted sum + activation           |
| Gradient         | Direction of steepest loss increase |
| Backpropagation  | Chain rule                          |
| Gradient Descent | Optimisation                        |

------------------------------------------------------------------------

**Final Interview One‑Liner**

“A neural network is a layered mathematical function where each neuron computes a weighted sum followed by a non‑linear activation, and the weights are learned using gradient descent through backpropagation.”

------------------------------------------------------------------------

**Mathematics Inside a Neuron**

Each neuron performs two steps:

**1. Weighted Sum**

$$
z = w_{1}x_{1} + w_{2}x_{2} + \cdots + w_{n}x_{n} + b
$$

- $x_{i}$: inputs

- $w_{i}$: weights

- $b$: bias

------------------------------------------------------------------------

**2. Activation Function**

$$
a = f(z)
$$

The **activation function** introduces non‑linearity, allowing the network to model complex relationships.

------------------------------------------------------------------------

**ReLU (Rectified Linear Unit)**

**Definition**

$$
\text{ReLU}(z) = \max(0,z)
$$

- If $z > 0$→ output $z$

- If $z \leq 0$→ output $0$

**Why ReLU is Used in Neural Networks**

**1. Introduces Non‑Linearity**

Without ReLU, a neural network becomes a chain of linear functions and cannot model complex patterns.

------------------------------------------------------------------------

**2. Solves the Vanishing Gradient Problem**

Earlier activations like sigmoid and tanh squash values into small ranges, causing gradients to become very small.

ReLU:

- Gradient = **1** for $z > 0$

- Gradient = **0** for $z \leq 0$

This allows **faster and more stable training**.

------------------------------------------------------------------------

**3. Computationally Efficient**

- Simple max operation

- Faster than sigmoid/tanh

------------------------------------------------------------------------

**Derivative of ReLU (for Backpropagation)**

$$
\frac{d}{dz}\text{ReLU}(z) = \left\{ \begin{matrix}
1, & z > 0 \\
0, & z \leq 0
\end{matrix} \right.\ 
$$

This derivative is used during **backpropagation** to update weights using gradient descent.

------------------------------------------------------------------------

**ReLU in Training (Backpropagation Context)**

1.  Forward pass computes:

$$
z = Wx + b,a = \max(0,z)
$$

2.  Loss is calculated

3.  Backpropagation computes gradients:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}
$$

> Where:
>
> $\frac{\partial L}{\partial w}$tells:

- **Direction** to change the weight

- **How much** the change affects the loss

<!-- -->

- $\frac{\partial a}{\partial z} = f'(z)$(activation derivative)

- $\frac{\partial z}{\partial w} = x$

4.  Weights updated using gradient descent:

$$
w_{new} = w_{old} - \eta\frac{\partial L}{\partial w}
$$

------------------------------------------------------------------------

**Limitations of ReLU**

**Dying ReLU Problem**

- If a neuron’s weights make $z \leq 0$always,

- Gradient becomes **zero**

- Neuron stops learning

------------------------------------------------------------------------

**Variants of ReLU (Briefly)**

- **Leaky ReLU:** Allows small gradient when $z < 0$

$$
f(z) = \max(0.01z,z)
$$

- **Parametric ReLU (PReLU):** Learnable slope

- **ELU:** Smooth negative values

------------------------------------------------------------------------

**Interview Comparison (Quick)**

| **Activation** | **Issue**                |
|----------------|--------------------------|
| Sigmoid        | Vanishing gradients      |
| Tanh           | Vanishing gradients      |
| ReLU           | Faster, sparse, scalable |
| Leaky ReLU     | Fixes dying ReLU         |

------------------------------------------------------------------------

**Final Interview One‑Liner**

“A neural network is a layered mathematical model where each neuron computes a weighted sum followed by an activation, and ReLU is the most commonly used activation because it introduces non‑linearity and enables faster, more stable training.”

------------------------------------------------------------------------

**ReLU vs Sigmoid (Activation Functions)**

**Diagram: ReLU vs Sigmoid**

Show more lines

------------------------------------------------------------------------

**1. Sigmoid Activation Function**

**Mathematical Definition**

$$
\sigma(z) = \frac{1}{1 + e^{- z}}
$$

**Key Characteristics**

- Output range: **(0, 1)**

- Smooth, S‑shaped curve

- Interpretable as probability

**Problems (Math‑Driven)**

- **Vanishing gradient**:\
  For large $\mid z \mid$,

$$
\sigma'(z) \approx 0
$$

- Slows learning in deep networks

- Gradients die as layers increase

**Typical Use**

- **Output layer** for binary classification

------------------------------------------------------------------------

**2. ReLU (Rectified Linear Unit)**

**Mathematical Definition**

$$
\text{ReLU}(z) = \max(0,z)
$$

**Key Characteristics**

- Output range: **\[0, ∞)**

- Piecewise linear

- Sparse activation (many zeros)

**Gradient Behaviour**

$$
\frac{d}{dz}\text{ReLU}(z) = \left\{ \begin{matrix}
1 & z > 0 \\
0 & z \leq 0
\end{matrix} \right.\ 
$$

- Strong gradients when active

- Enables **fast and stable training**

**Typical Use**

- **Hidden layers** in deep neural networks

------------------------------------------------------------------------

**Key Comparison Table (Interview‑Friendly)**

| **Aspect**     | **Sigmoid**           | **ReLU**              |
|----------------|-----------------------|-----------------------|
| Formula        | $\frac{1}{1 + e^{- z}}$ | $\max(0,z)$         |
| Output Range   | (0, 1)                | \[0, ∞)               |
| Gradient Issue | Vanishing gradient    | Zero for $z \leq 0$ |
| Speed          | Slower                | Faster                |
| Deep Networks  | Poor                  | Very good             |
| Common Usage   | Binary output         | Hidden layers         |

------------------------------------------------------------------------

**Intuition Using the Diagram**

- **Sigmoid** flattens at both ends → gradients shrink

- **ReLU** grows linearly for positive values → strong gradients

- This is why **ReLU dominates modern deep learning**

**Final Interview One‑Liner**

“Sigmoid squashes values between 0 and 1 but suffers from vanishing gradients, while ReLU is computationally simple, avoids gradient shrinkage, and enables efficient training of deep neural networks.”

------------------------------------------------------------------------

# Clustering

------------------------------------------------------------------------

**Clustering**

**Definition:**\
Clustering is an **unsupervised machine learning technique** used to **group similar data points together** without using labelled data.

------------------------------------------------------------------------

**Purpose**

- Discover **natural groupings or structure** in data

- Identify patterns when outcomes or labels are **unknown**

- Simplify large datasets by segmentation

------------------------------------------------------------------------

**How Clustering Works (High Level Maths)**

- A **similarity or distance measure** (e.g. Euclidean distance) is used

- Data points that are **closer** are grouped into the same cluster

- The goal is:

  - **High similarity within clusters**

  - **Low similarity between clusters**

------------------------------------------------------------------------

**Common Clustering Techniques**

**1. K‑Means Clustering**

**Idea:** Partition data into **K clusters** by minimising within‑cluster variance.

**Mathematical objective:**

$$
\min\sum_{i = 1}^{K}{\sum_{x \in C_{i}}^{}{\parallel x -}}\mu_{i} \parallel^{2}
$$

- $\mu_{i}$: centroid of cluster $i$

- Iterative assignment → update centroids → repeat

**Pros:** Fast, simple\
**Cons:** Need to pre‑define $K$, sensitive to outliers

------------------------------------------------------------------------

**2. Hierarchical Clustering**

**Idea:** Builds a **tree (dendrogram)** of clusters.

- **Agglomerative:** bottom‑up (merge clusters)

- **Divisive:** top‑down (split clusters)

Uses distance measures like:

- Single linkage

- Complete linkage

- Average linkage

------------------------------------------------------------------------

**3. DBSCAN (Density‑Based Clustering)**

**Idea:** Groups points in **dense regions** and labels sparse points as noise.

- Does not require number of clusters

- Good for irregular shapes and outliers

------------------------------------------------------------------------

**Applications**

- **IT operations:**

  - Grouping similar incidents or alerts

  - Detecting unusual system behaviour (pre‑step to anomaly detection)

- **Business:**

  - Customer segmentation

  - Usage pattern analysis

- **Security:**

  - Identifying abnormal access patterns

- **Data exploration:**

  - Understanding structure in large datasets

------------------------------------------------------------------------

**Key Characteristics (Interview Focus)**

| **Aspect**      | **Clustering**                         |
|-----------------|----------------------------------------|
| Learning type   | Unsupervised                           |
| Labels required | No                                     |
| Output          | Grouped clusters                       |
| Main challenge  | Choosing distance & number of clusters |

------------------------------------------------------------------------

**Clustering vs Classification (Quick Contrast)**

- **Clustering:** Finds groups with *no labels*

- **Classification:** Assigns labels using *training data*

------------------------------------------------------------------------

**Final Interview One‑Liner**

“Clustering is an unsupervised learning technique that groups similar data points based on distance or density to discover hidden structure in datasets.”

------------------------------------------------------------------------

**K‑Means Clustering: Step‑by‑Step**

**What is K‑Means?**

K‑Means is an **unsupervised learning algorithm** that groups data into **K clusters** by minimising the distance between data points and their cluster centre (centroid).

------------------------------------------------------------------------

**Step 1: Choose the Number of Clusters (K)**

- Decide how many clusters you want (**K**) before running the algorithm.

- This is usually based on domain knowledge or methods like the **Elbow method**.

**Example:**\
Choose $K = 3$to group incidents into 3 patterns.

------------------------------------------------------------------------

**Step 2: Initialise Centroids**

- Randomly select **K data points** as initial cluster centroids.

- Each centroid represents the “centre” of a cluster.

**Why it matters:**\
Random initialisation can affect the final result.

------------------------------------------------------------------------

**Step 3: Assign Data Points to the Nearest Centroid**

- Calculate the **distance** between each data point and every centroid.

- Assign the data point to the **closest centroid**.

Most common distance:

$$
\text{Euclidean~Distance} = \sqrt{\sum(x_{i} - \mu_{i})^{2}}
$$

------------------------------------------------------------------------

**Step 4: Update Centroids**

- For each cluster, recompute the centroid as the **mean of all assigned points**.

$$
\mu = \frac{1}{n}\sum_{i = 1}^{n}x_{i}
$$

This moves the centroid closer to the centre of its cluster.

------------------------------------------------------------------------

**Step 5: Repeat Assignment and Update**

- Reassign points using the **new centroids**

- Recalculate centroids again

- Continue iterating until:

  - Centroids no longer move **or**

  - Assignments stop changing **or**

  - Maximum iterations reached

This is called **convergence**.

------------------------------------------------------------------------

**Step 6: Final Clusters Output**

- Each data point belongs to one cluster

- Each cluster has a final centroid

- Within‑cluster variance is minimised

Mathematical objective:

$$
\min\sum_{k = 1}^{K}{\sum_{x \in C_{k}}^{}{\parallel x -}}\mu_{k} \parallel^{2}
$$

------------------------------------------------------------------------

**Key Characteristics (Interview Focus)**

| **Aspect**      | **K‑Means**                      |
|-----------------|----------------------------------|
| Learning type   | Unsupervised                     |
| Input           | Numerical data                   |
| Objective       | Minimise within‑cluster variance |
| Distance metric | Usually Euclidean                |
| Output          | K clusters + centroids           |

------------------------------------------------------------------------

**Advantages**

- Simple and fast

- Scales well to large datasets

- Easy to implement

------------------------------------------------------------------------

**Limitations**

- Must pre‑define **K**

- Sensitive to initial centroids

- Struggles with non‑spherical clusters

- Sensitive to outliers

------------------------------------------------------------------------

**Real‑World Example (IT Operations)**

- Cluster incidents by **resolution time and category**

- Identify common failure patterns

- Support proactive problem management

------------------------------------------------------------------------

**Final Interview One‑Liner**

“K‑Means works by choosing K cluster centres, assigning points to the nearest centre, updating the centres using the mean, and repeating the process until the clusters stabilise.”

------------------------------------------------------------------------

**Where Do You Use K‑Means Clustering?**

K‑Means is used when you want to **group similar data points** and **don’t have predefined labels**. It is most suitable when the data is **numerical** and clusters are expected to be relatively **well‑separated**.

------------------------------------------------------------------------

**Common Real‑World Use Cases**

**1. IT Operations (Very Interview‑Relevant ✅)**

- **Incident clustering:**\
  Group incidents based on resolution time, category, and impact to identify common failure patterns

- **Alert noise reduction:**\
  Cluster similar alerts to eliminate duplicates and prioritise root causes

- **System performance analysis:**\
  Group servers or applications based on CPU, memory, and latency behaviour

**Example:**

Clustering incidents to identify which issues repeatedly cause SLA breaches.

------------------------------------------------------------------------

**2. Customer Segmentation**

- Group customers based on behaviour such as:

  - Usage frequency

  - Spending patterns

  - Engagement levels

**Example:**

Dividing users into high‑value, medium‑value, and low‑usage clusters.

------------------------------------------------------------------------

**3. Business & Sales Analytics**

- Market segmentation

- Sales territory analysis

- Product usage pattern identification

**Example:**

Grouping products by sales volume and profitability.

------------------------------------------------------------------------

**4. Data Exploration & Pattern Discovery**

- First step in **exploratory data analysis**

- Helps understand structure before applying other models

**Example:**

Exploring unknown datasets to see natural groupings.

------------------------------------------------------------------------

**5. Image Compression (Classic Example)**

- Pixels are clustered by colour

- Each pixel is replaced by its cluster centroid

**Result:**\
Lower storage size with minimal quality loss.

------------------------------------------------------------------------

**6. Telecommunications & Network Analysis**

- Grouping cell towers by traffic load

- Identifying usage hotspots

- Network capacity planning

------------------------------------------------------------------------

**7. Healthcare & Research**

- Patient risk grouping

- Grouping medical records with similar attributes

- Disease pattern exploration

------------------------------------------------------------------------

**When K‑Means Is a Good Choice**

✅ You use K‑Means when:

- Data is **numerical**

- You want **quick, scalable clustering**

- Approximate cluster shapes are expected

- You know or can estimate the number of clusters (**K**)

**When NOT to Use K‑Means (Interview Tip)**

❌ Avoid K‑Means when:

- Clusters are non‑spherical

- Many outliers exist

- Data is categorical

- You don’t know K and clusters vary widely in size

------------------------------------------------------------------------

**Quick Interview Summary**

**One‑liner:**

“K‑Means is used to group similar data points in large, unlabeled datasets, such as clustering IT incidents, customer segments, or system performance patterns.”

------------------------------------------------------------------------

**Model Evaluation Metrics**

Metrics are used to **measure how well a machine‑learning model performs** by comparing predictions with actual values.

------------------------------------------------------------------------

**1. Regression Metrics**

(Used when the target variable is **continuous**)

**1. Mean Absolute Error (MAE)**

$$
MAE = \frac{1}{n}\sum \mid y - \widehat{y} \mid 
$$

- Average absolute difference between actual and predicted values

- Easy to interpret

- Less sensitive to outliers

**Best when:** Errors should be treated equally\
**Example:** Average error in predicting response time

------------------------------------------------------------------------

**2. Mean Squared Error (MSE)**

$$
MSE = \frac{1}{n}\sum(y - \widehat{y})^{2}
$$

- Squares errors → larger errors penalised more

- Differentiable, widely used in optimisation

**Downside:** Units are squared\
**Example:** Predicting server load

------------------------------------------------------------------------

**3. Root Mean Squared Error (RMSE)**

$$
RMSE = \sqrt{MSE}
$$

- Same unit as target variable

- Penalises large errors strongly

**Best when:** Large errors are costly\
**Example:** Forecasting downtime duration

------------------------------------------------------------------------

**4. R‑squared (**$\mathbf{R}^{\mathbf{2}}$**)**

$$
R^{2} = 1 - \frac{SS_{res}}{SS_{tot}}
$$

- Measures **variance explained** by the model

- Range: $0$to $1$(can be negative)

**Interpretation:**

- $R^{2} = 0.85$→ 85% variance explained

**Limitation:**

- Doesn’t show prediction accuracy directly

------------------------------------------------------------------------

**5. Adjusted R‑squared**

- Penalises unnecessary features

- Better for **multiple linear regression**

------------------------------------------------------------------------

**Regression Metrics Summary**

| **Metric** | **Focus**             |
|------------|-----------------------|
| MAE        | Average error         |
| MSE        | Penalise large errors |
| RMSE       | Error magnitude       |
| R²         | Model fit             |

------------------------------------------------------------------------

**2. Classification Metrics**

(Used when the target variable is **categorical**)

Based on the **Confusion Matrix**:

| **Actual \\ Predicted** | **Positive** | **Negative** |
|-------------------------|--------------|--------------|
| Positive                | TP           | FN           |
| Negative                | FP           | TN           |

------------------------------------------------------------------------

**1. Accuracy**

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

- Overall correctness

**Limitation:**

- Misleading for imbalanced datasets

------------------------------------------------------------------------

**2. Precision**

$$
Precision = \frac{TP}{TP + FP}
$$

- Of predicted positives, how many are correct

- Focuses on **false positives**

**Example:** Spam detection (avoid flagging valid emails)

------------------------------------------------------------------------

**3. Recall (Sensitivity)**

$$
Recall = \frac{TP}{TP + FN}
$$

- Of actual positives, how many were captured

- Focuses on **false negatives**

**Example:** Security threat detection

------------------------------------------------------------------------

**4. F1‑Score**

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

- Balance between precision and recall

- Best for **imbalanced classes**

------------------------------------------------------------------------

**5. Specificity**

$$
Specificity = \frac{TN}{TN + FP}
$$

- True negative rate

- Important in medical or risk models

------------------------------------------------------------------------

**6. ROC Curve & AUC**

- **ROC:** Recall vs False Positive Rate

- **AUC:** Area under ROC curve

**Interpretation:**

- AUC = 1 → perfect model

- AUC = 0.5 → random guessing

------------------------------------------------------------------------

**Classification Metrics Summary**

| **Metric** | **Measures**           |
|------------|------------------------|
| Accuracy   | Overall correctness    |
| Precision  | False positives        |
| Recall     | False negatives        |
| F1‑Score   | Balance                |
| AUC‑ROC    | Classification quality |

------------------------------------------------------------------------

**Regression vs Classification (Quick Contrast)**

| **Aspect**   | **Regression** | **Classification**          |
|--------------|----------------|-----------------------------|
| Output       | Continuous     | Discrete                    |
| Core metrics | MAE, RMSE, R²  | Accuracy, Precision, Recall |
| Typical use  | Prediction     | Decision making             |

------------------------------------------------------------------------

**Final Interview One‑Liners**

- **Regression:**

“Regression metrics measure prediction error and model fit on continuous values.”

- **Classification:**

“Classification metrics evaluate correctness and trade‑offs between false positives and false negatives.”

------------------------------------------------------------------------

# Types of Machine Learning

Machine learning can be broadly classified based on **how the model learns from data** and **whether labelled data is available**.

------------------------------------------------------------------------

**1. Supervised Learning**

**Definition:**\
The model is trained on **labelled data** (input + correct output).

**Goal:**\
Learn a mapping from inputs to outputs to make accurate **predictions or classifications**.

**Common Tasks**

- **Regression:** Predict continuous values

- **Classification:** Predict categories

**Algorithms**

- Linear Regression

- Logistic Regression

- Decision Trees

- Random Forests

- Support Vector Machines

- Neural Networks

**Applications**

- Predicting incident volumes

- Spam detection

- Credit scoring

- Disease diagnosis

**Interview one‑liner:**

“Supervised learning learns from labelled examples to predict outcomes.”

------------------------------------------------------------------------

**2. Unsupervised Learning**

**Definition:**\
The model learns from **unlabelled data** with no predefined output.

**Goal:**\
Discover **patterns, structures, or groupings** in data.

**Common Tasks**

- Clustering

- Pattern discovery

- Dimensionality reduction

**Algorithms**

- K‑Means Clustering

- Hierarchical Clustering

- DBSCAN

- PCA (Principal Component Analysis)

**Applications**

- Customer segmentation

- Incident pattern analysis

- Anomaly detection

**Interview one‑liner:**

“Unsupervised learning finds hidden patterns in data without labels.”

------------------------------------------------------------------------

**3. Semi‑Supervised Learning**

**Definition:**\
Uses a **small amount of labelled data** and a **large amount of unlabelled data**.

**Goal:**\
Improve model accuracy when labelled data is expensive or limited.

**Techniques**

- Self‑training

- Label propagation

- Pseudo‑labelling

**Applications**

- Image classification

- Text classification

- Web content tagging

**Interview one‑liner:**

“Semi‑supervised learning combines limited labelled data with abundant unlabelled data.”

------------------------------------------------------------------------

**4. Reinforcement Learning**

**Definition:**\
An agent learns by **interacting with an environment** and receiving **rewards or penalties**.

**Goal:**\
Learn the **best action policy** to maximise cumulative reward.

**Key Elements**

- Agent

- Environment

- Actions

- Rewards

- Policy

**Algorithms**

- Q‑Learning

- SARSA

- Deep Q‑Networks (DQN)

**Applications**

- Robotics

- Game AI (e.g., AlphaGo)

- Resource optimisation

- Automated control systems

**Interview one‑liner:**

“Reinforcement learning learns optimal actions through trial and error using rewards.”

------------------------------------------------------------------------

**5. Self‑Supervised Learning (Modern Category)**

**Definition:**\
The model creates its **own labels from raw data**.

**Goal:**\
Learn useful representations without manual labelling.

**Examples**

- Predicting masked words in text

- Image feature learning

**Applications**

- Large Language Models

- Speech recognition

- Computer vision

**Interview one‑liner:**

“Self‑supervised learning generates labels from the data itself to learn representations.”

------------------------------------------------------------------------

**Summary Table (Interview Recall)**

| **Type**        | **Labels Needed** | **Main Use**               |
|-----------------|-------------------|----------------------------|
| Supervised      | Yes               | Prediction, classification |
| Unsupervised    | No                | Pattern discovery          |
| Semi‑Supervised | Few               | Cost‑efficient learning    |
| Reinforcement   | Reward‑based      | Decision‑making            |
| Self‑Supervised | Generated         | Representation learning    |

------------------------------------------------------------------------

**Final Interview Wrap‑Up (30 seconds)**

“Machine learning can be supervised, unsupervised, semi‑supervised, or reinforcement‑based, depending on whether labelled data or reward signals are used. Modern systems also use self‑supervised learning to scale with unlabelled data.”

------------------------------------------------------------------------

# The Machine Learning Pipeline

The machine learning pipeline describes the **sequence of steps followed to build, train, evaluate, and deploy an ML model** in a systematic and repeatable way.

------------------------------------------------------------------------

**1. Problem Definition**

**What happens:**

- Define the **business problem**

- Decide if it is **regression, classification, clustering**, etc.

- Identify success criteria (KPIs)

**Example:**\
Predict incident resolution time → **Regression problem**

------------------------------------------------------------------------

**2. Data Collection**

**What happens:**

- Gather data from sources such as:

  - Databases

  - Logs

  - APIs

  - Sensors

  - CSV / Excel files

**Key point:**\
Data quality directly affects model quality.

------------------------------------------------------------------------

**3. Data Understanding & Exploration (EDA)**

**What happens:**

- Understand structure and content of data

- Identify:

  - Missing values

  - Outliers

  - Distributions

  - Correlations

**Techniques:**

- Summary statistics

- Visualisations (histograms, box plots)

- Correlation analysis

------------------------------------------------------------------------

**4. Data Preprocessing & Cleaning**

**What happens:**

- Handle missing values (mean, median, drop)

- Remove duplicates

- Handle outliers

- Encode categorical variables

- Scale/normalise features

**Why important:**

ML models learn patterns — bad data → bad patterns.

------------------------------------------------------------------------

**5. Feature Engineering & Selection**

**What happens:**

- Create new features from existing ones

- Select relevant features

- Remove redundant or irrelevant features

**Examples:**

- Creating “average response time per day”

- Selecting most impactful metrics

**Goal:**\
Improve model performance and interpretability.

------------------------------------------------------------------------

**6. Train–Test Split**

**What happens:**

- Split data into:

  - **Training set** (e.g. 70–80%)

  - **Test set** (e.g. 20–30%)

**Why needed:**

- To evaluate model performance on **unseen data**

- Prevent overfitting

------------------------------------------------------------------------

**7. Model Selection**

**What happens:**

- Choose appropriate algorithm:

  - Linear Regression

  - Decision Trees

  - Random Forest

  - Neural Networks

**Factors considered:**

- Problem type

- Data size

- Interpretability

- Complexity

------------------------------------------------------------------------

**8. Model Training**

**What happens:**

- Model learns patterns from training data

- Optimises parameters (weights) by minimising loss

**Techniques used:**

- Gradient descent

- Backpropagation (for neural networks)

------------------------------------------------------------------------

**9. Model Evaluation**

**What happens:**

- Evaluate model on test data using metrics

**Metrics:**

- **Regression:** MAE, RMSE, R²

- **Classification:** Accuracy, Precision, Recall, F1‑score, AUC

**Goal:**\
Measure how well the model generalises.

------------------------------------------------------------------------

**10. Hyperparameter Tuning**

**What happens:**

- Optimise parameters not learned automatically

**Techniques:**

- Grid search

- Random search

- Cross‑validation

**Example:**\
Number of trees in Random Forest

------------------------------------------------------------------------

**11. Model Deployment**

**What happens:**

- Deploy model into production

- Integrate with applications or systems

- Expose via APIs or pipelines

**Outcome:**\
Model starts making **real‑time or batch predictions**.

------------------------------------------------------------------------

**12. Monitoring & Maintenance**

**What happens:**

- Monitor model performance

- Detect data drift or concept drift

- Retrain model periodically

**Why important:**

Real‑world data changes over time.

------------------------------------------------------------------------

**ML Pipeline Summary Flow**

Problem → Data → EDA → Preprocessing → Features

→ Train/Test Split → Model Training

→ Evaluation → Tuning → Deployment → Monitoring

------------------------------------------------------------------------

**Interview One‑Liner**

“The machine learning pipeline is a structured process that starts with problem definition and data preparation, followed by model training, evaluation, deployment, and continuous monitoring.”

------------------------------------------------------------------------

**15‑Second Interview Version**

“The ML pipeline includes data collection, preprocessing, feature engineering, model training, evaluation, deployment, and monitoring to ensure reliable, scalable predictions.”

------------------------------------------------------------------------

<img src="./media/image8.png" style="width:6.26806in;height:4.45in" />

------------------------------------------------------------------------

------------------------------------------------------------------------

**✅ How to Explain This Diagram (Interview‑Ready)**

“The machine learning pipeline starts with problem definition and data collection. The data is then explored, cleaned, and transformed through feature engineering. After splitting into training and test sets, models are trained, evaluated, and tuned. Once the best model is selected, it is deployed and continuously monitored and retrained as data evolves.”

------------------------------------------------------------------------

**✅ Key Characteristics of This Diagram**

- Clear **top‑to‑bottom flow**

- Each step represented as a **distinct block**

- Logical separation between:

  - Data stages

  - Modeling stages

  - Operational stages

- Easy to **reproduce on a whiteboard**

------------------------------------------------------------------------

**✅ Whiteboard / Exam Shortcut Version**

If you need to redraw quickly:

Problem

↓

Data → EDA → Preprocess → Features

↓

Train/Test → Train → Evaluate → Tune

↓

Deploy → Monitor → Retrain

------------------------------------------------------------------------

# Model Drift

------------------------------------------------------------------------

**How Do You Monitor Model Drift?**

**Model drift** happens when a machine‑learning model’s performance degrades over time because **data or real‑world behaviour changes**. Monitoring drift ensures the model remains **accurate, reliable, and trustworthy in production**.

There are **three main types of drift**, and each is monitored differently.

------------------------------------------------------------------------

**1. Data Drift (Input Drift)**

**What it is**

When the **distribution of input features changes** compared to training data.

**Example:**\
User traffic patterns shift after a system upgrade.

------------------------------------------------------------------------

**How to Monitor**

**✅ Statistical Distribution Monitoring**

Compare **training vs production data**:

- Mean / median

- Variance

- Histograms

- Percentiles

**✅ Statistical Tests**

- **KS Test (Kolmogorov–Smirnov)** – continuous features

- **Chi‑Square Test** – categorical features

- **Population Stability Index (PSI)** – common in industry

**Rule of thumb (PSI):**

- \< 0.1 → No drift

- 0.1–0.25 → Moderate drift

- 0.25 → Significant drift

------------------------------------------------------------------------

**Interview one‑liner**

“I monitor data drift by comparing feature distributions in production against training data using statistical tests like KS test or PSI.”

------------------------------------------------------------------------

**2. Concept Drift (Relationship Drift)**

**What it is**

The **relationship between inputs and outputs changes**, even if inputs look similar.

**Example:**\
Incidents start resolving faster after automation, so old predictors lose relevance.

------------------------------------------------------------------------

**How to Monitor**

**✅ Performance Metrics Over Time**

Track metrics on recent labelled data:

- Regression: RMSE, MAE

- Classification: Accuracy, Precision, Recall, F1

Sudden metric drops indicate concept drift.

**✅ Sliding Window Evaluation**

- Compare **recent window performance vs historical baseline**

- E.g. last 7 days vs training period

------------------------------------------------------------------------

**Interview one‑liner**

“I detect concept drift by monitoring model performance metrics over time using rolling windows.”

**3. Prediction Drift (Output Drift)**

**What it is**

Model predictions change abnormally, even before labels arrive.

**Example:**\
Sudden spike in high‑priority incident predictions.

------------------------------------------------------------------------

**How to Monitor**

**✅ Output Distribution Monitoring**

- Track class probabilities

- Monitor prediction frequencies

Example:

- % of incidents predicted as “Critical”

- Average predicted resolution time

This is useful when **labels are delayed**.

------------------------------------------------------------------------

**4. Thresholds, Alerts & Dashboards**

**What You Put in Place**

✅ Automated alerts when:

- PSI crosses threshold

- Accuracy drops by X%

- Prediction distribution deviates significantly

✅ Dashboards showing:

- Feature drift trends

- Model performance over time

- Prediction stability

------------------------------------------------------------------------

**5. Retraining Strategy (What Happens After Drift)**

When drift is detected:

1.  Confirm drift type (data vs concept)

2.  Collect fresh labelled data

3.  Retrain model

4.  Re‑validate performance

5.  Redeploy model

6.  Reset monitoring baselines

------------------------------------------------------------------------

**End‑to‑End Monitoring Flow (Simple)**

Production Data

↓

Statistical Drift Checks

↓

Performance Monitoring

↓

Alerts & Dashboards

↓

Retraining Decision

------------------------------------------------------------------------

**Real‑World IT Operations Example**

- Monitor drift in:

  - Incident volume features

  - Resolution time predictions

- Detect seasonality or process changes

- Retrain quarterly or when thresholds breach

------------------------------------------------------------------------

**Final Interview‑Perfect Answer (30 seconds)**

“I monitor model drift by tracking data drift using statistical tests like PSI and KS tests, monitoring concept drift through performance metrics over time, and observing prediction distributions when labels are delayed. When drift exceeds thresholds, the model is retrained and redeployed.”

------------------------------------------------------------------------

## Clean Drift Monitoring Diagram

<img src="./media/image9.png" style="width:6.26806in;height:2.7125in" />

**What it shows (quick read):**

- **Training data** sets the baseline → **Data drift checks**

- **Production data** → **Prediction drift checks**

- Drift signals feed into **Performance monitoring** + **Threshold decision**

- If breached → **Investigate & retrain** → **Deploy updated model**

- Deployment feeds back into production for **continuous monitoring**

------------------------------------------------------------------------

**2) Swimlane Version (Data vs Prediction vs Concept Drift)**

<img src="./media/image10.png" style="width:6.26806in;height:3.06458in" />

**Swimlanes included:**

1.  **Data drift (inputs):** Training baseline vs production feature distributions (PSI/KS/χ²)

2.  **Prediction drift (outputs):** Prediction score/class mix changes (useful when labels are delayed)

3.  **Concept drift / Performance:** Ground truth labels → metrics trend (RMSE/F1/AUC) → retrain/redeploy

------------------------------------------------------------------------

## How are PSI and Chi‑Square Test Measured?

Both **PSI** and **Chi‑Square tests** are used to **measure data drift**, but they differ in **what they compare and how they interpret change**.

------------------------------------------------------------------------

**1. Population Stability Index (PSI)**

**What PSI Measures**

PSI measures **how much the distribution of a feature in production data has shifted compared to training (baseline) data**.

- Widely used in **industry for drift monitoring**

- Works for **numerical and categorical** variables

- Simple and interpretable

------------------------------------------------------------------------

**How PSI Is Calculated (Step‑by‑Step)**

**Step 1: Bin the Data**

- Split the feature into equal bins (e.g. deciles or fixed ranges) - Deciles divide data into ten equal‑sized groups based on rank, with each group containing 10% of the observations.

- Use **same bins** for training and production

Example bins:

Bin1 \| Bin2 \| Bin3 \| Bin4 \| Bin5

------------------------------------------------------------------------

**Step 2: Calculate Percentage per Bin**

For each bin $i$:

- $Expected_{i}$→ % of training data

- $Actual_{i}$→ % of production data

------------------------------------------------------------------------

**Step 3: Apply PSI Formula**

$$
PSI = \sum_{i = 1}^{n}{(Actua}l_{i} - Expected_{i}) \times \ln\left( \frac{Actual_{i}}{Expected_{i}} \right)
$$

Where:

- $n$= number of bins

- Log = natural logarithm

------------------------------------------------------------------------

**Step 4: Interpret PSI Value**

| **PSI Value** | **Interpretation** |
|---------------|--------------------|
| \< 0.10       | No drift           |
| 0.10 – 0.25   | Moderate drift     |
| \> 0.25       | Significant drift  |

------------------------------------------------------------------------

**PSI Example (Simple)**

| **Bin** | **Training %** | **Production %** |
|---------|----------------|------------------|
| Low     | 30%            | 20%              |
| Medium  | 40%            | 50%              |
| High    | 30%            | 30%              |

PSI quantifies **how different these percentages are across bins**.

------------------------------------------------------------------------

**PSI Interview One‑Liner**

“PSI quantifies feature distribution shifts by comparing binned percentages between training and production data.”

------------------------------------------------------------------------

**2. Chi‑Square (χ²) Test**

**What Chi‑Square Measures**

The Chi‑Square test measures whether **observed frequencies differ significantly from expected frequencies**.

- Best for **categorical features**

- Tells **statistical significance**, not magnitude

- Returns a **p‑value**

------------------------------------------------------------------------

**How Chi‑Square Is Calculated (Step‑by‑Step)**

**Step 1: Create a Frequency Table**

Example:

| **Category** | **Expected (Training)** | **Observed (Production)** |
|--------------|-------------------------|---------------------------|
| A            | 50                      | 40                        |
| B            | 30                      | 45                        |
| C            | 20                      | 15                        |

------------------------------------------------------------------------

**Step 2: Apply Chi‑Square Formula**

$$
\chi^{2} = \sum\frac{(Observed - Expected)^{2}}{Expected}
$$

------------------------------------------------------------------------

**Step 3: Compute p‑value**

- Compare χ² statistic to **Chi‑Square distribution**

- Degrees of freedom:

$$
df = (number\ of\ categories - 1)
$$

------------------------------------------------------------------------

**Step 4: Interpret Result**

| **p‑value** | **Meaning**          |
|-------------|----------------------|
| p \< 0.05   | Significant drift    |
| p ≥ 0.05    | No significant drift |

------------------------------------------------------------------------

**Chi‑Square Interview One‑Liner**

“The Chi‑Square test checks whether differences between training and production category frequencies are statistically significant.”

------------------------------------------------------------------------

**PSI vs Chi‑Square (Very Important for Interviews)**

| **Aspect**      | **PSI**               | **Chi‑Square**           |
|-----------------|-----------------------|--------------------------|
| Data type       | Numeric & categorical | Categorical              |
| Output          | Drift magnitude       | Statistical significance |
| Threshold‑based | ✅ Yes                | ❌ No                    |
| Easy to explain | ✅                    | ⚠️ Moderate              |
| Industry use    | Very common           | Common                   |

------------------------------------------------------------------------

**When to Use Which?**

✅ **Use PSI when:**

- Monitoring numeric features continuously

- You want a **simple threshold‑based alert**

- Labels are unavailable

✅ **Use Chi‑Square when:**

- Feature is categorical

- You need **statistical significance**

- Feature frequencies matter

------------------------------------------------------------------------

**Final Interview Answer (30 seconds)**

“PSI measures how much production data distributions deviate from training data by comparing binned percentages, while the Chi‑Square test evaluates whether observed category frequencies differ significantly from expected ones using a statistical hypothesis test.”

------------------------------------------------------------------------

# KPIs for Algorithm Accuracy

Algorithm accuracy KPIs measure **how well a model’s predictions match reality** and whether it is **fit for production use**.

------------------------------------------------------------------------

**1. Core Accuracy KPIs (by Problem Type)**

**✅ Classification Models**

| **KPI** | **What it Measures** | **When to Use** |
|----|----|----|
| **Accuracy** | Overall correctness | Balanced datasets |
| **Precision** | False positives control | Spam, fraud alerts |
| **Recall (Sensitivity)** | False negatives control | Security, incident detection |
| **F1‑Score** | Balance of precision & recall | Imbalanced datasets |
| **AUC‑ROC** | Ranking quality across thresholds | Risk scoring systems |
| **Specificity** | True negative rate | Medical / risk domains |

**Interview one‑liner:**

“For classification accuracy, I track F1‑score and AUC rather than raw accuracy on imbalanced data.”

------------------------------------------------------------------------

**✅ Regression Models**

| **KPI**  | **What it Measures**     | **When to Use**            |
|----------|--------------------------|----------------------------|
| **MAE**  | Average prediction error | Business interpretability  |
| **RMSE** | Penalises large errors   | SLA / risk‑sensitive cases |
| **R²**   | Variance explained       | Model fit assessment       |
| **Map** | Percentage error         | Forecasting, demand        |

**Interview one‑liner:**

“For regression accuracy, RMSE shows error magnitude while R² explains model fit.”

------------------------------------------------------------------------

**2. Business‑Aligned Accuracy KPIs (Very Important)**

Accuracy alone is not enough. You should track **impact‑based KPIs**.

**Examples**

- **SLA prediction accuracy (%)**

- **Wrong critical predictions (%)**

- **Cost of incorrect predictions**

- **Automation success rate**

- **Incident prioritisation accuracy**

**Example (IT Ops):**

% of incidents correctly classified as P1/P2

**3. Production Accuracy KPIs (Operational)**

These ensure **accuracy remains stable after deployment**.

**✅ Performance Stability**

- Accuracy / RMSE trend over time

- Rolling window performance (e.g. last 7 vs last 30 days)

**✅ Drift‑Aware Accuracy**

- Accuracy before vs after drift detection

- Accuracy drop % triggering retraining

**✅ Latency‑Adjusted Accuracy**

- Accuracy under real‑time constraints

- Accuracy vs response‑time trade‑off

------------------------------------------------------------------------

**4. Threshold‑Based Accuracy KPIs (Governance)**

Used for **alerts, audit, and retraining decisions**.

| **KPI**       | **Example Threshold** |
|---------------|-----------------------|
| Accuracy drop | \> 5–10%              |
| F1‑score drop | \> 0.05               |
| RMSE increase | \> 15%                |
| AUC drop      | \< 0.7                |

**Interview phrasing:**

“We define accuracy thresholds, and retraining is triggered when metrics breach agreed limits.”

------------------------------------------------------------------------

**5. Model Confidence & Reliability KPIs (Advanced)**

- **Prediction confidence distribution**

- **Calibration error**

- **Coverage at confidence ≥ X%**

- **Error concentration (top decile error rate)**

Useful for **high‑risk decisions**.

------------------------------------------------------------------------

**6. KPI Selection Cheat Sheet**

| **Scenario**              | **Primary KPI**              |
|---------------------------|------------------------------|
| Balanced classification   | Accuracy                     |
| Imbalanced classification | F1 / AUC                     |
| False positives expensive | Precision                    |
| False negatives expensive | Recall                       |
| Forecasting               | RMSE / Map                  |
| Model governance          | Accuracy trends + thresholds |
| Production ML             | Accuracy + drift metrics     |

------------------------------------------------------------------------

**Final Interview Answer (30 seconds)**

“Algorithm accuracy KPIs depend on the problem type. For classification, I track F1‑score, precision, recall, and AUC, especially for imbalanced data. For regression, I use MAE, RMSE, and R². In production, I also monitor accuracy trends, threshold breaches, and business‑impact KPIs to ensure accuracy remains reliable over time.”

------------------------------------------------------------------------

This tool calculates the F1 Score and AUC (Area Under the Curve) for binary classification models based on input confusion matrix values or prediction scores. \[[1](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml?view=azureml-api-2), [2](https://sebastianraschka.com/faq/docs/computing-the-f1-score.html), [3](https://www.researchgate.net/figure/Confusion-matrix-The-accuracy-precision-recall-F1-score-and-AUC-mainly-rely-on-the_fig2_355985914), [4](https://www.geeksforgeeks.org/deep-learning/how-to-calculate-the-f1-score-and-other-custom-metrics-in-pytorch/)\]

**1. F1 Score & AUC Calculator**

Enter your model's confusion matrix values to calculate metrics instantly. \[[1](https://www.aiclouddatapulse.com/auc-vs-f1-score/), [2](https://calcbe.com/en/calculators/precision-recall/)\]

| **Metric \[[1](https://www.statsig.com/perspectives/calculate-true-positive-rate), [2](https://igulms.iqdigit.com/storage/16071/lec-27.pdf), [3](https://telnyx.com/learn-ai/calculating-f1-score), [4](https://medium.com/@balaji92/mastering-classification-metrics-a-deep-dive-from-f1-score-to-auc-roc-87e82b0ebfae), [5](https://www.aiclouddatapulse.com/auc-vs-f1-score/)\]** | **Formula** | **Calculator** |
|----|----|----|
| **True Positives (TP)** | Correct Positive Predictions | \[Input\] |
| **False Positives (FP)** | Incorrect Positive Predictions | \[Input\] |
| **False Negatives (FN)** | Incorrect Negative Predictions | \[Input\] |
| **True Negatives (TN)** | Correct Negative Predictions | \[Input\] |
| **Precision** | \\\frac{TP}{TP+FP}\\ | \[Auto-Calc\] |
| **Recall** | \\\frac{TP}{TP+FN}\\ | \[Auto-Calc\] |
| **F1 Score** | \\2 \times \frac{Precision \times Recall}{Precision + Recall}\\ | \[Auto-Calc\] |
| **AUC-ROC** | \\\text{Area\\ under\\ TPR/FPR\\ Curve}\\ | \[Requires Thresholds\] |

**2. Formulas and Interpretation**

- **F1 Score:** The harmonic mean of precision and recall. It is best used for imbalanced datasets where you need a balance between precision and recall, ranging from 0 to 1.

- **AUC-ROC:** Represents the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one.

  - **0.5:** Random guessing.

  - **1.0:** Perfect classifier. \[[1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html), [2](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall), [3](https://stackoverflow.com/questions/44172162/f1-score-vs-roc-auc), [4](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml?view=azureml-api-2), [5](https://www.evidentlyai.com/classification-metrics/explain-roc-curve)\]

**3. Example Calculation (Binary Classification)**

If your model has:

- **TP:** 90, **FP:** 20, **FN:** 10, **TN:** 880

- **Precision:** \\\frac{90}{90+20} = 0.818\\

- **Recall:** \\\frac{90}{90+10} = 0.900\\

- **F1 Score:** \\2 \times \frac{0.818 \times 0.900}{0.818+0.900} \approx \mathbf{0.857}\\ \[[1](https://www.aiclouddatapulse.com/auc-vs-f1-score/)\]

------------------------------------------------------------------------

**4. Implementation in Python (scikit-learn)**

python

from sklearn.metrics import f1_score, roc_auc_score

\# Example Predictions and Actual Labels

y_true = \[0, 1, 1, 0, 1, 0\]

y_scores = \[0.1, 0.9, 0.8, 0.2, 0.6, 0.3\] \# Probability scores

y_pred = \[0, 1, 1, 0, 1, 0\] \# Thresholded predictions

\# Calculate F1 Score

f1 = f1_score(y_true, y_pred)

\# Calculate AUC

auc = roc_auc_score(y_true, y_scores)

print(f"F1 Score: {f1:.4f}")

print(f"AUC Score: {auc:.4f}")

------------------------------------------------------------------------

To calculate \\R^{2}\\ (the Coefficient of Determination), you compare the variance explained by your regression model against the total variance in the data. The \\R^{2}\\ value for this example is **\\0.9486\\**, indicating that the model explains approximately **\\94.86\\\\** of the variability in the dependent variable. \[[1](https://www.youtube.com/watch?v=bMccdk8EdGo&t=104), [2](https://www.investopedia.com/terms/r/r-squared.asp), [3](https://mbrenndoerfer.com/writing/r-squared-coefficient-of-determination-formula-intuition-model-fit), [4](https://lean6sigmahub.com/how-to-calculate-and-interpret-the-coefficient-of-determination-r-squared-in-data-analysis/)\]

------------------------------------------------------------------------

**Step-by-Step Calculation Example**

We will use the following actual values (\\y\\) and predicted values (\\\\{y}\\):

- **Actual values (\\y\\):** \\\[3, -0.5, 2, 7\]\\

- **Predicted values (\\\\{y}\\):** \\\[2.5, 0, 2, 8\]\\ \[[1](https://medium.com/@ebimsv/machine-learning-series-day-2-simple-linear-regression-46a8566a5ac4), [2](https://medium.com/@tavishi.1402/linear-regression-in-ml-56107a59be03), [3](https://quantra.quantinsti.com/community/t/trading-with-machine-learning-regression/25169)\]

**1. Calculate the Mean of Actual Values**

First, find the average (\\\\{y}\\) of the actual data points.\
\\\\{y}=\frac{3+(-0.5)+2+7}{4}=2.875\\

**2. Find the Total Sum of Squares (\\SST\\)**

\\SST\\ measures the total variation in the actual data relative to the mean.\
\\SST=\sum (y\_{i}-\\{y})^{2}\\

- \\(3 - 2.875)^2 = 0.015625\\

- \\(-0.5 - 2.875)^2 = 11.390625\\

- \\(2 - 2.875)^2 = 0.765625\\

- \\(7 - 2.875)^2 = 17.015625\\

- **\\SST = 29.1875\\**

**3. Find the Residual Sum of Squares (\\SSR\\) \[[1](https://medium.com/@vasu.koradiya1998/simple-linear-regression-96a1f4ec27c2)\]**

\\SSR\\ (also known as \\SSE\\) measures the variation that the model *cannot* explain—the distance between actual and predicted values.\
\\SSR=\sum (y\_{i}-\\{y}\_{i})^{2}\\

- \\(3 - 2.5)^2 = 0.25\\

- \\(-0.5 - 0)^2 = 0.25\\

- \\(2 - 2)^2 = 0\\

- \\(7 - 8)^2 = 1\\

- **\\SSR = 1.5\\**

**4. Compute \\R^{2}\\**

Plug the values into the [standard \\R^{2}\\ formula](https://www.investopedia.com/terms/r/r-squared.asp) provided by Investopedia.\
\\R^{2}=1-\frac{SSR}{SST}\\\\R^{2}=1-\frac{1.5}{29.1875}\approx 1-0.05139=0.94861\\

The visualization above highlights the residuals (gray lines), which are the errors the model makes. Because these residuals are small compared to the distance from the mean (green line), the resulting \\R^{2}\\ is high. \[[1](https://www.mas.ncl.ac.uk/ask/numeracy-maths-statistics/statistics/regression-and-correlation/coefficient-of-determination-r-squared.html), [2](https://www.youtube.com/watch?v=-7U10N8PvlQ&t=35), [3](https://arize.com/blog-course/r-squared-understanding-the-coefficient-of-determination/), [4](https://amanrai77.medium.com/decoding-r-squared-back-to-basics-39a2aea6e83c), [5](https://www.youtube.com/watch?v=bMccdk8EdGo&t=104)\]

------------------------------------------------------------------------

**Final Answer**

The \\R^{2}\\ value for this regression model is **\\0.9486\\**.\
This indicates that approximately **\\94.86\\\\** of the variance in the actual data is accounted for by the model's predictions. \[[1](https://mbrenndoerfer.com/writing/r-squared-coefficient-of-determination-formula-intuition-model-fit), [2](https://lean6sigmahub.com/how-to-calculate-and-interpret-the-coefficient-of-determination-r-squared-in-data-analysis/)\]

------------------------------------------------------------------------

python

import numpy as np

\# Simple example data

y_true = np.array(\[3, -0.5, 2, 7\])

y_pred = np.array(\[2.5, 0.0, 2, 8\])

\# 1. Calculate Mean of y_true

y_mean = np.mean(y_true)

\# 2. Calculate Total Sum of Squares (SST)

sst = np.sum((y_true - y_mean)\*\*2)

\# 3. Calculate Residual Sum of Squares (SSR or SSE)

ssr = np.sum((y_true - y_pred)\*\*2)

\# 4. Calculate R2

r2 = 1 - (ssr / sst)

print(f"{y_true=}")

print(f"{y_pred=}")

print(f"{y_mean=}")

print(f"{sst=}")

print(f"{ssr=}")

print(f"{r2=}")

------------------------------------------------------------------------

# Poor Data quality

When **data quality is not good**, **pure accuracy metrics are unreliable**. In that situation, you should shift focus from *“how accurate is the prediction?”* to *“how reliable, stable, and trustworthy is the model given bad data?”*

------------------------------------------------------------------------

**✅ Short Answer (Interview‑ready)**

**When data quality is poor, accuracy alone should not be used. Instead, use robustness, stability, drift, and confidence‑based KPIs alongside error metrics like MAE rather than accuracy.**

------------------------------------------------------------------------

**✅ Recommended KPIs When Data Quality Is Poor**

**1. Error‑Based KPIs (More Robust than Accuracy)**

**✅ MAE (Mean Absolute Error)**

**Why:**

- Less sensitive to noise and outliers

- Easier to interpret with messy data

✅ Prefer **MAE** over RMSE when data quality is poor.

📌 *Use for regression models*

------------------------------------------------------------------------

**✅ Median Absolute Error**

- Even more robust to bad data

- Ignores extreme outliers caused by data issues

📌 *Very interview‑friendly answer for poor data quality*

------------------------------------------------------------------------

**2. Stability & Trend KPIs (Critical)**

When labels or data are noisy, **consistency matters more than correctness**.

**✅ Metric Stability Over Time**

- Accuracy / MAE trend (rolling windows)

- Week‑on‑week or month‑on‑month change

📌 KPI example:

% variation in MAE over last 30 days

------------------------------------------------------------------------

**✅ Prediction Stability**

- Drift in prediction distribution

- Sudden spikes indicate data problems

📌 KPI example:

% change in predicted critical cases

------------------------------------------------------------------------

**3. Drift‑Focused KPIs (Must‑have)**

Poor data quality often shows up first as **drift**.

**✅ Data Drift KPIs**

- **PSI**

- **KS‑test**

- Feature missing rate (% null increase)

📌 KPI example:

Number of features breaching PSI threshold

------------------------------------------------------------------------

**✅ Prediction Drift KPIs**

- Change in class mix

- Change in score distribution

📌 Useful when labels are unreliable

------------------------------------------------------------------------

**4. Confidence & Coverage KPIs (Very Strong Interview Point)**

When data quality is low, evaluate **how confident the model is**.

**✅ Coverage at Confidence Threshold**

% of predictions made with confidence ≥ 80%

Low coverage = unreliable input data.

------------------------------------------------------------------------

**✅ Low‑Confidence Prediction Rate**

% predictions below confidence threshold

High value = poor data quality affecting model.

------------------------------------------------------------------------

**5. Business‑Safe KPIs (Instead of Accuracy)**

When data is unreliable, ask:

“Is the business impact acceptable?”

**Examples:**

- % high‑risk predictions manually overridden

- % automated decisions rolled back

- Cost of wrong predictions

- SLA breach rate due to model output

------------------------------------------------------------------------

**🚫 KPIs to Avoid When Data Quality Is Poor**

❌ Raw Accuracy\
❌ R² alone\
❌ Precision/Recall without context\
❌ Optimised metrics on noisy labels

**Why:**\
They give a **false sense of performance**.

------------------------------------------------------------------------

**✅ KPI Selection Summary (Cheat Sheet)**

| **Situation**               | **Recommended KPI**          |
|-----------------------------|------------------------------|
| Poor data quality           | MAE, Median Error            |
| Noisy labels                | Stability trends             |
| Missing / inconsistent data | Drift KPIs (PSI, KS)         |
| Low trust inputs            | Confidence & coverage        |
| Production monitoring       | Accuracy + drift + stability |

------------------------------------------------------------------------

**✅ Final 30‑Second Interview Answer**

“When data quality is poor, I don’t rely on accuracy alone because it becomes misleading. I prioritise robust metrics like MAE or median error, monitor performance stability over time, track data and prediction drift using PSI or distribution checks, and use confidence‑based KPIs to understand reliability. Accuracy is reviewed only in combination with these signals.”

------------------------------------------------------------------------

# select and apply the most effective/appropriate AI and data science techniques to solve complex business problems

------------------------------------------------------------------------

**1) Start with the business problem (not the model)**

**What I do**

- Clarify the **decision** the business needs to make and **who** will use it.

- Convert the problem into a measurable objective:

  - *Reduce cost? Improve SLA compliance? Detect risk earlier? Increase conversion?*

- Define **success KPIs** and constraints:

  - Accuracy targets, latency, interpretability, regulatory/compliance, cost, operational effort.

**Interview phrasing**

“I start by translating the business objective into a measurable ML objective, with clear KPIs and constraints—because the ‘best model’ is the one that meets the business outcome reliably.”

------------------------------------------------------------------------

**2) Diagnose whether AI/ML is even needed**

Before choosing techniques, I run a quick “fit check”:

**Use rules/automation (non‑ML) when:**

- Logic is stable and explicit (e.g., policy rules)

- High auditability is required

- Data is sparse, noisy, or labels are missing

**Use analytics/BI when:**

- Need insight and reporting (dashboards, trends)

- Not required to predict, classify, or optimise decisions

**Use ML/AI when:**

- Pattern is complex or non‑linear

- Scale is large (too many cases for humans)

- Predictions/segmentation are needed and data exists (or can be generated)

**Interview phrasing**

“I don’t force ML. If a rules engine or BI solves it with lower risk and cost, that’s the right choice.”

------------------------------------------------------------------------

**3) Frame the problem into the right ML task type**

I map the business question to an ML formulation:

**Common mappings**

- **Forecasting / numerical estimate** → *Regression* (e.g., time-to-resolve, demand)

- **Yes/No decision** → *Binary classification* (e.g., churn, fraud)

- **Multiple categories** → *Multi-class classification* (e.g., ticket routing)

- **Group similar items** → *Clustering* (e.g., incident patterns)

- **Find unusual behaviour** → *Anomaly detection* (e.g., security, outages)

- **Recommend next best action** → *Recommenders*

- **Optimise sequential decisions** → *Reinforcement learning* (less common in enterprises)

------------------------------------------------------------------------

**4) Assess data readiness (this drives technique choice)**

This is where many projects succeed/fail.

**I check:**

- **Availability**: Do we have enough history? Are features accessible?

- **Quality**: missingness, duplicates, outliers, inconsistent definitions

- **Label quality**: correctness, bias, timeliness (for supervised ML)

- **Leakage risks**: features that “know the future”

- **Freshness**: does data change quickly? drift risk?

**If data quality is poor:**

I prioritise:

- **robust methods** (e.g., tree ensembles)

- **simple baselines**

- **data quality KPIs + drift monitoring**

- **human-in-the-loop** workflows for high risk decisions

**Interview phrasing**

“My technique selection is data-driven: data quality and label reliability often decide whether we use supervised learning, weak supervision, or unsupervised methods.”

------------------------------------------------------------------------

**5) Build a baseline first (fast, interpretable, measurable)**

I always create a **baseline** before advanced AI:

- **Naïve baseline** (e.g., last value / simple rules)

- **Simple statistical model** (linear/logistic regression)

- **Basic tree model**

Why?

- Confirms feasibility

- Sets a performance floor

- Helps stakeholders understand improvement

------------------------------------------------------------------------

**6) Choose models using a decision matrix (performance vs constraints)**

**A practical selection guide**

**If interpretability is critical:**

- Linear/logistic regression

- Decision trees

- Explainable boosting (where available)

- Post-hoc explainability (SHAP) for ensembles

**If performance is primary and data is tabular:**

- Random Forest, Gradient Boosting (XGBoost/LightGBM/CatBoost)

**If text is central (emails, tickets, documents):**

- NLP embeddings + classifier

- Transformer models (where needed)

- Retrieval‑augmented methods for knowledge tasks

**If images/video:**

- CNNs / Vision Transformers

**If time series:**

- ARIMA/Prophet (baseline), gradient boosting with lag features

- LSTM/Transformers if complex patterns and scale justify

**If labels are limited:**

- Semi-supervised learning

- Self-supervised feature learning

- Active learning (label the most informative samples)

- Clustering + human validation to bootstrap labels

**Interview phrasing**

“I select the simplest model that meets performance, latency, interpretability, and governance needs—then only increase complexity if the business benefit is clear.”

------------------------------------------------------------------------

**7) Validate properly (metrics aligned to business risk)**

**Metrics selection (examples)**

**Classification**

- **F1 / AUC** for imbalanced data

- **Precision** if false positives are costly (e.g., blocking users)

- **Recall** if false negatives are costly (e.g., security threats)

**Regression**

- **MAE** for robustness and interpretability

- **RMSE** when large errors are especially harmful

- **Map** for percentage error (if scale varies)

**Operational**

- latency, throughput, cost per prediction

- calibration (confidence reliability)

- fairness/bias checks where relevant

**Business**

- SLA improvement, cost reduction, deflection rate, MTTR impact

------------------------------------------------------------------------

**8) Make it production-ready (MLOps + monitoring)**

Complex problems fail if they don’t operationalise.

**What I implement**

- Feature pipelines (repeatable transformations)

- Model versioning and reproducibility

- Automated tests (data schema, missing rate, ranges)

- Deployment strategy (shadow, A/B, canary)

- Monitoring:

  - **Data drift** (PSI/KS/χ²)

  - **Prediction drift**

  - **Performance drift** (sliding window metrics)

- Retraining triggers and governance approvals

**Interview phrasing**

“I treat ML as a product: deployment, monitoring, and retraining are part of the solution, not afterthoughts.”

------------------------------------------------------------------------

**9) Manage stakeholders with a “value + risk” narrative**

To solve complex business problems, I keep stakeholders aligned with:

- **What decisions improve** (value)

- **What could go wrong** (risk)

- **How we control it** (governance, monitoring, fallback)

I also define:

- Human override paths

- Escalation policies when confidence is low

- Periodic model review cadence

------------------------------------------------------------------------

**A concise “STAR-style” interview answer (60–90 seconds)**

“I start by clarifying the business decision, defining measurable success KPIs, and checking whether ML is even required. I then map the problem to the right technique—regression, classification, clustering, anomaly detection, or NLP—based on the outcome needed. Next I assess data readiness and label quality, build a baseline model first, and then select models using a trade-off between performance, interpretability, latency, and governance. I validate using metrics aligned to business risk—precision/recall or MAE/RMSE—and I productionise with MLOps, drift monitoring, and retraining triggers. Finally, I ensure adoption with stakeholder alignment, explainability, and operational controls.”

------------------------------------------------------------------------

**Quick example (IT operations – to make it tangible)**

**Problem:** Reduce SLA breaches and speed up incident resolution\
**Approach:**

- Predict **resolution time** → regression (MAE/RMSE)

- Classify **likely breach** → classification (recall for high-risk, AUC)

- Cluster incidents → identify recurring patterns for problem management

- Monitor drift (PSI, performance trend) as processes and systems change

------------------------------------------------------------------------

# How do you disseminate AI and Data Science practices?

------------------------------------------------------------------------

**✅ 1. Establish Standard Frameworks and Guidelines**

**What I do:**

- Define **common methodologies** (e.g., ML lifecycle, model governance, ethical AI)

- Create **standard templates**:

  - Problem definition

  - Model evaluation

  - KPI dashboards

  - Documentation

**Why:**\
Ensures **consistency, quality, and auditability** across teams.

**Interview line:**

“I start by standardising AI practices through frameworks, guidelines, and reusable templates.”

------------------------------------------------------------------------

**✅ 2. Build Knowledge Sharing Mechanisms**

**a) Communities of Practice (CoP)**

- Create internal AI/data science forums

- Regular meetups or knowledge sessions

- Share:

  - Use cases

  - Lessons learned

  - Best practices

**b) Internal Documentation**

- Wikis (e.g., Confluence, SharePoint)

- Playbooks and case studies

- Code repositories (Git)

**Interview line:**

“I promote knowledge sharing through communities of practice, internal wikis, and reusable code repositories.”

------------------------------------------------------------------------

**✅ 3. Training & Enablement Programs**

**What I implement:**

- Role‑based training:

  - Business users → AI awareness

  - Engineers → ML techniques

  - Leaders → AI strategy & governance

- Hands‑on workshops and labs

**Why:**\
Bridges the gap between **data science teams and business users**.

**Interview line:**

“I ensure capability building through structured training programs tailored to different roles.”

------------------------------------------------------------------------

**✅ 4. Reusable Assets and Tooling**

**What I create:**

- Reusable ML pipelines

- Feature engineering libraries

- Prebuilt models / APIs

- Data quality and drift monitoring tools

**Outcome:**

- Faster delivery

- Reduced duplication

- Increased consistency

**Interview line:**

“I accelerate adoption by creating reusable assets and standard pipelines.”

------------------------------------------------------------------------

**✅ 5. Embed Governance and Best Practices**

**Key elements:**

- Model validation and approval process

- Bias and fairness checks

- Data privacy compliance

- Version control and audit trails

**Frameworks:**

- MLOps practices

- Responsible AI guidelines

**Interview line:**

“I embed governance into the lifecycle to ensure models are reliable, compliant, and auditable.”

------------------------------------------------------------------------

**✅ 6. Use Real Use Cases & Pilots**

**Approach:**

- Start with **high‑impact use cases**

- Deliver quick wins (PoCs → scaled solutions)

- Showcase outcomes:

  - Cost savings

  - SLA improvement

  - Automation benefits

**Why:**\
Real results drive **adoption faster than theory**.

**Interview line:**

“I demonstrate value through pilot use cases and scale successful solutions across the organisation.”

**✅ 7. Create Dashboards & Transparency**

**What I share:**

- Model performance dashboards

- Drift monitoring dashboards

- Business impact metrics

**Tools:**

- Power BI / Tableau

**Purpose:**

- Build **trust and transparency**

- Enable **data‑driven decisions**

------------------------------------------------------------------------

**✅ 8. Foster a Data‑Driven Culture**

**Cultural initiatives:**

- Encourage decision-making based on data

- Promote experimentation

- Reward data‑driven outcomes

**Leadership alignment:**

- Ensure senior stakeholders support AI adoption

------------------------------------------------------------------------

**✅ End‑to‑End Dissemination Flow**

Standards → Training → Tools/Assets → Use Cases → Governance → Scaling → Culture

------------------------------------------------------------------------

**✅ Final Interview Answer (30–40 seconds)**

“I disseminate AI and data science practices by establishing standard frameworks and governance, enabling teams through training and communities of practice, and providing reusable tools and pipelines. I promote adoption by delivering high‑impact use cases, sharing results through dashboards, and embedding AI into business processes. This ensures consistency, scalability, and a strong data‑driven culture.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“Standardise, enable, reuse, govern, and scale AI through training, tools, and real business use cases.”

------------------------------------------------------------------------

# How do you identify trends in the current AI landscape?

------------------------------------------------------------------------

**✅ 1. Track Industry Research & Publications**

**What I do:**

- Follow leading sources:

  - Research papers (arXiv, Google, OpenAI, DeepMind)

  - Industry reports (Gartner, McKinsey, Forrester)

- Identify:

  - Emerging techniques (e.g., LLMs, multimodal AI)

  - Shifts in adoption patterns

**Interview line:**

“I continuously track research papers and industry reports to understand emerging AI capabilities and adoption trends.”

------------------------------------------------------------------------

**✅ 2. Monitor Technology & Vendor Ecosystem**

**What I look at:**

- Major platform updates (Microsoft, AWS, Google)

- New product launches (Copilot, GPT, AI agents)

- Open‑source ecosystem (Hugging Face, LangChain)

**Why:**

Vendors often signal where the market is moving.

------------------------------------------------------------------------

**✅ 3. Analyse Enterprise Adoption Patterns**

**Focus areas:**

- Where AI is being used at scale:

  - Automation (RPA + AI)

  - Generative AI (content, coding, chatbots)

  - Predictive analytics (forecasting, risk)

**Example trends:**

- Shift from **ML models → Generative AI / LLMs**

- Rise of **AI copilots in business processes**

- Focus on **AI governance and responsible AI**

------------------------------------------------------------------------

**✅ 4. Use Data‑Driven Trend Analysis**

**Approach:**

- Analyse:

  - Job market demand (skills, roles)

  - Investment trends

  - AI adoption across industries

- Monitor:

  - Growth rates

  - Usage patterns

  - Benchmark improvements

------------------------------------------------------------------------

**✅ 5. Engage with Communities & Networks**

**What I do:**

- Participate in:

  - AI forums, LinkedIn, GitHub

  - Conferences (e.g., NeurIPS, industry events)

- Learn from:

  - Practitioner discussions

  - Real-world challenges and solutions

------------------------------------------------------------------------

**✅ 6. Observe Business Use Case Evolution**

**Key insight:**

Trends are best identified through **real problem-solving patterns**

**Examples:**

- Shift from **descriptive analytics → predictive → prescriptive**

- Move from **standalone models → integrated AI platforms**

- Growth of **AI in decision support (Copilots, assistants)**

------------------------------------------------------------------------

**✅ 7. Track Regulatory & Governance Trends**

**Important signals:**

- AI regulations (EU AI Act, data privacy laws)

- Ethical AI guidelines

- Enterprise compliance requirements

**Trend:**

Increasing focus on **trustworthy and explainable AI**

------------------------------------------------------------------------

**✅ 8. Validate Trends with Practical Experiments**

**What I do:**

- Build **PoCs and pilots**

- Test:

  - New models

  - New frameworks

- Evaluate:

  - Performance

  - Scalability

  - Business impact

------------------------------------------------------------------------

**✅ 9. Identify Technology Maturity**

Not all trends are actionable.

I assess:

- **Hype vs real adoption**

- Scalability

- Cost vs benefit

- Integration feasibility

------------------------------------------------------------------------

**✅ Current AI Trends (Example Talking Points)**

You can mention these in interviews:

- Generative AI and Large Language Models (LLMs)

- AI copilots embedded in enterprise workflows

- Multimodal AI (text + image + voice)

- AI agents and automation

- Responsible AI and governance

- Edge AI and real-time inference

------------------------------------------------------------------------

**✅ Final Interview Answer (30–40 seconds)**

“To identify trends in the AI landscape, I analyse research publications, track vendor innovations, and study enterprise adoption patterns. I also monitor data-driven indicators like investment and job trends, engage with industry communities, and validate insights through hands-on experiments. Importantly, I distinguish between hype and practical applicability by assessing business impact, scalability, and governance requirements.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“I identify AI trends by combining research insights, market adoption patterns, vendor developments, and hands-on experimentation to separate real value from hype.”

------------------------------------------------------------------------

# Common algorithms to know

------------------------------------------------------------------------

**1. Support Vector Machine (SVM)**

**✅ Core Idea**

Find a **decision boundary (hyperplane)** that **maximises the margin** between classes.

------------------------------------------------------------------------

**📐 Mathematical Formulation**

**Hyperplane:**

$$
w \cdot x + b = 0
$$

- $w$: weight vector

- $x$: input features

- $b$: bias

**Objective (Maximise Margin)**

Margin = distance between closest points (support vectors)

$$
\min\frac{1}{2} \mid \mid w \mid \mid^{2}
$$

Subject to:

$$
y_{i}(w \cdot x_{i} + b) \geq 1
$$

------------------------------------------------------------------------

**Key Concept**

- Only **support vectors** (boundary points) affect the decision boundary

------------------------------------------------------------------------

**✅ Example**

Classify emails: spam vs not spam

Data:

- Spam emails (feature: word “offer” frequency high)

- Not spam (low frequency)

SVM draws a **line (or hyperplane)** that separates the two with **maximum margin**.

------------------------------------------------------------------------

**✅ Interview One‑liner**

“SVM finds the optimal hyperplane that maximises the margin between classes using support vectors.”

------------------------------------------------------------------------

**2. Principal Component Analysis (PCA)**

**✅ Core Idea**

Reduce dimensions by finding **new axes (principal components)** that maximise variance.

------------------------------------------------------------------------

**📐 Mathematical Steps**

**Step 1: Standardise data**

------------------------------------------------------------------------

**Step 2: Compute covariance matrix**

$$
C = \frac{1}{n - 1}X^{T}X
$$

------------------------------------------------------------------------

**Step 3: Eigen decomposition**

$$
Cv = \lambda v
$$

- $v$: eigenvectors (directions)

- $\lambda$: eigenvalues (variance)

------------------------------------------------------------------------

**Step 4: Select top components**

Pick eigenvectors with **highest eigenvalues**

------------------------------------------------------------------------

**Step 5: Transform data**

$$
Z = XV
$$

------------------------------------------------------------------------

**✅ Example**

Dataset:

- Features: CPU usage, Memory, Disk

PCA:

- Combines into:

  - PC1 = “overall system load”

  - PC2 = “I/O vs compute difference”

------------------------------------------------------------------------

**✅ Interview One‑liner**

“PCA reduces dimensionality by projecting data onto directions of maximum variance using eigen decomposition.”

------------------------------------------------------------------------

**3. Apriori Algorithm**

**✅ Core Idea**

Find **frequent itemsets** and generate **association rules**.

------------------------------------------------------------------------

**📐 Key Metrics**

**(1) Support**

$$
Support(A) = \frac{\text{transactions~containing~A}}{\text{total~transactions}}
$$

------------------------------------------------------------------------

**(2) Confidence**

$$
Confidence(A \rightarrow B) = \frac{Support(A \cap B)}{Support(A)}
$$

------------------------------------------------------------------------

**(3) Lift**

$$
Lift(A \rightarrow B) = \frac{Confidence(A \rightarrow B)}{Support(B)}
$$

------------------------------------------------------------------------

**✅ Algorithm Steps**

1.  Generate frequent **1‑itemsets**

2.  Remove those below **minimum support**

3.  Generate **2‑itemsets**

4.  Repeat (Apriori property: subset must be frequent)

------------------------------------------------------------------------

**✅ Example (Market Basket)**

Transactions:

| **Basket**          |
|---------------------|
| Milk, Bread         |
| Milk, Bread, Butter |
| Bread, Butter       |

- Support(Milk, Bread) = 2/3

- Confidence(Milk → Bread) = 100%

------------------------------------------------------------------------

**✅ Interview One‑liner**

“Apriori finds frequent item combinations using support and generates association rules using confidence and lift.”

------------------------------------------------------------------------

**4. Naive Bayes**

**✅ Core Idea**

Uses **Bayes’ theorem** assuming **feature independence**

------------------------------------------------------------------------

**📐 Mathematical Formula**

$$
P(Y \mid X) = \frac{P(X \mid Y) \cdot P(Y)}{P(X)}
$$

Since $P(X)$is constant:

$$
P(Y \mid X) \propto P(X \mid Y) \cdot P(Y)
$$

------------------------------------------------------------------------

**Naive Assumption:**

$$
P(X \mid Y) = P(x_{1} \mid Y) \cdot P(x_{2} \mid Y) \cdot \ldots
$$

------------------------------------------------------------------------

**✅ Example (Spam Detection)**

Features:

- x₁ = “offer”

- x₂ = “free”

$$
P(Spam \mid X) \propto P(offer \mid Spam) \cdot P(free \mid Spam) \cdot P(Spam)
$$

Compare with:

$$
P(NotSpam \mid X)
$$

Pick the higher probability.

------------------------------------------------------------------------

**✅ Interview One‑liner**

“Naive Bayes applies Bayes’ theorem with independence assumptions to compute class probabilities efficiently.”

------------------------------------------------------------------------

**✅ Final Comparison (Quick Recall)**

| **Algorithm** | **Core Maths Idea**   | **Type**                 |
|---------------|-----------------------|--------------------------|
| SVM           | Max margin hyperplane | Classification           |
| PCA           | Eigen decomposition   | Dimensionality reduction |
| Apriori       | Support & confidence  | Association rules        |
| Naive Bayes   | Bayes theorem         | Classification           |

------------------------------------------------------------------------

**✅ Final 30‑Second Interview Answer**

“SVM maximises the margin between classes using support vectors, PCA reduces dimensionality using eigen decomposition, Apriori identifies frequent itemsets using support and confidence, and Naive Bayes uses Bayes’ theorem with independence assumptions to calculate class probabilities.”

------------------------------------------------------------------------

# Hyperparameter tuning

------------------------------------------------------------------------

**✅ What is Hyperparameter Tuning?**

**Hyperparameter tuning** is the process of **selecting the best set of configuration parameters (hyperparameters)** for a machine learning model to achieve **optimal performance**.

------------------------------------------------------------------------

**✅ Key Idea**

- **Model parameters** → learned automatically during training (e.g., weights)

- **Hyperparameters** → set **before training** and control how the model learns

------------------------------------------------------------------------

**✅ Examples of Hyperparameters**

| **Algorithm**     | **Hyperparameters**                         |
|-------------------|---------------------------------------------|
| Linear Regression | Regularisation (λ)                          |
| Decision Tree     | Max depth, min samples split                |
| Random Forest     | Number of trees, max features               |
| SVM               | Kernel type, C (regularisation)             |
| Neural Network    | Learning rate, batch size, number of layers |

------------------------------------------------------------------------

**✅ Why Hyperparameter Tuning is Important**

- Improves **accuracy and generalisation**

- Prevents **overfitting / underfitting**

- Optimises model performance for real‑world data

------------------------------------------------------------------------

**✅ How Hyperparameter Tuning Works**

**Step‑by‑Step**

1.  **Choose hyperparameters to tune**\
    (e.g., number of trees, learning rate)

2.  **Define value ranges**

    - Example: learning rate = 0.001, 0.01, 0.1

3.  **Train model on different combinations**

4.  **Evaluate using validation data**

    - Metrics: Accuracy, F1, RMSE

5.  **Select best combination**

------------------------------------------------------------------------

**✅ Common Tuning Techniques**

**1. Grid Search**

- Tries **all possible combinations**

- Accurate but computationally expensive

------------------------------------------------------------------------

**2. Random Search**

- Samples random combinations

- Faster and often equally effective

------------------------------------------------------------------------

**3. Bayesian Optimisation (Advanced)**

- Uses previous results to **choose smarter combinations**

- Efficient for complex models

------------------------------------------------------------------------

**✅ Example**

**Problem: Predict incident resolution time**

- Model: Random Forest

- Hyperparameters:

  - Trees: 100, 200, 300

  - Max depth: 5, 10, 15

Test combinations like:

- (100 trees, depth 5)

- (200 trees, depth 10)

Select the one with **lowest RMSE**

------------------------------------------------------------------------

**✅ Interview One‑Liner**

“Hyperparameter tuning is the process of optimising model settings such as learning rate or tree depth to improve performance using techniques like grid search or random search.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“Hyperparameters control how a model learns, and tuning them improves accuracy and generalisation.”

------------------------------------------------------------------------

**✅ Key Interview Tip**

You can add:

“I use cross‑validation during tuning to ensure the model generalises well to unseen data.”

------------------------------------------------------------------------

# Definition of SVM (Support Vector Machine)

------------------------------------------------------------------------

**Support Vector Machine (SVM)** is a **supervised machine learning algorithm** used for **classification and regression**, which works by finding the **optimal hyperplane that separates data into different classes with maximum margin**.

------------------------------------------------------------------------

**✅ Key Idea**

- SVM identifies a **decision boundary (hyperplane)** that best separates the data

- It chooses the boundary that **maximises the margin** between classes

- Only **critical data points (support vectors)** influence the model

------------------------------------------------------------------------

**✅ Mathematical Definition**

The decision boundary is given by:

$$
w \cdot x + b = 0
$$

SVM optimises:

$$
\min\frac{1}{2} \mid \mid w \mid \mid^{2}\text{subject~to }y_{i}(w \cdot x_{i} + b) \geq 1
$$

- $w$: weight vector

- $b$: bias

- $y_{i}$: class label (+1 or −1)

------------------------------------------------------------------------

**✅ Types of SVM**

- **Linear SVM** → linear separation

- **Non‑linear SVM** → uses kernels (e.g., polynomial, RBF)

------------------------------------------------------------------------

**✅ Simple Example**

- Classify emails as **Spam vs Not Spam**

- SVM finds a boundary that separates the two classes with **maximum distance from nearest points**

------------------------------------------------------------------------

**✅ Interview One‑Liner**

“SVM is a supervised learning algorithm that finds the optimal hyperplane to separate classes by maximising the margin between them using support vectors.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“SVM separates data by maximising the margin between classes using the most important boundary points called support vectors.”

# ✅ Activation Functions in Neural Networks

Activation functions convert the neuron output $z$into a **non‑linear output**, enabling neural networks to learn **complex patterns**.

$$
a = f(z)
$$

------------------------------------------------------------------------

**1. Sigmoid Function**

**✅ Definition**

$$
\sigma(z) = \frac{1}{1 + e^{- z}}
$$

**✅ Output Range**

$$
\left( 0,1 \right)
$$

------------------------------------------------------------------------

**✅ Characteristics**

- S‑shaped curve

- Outputs can be interpreted as **probabilities**

- Smooth and differentiable

------------------------------------------------------------------------

**✅ Problems**

- **Vanishing gradient** (for large positive/negative values)

- Slow training in deep networks

------------------------------------------------------------------------

**✅ Use Cases**

- Output layer in **binary classification**

------------------------------------------------------------------------

**✅ Example**

If input $z = 2$:

$$
\sigma(2) \approx 0.88
$$

------------------------------------------------------------------------

**✅ Interview One‑liner**

“Sigmoid squashes input into a probability value between 0 and 1.”

------------------------------------------------------------------------

**2. ReLU (Rectified Linear Unit)**

**✅ Definition**

$$
ReLU(z) = \max(0,z)
$$

------------------------------------------------------------------------

**✅ Output Range**

$$
\lbrack 0,\infty)
$$

------------------------------------------------------------------------

**✅ Characteristics**

- Simple and computationally efficient

- Sparse activation (many zeros)

- Avoids vanishing gradient for positive inputs

------------------------------------------------------------------------

**✅ Problems**

- **Dying ReLU** (neuron outputs always 0 if $z \leq 0$)

------------------------------------------------------------------------

**✅ Use Cases**

- Most common for **hidden layers in deep networks**

------------------------------------------------------------------------

**✅ Example**

- $z = 3$→ Output = 3

- $z = - 2$→ Output = 0

------------------------------------------------------------------------

**✅ Interview One‑liner**

“ReLU outputs the input if positive, otherwise zero, making training faster and more efficient.”

**3. Tanh (Hyperbolic Tangent)**

**✅ Definition**

$$
\tanh(z) = \frac{e^{z} - e^{- z}}{e^{z} + e^{- z}}
$$

------------------------------------------------------------------------

**✅ Output Range**

$$
( - 1,1)
$$

------------------------------------------------------------------------

**✅ Characteristics**

- Zero‑centred (better than sigmoid)

- Stronger gradients than sigmoid

- Still suffers from vanishing gradient

------------------------------------------------------------------------

**✅ Use Cases**

- Hidden layers (sometimes used instead of sigmoid)

------------------------------------------------------------------------

**✅ Example**

- $z = 2$→ Output ≈ 0.96

- $z = - 2$→ Output ≈ -0.96

------------------------------------------------------------------------

**✅ Interview One‑liner**

“Tanh maps inputs between −1 and 1 and is zero‑centred, making it better than sigmoid for hidden layers.”

------------------------------------------------------------------------

**✅ Comparison (Very Important for Interviews)**

| **Feature**        | **Sigmoid**  | **Tanh**     | **ReLU**     |
|--------------------|--------------|--------------|--------------|
| Range              | (0, 1)       | (-1, 1)      | \[0, ∞)      |
| Zero‑centred       | ❌ No        | ✅ Yes       | ❌ No        |
| Vanishing gradient | ❌ Yes       | ❌ Yes       | ✅ Less      |
| Speed              | Slow         | Medium       | Fast         |
| Usage              | Output layer | Hidden layer | Hidden layer |

------------------------------------------------------------------------

**✅ When to Use What**

- **Sigmoid** → Binary classification output

- **Tanh** → Hidden layers (better than sigmoid)

- **ReLU** → Preferred for deep learning (default choice)

------------------------------------------------------------------------

**✅ Final Interview Answer (30 seconds)**

“Sigmoid maps outputs between 0 and 1 and is mainly used for binary classification, tanh maps values between −1 and 1 and is zero‑centred, while ReLU outputs zero for negative inputs and linear for positive inputs, making it the most efficient and widely used activation function in deep neural networks.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

- **Sigmoid:** Probability (0 to 1)

- **Tanh:** Zero‑centred (−1 to 1)

- **ReLU:** Fast, efficient, most commonly used

------------------------------------------------------------------------

# What is Softmax?

**Softmax** is an **activation function** used in neural networks to convert raw outputs (logits) into **probabilities across multiple classes**.

------------------------------------------------------------------------

**✅ Mathematical Definition**

For a vector $z = \lbrack z_{1},z_{2},...,z_{n}\rbrack$:

$$
\text{Softmax}(z_{i}) = \frac{e^{z_{i}}}{\sum_{j = 1}^{n}e^{z_{j}}}
$$

------------------------------------------------------------------------

**✅ Key Properties**

- Outputs are **probabilities between 0 and 1**

- Sum of all outputs = **1**

- Emphasises the **largest values**

- Used for **multi-class classification**

------------------------------------------------------------------------

**✅ How It Works (Intuition)**

1.  Apply **exponential** to each input → ensures positivity

2.  Normalize by dividing by the sum → gives a **probability distribution**

------------------------------------------------------------------------

**✅ Example**

Suppose a model outputs:

$$
z = \lbrack 2,1,0.1\rbrack
$$

**Step 1: Apply exponential**

$$
e^{2} = 7.39,e^{1} = 2.72,e^{0.1} = 1.105
$$

**Step 2: Sum**

$$
7.39 + 2.72 + 1.105 = 11.215
$$

**Step 3: Softmax output**

$$
\left\lbrack 0.66,\text{\:\,}0.24,\text{\:\,}0.10 \right\rbrack
$$

✅ These now represent **probabilities of 3 classes**

------------------------------------------------------------------------

**✅ Where Softmax is Used**

- **Output layer of neural networks**

- **Multi-class classification**

  - Image classification

  - Text classification

  - Speech recognition

------------------------------------------------------------------------

**✅ Softmax vs Sigmoid**

| **Feature** | **Softmax**            | **Sigmoid**           |
|-------------|------------------------|-----------------------|
| Output      | Multiple probabilities | Single probability    |
| Sum         | = 1                    | Not constrained       |
| Use         | Multi-class            | Binary classification |

------------------------------------------------------------------------

**✅ Interview One‑Liner**

“Softmax converts raw model outputs into a probability distribution across multiple classes, where all probabilities sum to 1.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“Softmax turns model outputs into class probabilities for multi-class classification.”

------------------------------------------------------------------------

**✅ Key Interview Tip**

You can add:

“Softmax is usually used with cross‑entropy loss for training multi-class classification models.”

------------------------------------------------------------------------

# Will AI remove jobs?

------------------------------------------------------------------------

Yes — **AI will remove *some* jobs**, but it’s more accurate to say **AI will change jobs (tasks) faster than it eliminates whole occupations**. The net effect depends on **how quickly organisations adopt AI**, **which tasks are automatable**, and **how well people and companies reskill and redesign work**. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)

------------------------------------------------------------------------

**1) What credible research says (big picture)**

**Jobs will be both created and displaced**

The World Economic Forum (WEF) projects that structural labour‑market transformation will involve **both job creation and displacement** by 2030, with **170 million roles created** and **92 million displaced** (net +78 million), highlighting that transitions are large even if net numbers are positive. [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)

**A large share of jobs will be “affected”**

The IMF estimates **almost 40% of global employment is exposed to AI**, with higher exposure in advanced economies (about **60%**), and notes the impact can be **replacement for some tasks/jobs** and **productivity complementarity for others**. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf)

**GenAI mostly transforms tasks, especially in clerical work**

The ILO’s refined exposure work notes **“one in four workers”** are in occupations with **some** exposure to generative AI, and that **clerical occupations** remain among the most exposed; it emphasises **job transformation** as the most likely impact because jobs are bundles of tasks requiring human input. [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)

**Bottom line:** The best evidence suggests **significant disruption**, but not a simple “AI replaces everyone” story. It’s **task reallocation + new work creation + some job displacement**. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/), [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)

------------------------------------------------------------------------

**2) Why AI removes some jobs but not all jobs**

**AI automates tasks, not whole roles (most of the time)**

Most jobs combine:

- routine tasks (easier to automate),

- judgment/context tasks (harder),

- people-facing and accountability tasks (often required by policy/compliance). [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)

So organisations often:

- **remove/automate parts of a role**,

- then **redesign the role** (more analysis, oversight, stakeholder work),

- and sometimes **reduce headcount** where workload shrinks. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)

------------------------------------------------------------------------

**3) Which jobs are most at risk (and why)**

**Higher risk characteristics**

Jobs are more exposed when they involve:

- **high volumes of repeatable digital work**

- **standardised outputs**

- **low requirement for physical presence**

- **limited need for nuanced accountability** [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure), [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf)

The WEF highlights expected declines in **clerical and administrative roles** (e.g., data entry, clerical support) and similar routine information-processing work.\
The ILO also points to clerical work as especially exposed to GenAI capabilities. [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/) [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)

**Lower risk characteristics**

Jobs are typically less exposed when they require:

- complex human interaction (care, negotiation, leadership),

- physical work in unstructured environments,

- high-stakes accountability and regulated decisions. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)

------------------------------------------------------------------------

**4) What happens to people: “displacement” vs “augmentation”**

A useful way to explain this in interviews:

**Displacement**

- AI replaces a sufficient portion of tasks that the organisation needs **fewer people** in that function.\
  This is more likely for highly routine digital work. [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/), [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf)

**Augmentation**

- AI makes people faster/better, so the job shifts to **higher-value tasks** (review, judgment, stakeholder handling).\
  This is what many exposure studies expect to be common in practice. [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure), [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf)

------------------------------------------------------------------------

**5) So… will AI “remove people from jobs”?**

**A balanced answer**

- **Yes, some roles will shrink or disappear**, especially where work is routine and digitally standardised. [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/), [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)

- **Many more roles will be redesigned**, with AI doing the first draft/triage and humans doing decision-making, governance, and exception handling. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[ilo.org\]](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)

- The biggest risk is not “AI vs people,” but **people with AI skills vs people without**, because productivity and employability will diverge. [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)

------------------------------------------------------------------------

**6) Practical guidance (what to do about it)**

**For individuals (career resilience)**

Focus on skills that are repeatedly identified as rising in importance:

- **analytical thinking**

- **AI/data literacy**

- **cybersecurity/technology literacy**

- **creative problem solving**

- **communication and stakeholder management** [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/), [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf)

**For organisations (to avoid “replacement shock”)**

- Treat AI as **work redesign**, not just automation.

- Invest in **reskilling/upskilling** and **internal mobility** because skill shifts are large and ongoing. [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/), [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf)

------------------------------------------------------------------------

**Interview-ready 20‑second answer**

“AI will remove some jobs, especially routine digital roles, but more often it will **change jobs** by automating tasks and augmenting people. Research suggests large disruption: the IMF estimates ~40% of jobs are exposed to AI, while the WEF expects both job creation and displacement through 2030. The key is reskilling and redesigning work so humans focus on judgment, accountability, and complex problem solving.” [\[imf.org\]](https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf), [\[weforum.org\]](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)

------------------------------------------------------------------------

# Impact of AI on Industry and Society

AI is having a **transformational impact** across both **industries** (how businesses operate) and **society** (how people live and work). The impact is **mixed**—bringing significant benefits along with important risks.

------------------------------------------------------------------------

**✅ 1. Impact on Industry**

**🔹 a) Productivity & Efficiency Gains**

- AI automates **repetitive and data‑intensive tasks**

- Improves speed, accuracy, and consistency

- Enables **real‑time decision‑making**

👉 Result:

- Higher productivity and lower operational costs

- Faster service

------------------------------------------------------------------------

**Risks of Adopting AI in an Organisation**

Adopting AI brings significant value, but it also introduces **technical, operational, ethical, and business risks** that must be actively managed.

------------------------------------------------------------------------

**✅ 1. Data Risks (High Impact)**

**🔹 Poor Data Quality**

- Inaccurate, incomplete, or biased data → **wrong predictions**

- “Garbage in → garbage out”

**🔹 Data Privacy & Security**

- Exposure of **sensitive data (PII, client data)**

- Risk of violating **GDPR / compliance regulations**

**Example:**\
Using AI on employee or customer data without proper controls → compliance breach

------------------------------------------------------------------------

**✅ 2. Model Risks**

**🔹 Bias and Fairness Issues**

- AI may learn **biased patterns** from historical data

- Leads to unfair or discriminatory decisions

**🔹 Lack of Explainability**

- Complex models (e.g., neural networks) behave like **black boxes**

- Difficult to justify decisions to clients, auditors, regulators

------------------------------------------------------------------------

**✅ 3. Operational Risks**

**🔹 Model Drift**

- Data changes over time → model accuracy drops

- If not monitored → poor decisions

**🔹 Reliability & Performance**

- AI systems may:

  - Produce inconsistent outputs

  - Fail under edge cases

  - Have latency issues in real-time systems

------------------------------------------------------------------------

**✅ 4. Business Risks**

**🔹 Wrong Decision Impact**

- AI errors can:

  - Misclassify critical incidents

  - Make incorrect predictions

  - Impact SLAs and customer experience

**🔹 Overdependence on AI**

- Teams may rely too much on AI outputs without validation

- Reduces human oversight and accountability

------------------------------------------------------------------------

**✅ 5. Security Risks (Critical)**

**🔹 Adversarial Attacks**

- Attackers manipulate inputs to fool AI models

**🔹 Data Poisoning**

- Malicious data injected during training → corrupt model

------------------------------------------------------------------------

**✅ 6. Compliance & Governance Risks**

- Regulatory non‑compliance (GDPR, AI regulations)

- Lack of audit trail

- No model approval or validation process

------------------------------------------------------------------------

**✅ 7. Skills & Adoption Risks**

**🔹 Skill Gap**

- Lack of:

  - Data scientists

  - AI engineers

  - AI governance expertise

**🔹 Resistance to Change**

- Employees may:

  - Not trust AI outputs

  - Resist new workflows

------------------------------------------------------------------------

**✅ 8. Financial Risks**

- High implementation cost

- Unclear ROI if use case not well defined

- Maintenance and retraining costs

------------------------------------------------------------------------

**✅ 9. Ethical & Societal Risks**

- Job displacement concerns

- Misuse of AI (automation without control)

- Loss of human accountability

------------------------------------------------------------------------

**✅ How to Mitigate These Risks (Strong Interview Add‑On)**

You should always mention mitigation (this differentiates strong candidates):

✅ Data governance (quality checks, access control)\
✅ Model validation & explainability tools (SHAP, LIME)\
✅ Continuous monitoring (drift, performance KPIs)\
✅ Human‑in‑the‑loop decision making\
✅ Security controls (data protection, adversarial testing)\
✅ AI governance framework (approval, audit, compliance)\
✅ Training and change management

------------------------------------------------------------------------

**✅ IT Operations Example (Very Relevant for You)**

If AI is used for:

- Incident prediction

- Ticket classification

**Risks:**

- Wrong priority classification → SLA breach

- Drift → inaccurate predictions over time

- Over-reliance by service desk

**Mitigation:**

- Confidence thresholds

- Manual override for critical cases

- Continuous monitoring dashboards

------------------------------------------------------------------------

**✅ Final Interview Answer (30–40 seconds)**

“The main risks of adopting AI include data quality and privacy issues, model bias and lack of explainability, operational risks like model drift, and business risks where incorrect predictions impact decisions. There are also security and compliance risks, along with skill and adoption challenges. These risks can be mitigated through strong data governance, model validation, continuous monitoring, and human oversight.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“AI risks include data issues, bias, lack of explainability, model drift, and business impact, which must be managed through governance, monitoring, and human oversight.”

------------------------------------------------------------------------

# Why Do We Use Unsupervised Learning?

We use **unsupervised learning when we don’t have labelled data** and want to **discover hidden patterns or structure** in data.

**Key reasons:**

**🔹 1. No Labels Available**

- Data does not have predefined outputs

- Manual labelling is **expensive or impossible**

👉 Example:

- No labels for customer segments → use clustering

------------------------------------------------------------------------

**🔹 2. Data Exploration (First Step)**

- Helps understand:

  - Structure of data

  - Relationships between variables

- Often used during **EDA (Exploratory Data Analysis)**

------------------------------------------------------------------------

**🔹 3. Pattern Discovery**

- Identify **groups, trends, or associations** that are not obvious

------------------------------------------------------------------------

**🔹 4. Feature Learning / Dimensionality Reduction**

- Reduce complexity (PCA)

- Identify **important features**

------------------------------------------------------------------------

**🔹 5. Anomaly / Outlier Detection**

- Detect unusual behaviour

- Useful for fraud, security, or system failures

------------------------------------------------------------------------

**✅ One‑line reason**

“We use unsupervised learning to discover hidden patterns in data when labelled outputs are not available.”

------------------------------------------------------------------------

**✅ 2. What Do We Find in Unsupervised Learning?**

Unsupervised learning helps uncover **four major things**:

------------------------------------------------------------------------

**🔹 1. Clusters (Grouping Similar Data)**

**What you find:**

- Natural groupings of data points based on similarity

**Example:**

- Group customers based on behaviour

- Group incidents based on patterns

------------------------------------------------------------------------

**🔹 2. Relationships / Associations**

**What you find:**

- Items or variables that frequently occur together

**Example (Apriori):**

- Customers who buy **laptop → also buy mouse**

------------------------------------------------------------------------

**🔹 3. Data Structure & Patterns**

**What you find:**

- Hidden structures

- Data distribution patterns

**Example:**

- Seasonality in demand

- Behaviour patterns in logs

------------------------------------------------------------------------

**🔹 4. Anomalies / Outliers**

**What you find:**

- Unusual or rare observations

**Example:**

- Cybersecurity threats

- Sudden spike in system errors

------------------------------------------------------------------------

**🔹 5. Reduced Dimensional Representation**

**What you find:**

- Key underlying factors (via PCA)

**Example:**

- Combine CPU, memory, disk into “system load” metric

------------------------------------------------------------------------

**✅ 3. Simple Example (Very Interview‑Friendly)**

**Problem:**

You have customer data but no labels

**Apply:**

- K‑Means clustering

**Output:**

- Segment customers into:

  - High-value

  - Medium-value

  - Low-value

👉 Insight:

- Target marketing strategies

------------------------------------------------------------------------

**✅ 4. Real‑World IT Operations Example (Important for you)**

**Use Case:**

Incident Management

**Apply clustering to:**

- Group incidents by:

  - Category

  - Resolution time

  - System affected

**Find:**

- Repeated failure patterns

- Root causes

- Noise alerts

------------------------------------------------------------------------

**✅ 5. Summary Table**

| **Why we use it** | **What we find**  |
|-------------------|-------------------|
| No labelled data  | Clusters (groups) |
| Explore data      | Relationships     |
| Discover patterns | Hidden structures |
| Reduce complexity | Key features      |
| Detect anomalies  | Outliers          |

------------------------------------------------------------------------

**✅ Final Interview Answer (30 seconds)**

“We use unsupervised learning when labelled data is not available, primarily to explore and understand the data. It helps us discover hidden patterns such as clusters, relationships, and anomalies. For example, clustering can segment customers or incidents, association rules can identify relationships between variables, and anomaly detection can highlight unusual behaviour.”

------------------------------------------------------------------------

**✅ Ultra‑Short Version**

“Unsupervised learning is used to find hidden patterns like clusters, relationships, and anomalies in unlabeled data.”

------------------------------------------------------------------------
