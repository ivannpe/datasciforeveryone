#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  In this lab I am generating visualizations of data from the Polity IV project

# In[2]:


from datascience import *
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
import numpy as np


# In[3]:


data = 'https://raw.githubusercontent.com/ajr348/polity4/master/p4v2017.csv'


# In[4]:


polity = Table.read_table(data)
polity


# In[117]:


venezuela = polity.where('country',are.equal_to('Venezuela'))


# In[118]:


recent = polity.where('year',are.equal_to(2017))
ww2 = polity.where('year', are.equal_to(1940))
ww1 = polity.where('year',are.equal_to(1915))


# # Bar Chart

# In[119]:


ww1.barh('country','polity2')


# In this Bar chart I chose to visualize polity scores of countries in the midst of World War I. I was interesting to see the contrasting scores of different countries, and the scores of the countries involved in the war.

# # Line Graph

# In[120]:


venezuela.plot('year','polity2')


# I chose to plot the Polity score of Venezuela based on the years of collected data for it because its recent turmoil has brought me to think about its history as a country and the roles of its different leaders on its Polity score

# # Scatter Plot

# In[121]:


recent.scatter('autoc','durable')


# I chose to plot the association between autocracy score and regime durability. I thought it would be interesting to see how durable Autocracy would be and this graph shows that the closer the autocracy score is to 0, the more durable the regime is which makes sense.

# # Histogram

# In[122]:


ww2.hist('autoc',bins = np.arange(0,11,1))


# I chose to understand the distribution of autocracy scores in the midst of World War 2 in 1940. I thought this was interesting because I didn't expect to see as many scores leaning to the score of 10.

# # Overlaid Plot

# In[177]:


us = polity.where('country',are.equal_to('United States'))
us1 = us.select('year','democ')
usnew = us1.where('year',are.above(2013))
china = polity.where('country',are.equal_to('China'))
china1 = china.select('year','democ')
chinanew = china1.where('year',are.above(2013))
japan = polity.where('country',are.equal_to('Japan'))
japan1 = japan.select('year','democ')
japannew = japan1.where('year',are.above(2013))
germany = polity.where('country',are.equal_to('Germany'))
germany1 = germany.select('year','democ')
germanynew = germany1.where('year',are.above(2013))
uk = polity.where('country',are.equal_to('United Kingdom'))
uk1 = uk.select('year','democ')
uknew = uk1.where('year',are.above(2013))
year = chinanew.column(0)
uspol = usnew.column(1)
chinapol = chinanew.column(1)
japanpol = japannew.column(1)
germanypol = germanynew.column(1)
ukpol = uknew.column(1)
new_polity = Table().with_columns("Year",year,"US",uspol,"China",chinapol,"Japan",japanpol,"Germany",germanypol,"United Kingdom",ukpol)
new_polity.plot("Year")


# In this overlaid plot, I wanted to compare the democracy scores of the top 5 economies in the world from 2014 to now. I though it was interesting that most are concentrated in the high democracy scores, but china proves that a democracy score has nothing to do with economic success.

# # Conclusion

# Which of the above graphs do you think is the most useful/insightful? Why?
# -  I think the most insightful graph for me was the one about Venezuela because I was able to visualize an anready seemingly unstable government.
# Which is the least useful/insightful? Why?
# -  I think the least insightful was the histogram about autocratic scores during WW2 because I expected a different outcome
# What's another kind of graph that might be interesting to generate from this data?
# -  It would be interesting to have a graph of countries that the United States President has bashed and called names, and view their polity score to contrast his negative descriptions about them.
