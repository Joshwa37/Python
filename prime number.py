#!/usr/bin/env python
# coding: utf-8

# In[4]:


for n in range(2,10):
    for k in range(2,n):
        if n%k==0:
            print(n,"not a prime")
            break
    else:
        print(n,"prime number")


# In[ ]:




