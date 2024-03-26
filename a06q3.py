#!/usr/bin/env python
# coding: utf-8

# In[3]:


from typing import *
import check
import json
import csv


def alchemy(csvfilename:str, jsonfilename:str) -> None:
    """Copy the data from the csvfilename csv and write it on the jsonfilename json, returning none"""
    data = {}
    with open(csvfilename, 'r') as myfile:
        myfile = csv.DictReader(myfile)
        for line in myfile:
            for key in line:
                if key not in data:
                    data[key] = []
                data[key].append(float(line[key]))

    with open(jsonfilename, 'w') as secondfile:
        secondfile.write(json.dumps(data))
            

check.expect("A0", alchemy('elements.csv', 'test-output.json'), None)

with open('test-output.json', 'r') as myfile:
    data = json.load(myfile)
check.expect("A0b", data,
             {'Na': [2.1, 4.5, 6.3, 0.1, 1.5],
              'Sn': [6.4, 13.6, 19.0, 0.4, 4.6],
              'Fe': [18.54, 29.35, 35.23, 64.26, 44.35],
              'Cl': [4.2, 9.0, 12.6, 0.2, 3.0]})

check.expect("A1", alchemy('elephants.csv','test1-output.json'), None)

with open('test1-output.json', 'r') as myfile1:
    data = json.load(myfile1)
check.expect("A1b", data, {'Jumbo': [1.1, 1.2, 1.3], 'Dumbo': [4.5, 4.6, 4.7], 'Lego': [7.6, 7.7, 7.8]})

check.expect("A2",alchemy('eleven.csv','test2-output.json'),None)

with open('test2-output.json', 'r') as myfile2:
    data = json.load(myfile2)
check.expect("A2b", data, 
             {'Armstrong': [4.85, 7.35, 2.75, 6.35, 7.36, 3.58, 3.24], 'Aldrin': [2.63, 3.67, 3.76, 2.33, 7.2, 8.53, 2.75], 'Collins': [6.25, 2.47, 5.25, 8.35, 1.35, 4.46, 3.46]})
    


# In[ ]:





# In[ ]:




