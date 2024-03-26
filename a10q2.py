#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import *
import check

# def alan(nums: List[int]) -> List[int]:
#     """Do what it does with nums."""
#     answer = []
#     while nums != []:
#         last = nums.pop()
#         if last % 2 == 0:
#             answer.append(last // 2)
#         else:
#             answer.append(last)
#     return answer

# ## You should write additional tests 
# ## to be certain you understand what alan does.
# check.expect("A0", alan([0]), [0])
# check.expect("A1", alan([2,3,4]), [2, 3, 1])
# check.expect("A2", alan([2,3,5]), [5, 3, 1])
# mylist = [0]
# check.expect("A1", alan(mylist), [0])
# check.expect("A1m", mylist, [])
# check.expect("A2", alan(mylist), [])

def alan_recursive (nums: List[int], answer: List[int]=None)-> List[int]:
    """Return a new list called answer with the order of the list reversed from nums.
    If number is even, divide it by 2,
    if number is odd, append it the same to answer"""
    if answer == None:
        answer =[]
    if nums != []:
        last = nums.pop()
        if last % 2 == 0:
            answer.append(last//2)
        else:
            answer.append(last)
        return alan_recursive(nums, answer)
    else:
        return answer


mylist = [0]
check.expect("Ar1", alan_recursive(mylist), [0])
check.expect("Ar1m", mylist, [])
check.expect("Ar2", alan_recursive(mylist), [])
l1 = [2,3,4,5]
check.expect("mytest1", alan_recursive(l1), [5, 2, 3, 1])
check.expect("mytest2", l1, [])

#check.expect("Ar == A 0", alan_recursive([1, 1]), alan([1, 1]))
    


# In[ ]:




