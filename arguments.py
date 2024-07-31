#!/usr/bin/env python
# coding: utf-8

# In[6]:


#* explain the position argument and store in tuple
#** explain the keyword argument and store in dictionary
def color(*address,**name):
    for k in name:
        print(k,":",name[k])
    for x in address:
        print("Your address is ",address)
color('chennai','tirupur',name='ravi',name2='ram') 


# In[ ]:





# In[ ]:




