#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

def radius_of_gyration(mass: float, inertia: float) -> float:
    """Return the radius of gyration in m
    Required: mass > 0
    Required: inertia >=0
    """
    return math.sqrt(inertia/mass)
print("The radius of gyration is", radius_of_gyration(20.0, 5.0), "m")

import check 

check.within("T1", radius_of_gyration(2.0, 18.0), 3.0, 0.0001)
check.within("T2", radius_of_gyration(2.0, 50.0), 5.0, 0.0001)


# In[ ]:




