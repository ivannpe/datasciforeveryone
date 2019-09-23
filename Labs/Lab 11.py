#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  In this lab I will conduct regression analysis!

# # Instructions
# -  Conduct one OLS regression analysis with any dependent variable and independent variable(s) you like.

# In[41]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib


# In[42]:


url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/hate-crimes/hate_crimes.csv'
pd.set_option('display.max_columns',50)
data = pd.read_csv(url)
data[:5]


# In[43]:


data.shape


# -  Why did you choose these variables, and what are your null and alternative hypotheses?(One per DV.)

# My dependent variable is 'Share of Voters that Voted for Trump' and my independent variable is the 'Share of White People in Poverty'.
# -  My null hypothesis is that there is no correlation between the number of poor whites in states and the number of voters in that state that voted for trump.
# -  My alternative Hypothesis is that the share of voters that voted for trump is directly correlated to the share of white poverty in that state.

# In[52]:


data.plot.scatter('share_white_poverty','share_voters_voted_trump')


# In[53]:


results = smf.ols('share_voters_voted_trump ~ share_white_poverty',data = data).fit()
results.summary()


# Identify and briefly interpret the R-squared, intercept, and the coefficient, p-value, and confidence interval on one dependent variable.
# -  The r-squared in the table is .306 which isnt that great and shows that the line of best fit has high variance between the actual values
# -  The intercept is 0.2463 when x = 0
# -  Coef on share of white poverty : A one-unit increase in the value of the IV is associated with a 2.6554 unit increase in the value of the DV
# -  P>|t| is statistically significant
# -  Confidence interval on the share of white povery at 97 percent is 3.804

# In[54]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(results,"share_white_poverty",fig=fig)


# -  Finally: What’s one possible flaw with these results? (Anything at all!)

# One flaw could be that the relationship between these variables is merely coincidental, and is not important even though the data might say it is or vice versa
