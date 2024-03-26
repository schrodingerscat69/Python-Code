#!/usr/bin/env python
# coding: utf-8

# In[15]:


from typing import *
import check
import math


class Chemical:
    """Describe a chemical"""
    formula: Dict[str, int]
    
    def __init__ (self, formula:Dict[str,int]):
        answer= {}
        for i in formula:
            if formula[i] > 0:
                answer[i] = formula[i]
        self.formula = answer
    def __repr__ (self):
        return(sorted(formula))
    
    def __eq__ (self, other: Dict[str, int]):
        return (isinstance(other, Chemical) and self.formula == other.formula)
        
    def __repr__ (self):
        L = []
        for i in self.formula:
            L.append(i)
        L.sort()
        gcd = math.gcd(*self.formula.values())
        e_string= ''
        if gcd > 1:
            e_string = e_string + str(gcd) + '('
        for ele in L:
            e_string = e_string + ele
            if self.formula[ele] // gcd > 1:
                e_string = e_string + str(self.formula[ele]//gcd)
        if gcd > 1:
            e_string = e_string + ')'
        return e_string
    
    def __add__(self, other: "Chemical") -> "Chemical":
        """Add values in self with other if they have the same index, or add a new key if 
        index is in self and not formula"""
        answer = other.formula
        for i in self.formula:
            if i in other.formula:
                answer[i] = self.formula[i] + other.formula[i]
            else:
                answer[i] = self.formula[i]
        return Chemical(answer)
    def __mul__(self, n: int) -> "Chemical":
        """Multiply each index self by n"""
        answer_1 = {}
        for i in self.formula:
            answer_1[i] = self.formula[i] * n
        return Chemical(answer_1)
    
    def __rmul__(self, n: int) -> "Chemical":
        """Define n*self to be the same as self*n."""
        return self * n
    
water = Chemical({'O': 1, 'H': 2})
check.expect("Water is water", water.formula, {'H': 2, 'O': 1})

salt = Chemical({'Na':1, 'Cl':1})
check.expect("Salt is salt", salt.formula, {'Cl':1, 'Na':1})

## Ignore zero values:
helium = Chemical({'He': 1, 'O': 0, 'H': 0})
check.expect("Helium is noble", helium.formula, {'He': 1})

oxygen = Chemical({'Na':0, 'He':0, 'O':2})
check.expect("Oxygen is diatomic", oxygen.formula, {'O':2})

testd = {'T': 1, 'E': 2, 'S': 3, 'D': 4}
test = Chemical(testd)
testd['X'] = 5 # This should mutate testd but not change test.
check.expect("No aliasing", test.formula, {'T': 1, 'E': 2, 'S': 3, 'D': 4})

check.expect("Long names are OK",
             Chemical({'Charlie': 5, 'Brown': 2}).formula,
             {'Charlie': 5, 'Brown': 2})

check.expect("str0", str(Chemical({'O': 1, 'H': 2})), "H2O")
check.expect("str1", str(Chemical({'H': 2, 'O': 1})), "H2O")
check.expect("str2", str(Chemical({'H': 2, 'O': 2})), "2(HO)")
check.expect("str3", str(Chemical({'O': 1, 'H': 4, 'C': 1})), "CH4O")
check.expect("str4", str(Chemical({'C': 6, 'H': 12, 'O': 6})), "6(CH2O)")
check.expect("str5", str(Chemical({'H': 6, 'C': 2})), "2(CH3)")
check.expect("str6", str(Chemical({'O': 4, 'P': 1, 'Li': 3})), "Li3O4P")
check.expect("str7", str(Chemical({'Ag': 1, 'N': 1, 'O': 3})), "AgNO3")
check.expect("str8", str(Chemical({'Ag': 14, 'N': 21, 'O': 7})), "7(Ag2N3O)")
check.expect("str9", str(Chemical({'C': 4, 'H': 10})), "2(C2H5)")

check.expect("str10", str(Chemical({'Na':1,'S':1,'O':4})), "NaO4S")
check.expect("str11", str(Chemical({'O':6, 'S':3})), "3(O2S)")

check.expect("A thing is itself",Chemical({'C': 1, 'O': 1}) == Chemical({'C': 1, 'O': 1}), True)
check.expect("A thing is not something else",Chemical({'C': 1, 'O': 1}) == Chemical({'C': 1, 'O': 2}), False)
check.expect("Water is not wet", water == "wet", False)
check.expect("Equal strings",str(Chemical({'C': 1, 'o': 1})) == str(Chemical({'Co': 1})), True)
check.expect("Different objects",Chemical({'C': 1, 'o': 1}) == Chemical({'Co': 1}), False)

water = Chemical({'H': 2, 'O': 1})
check.expect("3*water", 3*water, Chemical({'H': 6, 'O': 3}))
check.expect("3*water", water*3, Chemical({'H': 6, 'O': 3}))

nitrogen = Chemical({'N':2})
check.expect("2*nitrogen", 2*nitrogen, Chemical({'N':4}))
check.expect("2*nitrogen", nitrogen*2, Chemical({'N':4}))
             
glucose = Chemical({'C': 6, 'H': 12, 'O': 6})
h2gas = Chemical({'H': 2})
o2gas = Chemical({'O': 2})
water = Chemical({'H': 2, 'O': 1})
co2gas = Chemical({'C': 1, 'O': 2})
check.expect("burn glucose",
             glucose + 6*o2gas == 6*co2gas + 6*water, True)
check.expect("burn hydrogen",
             2*h2gas + o2gas == 2*water, True)

ammonia = Chemical({'N':1, 'H':3})
nitrogen = Chemical({'N':2})
hydrogen = Chemical({'H':2})

check.expect("make ammonia", nitrogen + 3*hydrogen == 2*ammonia, True)

hcl = Chemical({'H':1, 'Cl':1})
naoh = Chemical({'Na':1,'O':1,'H':1})
salt= Chemical({'Na':1, 'Cl':1})
water = Chemical({'H': 2, 'O': 1})

check.expect("neutralization", hcl + naoh == salt + water, True)


# In[ ]:




