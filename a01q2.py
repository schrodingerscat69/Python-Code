#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math 

def electrical(speed: float, magnetic: float) -> float:
    """Return the electrical permittivity
     Requires: speed > 0
     Requires: magnetic > 0
     """
    return (1/(magnetic * (speed**2)))
print ("The electrical permitivity is", electrical(3e8, 0.005))

import check
check.within("P1", electrical(5.0, 7.0), 0.005714, 0.0001)
check.within("P2", electrical(2e7, 1e-14), 0.25, 0.0001)


# In[ ]:




