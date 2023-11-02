#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


# Set a specific colmn as index to the dataframe

df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Python\Web Scraping\LargestCompaniesByRevenue.csv", index_col = 'Name')

df


# In[4]:


# Reset the index of the dataframe
df.reset_index(inplace = True)


# In[5]:


df


# In[6]:


df.set_index('Name')


# In[7]:


df


# In[16]:


df.set_index('Name', inplace = True)


# In[17]:


df


# In[18]:


df.loc['Apple']


# In[20]:


df.iloc[3]


# In[21]:


df.reset_index(inplace = True)
df


# In[25]:


# Multi - index

df.set_index(['Name','Industry'], inplace = True)


# In[26]:


df


# In[27]:


df.sort_index()


# In[ ]:




