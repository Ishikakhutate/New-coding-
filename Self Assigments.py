#!/usr/bin/env python
# coding: utf-8

# In[6]:


list = [1,5,3,2,1,3,5,0,9]
print("The original list:",list)

result = []
for i in list:
    if i not in result:
        result.append(i)
    
print("The new list is:",result)
    

    

    


# In[3]:


test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
 
# printing list after removal
print("The list after removing duplicates : " + str(res))


# In[15]:


#program to find input character is vowel or not
ch = input("enter a character")

if ch in "aeiouAEIOU":
    print("ch is vowel")
else:
    print("ch is not vowel")


# In[17]:


num = input("enter a number")
if len(num)==3:
    print("3 digit number")
else:
    print("is not 3 digit number")


# In[19]:


num = 1
while num<=10:
    print(num,end=" ")
    num+=1


# In[28]:


class Employee:
    def __init__(self,e,n,s):
        self.id=e
        self.name=n
        self.salary=s
        
    def main():
        emp1=Employee(101,"abc",2000)
        emp2=Employee(102,"pqr",4000)
        print(f'{emp1.id},{emp2.name},{emp2.salary}')
    main()
        


# In[2]:


#print number from 1 to 5
n = 1 
num = input("enter a number")
while n <= 50:
    print(n,end=" ")
    n = n+1


# In[2]:


for i in range(1,51):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




