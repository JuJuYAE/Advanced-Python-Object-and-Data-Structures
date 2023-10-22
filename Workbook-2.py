#!/usr/bin/env python
# coding: utf-8

# In[1]:


hex(10)


# In[2]:


hex(512)


# In[3]:


bin(4)


# In[4]:


2**4


# In[5]:


pow(2,5)


# In[8]:


pow(2,6,2)


# In[9]:


abs(-5)


# In[15]:


round(4.5)


# In[18]:


round(3.1458588,2)


# In[25]:


s = "hello world i am home"


# In[26]:


s.title()


# In[30]:


s.split()


# In[32]:


s


# In[33]:


s.partition("e",)


# In[34]:


s = set()


# In[35]:


s.add(1)


# In[36]:


s.add(2)


# In[37]:


s.add(2)


# In[38]:


s


# In[39]:


s.clear()


# In[40]:


s


# In[41]:


s = {1,2,3}


# In[42]:


sc = s.copy()


# In[43]:


sc


# In[44]:


s.add(5)


# In[45]:


s


# In[46]:


sc


# In[47]:


s.difference(sc)


# In[49]:


s = "hello world i am home"


# In[50]:


s


# In[51]:


s = set(s)


# In[52]:


s


# In[53]:


s.remove(" ")


# In[54]:


s


# In[55]:


s1 = {1,2,3,4,5}


# In[56]:


s2 = {1,2,4}


# In[57]:


s3 = {7}


# In[59]:


s1.isdisjoint(s3)


# In[64]:


s1


# In[65]:


s2


# In[68]:


s2.s(s1)


# In[69]:


d = {"k1":1,"k2":2}


# In[75]:


d.items()


# In[74]:


{x:x**2 for x in range(10)}


# In[ ]:




