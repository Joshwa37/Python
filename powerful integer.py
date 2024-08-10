#!/usr/bin/env python
# coding: utf-8

# In[28]:


x=2
y=3
res=[]
bound=10
for i in range(10):
    for j in range(10):
        s = x**i + y**j
        if s <= bound:
            res.append(s)
print(res)            

