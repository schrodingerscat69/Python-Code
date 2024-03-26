#!/usr/bin/env python
# coding: utf-8

# In[5]:


from typing import *
import check
import math 
def sqr(n: int) -> int:
    """Return the square of n."""
    return n**2
check.expect("Sqr0", sqr(-2), 4)
check.expect("Sqr1", sqr(-15), 225)
check.expect("Sqr2", sqr(15), 225)

def sqrt(a: int) -> float:
    """Return the square root of a
    Requires a >= 0"""
    return math.sqrt(a)

check.within("t1", sqrt(5), 2.2360, 0.0001)
check.expect("t2", sqrt(9), 3.0)

def find_biggest(f:Callable, vals: List[int]) ->int:
    """Return the largest integer value from the vals list obtained from the callable function,f"""
    x = vals[0]
    for i in vals:
        if f(i) > f(x):
            x = i
    return x
        
check.expect("FB3", find_biggest(sqr, [1, -18, 18, 2]), -18)
check.expect("FB4", find_biggest(sqr, [1, -16, 16, 24]), 24)
check.expect("FB5", find_biggest(sqrt, [2, 5, 10, 25, 9]), 25)
check.expect("FB6", find_biggest(sqrt, [3, 81, 65, 21, 18]), 81)
check.expect("FB7", find_biggest(sqrt, [100, 27, 69, 54, 88]), 100)


# In[ ]:




