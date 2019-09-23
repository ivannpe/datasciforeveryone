#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  In this lab I am investigation the racial / ethnic diversity of companies in the Forbes 500
# -  Specifically, the research question is: How many POC of color are represented in Fortune 500 companies?
# -  And the data source is: Forbes 500 diversity data from EEO-1 forms
# 
# from datascience import *

# In[46]:


#importing data from github
data = 'https://raw.githubusercontent.com/fortunedatateam/f500-diversity/master/2017-f500-diversity-data.csv'


# In[47]:


# read data from forbes
div = Table.read_table(data)


# In[48]:


#save data that is available
diversity_Y = div.where('data-avail',are.equal_to('Y'))


# In[49]:


# make copy for cleanliness
diversity = diversity_Y.copy()


# # Percentages of each entire company that are POC
# 

# In[87]:


white  = diversity.column('WHM10') + diversity.column('WHF10')
pctwhite = white / diversity.column('TOTAL10')
#total of all POC's
percentPOC = 1 - pctwhite


# In[80]:


#new table with columns of only company name and total employees
diverse = diversity.select('name','TOTAL10')


# In[88]:


#adding percent poc row to diverse table
percentPOCs = diverse.with_columns('Percent POC',percentPOC)


# In[101]:


#formatting percentage
percentPOCs.set_format('Percent POC',PercentFormatter)
percentPOCs.sort('Percent POC', descending = True)
#new column of sorted percentages in decreasing order
POCsorted = percentPOCs.sort('Percent POC', descending = True) 
POCsorted = POCsorted.relabeled('name','Company Name') #renaming
POCsorted = POCsorted.relabeled('TOTAL10','Total Employees') #renaming
POCsorted #table with company name, total employees, and percentage of POC


# # Percentages of the top-level of leadership that are POC

# In[90]:


pctwhite_leadership = ((diversity.column('WHM1') + diversity.column('WHF1') ) / 
                       (diversity.column('TOTAL1')))


# In[91]:


#calculating the percent of POC in leadership
POCLeadershipPercent = 1 - pctwhite_leadership


# In[102]:


#adding percent poc leadership row to previous sorted table
POCleaders = percentPOCs.with_columns('Percent POC in Leadership',
                                      POCLeadershipPercent) 
#formatting percentage
POCleaders.set_format('Percent POC in Leadership',PercentFormatter)
#sort poc in leadership
leadership = POCleaders.sort('Percent POC in Leadership', descending = True) 
leadership


# # Ratios of leadership to full company that are POC

# In[96]:


#calculating ratio of leadership to overall POC
leadershipratio = POCLeadershipPercent / percentPOC


# In[104]:


#adding percent ratio leadership row to previous sorted table
POCdata = POCleaders.with_columns('Ratio of Leadership',leadershipratio) 
#formatting percentage
# POCdata.set_format('Ratio of Leadership',PercentFormatter)
POCtablefinal = POCdata.sort('Ratio of Leadership', descending = True) 
POCtablefinal


# # Conclusion  

# - What have you learned about these companies in terms of the three findings? 
# 
# 
#     I have learned that data can be misleading. Many companies with very high percentages of people of color, have very small percentages of POC in leadership. The way these companies might present their data could be hiding some important numbers.
# 

# - What have you learned about coding in python and working with tables?
# 
# 
#     I have learned the importance of being able to manipulate data to give it meaning. I did so through python tables and many methods that allowed me to present data in a way where I had the most important information to offer. It was also interesting to see what bugs I encountered, and how the way I approached finding the data gave me different formats in my table
