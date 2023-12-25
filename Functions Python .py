#!/usr/bin/env python
# coding: utf-8

# In[3]:


#palindrome program 
n = int(input("enter the number"))
temp = n
rev = 0
while(n>0):
    digit = n%10
    rev = rev*10+digit
    n = n//10
if(rev == temp): 
    print("Number is Palindrome")
else:
    print("Number is not a Palindrome")


# In[7]:


#write a python function to find the maximum of three 
list = [22,25,1]
print(max(list))


# In[13]:


#write a python program to find the maximum of three using if else
num1 = 10
num2 = 23
num3 = 41

if(num1 >=num2 and num1>=num3):
    print("10 is greater")
elif(num2>=num1 and num2>=num3):
        print("23 is greater")
else:
        print("41 is greater")


# In[1]:


#Write a python function to sum all the numbers in list
list = [8,2,3,0,7]
total = sum(list)
print("sum of all numbers in list:",total)


# In[4]:


#Write a python function to sum all the numbers in list
total = 0
ele = 0
List1 = [8,2,3,0,7]
while(ele < len(List1)):
    total = total + List1[ele]
    ele += 1
    
print("Sum of elements in list:",total)


# In[19]:


#reverse a string 

def reverse(string):
    
    string = string [::-1]
    return string 
s = "123abc"
print("enter the reverse string",end='') #imp line (end="")
print(reverse(s))  


# In[16]:


#Python function to calculate factorial of a number
num =int(input("enter a number:"))
factorial = 1
if num < 0 :
    print("The factorial of negative is not possible.")
elif num == 0:
    print("The Factorial of zero is 1.")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial", num ,"is" ,factorial)
        


# In[ ]:




