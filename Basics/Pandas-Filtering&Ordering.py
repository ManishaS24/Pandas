#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Python\Web Scraping\LargestCompaniesByRevenue.csv")


# In[6]:


df


# In[5]:


# Filtering by a specific column using column name
df[df['Rank'] <= 10]


# In[8]:


# Filtering values on specific coulmn using its column values

specific_industry = ['Amazon', 'Alphabet']

df[df['Name'].isin(specific_industry)]


# In[11]:


# Filtering values on specific coulmn using string

df[df['Name'].str.contains('Corporation')]


# In[7]:


df2 = df.set_index('Name')
df2


# In[18]:


# Filteringon the indexes using FILTER function

df2.filter(items = ['Name', 'Employees'])



# In[19]:


# FILTER function with 'axis' parameter

#df2.filter(items = ['Name', 'Employees'], axis = 1)

#df2.filter(items = ['Name', 'Employees'], axis = 0)

df2.filter(items = ['Apple'], axis = 0)


# In[20]:


# FILTER function with 'like' parameter

df2.filter(like = 'United', axis = 0)


# In[22]:


# Filtering on indexes (string) using loc (location)

df2.loc['United Airlines']


# In[23]:


# Filtering on indexes (integer) using iloc (integer location)

df2.iloc[4]


# In[24]:


# Ordering or sorting dataframe

df[df['Rank'] <= 10].sort_values(by = 'Rank', ascending = False)


# In[26]:


df[df['Rank'] <= 10].sort_values(by = ['Rank', 'Name'], ascending = False)


# In[27]:


df[df['Rank'] <= 10].sort_values(by = ['Name', 'Rank'], ascending = False)


# In[29]:


df[df['Rank'] <= 10].sort_values(by = ['Rank', 'Name'], ascending = [False, True])


# In[ ]:




