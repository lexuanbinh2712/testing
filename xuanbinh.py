#!/usr/bin/env python
# coding: utf-8

# In[15]:


def sumx(lst):
  for num in lst:
    yield num**2


# In[48]:


x = sumx([1,2,3])
for value in x:
    print(value)


# In[49]:


def tong(*input):
    s= 0
    for x in input:
        yield s+x


# In[55]:


t=tong()
next(t)
print(t.send(1,2,3))


# In[32]:


def 


# In[45]:


def gen():
    while 1:
        x =yield
        yield x**2


# In[56]:


g=gen()
next(g)
print(g.send(2))
next(g)
print(g.send(5))


# In[105]:


def tb(number):
    return (sum(number)/len(number))
    


# In[109]:


import numpy


# In[112]:


a=[1,2,3]
numpy.mean(a)


# In[122]:


a=[lambda:2**2,lambda x:x**3,lambda x:x**4]


# In[126]:


print(a[1](3))


# In[127]:


def xb(a,x):
    return lambda a, x: a + x


# In[146]:


c = lambda a,b: a + b
print(c('binh',' dep trai'))


# In[ ]:




