#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


sns.get_dataset_names()


# In[3]:


df = sns.load_dataset("diamonds")


# In[4]:


df


# In[5]:


df.cut.unique()


# In[15]:


df.cut.value_counts()


# In[16]:


df.head()


# In[17]:


df.tail()


# In[22]:


sns.lineplot(x='carat', y='price', data=df, ci=None) #Confidence interval
plt.show()


# In[24]:


sns.boxplot(x = 'carat', data = df)
plt.show()


# In[34]:


sns.scatterplot(x = 'cut', y = 'price', data = df)
plt.show()


# In[5]:


sns.lineplot(x='carat', y='price', data=df,hue='cut', ci=None)
plt.show()


# In[15]:


import seaborn as sns
sns.barplot(x='cut', y='price', data=df)
plt.show()


# In[16]:


sns.countplot( x = 'cut', data = df)
plt.show()


# In[19]:


sns.violinplot( x = 'cut', y = 'carat', data = df)
plt.show()


# In[22]:


sns.histplot( x ='cut',  data = df)
plt.show()


# In[25]:


sns.stripplot( x = 'cut', y = 'carat', data = df)
plt.show()


# In[11]:


sns.histplot( x = 'price', hue = 'cut',data = df, kde = True)
plt.show()


# In[6]:


sns.catplot( x = 'carat', data = df , kind = 'violin')
plt.show()


# In[10]:


tc = df.corr()
tc


# In[11]:


sns.heatmap(tc, annot = True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




