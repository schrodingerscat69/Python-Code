#!/usr/bin/env python
# coding: utf-8

# In[40]:


import check 

def eutectic(pct_eth:float, temp: float) -> bool:
    """Return the state of the mixture of ethanol (pct_eth) in percentage and water at a given temperature (temp) in Celcius
    Requires temperature <= 0
    Requires percentage of ethanol >= 0 and <= 100"""
    
    if temp<= -118.2:
        return "solid"
    elif ((-114.1<temp> -118.2) <= (4.1/6.9)*(93.1<pct_eth<100)):
        return "slush"
    elif (temp>= (-118.2/93.1)*pct_eth):
        return "liquid"
    elif (temp<= (-118.2/93.1)*pct_eth):
        return "slush"

check.expect("E1", eutectic(60, -140.0), "solid")
check.expect("E2", eutectic(0,0), "liquid")
check.expect("E3", eutectic(98.0, -118.0), "slush")
check.expect("E4", eutectic(45, -10.0), "liquid")
check.expect("E5", eutectic(20, -120.0), "solid")


# In[ ]:





# In[ ]:




