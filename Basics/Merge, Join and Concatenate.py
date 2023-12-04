#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Pandas\LOTR.csv")
df1


# In[3]:


df2 = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Pandas\LOTR 2.csv")
df2


# In[6]:


df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'])
#df1.merge(df2)


# In[8]:


df1.merge(df2, how = 'outer')


# In[9]:


df1.merge(df2, how = 'outer', on = ['FellowshipID', 'FirstName'])


# In[10]:


df1.merge(df2, how = 'right')


# In[11]:


df1.merge(df2, how = 'left')


# In[12]:


df1.merge(df2, how = 'cross')


# In[16]:


df1.join(df2, how = 'outer', on = 'FellowshipID', lsuffix = '_left', rsuffix = '_right')


# In[18]:


df3 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), how = 'outer', lsuffix = '_left', rsuffix = '_right')
df3


# In[19]:


pd.concat([df1,df2])


# In[21]:


pd.concat([df1,df2], join = 'outer', axis = 1)


# In[22]:


df1.append(df2)


# In[ ]:





# In[ ]:





# In[ ]:




