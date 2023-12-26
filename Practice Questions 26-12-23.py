#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a program to print version you are using 
import sys
print("python version")
print("sys.version")
print("Version_info")
print(sys.version_info)


# In[5]:


#Write a program to print current date and time 
import datetime
now = datetime.datetime.now()
print("Current date and time:",now)


# In[6]:


#Write a python Program which accepts the radius of circle from user and compute the area 
r = float(input("enter radius:"))
area = 3.14*r*r
print("Area of Circle",area)


# In[4]:


#Write a Python Program which accepts the user's first and last name and print them in reverse order with a space between them
def reversethestring():
    first_name=input("enter first name")
    last_name=input("enter last name")
    return last_name[::-1],first_name[::-1]
reversethestring()


# In[7]:


#Write a Python Program which accepts a sequence of comma separated numbers from user and generate a list from those number 
values = input("Input some comma separated numbers:")
list1 = values.split(",") #split string into list
print(list1)


# In[12]:


#write a python program to accept a filename from the user and print the extension of that
file_name=input("Enter the name of file:")
a = file_name.split(',')
print(a[1])


# In[14]:


#Write a python Program to Print first and last color from the list
color_list = ['red','blue','orange','white']
print(color_list[0])
print(color_list[-1])


# In[23]:


#Write a python program that accepts an integer(n) and computes the value of n+nn+nnn
x = int(input("Enter integer"))
n1 = int("%s" % (x))
n2 = int("%s%s" % (x, x))
n3 = int("%s%s%s" % (x,x,x))
print(n1 + n2 + n3,end = '')


# In[2]:


#Python program to find a sum of array 
import numpy as np 
def sumofarray(b):
    add = 0
    for i in b:
        add = add+i
    return add
sumofarray(np.array([1,2,3]))


# In[ ]:




