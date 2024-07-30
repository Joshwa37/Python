#!/usr/bin/env python
# coding: utf-8

# In[12]:


a=input("enter the first name to find it is an anomlies")
b=input("enter the second name to find it is an anomlies")
c=set(a)
d=set(b)
e=c-d
if(e==set()):
    print("anomalies")
else:
    print(e)
    


# In[ ]:




