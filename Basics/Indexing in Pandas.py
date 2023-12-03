#!/usr/bin/env python
# coding: utf-8

# In[5]:


# INDEXING

import pandas as pd


# In[6]:


df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Pandas\world_population.csv")

df


# In[3]:


df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Pandas\world_population.csv", index_col = 'Country')

df


# In[5]:


df.reset_index(inplace = True)


# In[6]:


df


# In[8]:


df1 = df.set_index('Country')
df1


# In[9]:


df.set_index('Country', inplace = True)
df


# In[11]:


df.loc['Albania']


# In[12]:


df.iloc[1]


# In[14]:


df.reset_index(inplace = True)


# In[15]:


df


# In[7]:


#Multi Indexing

df.set_index(['Continent', 'Country'], inplace = True)


# In[8]:


df


# In[15]:


pd.set_option('display.max.rows', 235)


# In[16]:


#df.sort_index(ascending = [False, True])

df.sort_index()


# In[18]:


df.loc['Africa', 'Angola']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




