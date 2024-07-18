#!/usr/bin/env python
# coding: utf-8

# In[15]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n,"not a prime")
            break
    else:
        print(n,'is a prime number')


# In[ ]:





# In[ ]:




