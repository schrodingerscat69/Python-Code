#!/usr/bin/env python
# coding: utf-8

# In[5]:


from typing import *
import check

def cascade(pattern: str, start: str) -> List[str]:
    """Return a list by taking start and pattern and transforming start with the next value in pattern
    Requires that characters in pattern do not repeat
    Requires the returned list to not have only blank spaces ' ' """
    counter = 0
    x = list(pattern)
    y = list(start)
    z = [start]
    
    while z[-1] != ' '*len(start):
        e = '' 
        for item in z[-1]:
            if item in pattern: 
                f = pattern.find(item)
                if f == len(pattern)-1 :
                    e = e + ' '
                    counter += 1
                else: 
                    e = e + pattern[f+1]
            else:
                e = e + ' '
                counter += 1
        z.append(e)
    return z[:-1]


## Remember to write additional tests of your own.
check.expect("N0", cascade('Oo.', 'O'), ['O', 'o', '.'])
check.expect("N1", cascade('Oo.', 'o'), ['o', '.'])
check.expect("N2", cascade('Oo.', 'Oo.'), ['Oo.', 'o. ', '.  '])

check.expect("N3", cascade('Xigb:pcTaEnro0', 'Trace program: running'),
["Trace program: running",
 "aoET  co0boE p o rrgrb",
 "E0na  T0 :0n c 0 oobo:",
 "n rE  a  p r T   00:0p",
 "r on  E  c o a     p c",
 "o 0r  n  T 0 E     c T",
 "0  o  r  a   n     T a",
 "   0  o  E   r     a E",
 "      0  n   o     E n",
 "         r   0     n r",
 "         o         r o",
 "         0         o 0",
 "                   0  "]
)


check.expect("N4", cascade("wthraib", "whiterabbit"),
['whiterabbit',
 'trbh ai  bh',
 'ha r ib   r',
 'ri a b    a',
 'ab i      i',
 'i  b      b',
 'b          ']
             )
check.expect("N5", cascade ("pselt", "pastle"), ['pastle', 's e tl', 'e l  t', 'l t   ', 't     '])
check.expect("N6", cascade ("cgreni", "cringe"), ['cringe', 'ge irn', 'rn  ei', 'ei  n ', 'n   i ', 'i     '])


# In[ ]:




