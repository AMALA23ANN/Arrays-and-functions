#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1st question part c
a=[["emp_id","emp_name","emp_salary","emp_age","emp_exp"],[1,"Manoj",25,30000,2],[2,"Teena",21,10000,1],
   [3,"himous",53000,41,20],[6,"hatriya",47000,44,8]]
print(a)
postn=1
lage=a[1][2]
mexp=a[1][4]
#youngest employee
for  i in range(len(a)):
        if i==0:
            continue
        if a[i][2]<lage:
            lval=a[i][2]
            postn=i
print("youngest employee is ",a[postn][1])

#experience
postn=1
for  i in range(len(a)):
        if i==0:
            continue
        if a[i][4]>mexp:
            mexp=a[i][4]
            postn=i
print("most experienced employee is ",a[postn][1])

#avg salary of employees age btwn 40 and 50
tsal=0
nemp=len(a)-1
for i in range(len(a)):
    if i==0:
        continue
    if 40<=a[i][3]<=50:
        tsal+=a[i][2]
avgsal=tsal/nemp
print("avg salary of employees between age 40 and 50 is : ",avgsal)


# In[ ]:




