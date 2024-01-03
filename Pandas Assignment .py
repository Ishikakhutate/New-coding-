#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1.	Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd

list1 = pd.Series([2,4,6,7])
list2 = pd.Series([3,8,1,9])
list3 = list1 + list2
print("sum of two series:")
print(list3)
list3 = list1 - list2
print("Sub of two Series:")
print(list3)
list3 = list1*list2
print("Multiplication of two Series:")
print(list3)
list3 = list1//list2
print("Division of two Series:")
print(list3)


# In[9]:


#2.	Write a Pandas program to convert a NumPy array to a Pandas series.
import pandas as pd 
import numpy as np
array1 = np.array([10,20,30,40,50])
print("Given array:",array1)
new_series = pd.Series(array1)
print("Converted Pandas Series:")
print(new_series)


# In[16]:


#3.	Write a Pandas program to get the first 3 rows of a given DataFrame. 
#Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index)
print("First three rows:")
print(df.iloc[:3])


# In[22]:


#4.	Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jones'],
            'score': [12.5, 9, 16.5, np.nan, 9,20,14.5,np.nan,8,19],
            'attempts': [1,3,2,3,2,3,1,1,2,1],
            'qualify': ['yes', 'no','yes','no','no','yes','yes','no','no','yes']}
index = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index)
print("Students score in less than 2 attempts and score greater than 15")
print(df[(df['attempts']<2) & (df['score']>15)])


# In[5]:


#5.	Write a Pandas program to calculate the mean score for each different student in data frame.
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jones'],
            'score': [12.5, 9, 16.5, np.nan, 9,20,14.5,np.nan,8,19],
            'attempts': [1,3,2,3,2,3,1,1,2,1],
            'qualify': ['yes', 'no','yes','no','no','yes','yes','no','no','yes']}
index = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data,index)
print("Mean score for each different students in data frame:")
print(df['score'].mean())


# In[ ]:




