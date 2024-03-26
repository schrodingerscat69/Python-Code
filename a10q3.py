#!/usr/bin/env python
# coding: utf-8

# In[4]:


import check
from typing import *

def slowfunc(oldlist: List[int]) -> List[int]:
    """Do what it does with oldlist."""
    ans = []

    for i in range(2):
        extralist = oldlist[:]
        for i in range(len(extralist)):
            x = extralist.pop(0)
            ans = ans + [x, x**2]
            
    return ans

check.expect("SF0", slowfunc([]), [])
check.expect("SF1", slowfunc([1]), [1,1,1,1])


def fastfunc(oldlist: List[int]) -> List[int]:
    """Do what slowfunc does with oldlist."""
    ans = []
    for i in range(len(oldlist)):
        x = oldlist[i]
        ans.append(x)
        ans.append(x**2)
    return ans + ans
    
check.expect("FF0", fastfunc([]), [])
check.expect("FF1", fastfunc([1]), [1,1,1,1])
check.expect("FF == SF 0", fastfunc([1, 1]), slowfunc([1, 1]))

l1= [1,2,3]
check.expect("mytest1", fastfunc(l1), [1, 1, 2, 4, 3, 9, 1, 1, 2, 4, 3, 9])
check.expect("mytest2", fastfunc(l1), slowfunc(l1))


# In[ ]:




