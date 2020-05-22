#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1st question part b
import numpy as np
from numpy.linalg import inv
#creating 4x4 matrix
A= np.arange(4, 1).reshape(3,4)
print(A)

#Inverse of a matrix
ainv = inv(np.matrix(A))
print("\n")
print(ainv)

#Normalisation of the matrix
x= np.random.random((1,4))
print("\nOriginal Array:")
print(x)
xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin)
print("\nAfter normalization:")
print(x)

#Compute the reciprocal array from the original array
y= np.random.random((2,2))
print("\nArray:")
print(y)
reci = np.reciprocal(y)  
print ("\nReciprocated array : ", reci)  

#Calculating cot theta for the first three elements 
y= np.random.random((2,2))
print("\nArray:")
print(y)
z=np.arctan(y[0,:3])
print("\nCot Theta values of the first three elements")
print(z)


# In[ ]:




