#!/usr/bin/env python
# coding: utf-8

# In[3]:


#2nd question part a
def taxcalc(x):
    if x<=250000:
        return 0
    elif x<=500000:
        return((x/100)*15)
    elif x<=1000000:
        return((x/100)*10)
    else:
        return((x/100)*30)

christ=[["emp_id","emp_name","annual_salary","tax"],[1,"manoj",150000,0],[2,"deeksha",200000,0],
   [3,"Amala",550000,0],[6,"abhiskeh",470000,0]]
print(christ)
#tax calcuation
for  i in range(len(christ)):
    if i==0:
        continue
    else:
        christ[i][3]=taxcalc(christ[i][2])
print(christ)

#highest tax payer
htpyr=christ[1][3]
postn=1
for  i in range(len(christ)):
        if i==0:
            continue
        if christ[i][3]>htpyr:
            htpyr=christ[i][3]
            postn=i
print("highest tax paying employee is ",christ[postn][1])


# In[ ]:




