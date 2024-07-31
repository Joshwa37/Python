#!/usr/bin/env python
# coding: utf-8

# In[1]:


#shallow copy affect the two varianbles
a=[1,2,3,4,5,6]
b=a
print(b)


# In[4]:


a.append(8)
a.pop()
print(b)
b.append(9)
print(a,b)


# In[5]:


#how to correct shollow copy
c=[1,2,3,4,5,6,7]
d=c.copy()
print(d)


# In[6]:


c.append(9)
d.pop()
print(c,d)


# In[ ]:




