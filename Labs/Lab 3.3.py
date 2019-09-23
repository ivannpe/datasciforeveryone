#!/usr/bin/env python
# coding: utf-8

# -  My name is Ivanna Pena
# -  I worked with Pooja Patel

# # Expressions and names

# In[29]:


import math
x = 9
y = 9
z = x * y
my_square_root = math.sqrt(z)
my_square_root


# # Data Types
# ## Generating variables

# In[1]:


myint = 1
type(myint)


# In[8]:


myfloat = 1.0
type(myfloat)


# In[3]:


mystring = 'string'
type(mystring)


# In[4]:


myboolean = True
type(myboolean)


# ## Converting types

# In[30]:


mynewfloat = float(myint)
mynewfloat


# In[31]:


mynewbool = int(myboolean)
mynewbool


# In[32]:


mynewint = int(myfloat)
mynewint


# In[33]:


mynewstring = int(mystring)
mynewstring


# # Sequences

# ## Creating sequences
# 

# In[12]:


mylist = [1,2,3]
mylist


# In[13]:


import numpy as np
myarray = np.array([1,2,3])
myarray


# In[14]:


mytuple = (1,2,3)
mytuple


# In[15]:


myrange = np.arange(1,10,2)
myrange


# ## Manipulating sequences

# In[16]:


myarray[1] = 0
myarray


# In[17]:


mytuple(1) = 0
mytuple


# In[18]:


mylist2 = [4,5,6]
mylist2


# In[21]:


myarray2 = np.array([4,5,6])
myarray2


# In[22]:


mylist*mylist2


# In[23]:


myarray*myarray2


# # Containers

# In[24]:


myset = {"Data",101,False}
myset


# In[25]:


mydictionary = {"Data":"Science", "Computer":"Science"}
mydictionary


# In[26]:


mydictionary["Data"]


# # Tables

# In[27]:


from datascience import *


# In[28]:


myTable = Table().with_columns(
    'Number of Shoes', make_array(2, 3, 4),
    'Brand', make_array('Nike', 'Adidas', 'Birkenstock')
)
myTable #output on pdf is weird for table you said it was fine

