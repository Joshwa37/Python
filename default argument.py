#!/usr/bin/env python
# coding: utf-8

# In[2]:


def color(licence,age=21,address='chennai'):
    replay=licence
    if replay in {'y','yes','ok'}:
        print("Your age is ",age)
    if replay in {'n','no','none'}:
        print("Your address is ",address)
    if replay is None:
        raise ValueError('invalid user')
color('y')


# In[ ]:





# In[ ]:




