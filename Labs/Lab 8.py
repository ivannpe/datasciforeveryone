#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  In this lab, I'm going to get started working with the pandas package for data science with python
# -  It might feel tedious, but I'm going to type all this out, plus fill in my own answers and examples where prompted

# # Preamble

# In[28]:


import pandas as pd
import numpy as np


# # Building tables
# ## Generic case
# -  The syntax for building tables in pandas is slightly different, but the overall logic is the same
# -  Please replicate the below for practice:

# In[2]:


mytable = {'Var1': ['var1_obs1', 'var1_obs2', 'var1_obs3'],
'Var2': ['var2_obs1', 'var2_obs2', 'var2_obs3'],
'Var3': ['var3_obs1', 'var3_obs2', 'var3_obs3']}


# In[3]:


mytable


# -  That was a raw table. To put it into a more easily readable (and familiar) format, try the following:

# In[4]:


df = pd.DataFrame(mytable, columns = ['Var1', 'Var2', 'Var3'])


# In[5]:


df


# ## Your example
# -  Now, build a 3-row, 3-column table of anything you like
# -  Show both the raw and dataframe format

# In[11]:


ivannatable = {'Study': ['Bobst', 'Kimmel', 'Silver'],
'Dining': ['Palladium', 'Lipton', 'Upstein'],
'Lounge': ['CMEP', 'Lipton Commuter', 'Courant']}


# In[12]:


ivannatable


# In[14]:


df2 = pd.DataFrame(ivannatable, columns = ['Study', 'Dining', 'Lounge'])


# In[15]:


df2


# # Importing data
# -  Importing data with pandas is also a little bit different from the data science package in terms of specific syntax, but as you can see, it's conceptually pretty similar
# ## Example case

# In[16]:


url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv'
df = pd.read_csv(url)
df[:5]


# -  Play around with some other language here:

# In[17]:


df[df['fatal_accidents_00_14']>2]


# -  What is the above doing? 
#     -  Using a filter to adjust the data frame to show where the value for the number of fatal accidents from 2000-2014 are greater than 2
# -  Try another specification and show the output below

# In[22]:


df[df['fatalities_00_14']>350]


# In[23]:


df.shape


# -  What is the above telling you?
#     -  the rows, columns

# In[24]:


df.columns


# - What is the above doing?     
#     -  describes the dataframe columns

# In[25]:


df.mean()


# -  What is the above telling you?
#     -  the mean of values

# ## Your case
# -  Find any dataset at all and replicate the above using your dataset, being sure to explain what each step is doing

# In[32]:


#hate crimes
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/hate-crimes/hate_crimes.csv'
df1 = pd.read_csv(url1)
df1[:5]


# In[45]:


df1[df1['share_voters_voted_trump']>0.6]


# -  Shows the states where the "Share of 2016 U.S. presidential voters who voted for Donald Trump" is greater than .5

# In[41]:


df1[df1['share_non_citizen']>0.1]


# -  Shows the states where the Share of the population that are not U.S. citizens, 2015" is greater than .1

# In[42]:


df1.shape


# -  (rows, columns)

# In[43]:


df1.columns


# -  describes the dataframe columns

# In[44]:


df1.mean()


# -  the mean of values
