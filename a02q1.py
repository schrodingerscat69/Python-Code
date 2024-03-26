#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math  

def f (x: float) -> float:
    """ Return the value of the piece-wise function f(x) at each value of x"""
    
    if x < 3:
        return -2 * x + 4
    elif x >= 3 and x < 5:
        return (x - 7)/2 
    else:
        return x - 6

import check 

check.within("F0", f (0.2), 3.6, 0.0001)
check.within("F1", f (2.0), 0.0, 0.0001)
check.within("F2", f (4.0), -1.5, 0.0001)
check.within("F3", f (9.0), 3.0, 0.0001) 


# In[ ]:




