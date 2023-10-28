#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


#Reading in CSV file

df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Python\Web Scraping\LargestCompaniesByRevenue.csv")

#df = pd.read_table(r"C:\Users\Manisha\Documents\GitHub\Python\Web Scraping\LargestCompaniesByRevenue.csv", sep = ",")

df


# In[13]:


#Reading in text file

#df = pd.read_csv(r"C:\Users\Manisha\Documents\GitHub\Python\Small_Project\userScores.txt", header = None, sep = "\t")

df = pd.read_table(r"C:\Users\Manisha\Documents\GitHub\Python\Small_Project\userScores.txt", header = None)

df


# In[20]:


#Reading in JSON file

df = pd.read_json(r"Downloads\dwsample1-json.json")
df


# In[23]:


df = pd.read_json(r"Downloads\sample1-json.json")
df


# In[29]:


df = pd.read_excel(r"C:\Users\Manisha\Downloads\Spreadsheet.xlsx")
df


# In[27]:


pd.set_option('display.max.rows', 701)
pd.set_option('display.max.columns', 20)


# In[31]:


df2 = pd.read_excel(r"C:\Users\Manisha\Downloads\Spreadsheet.xlsx")
df2


# In[32]:


df2.info()


# In[38]:


df2.shape


# In[35]:


#df2.head()   #By default top 5 records will be displayed
df2.head(10)


# In[37]:


#df2.tail()   #By default last 5 records will be displayed
df2.tail(10)


# In[39]:


#Reading in specific column details
df2['Country']


# In[41]:


#Reading in specific row details
df2.loc[17]


# In[42]:


#Reading in specific row details
df2.iloc[17]


# In[ ]:




