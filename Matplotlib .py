#!/usr/bin/env python
# coding: utf-8

# In[3]:


#creating a line plot 
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,4,5,6]
plt.plot(x,y)
plt.show()


# In[4]:


#adding lables and title 
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("My first Plot")
plt.show()


# In[8]:


#customizing a Plot (colours,styles and markers)
plt.plot(x,y,color = 'purple',
        linestyle='--',
        marker='o')
plt.show()


# In[11]:


#creating multiple plots 
plt.subplot(3,4,5)
plt.plot(x,y)
plt.show()
#simple plot line

plt.subplot(2,6,2)
plt.scatter(x,y)

categories = ['A','B','C','D']
values = [67,88,45,22]
plt.subplot(2,1,2)
plt.bar(categories,values)
plt.show()


# In[16]:


#adding annotations 
x = [3,6,9,12,13]
y = [3,6,9,13,16]
plt.plot(x,y)

plt.annotate('Highest Point',xy=(13,16),
            xytext =(12,13),
             arrowprops=dict(facecolor = 'blue',
            arrowstyle='->'))
plt.show()


# In[19]:


#Adding legend 
x = [2,5,7,9,10]
y1 = [3,6,9,12,15]
y2 = [4,8,12,16,20]

plt.plot(x,y1,label='Line1')
plt.plot(x,y2,label ='Line2')
plt.legend()
plt.show()


# In[ ]:




