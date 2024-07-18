#!/usr/bin/env python
# coding: utf-8

# In[5]:


def twoSum(nums, target):
    i=0
    j=1
    for i in nums:
        for j in nums:
            a=i+j
            if(a==target):
                print("[",i,j,"]")
twoSum([1,2,3,4],3)                
    


# In[ ]:




