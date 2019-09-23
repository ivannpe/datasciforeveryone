#!/usr/bin/env python
# coding: utf-8

# -  Ivanna Pena
# -  In this assignment, I will generate descriptive statistics from a data set of my choice
# -  This assignment is due on Friday, April 12, at 1p

# # Pre-Step: I am generally interested in:

# -   Describe broadly what topic you’re interested in
#      -  I am interested in finding ways to measure or depict inequality in America
# -  Why are you interested in this? What do you hope to discover?
#     -  I am interested in this because people often think we're often in a post-racial society, or that racism doesn't exist. I want to show otherwise, that racism does exist, and just because we ignore it doesn't mean it's not there and it's not greatly impacting people.

# # Dataset

# -  What dataset did you choose? Why?
#     -   I chose the five thirty eight data set behind the story "Higher Rates of Hate Crimes Are Tied to Income Inequality" because I thought would be interesting to see what other conclusions I could make from the dataset.
# -  What are some limitations of this dataset that you can see so far?
#    -  Some limitations include the age of the data included. The data ranges from 2009 to 2016, so it doesn't accurately depict what things are like in the current moment.

# In[3]:


import pandas as pd
import numpy as np
from scipy.stats import iqr
from scipy.stats import zscore
import matplotlib.pyplot as plt


# In[6]:


url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/hate-crimes/hate_crimes.csv'
data = pd.read_csv(url)
data.set_index('state',inplace=True)
data[:5]


# # Frequency Statistics

# -  Generate three frequency statistics you think are interesting, showing all code
# -  Briefly interpret these statistics in the context of this data/your overall research question

# In[7]:


def percent(part,whole):
    return part/whole * 100


# Percentage of Hate crimes in NY in the 10 ten days after the 2016 election to the average hate crimes per year.

# In[15]:


nyafterelection = data.loc['New York','hate_crimes_per_100k_splc']
nypreelection = data.loc['New York','avg_hatecrimes_per_100k_fbi']
percent(nyafterelection,nypreelection).round(3)


# -  I believe 11% is a large number for just being 10 days of the 365 days used the measure the yerly average

# Number of states with a median household income greater than 70,000.

# In[13]:


data[data['median_household_income'] > 70000]


# -  It is very telling that only 4 states have a median household income above 70,000.

# Income inequality in 2015 as measured by the GINI Index
# -  "A Gini coefficient of zero expresses perfect equality, where all would have the same income,a Gini coefficient of one expresses maximal inequality among values"

# In[18]:


#0.4817 is the GINI Index of the US Overall in 2015
data[data['gini_index'] > 0.4817]


# -  It is very interesting to see that these 3 states have a greater overall income inequality than the national GINI index of that year which was 0.4817. Also super cool to see that Connecticut is a state that has one of the highest median household incomes, but also higher inequality among states.

# # Measures of central tendency

# -  Generate three measures of central tendency, showing all code
# -  Briefly interpret these statistics in the context of this data/your overall research question

# In[19]:


round(data['median_household_income'].mean())


# -  a sum of median household incomes

# In[20]:


data['median_household_income'].median()


# -  the average of median household incomes is 54,916

# In[21]:


data['median_household_income'].mode()


# - Median household income that appears the most. By this you can tell that no state has the same

# # Measures of dispersion or variation

# -  Generate three measures of dispersion or variation, showing all code
# -  Briefly interpret these statistics in the context of this data/your overall research question

# In[22]:


def range(x):
    return x.max() - x.min()


# In[23]:


range(data['median_household_income'])


# -  The highest and lowest values; or, the difference between highest and lowest incomes. This shows the disparity of incomes between the highest earning states and lowest earning states.

# In[24]:


data['gini_index'].var()


# -  How spread out the data is from the mean. This shows that it isnt very spread out. Perhaps showing that inequality throughout the US is the same

# In[25]:


data['gini_index'].std()


# -  How spread out the data is from the mean in a format that makes more sense intuitively

# # Measures of position

# -  Generate three measures of position, showing all code
# -  Briefly interpret these statistics in the context of this data/your overall research question

# State rankings for hightest hate crime rate 10 days after the election (where 1 = biggest)

# In[28]:


data['hate_crimes_per_100k_splc'].rank(ascending = True).sort_values()


# -  I think it is very intersting that the top 10 states are spread out across the country, and not specifically centrally located in one region

# New column showing the avg_hatecrimes_per_100k_fbi percentiles for states

# In[33]:


data['Percentile of Hate']= pd.qcut(data['avg_hatecrimes_per_100k_fbi'],100,labels=False)
data[:5]


# -  Shows the percentile of each state in relation to average hate crimes for the years

# 90th Percentile of Hate Crimes in 2016

# In[34]:


data['hate_crimes_per_100k_splc'].quantile(.9)


# # Z-scores and distributions

# -  Generate a new table with z-scores for all observations
# -  Briefly interpret a few z-scores in the context of this data/your overall research question

# In[39]:


data2 = data.apply(zscore)
data2[:5]


# Generate a visualization of some aspect of those z-scores. What does it tell you?
# -  How many standard deviations an element is from the mean

# In[40]:


data2['median_household_income'].hist()


# Z-score < 0: element is lower than the mean
# Z-score > 0: element is greater than the mean
# Z-score = 0: element is the same as the mean
# -  Shows the distribution of median household income in terms of its standard deviations away from the mean

# Generate a histogram of one variable of interest (not the z-scores, one of the original variables)
# -  Briefly interpret the histogram in the context of this data/your overall research question and your earlier measures of central tendency

# In[41]:


data['hate_crimes_per_100k_splc'].hist()


# -  More states have lower rates of hate crimes in the 10 days after the 2016 election, than states that have higher ones.

# # Conclusion

# -  What are some of the more interesting findings from this work?

# I found it very interesting to see the ranking of states in terms of the hate crime rates 10 days after the 2016 election, because it was interesting to see what states were greatly impacted by the rhetoric the election was centered around.

# -  What major questions do you have left that you’d like to explore with this data?

# I would like to see the connection between the ranking of states I mentioned above, with the share of voters in that state that voted for trump. And the income disparities of states that voted for trump.

# -  What might be the concrete next steps for you to take to explore those questions?

# To explore this I would just have to manipulate this data set more, or to be more accurate, bring in newer updated data, to try and be as accurate as possible
