#!/usr/bin/env python
# coding: utf-8

# In[8]:


import array as arr
print("array using array package")
a=arr.array('i',[2,3,4,5])
print(a)

import numpy as np
print("matrix using numpy using list")
b=np.array([[1,2],[3,4]])
print(b)


# In[9]:


import numpy as np
print("matrix using numpy using tuples")
b=np.array(((1,2),(3,4)))
print(b)


# In[10]:


#creating matrix using two predefined functions
A = np.zeros((4,3))
print('A =', A)
B = np.arange(12).reshape(4, 3)
print('B =')
print(B)


# In[11]:


#creating 4x4 matrix
m=[[1,9,5,6],[9,7,6,5],[3,6,4,8],[0,9,6,4]]
a=np.array(m)
print(a)
inv=np.linalg.inv(a)
print(inv)


# In[12]:


norm=np.linalg.norm(a)
print(norm)
reci=a.T
print(reci)


# In[13]:


import math
c=arr.array('d',[1,9,6,5,3])
c1=np.array(c)
reci=np.reciprocal(c)
print(reci)
for i in range(3):
    print("Cot of" ,reci[i],"=",math.atan(reci[i]))
    


# In[14]:


detail=[[1,10000,20,15],[2,5000,28,10],[3,9800,32,12],[4,5600,25,5]]
det=np.array(detail)
print(det)


# In[15]:


age=det[ : ,2]
print(age)
young= age.min()
for i in range(4) :
    if (det[i,2] == young) :
        print("youngest employee",i+1)


# In[16]:


exp=det[ : ,3]
highexp=exp.max()
for i in range(4) :
    if (det[i,3] == highexp) :
        print("Most experienced",i+1)


# In[ ]:


exp=det[ : ,1]
print(exp.sort())

for i in range(3):
    for j in range(3):
        if (exp[i]== det[j,1]):
        print("hello")


# In[ ]:





# In[ ]:




