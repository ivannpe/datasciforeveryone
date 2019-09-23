#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena. This is the midterm exam
# 
# # Preamble

# In[8]:


from datascience import *
import numpy as np
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots


# # Variables and sequences

# In[4]:


#boolean
myboolean = True
type(myboolean)


# In[5]:


#float
myfloat = 1.0
type(myfloat)


# In[6]:


#float to int
mynewint = int(myfloat)
mynewint


# In[7]:


type(mynewint)


# In[12]:


#range
myrange = np.arange(0,110,10)
myrange


# In[13]:


#list
mylist = [1,2,3,4,5]
mylist


# In[62]:


#Add a 6th element to that list and show the new list
#mylist[5] = 6
mylist = [1,2,3,4,5,6]
mylist


# In[15]:


#create a table
table1 = Table().with_columns('Animals',make_array('Cat','Dog','Cow','Sheep'),
                              'Sounds', make_array('Meow','Bark','Moo','Baa'))
table1


# # Working with data
# ## Understanding the data

# In[3]:


data = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv'


# In[16]:


druguse = Table.read_table(data)
druguse


# In[17]:


druguse.num_rows


# In[18]:


druguse.num_columns


# alcohol-use is "percentage of those in an age group who used alcohol in the past 12 months"

# alcohol-frequency is "Median number of times a user in an age group used alcohol in the past 12 months"

# In[20]:


#What age group has the highest alcohol use? 
highestuse = druguse.sort('alcohol-use',descending = True)
highestuse.take(0).select('age')


# In[21]:


#The least?
lowestuse = druguse.sort('alcohol-use',descending = False)
lowestuse.take(0).select('age')


# In[22]:


#marijuana-use
highestweeduse = druguse.sort('marijuana-use',descending = True)
highestweeduse.take(0).select('age')


# In[23]:


lowestweeduse = druguse.sort('marijuana-use',descending = False)
lowestweeduse.take(0).select('age')


# In[45]:


year18 = druguse.where('age',are.equal_to('18'))
year18
#max function is returning incorrectly


# 18 year olds use alcohol the most, and crack and heroin the least

# ## Analysis

# In[46]:


druguse.barh('age','alcohol-use')


# In[50]:


new = druguse.select('age','marijuana-use','alcohol-use')
new.barh('age')


# In[48]:


#new = Table().with_columns('age',age,'marijuana-use',highestweeduse,'alcohol-use',highestuse)
new.plot('age')


# You can learn the difference in usage by each individual age of each drug and the rate at which the use of the drug increases by age.

# two overlaid graphs is more useful because we get to compare data and make comparisons through observation rather than just looking at numbers

# In[54]:


newer = druguse.select('marijuana-use','alcohol-use')
newer.scatter('alcohol-use')


# the correlation between alcohol use and marijuana use becomes more related as age gets higher, but they seem to share a lot of correlation at younger ages

# one limitation of this dataset is the way data is structured, and the ability to compare by year. that would be more insightful.

# In[ ]:




