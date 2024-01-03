#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[17]:


df = sns.load_dataset('car_crashes')


# In[18]:


df


# In[17]:


df.head()


# In[18]:


df.tail()


# In[19]:


df.abbrev.unique()


# In[21]:


df.abbrev.value_counts()


# In[23]:


sns.lineplot( x = 'speeding' , y = 'alcohol' ,data = df , ci = None)
plt.show()


# In[35]:


sns.lineplot( x = 'speeding' , y = 'total', data = df  ,ci = None)
plt.show()


# In[36]:


sns.barplot (x = 'ins_losses', y = 'speeding', data = df)
plt.show()


# In[38]:


sns.histplot( x = 'ins_losses', y = 'speeding', data = df)
plt.show()


# In[40]:


sns.countplot( x = 'ins_losses', data = df)
plt.show()


# In[42]:


sns.boxplot(x = 'alcohol', data = df)
plt.show()


# In[45]:


sns.boxplot(x = 'total', y = 'alcohol',data = df)
plt.show()


# In[47]:


sns.violinplot( x = 'total', y = 'ins_premium',data = df)
plt.show()


# In[49]:


sns.stripplot (x = 'total', y = 'speeding',data = df)
plt.show()


# In[50]:


sns.histplot( x = 'speeding',data = df)
plt.show()


# In[52]:


sns.histplot( x = 'speeding',data = df,kde = True)
plt.show()


# In[21]:


import warnings 
warnings.filterwarnings('ignore')
sns.distplot(df['speeding'],color='y')
plt.show()


# In[22]:


sns.pairplot(data = df)
plt.show()


# In[23]:


tc = df.corr()
tc


# In[24]:


sns.heatmap(tc , annot = True)
plt.show()


# In[30]:


sns.stripplot( x = 'total', y = 'speeding', data= df)
plt.show()
sns.catplot( x = 'total' , y = 'speeding',data = df)
plt.show()
sns.violinplot( x = 'total', y = 'speeding', data = df)
plt.show()


# In[ ]:




