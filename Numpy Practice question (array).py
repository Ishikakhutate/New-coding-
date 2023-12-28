#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


#create empty array 
empty_arr = np.empty((3,4))
print(empty_arr)


# In[11]:


#create numpy array filled with all zeros 
arr = np.zeros((1,5))
print(arr)


# In[12]:


arr = np.zeros((3,5))
print(arr)


# In[23]:


#write a program of array filled with zeros
arr = np.zeros((3))
print("The matrix is:",arr)

arr2 = np.zeros((2,4))
print("The matrix is:",arr2)


# In[28]:


#check wheather numpy array contains specified row
arr = np.array([[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       ])
print(arr)


# In[30]:


print(arr)
print([1,2,3,4,5]in arr. tolist())


# In[31]:


print(arr)
print([23,4,5,8,11]in arr. tolist())
print([23,56,88,11]in arr. tolist())
print([6,7,8,9,10]in arr. tolist())


# In[39]:


#how to remove rows in numpy array that contains non numeric value :
n_arr = np.array([[1,2,3,4,5],
                  [6,8,9,11,3],
                  [32,np.nan,4,np.nan,np.nan],
                  [23,11,np.nan,5,6]
                 ])
print("Given array:")
print(n_arr)

print("\n Remove all rows contatining non numeric elements")
print(n_arr[~np.isnan(n_arr).any(axis=1)])


# In[41]:


#reverse a numpy array using flip()
arr1 = np.array([1,2,3,4,5])
res = np.flip(arr1)
print("Reverse of array:",res)


# In[2]:


#reverse a numpy array using slicing 
import numpy as np
arr1 = np.array([2,4,6,8,10])
res = arr1[::-1]
print('Reverse of array:',res)


# In[57]:


arr = np.array([[[2,2,2],[2,2,2]]])
print("initial array",arr)
print("Shape of array",np.shape(arr))

output_arr =np.squeeze(arr)
print("Output",output_arr)
print("Shape",np.shape(output_arr))


# In[71]:


arr = np.array([[2, 8, 9, 4],  
                   [9, 4, 9, 4], 
                   [4, 5, 9, 7], 
                   [2, 9, 4, 3]]) 
  
# Counting sequence 
output = repr(arr).count("9, 4") 
print(output) 


# In[2]:


import numpy as np
ini_array = np.array([1, 2, 3, 6, 4, 5])
 
# printing initial ini_array
print("initial array", str(ini_array))
 
# printing type of ini_array
print("type of ini_array", type(ini_array))
 
# using shortcut method to reverse
res = ini_array[::-1]
 
# printing result
print("final array", str(res))


# In[4]:


np.full((3,2),5)


# In[ ]:





# In[ ]:





# In[ ]:




