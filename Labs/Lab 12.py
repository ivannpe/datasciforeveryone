#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna
# -  In this lab I will conduct an original data science research project from start to finish.
# -  I am working with: Pooja Patel.
# -  This lab is due by 1p on Friday, May 3.

# In[2]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib


# # Importing

# In[3]:


data = pd.read_csv('happy.csv')
data[:5]


# In[4]:


data.shape


# In[5]:


data.describe()


# # Cleaning and Organizing

# In[6]:


data.rename(columns={'Country name': 'country','Social support': 'social',
                'Life Ladder':'ladder','Year':'year',
                'Log GDP per capita': 'gdp',
                'Healthy life expectancy at birth':'expectancy',
                'Freedom to make life choices': 'freedom',
                'Generosity':'generosity',
                'Perceptions of corruption':'corruption'}, inplace=True)
data.head()


# In[7]:


data[:2].round(2)


# In[8]:


dataUS = data[data['country'] == 'United States']
dataUS[:5]


# # Graphing
# -  Generate at least 3 graphs, whatever you like or are curious about, to explore your ideas
# -  Give brief explanations for why you include the graphs you did and what you’ve learned.

# In[9]:


data18 = data[data['year'] == 2018]


# In[10]:


data18.hist('social')


# -  We chose to graph Social support to visualize the distribution of how much social support countries recieve. We learned that the majority of people on a scale from 0 to 1 felt a .9 level of social support.

# In[11]:


data.plot.scatter('ladder','social')


# -  We chose to plot ladder against social support to see if there was correlation between happiness and the amount of social support one has. We learned that there is a positve correlation between happiness and social support among people surveyed.

# In[12]:


dataUS.plot.line('year','social')


# -  We chose to plot year against support to see how the level of support people felt changed over time. We learned that while it fluctuated, the level of support people felt over time did not change drastically.

# # Analyzing
# • Identify at least 3 trends or patterns you think are interesting by manipulating the table.

# In[13]:


data18['ladder_percentile'] = pd.qcut(data18['ladder'],100, labels=False)
data18[:5]


# In[14]:


columns = list(data18.columns.values)
columns


# In[15]:


data18 = data18[['country',
 'year',
 'ladder',
 'gdp',
 'social',
 'expectancy',
 'freedom',
 'generosity',
 'corruption',
 'ladder_percentile',
 'Positive affect',
 'Negative affect',
 'Confidence in national government',
 'Democratic Quality',
 'Delivery Quality',
 'Standard deviation of ladder by country-year',
 'Standard deviation/Mean of ladder by country-year',
 'GINI index (World Bank estimate)',
 'GINI index (World Bank estimate), average 2000-16',
 'gini of household income reported in Gallup, by wp5-year']]
data18[:5]


# In[16]:


data18.sort_values('ladder_percentile', ascending = False)
data18[:5]


# 

# -  Shows trends of ladder percentiles of all countries in the sample

# In[17]:


data18.set_index('country', inplace=True)
data18['gdp_rank'] = data18['gdp'].rank(ascending=False)
data18.sort_values(by=['gdp_rank'],ascending=False) 
data18[:5]


# -  Shows gdp rank amongst countries in 2018

# In[18]:


data18['social_rank'] = data18['social'].rank(ascending=False)
data18.sort_values(by=['social_rank'],ascending=False) 
data18[:5]


# -  displays ranks of social support from least to greatest

# # Hypothesis formation
# • Write out your regression model as an equation, with "ladder" as the DV.
# • What are your IVs, and why? What do you expect to find?
# • Formally write your null and alternative hypotheses.

# Regression equation - ladder = a + b * social support + c * freedom

# Independent variable - Social Support (the national
# average of the binary responses (either 0 or 1) to the GWP question “If you
# were in trouble, do you have relatives or friends you can count on to help you
# whenever you need them, or not?”)
# 
# 
# Independent variable 2 - Freedom (the national average of responses to the GWP
# question “Are you satisfied or dissatisfied with your freedom to choose what
# you do with your life?”)

# We expect to find a positive relationship between support, freedom, and ladder

# H0 - There is no relationship between happiness and the freedom and social support people felt in 2018
# 
# HA - There is a positive relationship between happiness and the freedom and social support people felt in 2018

# # Regression
# • Estimate the regression and generate the relevant plots!

# In[86]:


results18 = smf.ols('ladder ~ social + freedom + corruption',data=data18).fit()
results18.summary()


# In[81]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(results18,'social',fig=fig)


# In[82]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(results18,'freedom',fig=fig)


# # Interpretation & diagnostics

# -  What do the results mean? Interpret the coefficient, p-values, and confidence intervals for each coefficient (you don’t have to do the intercept), and the Rˆ2 and Adj. Rˆ2 (if relevant), and prof(F) for the whole model.
# 
# Coefficient - An increase of one unit in the Social Support is associated with a 6.8226 increase in ladder score. An increase of one unit in the Freedom is associated with a 2.5948 increase in ladder score
# 
# P-values - At a 95% confidence threshold, based on this analysis we can reject the null hypothesis of no relationship between social support, freedom and happiness. The probability of seeing a coefficient this extreme if the null hypothesis were true is 0.000 for both independent variables
# 
# Confidence Intervals - If we were to conduct this analysis 100 more times with other samples, 95% of the time this interval would contain the true value
# 
# R^2 & Adjusted R^2 - This model captures about 58% of the variance of the ladder score. Adj. R2 is about the same with one independent variable
# 
# Prob ( F-statistic) - Since the F-statistic (6.45e-26) is so close to 0, we can reject the null hypothesis that this model does not capture any relationship considering how small the F-statistic is.

# -  Which hypotheses do you reject and fail to reject, and why?
# 
# We reject the null hypothesis and fail to reject to Alternative hypothesis due to our results described above

# -  Does this model satisfy the major assumptions of OLS regression (see Lecture 12.1)? Evaluate your model according to each one.
# 
# Reasonable sample size - Yes there are 136 countries sampled for 2018 which is a good enough sample size for this analysis
# 
# Linear relationship - Yes there is a linear relationship between ladder and social support seen in the scatter plot as well as between ladder and freedom.
# 
# Minimal Outliers - There are few data points that are beyond the area of other points.
# 
# No or little multicollinearity - No multicollinearity, the variables of social support and freedom are very different and do not predict anything about the next .
# 
# Homoscedasticity - No general pattern seen when looking at the scedasticity of the collection of observations.
# 
# No autocorrelation - No autocorrelation because we are only looking at one year of data

# # Conclusions

# -  What biases might be present in the sample itself that could be affecting this outcome? 
# Social support is measured by (the national average of the binary responses (either 0 or 1) to the GWP question “If you
# were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”)
# 
# Freedom is measured by (the national average of responses to the GWP
# question “Are you satisfied or dissatisfied with your freedom to choose what
# you do with your life?”)
# 
# Selection - Choosing what countries to use. They used 136 countries out of the 195 existing.
# 
# Response - There could be bias in how people respond due to how they might want to be perceived as having people they can lean on, or what freedom could mean to them (very subjective).
# 
# Measurement - It is only measured on a binary scale of 0 to 1 which complicates how people would respond. Different responses if measured on the scale from 1 to 10
# 
# Invisibility - Data might ignore people who are unable to interact with others or who's definition of freedom is different.

# -  Overall, are you confident in your findings? Why or why not? What might improve this analysis? (This can be about anything from the original data, bias, and/or results and diagnostics.)
# 
# Overall we are confident in our findings because 1 the visualizations show a trend and 2, the p-value is very small. Something that would improve this analysis is changing how Social support was recorded, instead of 0 to 1 it could be 0 to 10 which could be more clear to respondents and also provide a more accurate coefficient, along with making it more clear what Freedom actually means.
