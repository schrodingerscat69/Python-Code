#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import *
import check
import math

LLT = Union[int, List['LLT']]

def tree_map(f: Callable, t: LLT) -> LLT:
    """Return a new LLT called t in which each leaf has been transformed by function f
    Requires the new LLT to have the same shape as the original LLT"""
    if isinstance(t,int):
        return f(t)
    
    elif isinstance (t,List):
        for val in range(len(t)):
            t[val] = tree_map(f,t[val])
        return t

def add1(x: int) -> int: 
    """Return 1 more than x."""
    return x + 1
check.expect("add1:0", add1(5), 6)
check.expect("add1:1", add1(0), 1)

def sqr(x: int) -> int: 
    """Return the square of x."""
    return x*x
check.expect("sqr:0", sqr(2), 4)
check.expect("sqr:1", sqr(5), 25)

def double(n: int) -> int: 
    """Return twice n."""
    return n * 2
check.expect("double:0", double(4), 8)
check.expect("double:1", double(6), 12)

check.expect("TM1",
             tree_map(add1, [2, [[4], 6], 0, [1]]), 
             [3, [[5], 7], 1, [2]])
check.expect("TM2",
             tree_map(double, [2, [[4], 6], 0, [1]]), 
             [4, [[8], 12], 0, [2]])
check.expect("TM3", tree_map(sqr, 7), 49)
check.expect("TM4", tree_map(add1, [[[[[[[7]]]]]]]), 
             [[[[[[[8]]]]]]])   

check.expect("mytest1", tree_map(sqr, [2, [3,7], 6]), [4, [9, 49], 36])
check.expect("mytest2", tree_map(add1, [2, [3,7], 6]), [3, [4,8], 7])
check.expect("mytest3", tree_map(double, [2, [3,7], 6]), [4, [6, 14], 12])

