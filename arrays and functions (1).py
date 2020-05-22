#!/usr/bin/env python
# coding: utf-8

# In[4]:


#2nd question part 3

def search(a, k, v):
    if k == len(a):
        print("Not found")
    elif a[k] == v:
        print("found",a[k])

    else:
        print("Recursing")
        return search(a, k + 1, v)

a = [1, 2, 3, 4, 5, 6]
skey = 4
size = len(a)
search(a, 0, skey)

