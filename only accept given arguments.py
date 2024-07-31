#!/usr/bin/env python
# coding: utf-8

# In[13]:


#/ only accept the position argument
#* only accept the keyword argument
def color(address,/,*,name):
    print("Your name is ",name)
    print("Your address is ",address)
color('chennai',name='ravi')


# In[14]:


def color(address,/,*,name):
    print("Your name is ",name)
    print("Your address is ",address)
color(address='chennai',name='ravi')


# In[ ]:




