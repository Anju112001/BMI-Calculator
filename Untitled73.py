#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bmi():
    weight=float(input("enter weight:"))
    height=float(input("enter height:"))

    bmi=weight/height**2
    print(f'your bmi is:{bmi:.2f}')

    if bmi<18.5:
        print("underweight")
    elif 18.5<=bmi<24.9:
        print("normal weight")
    elif 25<=bmi<24.9:
        print("overweight")
    else:
        print("obesity")


# In[ ]:


bmi()


# In[ ]:





# In[ ]:




