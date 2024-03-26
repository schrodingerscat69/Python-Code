#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math

def inside_one (xp: bool, yp: bool, x0: float, y0: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
    """Return True if point (xp, yp) is inside one rectangle from (x0,y0) to (x1,y1) oe if it is inside another rectangle (x2,y2) to (x3,y3) and False if (xp, yp) is inside both rectangles or outside the edge of any rectangles or none"""
    if y0 > y1:
        shoot=y0
        y0=y1
        y1=shoot
        
    elif x0 > x1:
        shoot=x0
        x0=x1
        x1=shoot
    
    if y2 > y3:
        shoot=y2
        y2=y3
        y3=shoot
    elif x2> x3:
        shoot=x2
        x2=x3
        x3=temp
    if (y0 <= yp <= y1 and x0 <= xp <=x1) and (y2 <= yp <= y3 and x2 <= xp <= x3):
        return False
    elif y0 <= yp <= y1 and x0 <= xp <= x1:
        return True
    elif y2 <= yp <=y3 and x2 <= xp <= x3:
        return True
    else:
        return False
    
import check 
check.expect("I1", inside_one(2.8,3.0, 2.3,2.4, 6.2,6.6, 4.5,8.2, 7.7,4.0), True)
check.expect("I2", inside_one(2.5,2.6, 2.8,5.0, 6.2,7.0, 5.8,8.2, 7.5,5.4), False)
check.expect("I3", inside_one(8.0,4.9, 2.2,2.3, 6.1,6.5, 4.4,8.3, 7.8,3.9), False)


# In[ ]:




