#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import *
import check
import numpy as np
import matplotlib.pyplot as plt
import json


def compare(filename:str, c0:str, c1:str)->float:
    """Return the slope (gradient) of the line of best fit from the plot where the x-axis is the c0 dataset and the y-axis is the c1 dataset where c0 and c1 are columns in a filename file"""
    with open (filename, 'r') as myfile:
        data = json.load(myfile)
        xvals = np.array(data[c0])
        yvals = np.array(data[c1])
        plt.plot(xvals,yvals, 'o')
        pfit = np.polynomial.Polynomial.fit(xvals, yvals, 1)
        coefs = pfit.convert().coef
        fitx = np.linspace(min(xvals), max(xvals), 100)
        plt.plot(fitx, coefs[0] + coefs[1] * fitx)
        plt.show()
        return coefs[1]
        
check.within("C0", compare("elements.json", "Na", "Cl"), 2.0, 0.0001)
check.within("C0", compare("elements.json", "Cl", "Na"), 0.5, 0.0001)
check.within("C1", compare("elements.json", "Fe", "Cl"), -0.1514, 0.0001)
check.within("C2", compare("elements.json", "Sn", "Na"), 0.0572, 0.0001)


# In[ ]:




