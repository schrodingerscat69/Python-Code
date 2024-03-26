#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import *
import check

def make_transformation(pattern: str) -> Dict[str, str]:
    """Return answer with the transformation from a string, pattern, where the index of the dictionary is the next character in pattern"""
    answer={}
    counter = 0
    for i in pattern:
        if counter == len(pattern)-1:
            answer[i] = " "
        else:
            answer[i] = pattern[counter+1]
        counter += 1
    return answer

check.expect("T0", make_transformation("wthraib"),
             {'w': 't',
              't': 'h',
              'h': 'r',
              'a': 'i',
              'r': 'a',
              'i': 'b',
              'b': ' '})
check.expect("T1", make_transformation("Oo."), {'O': 'o', 'o': '.', '.': ' '})
check.expect("T2", make_transformation("hike"),
             {'h':'i',
              'i':'k',
              'k':'e',
              'e': " "})
check.expect("T3", make_transformation("max"), {'m':'a', 'a':'x', 'x':' '})


# In[ ]:




