#!/usr/bin/env python
# coding: utf-8

# In[3]:


import check
import math 

def approx_cosh (x:float, threshold:float) -> float:
    """Return the approximation of cosh (x) with terms that are only bigger than the threshold
    Requires threshold >= 0"""
    
    
    count = 0
    total = 0.0
    term = (x**count)/(math.factorial(count))
    
    while term > threshold:
        count = count + 2
        total = total + term 
        term = (x**count)/(math.factorial(count))   
        
    return total

check.within("AC1", approx_cosh(2.0, 0.05), 3.75555, 0.0001)
check.within("AC2", approx_cosh(2.0, 1.0), 0.0, 0.0001)


# In[ ]:




