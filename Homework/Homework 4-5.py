#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna
# -  In this homework I will conduct an original data science research project with a dataset of my choosing, from start to finish.
# -  This homework is due by 1:50p on Friday, May 10.

# In[93]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns


# # Importing

# In[94]:


url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/hate-crimes/hate_crimes.csv'
data = pd.read_csv(url)
data[:5]


# In[95]:


data.shape


# In[96]:


data.describe()


# # Cleaning and Organizing

# In[97]:


data.set_index('state', inplace=True)


# In[98]:


columns = list(data.columns.values)
columns


# In[99]:


data.rename(columns={'median_household_income': 'income',
                     'share_voters_voted_trump': 'trumpvote',
                     'avg_hatecrimes_per_100k_fbi':'avghatecrimes',
                    'share_population_with_high_school_degree':'highschool'}, inplace=True)
data.head()


# In[100]:


data[:2].round(2)


# # Graphing
# -  Generate at least 3 graphs, whatever you like or are curious about, to explore your ideas
# -  Give brief explanations for why you include the graphs you did and what you’ve learned.

# In[101]:


data.hist('income')


# -  I chose to graph the distribution of median household income across all 50 states. The range of income is pretty small but it is interesting to see that most of the country makes about $55,000

# In[102]:


data.plot.scatter('income','highschool')


# -  I chose to plot the correlation between income and the share of the population with a high school degree. Through the graph it seems to have a positive correlation which makes sense.

# In[92]:


corr_matrix=data.corr()
plt.figure(figsize=(16,6))
mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(data.corr(),cmap="Reds",mask=mask)


# -  I chose to graph a heatmap of the correlation between different variables to see overall, rather than individual graphs, how (if at all), and to what extent these different factors are related. I really liked the ability of this graph to allow us to visualize that.

# # Analyzing
# • Identify at least 3 trends or patterns you think are interesting by manipulating the table.

# In[86]:


data['income_percentile'] = pd.qcut(data['income'],100, labels=False)
data[:5]


# -  Shows trends of income percentiles of all states in the sample

# In[89]:


data['hate_rank'] = data['avghatecrimes'].rank(ascending=False)
data.sort_values(by=['hate_rank'],ascending=False) 
data[:5]t 


# -  Shows average hate crime rank among states

# In[91]:


data['trump_rank'] = data['trumpvote'].rank(ascending=False)
data.sort_values(by=['trump_rank'],ascending=False) 
data[:5]


# -  displays ranks of votes for trump

# # Hypothesis formation
# • Write out your regression model as an equation, with "ladder" as the DV.
# • What are your IVs, and why? What do you expect to find?
# • Formally write your null and alternative hypotheses.

# Regression equation - hatecrimes = a + b * gini_index + c * income

# Independent variable - Gini index (the amount of inequality in a location, ranging from 0 to 1, 0 representing perfect equality
# 
# 
# Independent variable 2 - Income (the median household income in that state

# We expect to find a positive relationship between gini index, income and hate crimes

# H0 - There is no relationship between gini index, income and the amount of hatecrimes in a state
# 
# HA - There is a positive relationship between gini index, income and the amount of hatecrimes in a state

# # Regression
# • Estimate the regression and generate the relevant plots!

# In[113]:


results = smf.ols('avghatecrimes ~ income + gini_index',data=data).fit()
results.summary()


# In[107]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(results,'income',fig=fig)


# In[109]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(results,'gini_index',fig=fig)


# # Interpretation & diagnostics

# -  What do the results mean? Interpret the coefficient, p-values, and confidence intervals for each coefficient (you don’t have to do the intercept), and the Rˆ2 and Adj. Rˆ2 (if relevant), and prof(F) for the whole model.
# 
# Coefficient - An increase of one unit in income is associated with a decrease, or basically no change in avg hate crimes.
# An increase of one unit in the gini-index is associated with a 35.36 increase in avg hate crimes.
# 
# P-values - At a 95% confidence threshold, based on this analysis we can reject the null hypothesis of no relationship between income, gini_index and avg hate crimes. The probability of seeing a coefficient this extreme if the null hypothesis were true is 0.000 for gini_index, but .002 for income
# 
# Confidence Intervals - If we were to conduct this analysis 100 more times with other samples, 95% of the time this interval would contain the true value
# 
# R^2 & Adjusted R^2 - This model captures about 33% of the variance of the hatecrime. Adj. R2 is about the same with one independent variable
# 
# Prob ( F-statistic) - Since the F-statistic (9.34e-05) is so close to 0, we can reject the null hypothesis that this model does not capture any relationship considering how small the F-statistic is.

# -  Which hypotheses do you reject and fail to reject, and why?
# 
# We reject the null hypothesis and fail to reject to Alternative hypothesis due to our results described above

# -  Does this model satisfy the major assumptions of OLS regression (see Lecture 12.1)? Evaluate your model according to each one.
# 
# Reasonable sample size - Yes there are 50 states sampled which is a good enough sample size for this analysis
# 
# Linear relationship - Yes there is a linear relationship between hate crimes and income seen in the scatter plot as well as between hatecrimes and gini index.
# 
# Minimal Outliers - There are several outliers
# 
# No or little multicollinearity - No multicollinearity, the variables of gini index and income are very different and do not predict anything about the next .
# 
# Homoscedasticity - No general pattern seen when looking at the scedasticity of the collection of observations.
# 
# No autocorrelation - No autocorrelation because states have different values that cant predict anything about the other

# # Conclusions

# -  What biases might be present in the sample itself that could be affecting this outcome? 
# 
# 
# Gini index is a number between 0 and 1
# 
# Selection - Choosing what different factors to take in account 
# 
# Response - There could be bias in how certain data is collected, such as who is non_citizen or who is poor.
# 
# Measurement - Gini is only measured on a binary scale of 0 to 1 which complicates how this is shown in the data, causing a bigger jump due to limited values.
# 
# Invisibility - Data might ignore populations which have valueable insight into avg hate crimes of the state.

# -  Overall, are you confident in your findings? Why or why not? What might improve this analysis? (This can be about anything from the original data, bias, and/or results and diagnostics.)
# 
# Overall we are confident in our findings because the p-value is very small, and the graph of correlation between all variables shows a relationship. Something that would improve this analysis is adding different years of data for states, to see how different factors influence different hate crime averages across time across the country
