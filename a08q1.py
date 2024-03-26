#!/usr/bin/env python
# coding: utf-8

# In[20]:


from typing import *
import check
import math

class Mover:
    """Describe a Mover"""
    x:float
    y:float
    pathX:List[float]
    pathY:List[float]
    l:float
    
    def __init__(self, newX:float, newY:float):
        """Initialize self, newX and newY
        Requires newX and newY to be any numbers"""
        self.l=0
        nX = [newX]
        nY = [newY]
        self.x = newX
        self.y = newY
        self.pathX = nX
        self.pathY = nY
        
    def move(self, dx:float, dy:float)->None:
        """Map dx and dy onto self while updating l """
        self.l += distance(self.x, self.y,self.x+dx,self.y+dy)
        self.x += dx
        self.y += dy
        self.pathX.append(self.x)
        self.pathY.append(self.y)
        
    def length(self)->float:
        """Return the total length travelled"""
        return float(self.l)
        
        
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the  distance between (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

check.within("D0", distance(100.0, 100.0, 103.0, 104.0), 5.0, 0.0001)
check.within("D1", distance(200.0, 200.0, 201.0, 201.0), 1.4142, 0.0001)


mymover = Mover(10.0, 20.0)
check.expect("P0", (mymover.pathX, mymover.pathY), ([10.0],[20.0]))
check.within("Length: 0", mymover.length(), 0.0, 0.0001)
check.expect("I Like to Move It: 0", mymover.move(3.0, 4.0), None)
check.expect("P1", (mymover.pathX, mymover.pathY), ([10.0, 13.0], [20.0, 24.0]))
check.within("Length: 1", mymover.length(), 5.0, 0.0001)
check.expect("I Like to Move It: 1", mymover.move(7.0, 0.0), None)
check.expect("P2", (mymover.pathX, mymover.pathY), ([10.0, 13.0, 20.0], [20.0, 24.0, 24.0]))
check.within("Length: 2", mymover.length(), 12.0, 0.0001)
check.expect("I Like to Move It: 2", mymover.move(1.0, 1.0), None)
check.expect("P3", (mymover.pathX, mymover.pathY), ([10.0, 13.0, 20.0, 21.0],[20.0, 24.0, 24.0, 25.0]))
check.within("Length: 3", mymover.length(), 13.4142, 0.0001)


mymover1 = Mover(20.0, 21.0)
check.expect("P01", (mymover1.pathX, mymover.pathY),([20.0], [20.0, 24.0, 24.0, 25.0]))
check.expect("I Like to Move It: 4", mymover1.move(1.0, 1.0), None)
check.expect("P69", (mymover1.pathX, mymover1.pathY), ([20.0, 21.0], [21.0, 22.0]))
check.within("Length: 4", mymover1.length(), 1.4142, 0.0001)


# In[ ]:




