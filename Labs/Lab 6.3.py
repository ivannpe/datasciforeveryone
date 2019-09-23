#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  This is a lab practice for the midterm

# # Preamble
# - The setup code you need for packages and other tools goes here

# In[1]:


from datascience import *
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
import numpy as np


# # Variables and Sequences

# In[2]:


#Create one string variable and one int variable, name them, and show their types
string1 = 'string'
type(string1)


# In[3]:


int1 = 1
type(int1)


# In[4]:


#Convert the int into a float, name it, and show what type it is
float1 = float(int1)
type(float1)


# In[5]:


#Create an array of at least 4 numbers, name it, and show it
array1 = np.array([1,2,3,4])
array1


# In[6]:


#Create an array that doubles those numbers, name it, and show it
array2 = array1*2
array2


# In[7]:


#Create a dictionary of at least 3 items, show it, and pull one value by the key
dictionary1 = {"Cat":"Meow", "Dog":"Bark","Cow":"Moo"}
dictionary1


# In[8]:


dictionary1["Dog"]


# In[9]:


#Create one table of anything with at least 3 rows and 2 columns, name it, and show it
table1 = Table().with_columns('Animals',make_array('Cat','Dog','Cow'),
                              'Sounds', make_array('Meow','Bark','Moo'))
table1


# # Working with Data
# ## Understanding the data

# In[10]:


data = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv'
congress = Table.read_table(data)
congress
#Import the data from GitHub as a table and display it (don't need all rows)


# In[11]:


#Show how many rows and columns there are in this dataset
print(congress.num_rows)
print(congress.num_columns)


# In[12]:


#How many members of Congress have been 60 or older?
age60orolder = congress.where('age',are.above_or_equal_to(60))
age60orolder.num_rows


# In[13]:


#What percentage is that of the total number of members of Congress?
percent60orolder = (age60orolder.num_rows /congress.num_rows)*100
print(percent60orolder , '%')


# In[14]:


#How old is the oldest member of Congress ever? 
#In what Congress did they serve?
oldest = congress.sort('age',descending = True)
oldest = oldest.take(0)
oldest.select('congress','firstname','lastname','age')


# In[15]:


#How old is the youngest member of Congress ever? 
#In what Congress did they serve?
youngest = congress.sort('age',descending = False)
youngest = youngest.take(0)
youngest.select('congress','firstname','lastname','age')


# In[16]:


#What number is the most recent Congress?
recent = congress.sort('congress',descending = True)
recent = recent.take(0)
recent.select('congress')


# ## Analysis

# In[17]:


#Create a table of only members who are in the most recent Congress
mostrecentcongress = congress.where('congress',are.equal_to(113))
mostrecentcongress = mostrecentcongress.select('congress','firstname','lastname','age')
mostrecentcongress


# In[18]:


#Sort this table by their age from the oldest to youngest
mostrecentcongress.sort('age',descending = True)


# In[19]:


oldest113 = mostrecentcongress.take(0)
oldest113.select('congress','firstname','lastname','age')


# In[20]:


youngest113 = mostrecentcongress.take(534)
youngest113.select('congress','firstname','lastname','age')


# In[21]:


#Create a histogram of the distribution of the age of members in the most recent Congress
mostrecentcongress.hist('age')


# - What does this histogram tell you about the ages of the most recent Congress?

# In[23]:


#Create a histogram of the distribution of the age of members in any earlier Congress
anyearliercongress = congress.where('congress',are.equal_to(99))
anyearliercongress.hist('age')


# - What does this new histogram tell you about the age of members in the most recent Congress?
