#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 2

# ### INSTRUCTIONS
# #### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# ###### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
# ###### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# ###### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# ###### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# 
# 

# #### Use Import Convention "import pandas as pd" to access Pandas Library

# In[3]:


import pandas as pd


# #### Use the function .read_csv() to load data from a csv file then store the data in a data frame named cars

# In[34]:


cars =  pd.read_csv('cars.csv')


# #### .iloc[[n],[m]] returns the n index row and m index column. You can also input a range of indices.
# ###### 0:5 , where 0 is the start index and 5 is the end index, this will return rows 0 to 4 since the end index is excluded
# ###### 1::2, where 1 is the start index and ::2 skips 1 index and returns the next, this will return columns 1,3,5,7,9, and 11

# In[31]:


cars.iloc[0:5,1::2]


# #### Locates Mazda RX4 under 'Model' and returns its corresponding row

# In[16]:


cars.loc[cars['Model'] == 'Mazda RX4']


# #### Locates Camaro Z28 under 'Model' and returns data under the columns 'Model' and 'cyl'

# In[25]:


cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]


# #### Locates Mazda RX4 Wag, Ford Pantera L, and Honda Civic under 'Model' and returns data under the columns 'Model', 'cyl, and 'gear'

# In[35]:


cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L') |
         (cars['Model'] == 'Honda Civic'), ['Model','cyl','gear']]

