#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  This is the final exam.

# In[69]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import iqr


# # Importing

# In[70]:


data = pd.read_csv('happy.csv')
data[:5]


# In[71]:


data.shape


# # Cleaning and Organizing

# In[72]:


data.rename(columns={'Country name': 'country','Social support': 'social',
                'Life Ladder':'ladder','Year':'year',
                'Log GDP per capita': 'gdp',
                'Healthy life expectancy at birth':'expectancy',
                'Freedom to make life choices': 'freedom',
                'Generosity':'generosity',
                'Perceptions of corruption':'corruption'}, inplace=True)
data.head()


# -   Create a table just of observations from 2018.

# In[73]:


data18 = data[data['year'] == 2018]
data18.set_index('country', inplace=True)
data18[:5]


# -  Create a column in the 2018 table that ranks countries by percentiles of Log GDP per Capita and is sorted from the wealthiest to the poorest.

# In[74]:


data18['gdp_rank'] = data18['gdp'].rank(ascending = False)


# In[75]:


data18.sort_values(by=['gdp_rank'],ascending = True) 
data18[:5]


# -  What percentile is Argentina? How do you interpret this percentile?

# Argentina is in the 45th percentile. Which means that 45% of the countries are either at the same level or worse in terms of GDP.

# # Descriptive Statistics

# What is the median Log GDP per Capita?

# In[63]:


data['gdp'].median()


# What is the median Log GDP per Capita in 2016?

# In[64]:


data16 = data[data['year'] == 2016]


# In[65]:


data16['gdp'].median()


# What is the IQR for Perceptions of Corruption?

# In[91]:


iqr(data['corruption'],nan_policy='omit')
#without the ommition the iqr yielded nan, decided to omit
# to perform the calculations ignoring nan values


# What is the standard deviation of Freedom to Make Life Choices in the UK?

# In[79]:


dataUK = data[data['country'] == 'United Kingdom']


# In[80]:


dataUK['freedom'].std()


# # Graphing

# Generate a histogram of Perceptions of Corruption and briefly interpret it.

# In[83]:


data.hist('corruption')


# -  Many countries are closer to 1 in terms of the perception of corruption on a scale of 0 to 1

# Generate a line graph of Perceptions of Corruption in the US over time and briefly interpret
# it.

# In[84]:


dataUS = data[data['country'] == 'United States']


# In[85]:


dataUS.plot.line('year','corruption')


# -  Perceptions of corruption in the United States have been steadily increasing although big jumps in 2013 and 2016 with it now rising in 2018

# Generate a scatter plot of Perceptions of Corruptions vs. Log GDP per Capita and briefly
# interpret it.

# In[87]:


data.plot.scatter('gdp','corruption')


# -  This scatter plot doesnt really say much about the relationship between gdp and corruption perception because for most gdp values, the corruption is high, although when gdp goes higher than 10, corruption lowers significantly

# # Hypothesis formation
# -  We are going to test the hypothesis that the Perception of Corruption is negatively associated with the Log GDP per Capita.
# -  Write out your regression model as an equation, with "Log GDP Per Capita" as the DV, explaining each component.
# -  Formally write all of the null and alternative hypotheses.

# Regression equation - Log GDP Per Capita (DV) = a (Intercept) + b (Slope of the line) * Perception of Corruption (IV)

# Independent variable - Perception of Corruption

# We expect to find a negative relationship between perception of corruption and Log GDP per capita

# -  H0 - There is a positive relationship between Perception of Corruption and Log GDP per capita
# -  HA - There is a negative relationship between Perception of Corruption and Log GDP per capita

# # Regression
# • Estimate the regression and generate the relevant plots!

# In[88]:


results = smf.ols('gdp ~ corruption',data=data).fit()
results.summary()


# In[89]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(results,'corruption',fig=fig)


# # Interpretation & diagnostics

# -  What do the results mean? Interpret the coefficient, p-values, and confidence intervals for each coefficient (you don’t have to do the intercept), and the Rˆ2 and Adj. Rˆ2 (if relevant), and prof(F) for the whole model.
# 
# Coefficient - An increase of one unit in the Perception of Corruption is associated with a -2.1766 decrease in Log GDP per capita.
# 
# P-values - At a 95% confidence threshold, based on this analysis we can reject the null hypothesis of a positive relationship between Perception of Corruption and Log GDP per capita. The probability of seeing a coefficient this extreme if the null hypothesis were true is 0.000 for the independent variables.
# 
# Confidence Intervals - If we were to conduct this analysis 100 more times with other samples, 95% of the time this interval would contain the true value
# 
# R^2 & Adjusted R^2 - This model captures about 12% of the variance of the Log GDP per capita. Adj. R2 is the same. This is a very low R^2
# 
# Prob ( F-statistic) - Since the F-statistic (2.15e-44) is so close to 0, we can reject the null hypothesis that this model does not capture any relationship considering how small the F-statistic is.

# -  Which hypotheses do you reject and fail to reject, and why?
# 
# We reject the null hypothesis and fail to reject to Alternative hypothesis due to our results described above

# -  Does this model satisfy the major assumptions of OLS regression? Evaluate your model according to each one.
# 
# Reasonable sample size - Yes there are 136 countries sampled which is a good enough sample size for this analysis
# 
# Linear relationship - There seems to be no linear relationship between gdp and corruption seen in the scatter plot, but if there is it does not say much about the relationship between the variables.
# 
# Minimal Outliers - There are various data points that are beyond the area of other points.
# 
# No or little multicollinearity - No multicollinearity, the variables of gdp and corruption are very different and do not predict anything about the next .
# 
# Homoscedasticity - Seems to have some heteroscedasticity.
# 
# No autocorrelation - There might be some autocorrelation due to this data of gdp and corruption being over the time the data was collected.

# -  What other biases are present that concern you?
# 
# Perception of corruption is measured through "The measure is the national average of the survey responses to two questions in the GWP: “Is corruption widespread throughout the government or not” and “Is corruption widespread within businesses or not?” The overall perception is just the average of the two 0-or-1 responses. In case the perception of government corruption is missing, we use the perception of business corruption as the overall perception. The corruption perception at the national level is just the average response of the overall perception at the
# individual level."
# 
# Response - There could be bias in how people respond due to how they might define corruption, and the perception of corruption could vary from person to person(very subjective), especially if one has a bad experience with a certain business deeming it corrupt.
# 
# Measurement - It is only measured on a binary scale of 0 to 1 which complicates how people would respond. It also is based on perception of corruption in business versus in the government, which are drastically different.
# 

# # Conclusions

# -  Overall, how confident are you that you understand the relationship between GDP and corruption? Why? (This can be brief!)
# 
# Overall I am not very confident that I understand the relationship between gdp and corruption because although there is a p-value of 0, the visualization in the scatter plot is unclear, and the bias in the collection of corruption data, along with how much of the variance this regression captures makes me want to test for specific years, specific countries, especially those with accurate histories of corruption to compare.
