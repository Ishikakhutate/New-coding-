#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Replace NumPy array elements that doesn’t satisfy the given condition
import numpy as np
n_arr = np.array([ 122.4467 , 54.2345, 89.4567, 50.1234])
print("Given array:",n_arr)
print("Replace element in between 50. to 90.")
n_arr[n_arr > 90.] = 15.0 
print("new array:")
print(n_arr)


# In[16]:


#Multiplication of p and q matrix 
p = np.matrix([[2,3] ,[4,5]])
q =np.matrix ([[3,2] , [6,3]])
print( "Matrics 1")
print(p)
print("Matrics 2")
print(q)
print("Multiplication of p and q:")
res = np.dot(p,q)
print(res)


# In[35]:


# create an array of 10 zeros
import numpy as np
arr = np.zeros((10))
arr


# In[36]:


#create an array of 10 ones
import numpy as np 
arr = np.ones(10)
arr


# In[17]:


#create an array of 10 five 
arr = np.ones(10)
arr = arr*5
print("Array:",arr)


# In[37]:


#create an array of integer from 10 to 50
import numpy as np
arr = np.arange(10,51)
print("Array of integer from 10 to 50:")
arr


# In[6]:


#create an array of even numbers from 10 to 50 
arr = np.arange(10,51,2)
print("Even numbers from 10 to 50:")
print(arr)


# In[12]:


#create 3*3 matrix ranging from 0 to 8 
arr = np.arange(0,9).reshape(3,3)
print('Matrix ranging from 0 to 9:')
print(arr)


# In[16]:


#create a 3*3 matrix 
array = np.eye(3)
print(array)


# In[2]:


import numpy as np
arr = np.arange(0.01,1.01,0.01).reshape(10,10)
arr


# In[9]:


arr = np.linspace(0.01,1,100).reshape(10,10)
arr


# In[27]:


#use numpy to generate random number between 0 & 1
arr = np.random.rand()
print("array:",arr)


# In[33]:


#use a numpy to generate array of 25 random numbers sampled from standard normal distribution 
arr = np.random.randn(25)
arr


# In[50]:


#create an array of 20 linearly spaced points between 0 and 1
arr=np.linspace(0,1,20)
arr


# # Numpy and Indexing 

# In[4]:


arr = np.arange(1,26).reshape(5,5)
arr


# In[60]:


arr1 = arr[2:,1:]
arr1


# In[63]:


arr2 = arr[3,4]
arr2


# In[7]:


arr3 = arr[:3,1].reshape(-1,1)  #built in function verticle then use (-1,1) 1 indicates 1 column 
arr3


# In[66]:


arr4 = arr[4]
arr4


# In[67]:


arr5 = arr[3:]
arr5


# In[68]:


#Get the sum of all value in mat 
array = np.sum(arr)
array


# In[69]:


#Get standard deviation of values in mat 
array = np.std(arr)
array


# In[71]:


#Get sum of all columns in matrics 
array = np.sum(arr , axis =0) #column axis = 0 
array


# In[ ]:




