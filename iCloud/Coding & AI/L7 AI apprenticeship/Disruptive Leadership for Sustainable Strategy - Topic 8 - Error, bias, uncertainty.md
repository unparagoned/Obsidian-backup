
[Marr, B. (2022) Data Strategy: How to Profit from a World of Big Data, Analytics and Artificial Intelligence, Kogan Page (Chapter 11)](https://www.vlebooks.com/Product/Index/2510818), available at VleBooks.


AI is becoming capable of making decisions rather than just doing repetitive tasks.

Amazon uses AI to decide who to fire.

Automated systems can make it hard to figure out what's going on or change things, e.g. contractor was locked out and no one knew what was happening or let him into the office.

GAN result in deepfakes

Social media algorithms can lock people into echo chambers, e.g. conspiracy content

Transparency is a key requirement of the OECD's principles for AI

Carbon footprint of AI

## Data quality

Quality is a standard of metrics to assess how fit data is for what you want. 

- Consistency, so the data in a dataset is recorded and collected the same way. Fields should be used the same way across every record.
- Accuracy, error-free. Measurement devices and human data entry.
- Uniqueness, no duplicate entries. Recording the same data multiple times in multiple places and result in errors.
- Validity is it fit for intended use. Are dates the right format, are figures stored the same way
- Timeliness is the data relevant to the time it was collected. e.g. glaciers only need to monitored occasionally, but position of protons need to be measured to the millionth of a second.
- Completeness, How much of the total data is captured. 

## Data bias

- Data that is not truly representative. Maybe due to how the data was collected. 
- Facial recognition works worse for black people.
- Amazon stopped using it for recruitment since it was sexist. 

## Personal data
- Data minimalization

Homomorphic encryptions allows you to process that data without decrypting it

Masking would replace a city with another city, but only those with permissions can get back the original data.

Tokenisation replaces sensitive data and isn't derived from the original data

If using bluetooth or rfid to capture data from mobiles you need to ensure agreements in place about how you will use that data.






The above chapter on “Data governance, ethics, and trust” is only tangentially related to this week’s topic but it is an important chapter to read and should help you with ideas for Question 3 of the technical test and general knowledge regarding AI ethics which should be helpful for the professional discussion.

It is strongly advised that you read the recommended module reading list to ensure you have covered the learning outcomes fully. However, it is not compulsory that you read everything.

Error is the difference between true and measured value

Error = | Vtrue - Vobserved |

Algorithms  try and minimise errors like mean absolute error(MAE), mean squared error(MSE) or root mean square error(RMSE) to calculate loss at each iteration. Often called the loss.

Random error is a chance difference between observed and true value. e.g. a researcher misreading a weighing scale or not enough resolution on the scale. 
- Includes missing values and transcribing error. 
- Can reduce them by taking repeated measurements, using a large sample and controlling extraneous variables.

Systematic error is consistent or proportional difference between observed and true values. e.g. scale measures things higher than they are. 
- Can also be a biased sample, e.g. person rates certain races lower
- Unrepresentative sample.
- Reduced through increased awareness, good experiment design, careful checking and calibration of instruments. 

Error in output of data collection is data error. 
- e.g. incorrect values, missing values, duplication, inconsistent representations

Error in output analysis is model error
- Results of ML. 
- Could be because of data err fed into analysis
- Insufficient data has been captured
- Sub-optimal feature set has been selected
- Sub-optimal model has been produced(overfitted, underfitted, wrong algorithm)

To ensure data is good quality, compare against other systems. Collect other systems

Incorrect tagging, no tagging. 

Yes, if there are no concepts for something then the training can't train for them and would incorrectly label stuff.

# Bias

Historical bias 
- If previously just white men got the jobs it might do that as well
- Bail amounts in the us depended on race

Sample bias
- Needs to be a representative sample. 
- Also separating by segment might be useful e.g. don't want to treat inner city same as countryside.
- Selection bias, How you choose the population. e.g. if you select reviews under 50 char.
- coverage bias is where the data source is incapable of reaching, property of source. e.g. analysing reviews - you are missing out everyone who didn't leave a review
- availability bias, e.g. online most stuff is english, so there isn't as much regional stuff

Aggregation bias
- If say you give an average for the country rather than county by county, could smooth out bad results

Confirmation bias

Stratified random sampling random sample based on a characteristic.

Recent research has been directed towards developing fairness tests for machine learning models. An overview of some recent tools is given in ([Chen et al, 2024](https://dl.acm.org/doi/pdf/10.1145/3652155)).

To mitigate bias
- Select training data that is representative of the whole population
- Check results for bias
- Apply fairness tests
- Continue to monitor ML systems in operational to ensure they continue to perform well and fairly

Bias can occur in the output of data collection e.g. inappropriate sampling or systematic error
Bias in the output of data analysis, bias from data collection or sub-optimal model
Data bias is bias in the data being input
Model bias refers to the systematic errors in the model. Data sources, bad models, selection of training data, choice of features used.


[Fairness Testing: A Comprehensive Survey and Analysis of Trends (acm.org)](https://dl.acm.org/doi/pdf/10.1145/3652155)

1. What points from the paper do you find most interesting?
    
2. Is fairness testing something that can be employed in your organisation?

- **X**: Input feature vector, excluding sensitive attributes. X⁽ⁱ⁾ denotes the feature vector for individual i.
- **A**: Sensitive attributes. A⁽ⁱ⁾ denotes the sensitive attributes for individual i.
- **Y**: Actual outcome.
- **Ŷ**: Predicted outcome. Ŷ(X⁽ⁱ⁾, A⁽ⁱ⁾) denotes the predicted outcome for individual i.
- **P(·)**: Probability function.
- F favourable outcome
- UF unfavourable outcome

**Fairness through unawareness** - if the model doesn't know about protected data the idea is that it would be fair.X(i) = X(j), then Y(X(i))=Y(X(j))

**Fairness through awareness.** The distance between predicted outcomes should be smaller than the distance between inputs. As in if inputs are similar so should outcomes. 
D(Y(X(i), A(i)), Y(X(j), A(j))) ≤ d((X(i), A(i)), (X(j), A(j)))

**Counterfactual fairness** individuals predictions should be the same in the real world from the counterfactual if it's sensitive and other data is changed. Changing sensitive data can change other data as well.
P(Ŷ(x, a) = y | X = x, A = a) = P(Ŷ(x′, a′) = y | X = x, A = a)

**Causal fairness** If you change a sensitive characteristic the predictions shouldn't change
There should be no j that meets this (1) X⁽ⁱ⁾ = X⁽ʲ⁾; (2) A⁽ⁱ⁾ ≠ A⁽ʲ⁾; (3) Ŷ(X⁽ⁱ⁾, A⁽ⁱ⁾) ≠ Ŷ(X⁽ʲ⁾, A⁽ʲ⁾)

Statistical party/demographic parity requires probability of favourable outcomes to be the same among different groups. Ignores variations in performance between groups.
P[Y^=F∣A=a]=P[Y^=F∣A=a′]

Equalised odds, requires the groups have the same true positive rates and false positive rates. May be hard to satisfy in practice
$$P[\hat{Y} = F \mid A = a,\ Y = y] = P[\hat{Y} = F \mid A = a',\ Y = y] \quad \text{for } y \in \{F, UF\}$$
Equal opportunity groups have equal true positive rates. May be hard to satisfy in practice. 

$$P[\hat{Y} = F \mid A = a,\ Y = F] = P[\hat{Y} = F \mid A = a',\ Y = F]$$

Fairness bug/ML bug is any imperfection in ML that causes a discordance between existing and required conditions.

Fairness testing anything that finds fairness bugs.
![[Pasted image 20260306094605.png]]

## Test input generation
- Random Test Input Generation
- Search-based Test Input Generation. 
	- Two-phased search based techniques. Casual fairness definition, altering sensitive attributes should not impact the outcomes
		- Global search phrase, search for sets of individual discriminatory instances
		- Local search phase, fine tun what's already been found.

### Metamorphic relations as Test Oracles
You can test that sin(x) == sin(pi + x), if that fails you know something is wrong.
It's a pseudo oracle
So you could change sensitive attributes and expect the same results.


### Statistical measurements as test oracles
Statistical parity difference(SPD) difference between favourable and unfavourable group
or Disparate Impact(DI) ratio of fav to unfav
Equal Opportunity Difference(EOD) measures the difference in true positive rates of the groups
Average Odds Difference(AOD) average of false positives difference and true positive difference of the UP and P groups

Measurements based on neuron activation. In DNN if two classes don't show similar distance with regard to third class that might be a fairness bug.

Measurements based on situations testing. Kind of k-nearest neighbours

Measurements based on optimal transport projections. Rankings

Measurements considering multiple subgroups. Check they are statistically different.

Test Oracle for Data testing. 
- Feature bias: If features correlate with sensitive attributes
- Label bias: Could train on different datasets and then see if the model makes different predictions. 
- Selection bias: association between sensitive attributes and labels in the training data

![[Pasted image 20260306154609.png]]

Testing hyper-parameters, want to maximise fairness while also minimising impact on performance

Can distil complex models down that can be run on wider range of systems and people

Black box model testing relies on statistical analysis

White box model testing, looks at the training data and internal structure

# Uncertainty

~~Uncertainty is the quantitive estimate of error present in data.~~
Lack of confidence in the data or outputs. Results from ML or analysis always have some uncertainty.

Sources of uncertainty include 
- variance in data(noisy data)
- representativeness of data(incomplete coverage)
- imperfect model

Aleatoric uncertainty - uncertainty that is always present due to underlying probilistic variability - randomness. e.g. a coin flip

Epistemic uncertainty - refers to lack of knowledge about a complex system. e.g. whether you answered a question correctly or not on an exam

Ontological uncertainty - concerns the degree of conceptual understanding of the "the world". e.g. covid, we didn't know transmission mechanism

Structural uncertainty - relates to the simplifications we make to derive a "concrete" representation of the world from our conceptual understanding e.g. climate models make simplifications

Deep uncertainty  - derives from the extent to which we can anticipate the nature of the problem space we will need to understand the future. e.g. climate change, depends on technology breakthroughs, geopolitical shifts, etc.

Noisy data occurs as there could be error in the recording of data. Could be human or instrument error. It is aleatoric uncertainty which persists after data quality checks and prep

Incomplete coverage is when the training data is incomplete. A random sample by chance might have picked biased observations. It is epistemic uncertainty that can be reduced by increasing training data.

Imperfect model. Imperfectly at earlier stages can propagate through the model. Imperfect choices or execution. e.g. creating a sample, selection of features, selection of algorithm, tuning of parameters. Can be both aleatory or epistemic

Mitigating uncertainty
- Prepare the data to remove as much potential error as possible
- Use a representative sample
- Experiment with a variety of algorithms
- Employ hyper-parameter tuning or cross validation.

# Quantifying and communicating uncertainty

For classification it would be confidence probability. 

For regression it would be predication variance

Standard errors and confidence intervals can be used to quantify uncertainty

SEM=SD√n

![[Pasted image 20260317145358.png]]

So would say the mean = mean +/- SEM

([HealthKnowedge, no date](https://www.healthknowledge.org.uk/index.php/public-health-textbook/research-methods/1b-statistical-methods/methods-quantification-uncertainty)).

You would run over 10 samples, then say 95 certain that the value is 1.96 sd from the mean.

Metrics 

MSE, MAE, RMSE, R2, etc.

You can also test variations of models/hyperparameters. If you tests variations and the results are all similar it means there is lower uncertainty than if there was high uncertainty.

## Monte Carlo Dropout

Basically has dropout at testing time to get a distribution

The technique for determining probability is usually an approximation of Bayesian inference ([Gal and Ghahramani, 2016](https://proceedings.mlr.press/v48/gal16.html)), although standard Gaussian approaches have also been shown to be effective ([Kristiani, Hein and Hennig, 2020](https://dl.acm.org/doi/10.5555/3524938.3525442)). An interesting article which discusses experimentation with Monte Carlo drop out is given at ([Vecsei, no date](https://gaborvecsei.com/Monte-Carlo-Dropout/)).

## Ensemble methods

Various models created. 

NN often provide a confidence

Many neural networks now output a confidence rating with a prediction. However, research has shown that deep learning tends to be over-confident ([Meronen et al, 2024, Moon et al., 2020](https://openaccess.thecvf.com/content/WACV2024/papers/Meronen_Fixing_Overconfidence_in_Dynamic_Neural_Networks_WACV_2024_paper.pdf)) and sometimes inaccurate even with Monte Carlo Dropout applied ([Verdoja and Kyrki, 2021](https://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-097.pdf)).

. Efforts are being made by researchers to calibrate confidence ratings for greater accuracy in relation to prediction correctness ([Wang, 2021](https://proceedings.neurips.cc/paper_files/paper/2021/file/61f3a6dbc9120ea78ef75544826c814e-Paper.pdf)).

Tensorflow Probability is an extension which has many of these functionalities.

### Recommended reading

[Marr, B. (2022) Data Strategy: How to Profit from a World of Big Data, Analytics and Artificial Intelligence, Kogan Page (Chapter 11)](https://www.vlebooks.com/Product/Index/2510818) | VLeBooks.

The above chapter on **Data governance, ethics, and trust** is only tangentially related to this week’s topic but it is an important chapter to read and should help you with ideas for Question 3 of the technical test and general knowledge regarding AI ethics which should be helpful for the professional discussion.

### References

The following papers can be found on Google Scholar. Full texts are usually available by following the link on the right-hand side of the listing. It is not essential to read these papers. They are provided as references so that you are aware of the provenance of the content in the module notes and also for those who wish to delve deeper into the ideas.

[Chen, Z., Zhang, J.M., Hort, M., Harman, M. and Sarro, F. (2024) ‘Fairness testing: A comprehensive survey and analysis of trends’,  ACM Transactions on Software Engineering and Methodology, 33(5), pp.1-59.](https://dl.acm.org/doi/pdf/10.1145/3652155)

[Gal, Y. and Ghahramani, Z. (2016) ‘Dropout as a Bayesian approximation* arXiv preprint arXiv:1506.02157](https://proceedings.mlr.press/v48/gal16.html).

[HealthKnowledge (no date) ‘Methods for the Quantification of Uncertainty’, Faculty of Public Health](https://www.healthknowledge.org.uk/index.php/public-health-textbook/research-methods/1b-statistical-methods/methods-quantification-uncertainty) | Health Knowledge

[iMerit (2022) ‘A Comprehensive Introduction to Uncertainty in Machine Learning’, September 01](https://imerit.net/blog/a-comprehensive-introduction-to-uncertainty-in-machine-learning-all-una/)

[Kristiadi, A., Hein, M. and Hennig, P. (2020) ‘Being Bayesian, even just a bit, fixes overconfidence in ReLU networks’, International conference on machine learning (pp. 5436-5446), PMLR](https://dl.acm.org/doi/10.5555/3524938.3525442) | Proceedings of the 37th International Conference on Machine Learning

[Meronen, L., Trapp, M., Pilzer, A., Yang, L. and Solin, A.(2024) ‘Fixing overconfidence in dynamic neural networks’, In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (pp. 2680-2690)](https://openaccess.thecvf.com/content/WACV2024/papers/Meronen_Fixing_Overconfidence_in_Dynamic_Neural_Networks_WACV_2024_paper.pdf)

[Moon, J., Kim, J., Shin, Y. and Hwang, S. (2020) ‘Confidence-aware learning for deep neural networks’ In international conference on machine learning (pp. 7034-7044)](https://proceedings.mlr.press/v119/moon20a/moon20a.pdf) | PMLR

[Vecsei, G. (no date) ‘Experiments with Monte-Carlo dropout for uncertainty estimation’, February 24](https://imerit.net/blog/a-comprehensive-introduction-to-uncertainty-in-machine-learning-all-una/) | A Comprehensive Introduction to Uncertainty in Machine Learning

[Verdoja, F., & Kyrki, V. (2020) ‘Notes on the behavior of mc dropout’, arXiv preprint arXiv:2008.0262](https://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-097.pdf)

[Wang, D.B., Feng, L. and Zhang, M.L.(2021) ‘Rethinking calibration of deep neural networks: Do not be afraid of overconfidence’ Advances in Neural Information Processing Systems, 34, pp.11809-11820](https://proceedings.neurips.cc/paper_files/paper/2021/file/61f3a6dbc9120ea78ef75544826c814e-Paper.pdf)