#!/usr/bin/env python
# coding: utf-8

# In[27]:


from typing import Callable
import math
import check

def quartic(x: float) -> float:
    """Return the value of a particular quartic,
    with zeros at 10 and 13, and a max with value x somewhere between x0 and x1."""
    return (x - 7) * (x - 10) * (x - 13) * (x - 14)
check.expect("Q7", quartic(7), 0)
check.expect("Q10", quartic(10), 0)

def smallest_location(f: Callable, x0: int, x1: int) -> int:
    """Return an integer between x0 and x1 inclusive that provides the smallest value of f
    Requires x0 < x1"""
    x0 = x0
    while f(x0) <= f(x0-1):
        x0 = x0 + 1
    return x0

check.expect("LLcos", smallest_location(math.cos, 3, 11), 4)
check.expect("LLquartic", smallest_location(quartic, 8, 19), 9)


# In[ ]:




