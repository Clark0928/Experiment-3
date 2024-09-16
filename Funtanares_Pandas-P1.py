#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 1

# ### INSTRUCTIONS
# #### Using knowledge obtained from the experiment and demonstrations:###### 
# a. Load the corresponding .csv file into a data frame named cars using panda
# ###### 
# b. Display the first five and last five rows of the resulting cars

# #### Use Import Convention "import pandas as pd" to access Pandas Library

# In[3]:


import pandas as pd


# #### To access data from a csv file, the function .read_csv() was used. The data was then stored into a data frame named cars

# In[13]:


cars = pd.read_csv('cars.csv')


# #### The function .head(n) displays the first n rows of a data frame
# ##### (By default, it returns the first five rows)

# In[26]:


cars.head()


# #### The function .tail(n) displays the last n rows of a data frame
# ##### (By default, it returns the last five rows)

# In[28]:


cars.tail()

