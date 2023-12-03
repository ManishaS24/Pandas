#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Pandas\Flavors.csv")


# In[14]:


df


# In[8]:


group_by_frame = df.groupby('Base Flavor')


# In[12]:


group_by_frame.mean(numeric_only=True)


# In[11]:


df.groupby('Base Flavor').mean(numeric_only=True)


# In[13]:


df.groupby('Base Flavor').count()


# In[16]:


#df.groupby('Base Flavor').sum()
df.groupby('Base Flavor').sum(numeric_only=True)


# In[17]:


df.groupby('Base Flavor').min()


# In[18]:


df.groupby('Base Flavor').max()


# In[27]:


df.groupby('Base Flavor').agg({'Flavor': ['max', 'count'], 'Liked': ['max', 'count']})


# In[28]:


df.groupby('Base Flavor').describe()


# In[ ]:





# In[ ]:




