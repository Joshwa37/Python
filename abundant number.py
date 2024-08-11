#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=int(input("enter the number"))
a=0
for i in range(1,n):
    if(n%i==0):
        a=a+i
if(a>n):
    print(n,"It is Abundant Number")
else:
    print(n,"It is not Abundant Number")
        


# In[ ]:




