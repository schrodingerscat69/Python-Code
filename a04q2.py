#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import *
import check

def collect(S: str) -> List:
    """Return variables in S (string) separately in a new list"""
    
    new_list = []
    for ele in S:
        if ele not in new_list:
            new_list.append(ele)
    for i in range(0,len(new_list)):
        return new_list
        

    


check.expect("C0", collect("seven"), ['s','e', 'v','n'])
check.expect("C1", collect("money"),
             ['m', 'o', 'n', 'e', 'y'])
check.expect("C2", collect("coins"),
             ['c', 'o', 'i', 'n', 's'])


# In[ ]:




