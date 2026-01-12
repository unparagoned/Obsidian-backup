## The impact of error

Random error: e.g. misreading the weight. Could also be natural phenomena causing fluctuation in measurements.

Systematic error is a consistent or proportion difference. e.g. miscalibrated scales.

### Journal

Consider a data analytics project in your organisation and answer the following questions:

- What curation is done to the data to ensure it is of good quality?

Clean it, remove special characters, remove long stuff

- What if any data quality issues occur?

Remove the data.

- Could there be errors in the data that permeates through to the analytics model? If not, why not? If so, what errors could occur?

Yes. Maybe stuff like names or something

From <[https://app.qa.com/course/theme-6-error-bias-and-uncertainty-ai-1698/activity-impact-error/?context_id=14973&context_resource=lp](https://app.qa.com/course/theme-6-error-bias-and-uncertainty-ai-1698/activity-impact-error/?context_id=14973&context_resource=lp)>

## Bias in data

1. Historical bias e.g. might select males for jobs, since that was what happened in the past
2. Sample bias - sample must be representative. Must be truly randomised
3. Aggregation bias. e.g. if results are calculated at the county level, then those are averaged, that might not be right, since it doesn't account for the number of people or weightings. e.g. if county 1 has average income of £1m and pop of 10k and county 2 has average income of £2m and pop of 100, you can't just averages £1m and £2m it needs to be a weighted average.
4. Confirmation bias. When researchers select data that confirms their beliefs.

Fairness tests

[https://towardsdatascience.com/evaluating-machine-learning-models-fairness-and-bias-4ec82512f7c3](https://towardsdatascience.com/evaluating-machine-learning-models-fairness-and-bias-4ec82512f7c3)

- Select representative data of the whole population
- Check results for bias
- Apply fairness tests
- Monitor ML systems continuously

### Journal

What points from the paper do you find most interesting?

Calculating the difference

Logistic regression between attributes and sensitive attributes can be useful at determining proxies

Some of this stuff will lead to issues like Google faced. With AI that's not representative of the real world.

What fairness testing do you think could be employed in your organisation?

Fairness through unawareness

Fairness through awareness

Counterfactual fairness

Causal fairness

Fairness testing

Data testing, feature bias, label bias, selection bias

ML program testing.  Could be way it processes data, algorithm section, hyper parameters,

Framework testing

Model testing

Mon-ML component testing.

Make notes, including the rationale for your responses, and add them to your journal.

From <[https://app.qa.com/course/theme-6-error-bias-and-uncertainty-ai-1698/activity-fairness-testing/?context_id=14973&context_resource=lp](https://app.qa.com/course/theme-6-error-bias-and-uncertainty-ai-1698/activity-fairness-testing/?context_id=14973&context_resource=lp)>

## Aleatoric and epistemic uncertainty

Aleatoric uncertainty is inherent uncertainty and is always there. e.g. flipping a coin

Epistemic uncertainty lack of knowledge about the system. 

Ontological uncertainty - the degree of conceptual understanding of the world

Structural uncertainty relates to simplification we have to make

Deep uncertainty derives from the extent to which we can anticipate the nature of the problem space

Noisy data is aleatoric

Incomplete coverage is epistemic

### Quantifying and communicating uncertainty

Standard error and confidence intervals can quantify uncertainty.

Standard error of mean = sd/(number of observations)^0.5

[https://gaborvecsei.com/Monte-Carlo-Dropout/](https://gaborvecsei.com/Monte-Carlo-Dropout/)

Further reading

The following article provides a practical guide to Monte-Carlo Dropout. This further reading is optional.

| [Monte Carlo Dropout: a practical guide | by Ciaran Bench | Medium](https://medium.com/@ciaranbench/monte-carlo-dropout-a-practical-guide-4b4dc18014b5) |

References

The following papers can be found on Google Scholar. Full texts are usually available by following the link on the left-hand side of the listing. It is not essential to read these papers. They are provided as references so that you are aware of the provenance of the content in the module notes and for those who wish to delve deeper into the ideas.

- Gal, Y. and Ghahramani, Z., 2016. Dropout as a Bayesian approximation. arXiv preprint arXiv:1506.02157.
- Kristiadi, A., Hein, M. and Hennig, P., 2020, November. Being bayesian, even just a bit, fixes overconfidence in relu networks. In International conference on machine learning (pp. 5436-5446). PMLR.
- Meronen, L., Trapp, M., Pilzer, A., Yang, L. and Solin, A., 2024. Fixing overconfidence in dynamic neural networks. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (pp. 2680-2690).
- Moon, J., Kim, J., Shin, Y. and Hwang, S., 2020, November. Confidence-aware learning for deep neural networks. In international conference on machine learning (pp. 7034-7044). PMLR.
- Verdoja, F., &Kyrki, V. (2020). Notes on the behaviour of mc dropout. arXiv preprint arXiv:2008.0262
- Wang, D.B., Feng, L. and Zhang, M.L., 2021. Rethinking calibration of deep neural networks: Do not be afraid of overconfidence. Advances in Neural Information Processing Systems, 34, pp.11809-11820.

From <[https://app.qa.com/course/theme-6-error-bias-and-uncertainty-ai-1698/further-reading-and-references-1725111742300/?context_id=14973&context_resource=lp](https://app.qa.com/course/theme-6-error-bias-and-uncertainty-ai-1698/further-reading-and-references-1725111742300/?context_id=14973&context_resource=lp)>

[VanderPlas, J., Python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

[Spinello, R.A. (2021) Cyberethics: morality and law in cyberspace](https://www.vlebooks.com/Product/Index/2200669)

[Pears, R. and Shields, G.J. (2019) Cite them right: the essential referencing guide](https://www.vlebooks.com/Product/Index/2025007)

Habash, R.W.Y. (2019) Professional practice in engineering and computing: preparing for future careers

From <[https://app.qa.com/course/reflect-and-explore-ai-1698-31082024134432/explore-31082024134938/?context_id=14973&context_resource=lp](https://app.qa.com/course/reflect-and-explore-ai-1698-31082024134432/explore-31082024134938/?context_id=14973&context_resource=lp)>