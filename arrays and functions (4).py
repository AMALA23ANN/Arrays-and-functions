#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2nd question part b
# lambda function
#profit and loss
print("Enter buying price and sellng price")
buyp=float(input())
sellp=float(input())
loss=lambda bp,sp: bp-sp
print("Loss is",loss(buyp,sellp))
profit=lambda bp,sp: sp-bp
print("Profit  is",profit(buyp,sellp))

#simple intrest
p=float(input("Simple Intrest \n enter principal"))
r=float(input("Enter rate"))
t=float(input("Enter time"))

si= lambda p,r,t: (p*r*t)/100
print("Simple Intrest ",si(p,r,t))

#compound intrest
p=float(input("Compound Intrest \n enter principal"))
r=(float(input("Enter annual intrest rate (in percent)")))/100
t=float(input("Enter time"))
n=float(input("Number of times intrest is computed"))

pri= lambda p,r,t,n: p*pow((1+(r/n)),n*t)
print("Final Amount :", pri(p,r,t,n))

