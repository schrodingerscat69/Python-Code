#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List 
import check 

def subs(data:List[int], target:int, replacement:int) -> List[int]:
    """Returns a new list with values from data where each value that is equivalent to the target has been replaced by a replacement integer"""
    i = 0
    while i < len(data):
        if data[i] == target:
            data[i] = replacement
        i = i + 1
    return data
            

check.expect("S0", subs([3,1,4,1,5,9,2,6,5,4], 6, 7), [3,1,4,1,5,9,2,7,5,4])
check.expect("S1", subs([3,1,4,1,5,9,2,6,5,4], 5, 22), [3,1,4,1,22,9,2,6,22,4])

def mutate(data:List[int], target:int, replacement:int) -> None:
    """Mutate the data list to replace all values that are equivalent to the target with the replacement"""
    for i in range(len(data)):
        if data[i] == target:
            data[i] = replacement

thing1 = [3,1,4,1,5,9,2,6,5,4]
check.expect("M0a", mutate(thing1, 1, 10), None)
check.expect("M0b", thing1, [3,10,4,10,5,9,2,6,5,4])

thing2 = [3,1,4,1,5,9,2,6,5,4]
check.expect("M1a", mutate(thing2, 5, 7), None)
check.expect("M1b", thing2, [3,1,4,1,7,9,2,6,7,4])


# In[ ]:




