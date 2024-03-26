#!/usr/bin/env python
# coding: utf-8

# In[2]:

import math
def max_shear (torque: float, moment: float, radius: float) -> float:
    """Return the maximum shear stress in Pa
    
    Requires: torque >= 0
    Requires: moment > 0
    Requires: radius > 0 
    
    """
    return (torque * radius)/ moment
print ("The maximum shear stress is", max_shear (5, 6, 12), "Pa")






# In[ ]:




