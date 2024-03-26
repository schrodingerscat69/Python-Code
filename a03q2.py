#!/usr/bin/env python
# coding: utf-8

# In[12]:


from typing import Callable
import math
import check

def improve_sqrt3(g: float) -> float:
    """With g being a guess for sqrt(3), return a better guess."""
    
    return (g + 3.0 / g) / 2.0

check.within("sqrt3,1", improve_sqrt3(3.0), 2.0, 0.0001)
check.within("sqrt3,2", improve_sqrt3(1.0), 2.0, 0.0001)
check.within("sqrt3,3", improve_sqrt3(1000000.0), 500000.0, 0.0001)


def digit_sum(n: int) -> int:
    """Return the sum of the digits of n.
    Requires: n >= 0.
    """
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

check.expect("DS999...", digit_sum(999999999999993), 129)
check.expect("DS129", digit_sum(129), 12)
check.expect("DS12", digit_sum(12), 3)
check.expect("DS3", digit_sum(3), 3)

def approach10(n: int) -> int:
    """If n is a multiple of 10, return it; otherwise, return 1 less."""
    if n % 10 == 0:
        return n
    else:
        return n - 1

check.expect("43->42", approach10(43), 42)
check.expect("30->30", approach10(30), 30)

def find_fixed_point(f: Callable, x0: float, threshold: float) -> float:
    """Return the fixed point of the function f(x0) until it is less than or equal to the threshold
    Requires x0 >= 0
    Requires threshold >= 0"""
    x = x0
    y = f(x)
    z = f(y)
    
    while abs((z)-(y)) > threshold:
        y = f(z)
        z = f(y)
        
    return z

check.within("FQ2", find_fixed_point(improve_sqrt3, 7.5, 0.00001), 1.732, 0.0001)
check.within("FQ3", find_fixed_point(improve_sqrt3, 3.0, 1.0), 1.75, 0.0001)
check.expect("FD1", find_fixed_point(digit_sum, 999999999999993, 0.0), 3)
check.within("Fsqrt", find_fixed_point(math.sqrt, 1000, 0.00001), 1.0, 0.0001)
check.within("A10", find_fixed_point(approach10, 52, 0.00001), 50, 0.0)
check.within("Ad", find_fixed_point(math.cos, 5.0, 0.00001), 0.739085, 0.0001)
check.expect("FD1", find_fixed_point(digit_sum, 999999999999993, 0.0), 3)
check.within("Fsqrt", find_fixed_point(math.sqrt, 100, 0.00001), 1.00, 0.0001)
check.within("A1", find_fixed_point(approach10, 90, 0.00001), 90, 0.0)


# In[2]:





# In[ ]:





# In[ ]:





# In[ ]:




