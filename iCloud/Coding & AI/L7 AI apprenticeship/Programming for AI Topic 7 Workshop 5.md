Feature engineering extract new features from existing ones, like BMI, or day of week.

Reframing - where you change what the model does, e.g. rather than being continuous targets, you can use bins. Or that you are interested in watch time rather than clicks.

Regression, relationship between variables

[https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)

Autocorrelation can be used to help determine how many lags are significant

For ARIMA

The Box-Jenkins Methodology: A Three-Step Process:

1. Model Identification: Begin with visual tools like plots and leverage summary statistics. These aids help recognize trends, seasonality, and autoregressive elements. The goal here is to gauge the extent of differencing required and to determine the optimal lag size.
2. Parameter Estimation: This step involves a fitting procedure tailored to derive the coefficients integral to the regression model.
3. Model Checking: Armed with plots and statistical tests delve into the residual errors. This analysis illuminates the temporal structure that the model might have missed.

In SARIMAX (Seasonal Autoregressive Integrated Moving Average with eXogenous regressors), exogenous variables are external variables that can influence the time series being modeled but are not dependent on its past values. These variables, also called covariates or regressors, are included to improve the forecasting by accounting for outside factors that affect the target series.

For example, if modeling monthly sales, exogenous variables could include advertising spend, holidays, or special events that impact sales but are not part of the sales series itself. SARIMAX incorporates these external variables through the "exog" parameter, treating them like regressors in a regression model while also capturing autoregressive and seasonal patterns in the main series.