
Evdokia.krasteva@qa.com

Assumes linearity and normality

If you have categorical variables, then replace with x dummy variable just 0 or 1

e.g.

Location

North

South

->

North South Location

1           0        North

0           1        South

If multiple variables, remove any with p values over 0.05, etc.

= intercept +sumproduct(inputs, coefficients)

Compare prediction to actual

Removing outliers can improve the solution quite a bit

In R

Make sure right columns are as.factor e.g. region they live

Models should be used in the range they are trained on.

Python can use

Statsmodels.formula.api as smf

With categorical variables you always drop one level, to prevent multiple co-linearity.  e.g. if north = west = south = 0, then east is already defined in that, you don't need that column