#!/usr/bin/env python
# coding: utf-8

# In[3]:


#write a program to create students marks dictionary of n students this dict having roll no. as key 2 subject marks as values
n = int(input("Enter the number of students:"))
marks_dict={}
for i in range(n):
    rollno=int(input("enter rollno."))
    sub1=int(input("enter subject1:"))
    sub2=int(input("enter subject2:"))
    marks_dict[rollno]=[sub1,sub2]
    
for rollno,marks in marks_dict.items():
    print(rollno,marks,sum(marks),sum(marks)/2,max(marks),min(marks))
    
    
    
    
    
    
    
    


# In[2]:


#write a program to weather the number entered by user is even or odd
num = int(input("enter a number:"))
r=num%2
if r==0:
     print("number is even")
else:
      print("number is odd")   


# In[1]:


#calculate mean,median using python
#for mean
list = [2,4,77,34,68,90]
mean = sum(list)/len(list)
print(mean)


# In[2]:


#for median
list = [2,4,77,34,68,90]
list.sort()

if len(list)%2==0:
    m1 = list[len(list)//2]
    m2 = list[len(list)//2 + 1]
    median = (m1+m2)/2
else:
    median = list[len(list)+1//2]
print(median)


# In[3]:


#use of enumerate()
saleslist=[4500,3456,7700,1200]
e=enumerate(saleslist,2018)
sales1=next(e)
print(sales1)
sales2=next(e)
print(sales2)
for sales in e:
    print(sales)
    

