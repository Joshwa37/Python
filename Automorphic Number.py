#!/usr/bin/env python
# coding: utf-8

# In[37]:


n=int(input("enter number"))
x=n**2
a=0
l=[]
y=[]
b=[]

d=[]
for i in str(n):
    l.append(i)
    a=a+1
for j in str(x):
    y.append(j)
for k in range(-1,-a,-1):
    b.append(l[k])
    d.append(y[k])

if(b==d):
    print(n,"Automorphic Number")
else:
    print(n,"not an Automorphic Number")


# In[ ]:




