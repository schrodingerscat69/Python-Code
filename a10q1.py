#!/usr/bin/env python
# coding: utf-8

# In[5]:


import check
runtimes = ("1", "log n", "sqrt n", "n", "n**2", "n**3", "2**n")

##def f1(L):
    # if len(L) == 0:
    #     return ""
    # else:
    #     return f1(L[1:]) + f1(L[:-1])
r1 = "2**n"
e1 = """len function has order 2**n due to the 2 recursive calls (2T(n-1)) and slicing done (O(n))"""
# check.expect("f1", r1 in runtimes, True)


##def f2(L):
    # ans = 1
    # for x in L[:min(len(L), 16)]:
    #     ans = ans + L.pop(0) 
    # return ans
r2 = "n"
e2 = """the L.pop(0) runs on O(n) and the for loop runs on O(1)"""
# check.expect("f2", r2 in runtimes, True)


#def f3(L):
#     ans = 0
#     while L != []: ## O(n)
#         ans = ans + L[0] ## O(n)
#         L.pop()##O(1)
        
#     return ans > 100 
r3 = "n"
e3 = """The while loop will run O(n) times until L is empty, and updating ans will happen O(n) 
times in the while loop"""
# check.expect("f3", r3 in runtimes, True)


# In[ ]:




