#!/usr/bin/env python
# coding: utf-8

# In[9]:


from typing import *
import check
import math

class Family:
    """Store information about the Family of a person.""" 
    name: str
    children: List['Family']

    def __init__(self, name: str, children: List['Family']):
        self.name = name
        self.children = children

    def __repr__(self) -> str:
        return "Family('{}', {})".format(self.name, self.children)


def farthest_child(fam: Family) -> List[str]:
    """Return a list of names of chilren in Family fam starting from the leaf farthest from the root"""
    l = []
    if fam.children == []:
        return [fam.name]
    else:
        for child in fam.children:
            a = farthest_child(child)
            if len(a) >= len(l):
                l = a
        return l + [fam.name]

check.expect("leaf", farthest_child(Family("Robb", [])), ["Robb"])
check.expect("leaf", farthest_child(Family("Sansa", [])), ["Sansa"])

tully = Family('Hoster',
                 [Family('Lysa',
                         [Family('Robin', [])]),
                  Family('Edmure', []),
                  Family('Catelyn',
                         [Family('Robb', []),
                          Family('Sansa', []),
                          Family('Arya', []),
                          Family('Bran', []),
                          Family('Rickon', [])])])
check.expect("tully", farthest_child(tully), ["Rickon", "Catelyn", "Hoster"])

example1 = Family('Ann',
                  [Family('Bob', [
                      Family('Cy', [Family('Di',[]),
                                    Family('Ed',[Family('Ollie', [])]),
                                    Family('Fox',[])]),
                      Family('Glen', [])]),
                   Family('Hi', [
                       Family('Io', [Family('Jo',[Family('Nat', [])]),
                                     Family('Kim',[]),
                                     Family('Li',[])]),
                       Family('Mo', [])])])

check.expect("ann", farthest_child(example1), 
             ["Nat", "Jo", "Io", "Hi", "Ann"])

myf = Family('Sunil',[Family ('Gita', [Family ('Mann',[])])])
check.expect("myf", farthest_child(myf), ['Mann', 'Gita', 'Sunil'])

myf2 = Family('Sunil',[Family ('Gita', [Family ('Mann',[]),Family('Mega',[]), Family('Piya', [])])])
check.expect("myf2", farthest_child(myf2), ['Piya', 'Gita', 'Sunil'])


# In[ ]:




