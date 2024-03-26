#!/usr/bin/env python
# coding: utf-8

# In[2]:

from typing import *
import check
import numpy as np
import matplotlib.pyplot as plt
import csv


def plot_categories(filename:str, column:str) -> List[str]:
    """"Return a list of strings from the column called column in the file called filename and plot the x and y columns and return its plot
    Requires that the retured list be organized in alphabetical order and each category should only appear once in the list"""
    list_c = []
    xvals = {}
    yvals = {}
    
    with open (filename, 'r') as myfile:
        myf = csv.DictReader(myfile)
        for line in myf:
            cat = line[column]
            if cat not in list_c:
                list_c.append(cat)
                xvals[cat] = [float(line['x'])]
                yvals[cat] = [float(line['y'])]     
            else:
                xvals[cat].append(float(line['x']))
                yvals[cat].append(float(line['y']))
                        
    for ele in list_c:
        plt.plot(xvals[ele],yvals[ele],'o')
    return(sorted(list_c))
     
check.expect("PC0", plot_categories('happy-halloween.csv', 'zombie'),["eye1", "eye2", "mouth", "outline", "stem"])
check.expect("PC1", plot_categories('happy-halloween.csv', 'spider'),["diamond", "iron"])
check.expect("PC2", plot_categories('tictactoe.csv','ex'),['electron', 'photon', 'positron'])
check.expect("PC3", plot_categories('tictactoe.csv','oh'), ['neutron', 'proton'])
check.expect("PC4", plot_categories('tictactoe.csv','dot'),['down', 'strange', 'up'])


# In[ ]:




