#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Create Pandas Dataframe from 2D List using pd.DataFrame()

import pandas as pd
list = [['Abc',2],['dfg',3] ,['iop',4]]
df=pd.DataFrame(list,columns = ['Tag','Number'])
print(df)


# In[7]:


#Using Pandas DataFrame to create Dataframe from List
data = {'dictionary': ["Ishika","Isha","Mayank"],
        'Marks': [20,19,2]}
df=pd.DataFrame(data)
print(df)


# In[10]:


#Using Pandas Dataframe with the index parameter 
list = {"Area":["Circle","Rectangle","Square"],
         "Fig_1":[23,61,67],
          "Fig_2":[58,9,44]}
df=pd.DataFrame(list,index=['a','b','c'])
print(df)      


# In[12]:


#reindexing of rows
import numpy as np
import pandas as pd 


# In[21]:


column = ["A","B","C","D","E"]
index = ["a","b","c","d","e"]
df1=pd.DataFrame(np.random.rand(5,5),
                columns=column,index=index)
print(df1)
print("\nReindexing of rows:\n",
df1.reindex(["E","D","C","B","A"]))


# In[ ]:




