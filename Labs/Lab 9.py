#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  In this lab, I'm going to generate and interpret descriptive statistics!

# # Preamble

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import iqr
from scipy.stats import zscore
import matplotlib.pyplot as plt


# # Getting the data

# - Import the census data

# In[2]:


url = 'https://raw.githubusercontent.com/ajr348/us_population_est/master/us_pop_est.csv'
data = pd.read_csv(url)
data.set_index('location',inplace=True)
cols = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']
data[cols] = data[cols].replace({'$':'',',':''}, regex=True)
data2 = data[cols].astype(int)
pd.options.display.float_format = '{:20,.2f}'.format
states = data2[5:]


# # Frequency statistics

# - What percentage of the US population was the population of Alabama in 2017?

# In[3]:


def percent(part,whole):
    return part/whole * 100


# In[4]:


al = data2.loc['Alabama','2017']
us = data2.loc['United States','2017']
percent(al,us).round(3)


# - How many states in 2017 had a population greater than 20,000,000?

# In[29]:


states[states['2017'] > 20000000].count()


# # Measures of central tendency

# - What was the mean population size of states in 2017?

# In[5]:


round(states['2017'].mean())


# - The median?

# In[6]:


states['2017'].median()


# - The mode?

# In[7]:


states['2017'].mode()


# - What is the difference between the mean and the median (conceptually)?

# Although both are statistical averages the mean is a sum of numbers / how many numbers, while the median is the average of two middle numbers if even length

# # Measures of dispersion or variation 

# - What was the range of population sizes for 2017?

# In[8]:


def range(x):
    return x.max() - x.min()


# In[9]:


range(states['2017'])


# - The IQR?

# In[10]:


iqr(states['2017'])


# - The variance?

# In[11]:


states['2017'].var()


# - The standard deviation?

# In[12]:


states['2017'].std()


# - What does the standard deviation tell us (conceptually)?

# The Standard deviation is the square root of the variance or how spread out the data is from the mean in a format that makes more sense intuitively

# - What's the difference between the variance and std. dev. (conceptually)?

# Although both the variance and std. de. are measures of dispersion and variations, the variance tells us how ”spread out” the data are, or how spread out the data is from the mean, and the std. dev is the square root of that

# # Measures of position

# - What states were ranked 20, 21, 22, and 23 for population size (where 1 = biggest) in 2017?

# In[13]:


states['2017'].rank(ascending = True)


# Rank         
# 20 - Arkansas              
# 21 - Utah                   
# 22 - Iowa                       
# 23 - Puerto Rico

# - Generate a new column showing the 2017 percentiles for population size
# - Save that as a new table and print the first 5 rows

# In[14]:


states['2017_Percentile']= pd.qcut(states['2017'],100,labels=False)
percentile = states.copy()
percentile[:5]


# # Distributions and z-scores

# - Generate a histogram of the distribution of population sizes for 2017
# - Add a title, x- and y-axis labels, and make the x-axis readable (no scientific notation!)

# In[18]:


myhist = states['2017'].hist()
myhist.set_xlabel('Population')
myhist.set_ylabel('State Number')
myhist.set_title('State Population Sizes for 2017')
myhist.get_xaxis().get_major_formatter().set_scientific(False)
myhist.set_xticks(myhist.get_xticks()[::2])
myhist.set_xlim(xmin = 0)


# - What does this histogram tell us about how we can interpret the mean?

# The mean is skewed to the left because more states have populations that are around 5,000,000 than anything higher than that

# - What was the z-score for Nebraska for 2017?

# In[25]:


neb = states.apply(zscore)
nebraska = neb.loc['Nebraska','2017'] 
nebraska


# - What does this z-score mean conceptually?

# The z-score is a descriptive statistic that offers information about position, using information about variation, more specifically how many standard deviations an element is from the mean.
# In this case Nebraska is lower than the mean
