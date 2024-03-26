#!/usr/bin/env python
# coding: utf-8

# In[28]:


from typing import*
import check

def reverse_alphabet (elements:Tuple[str,str,float])->Tuple[str,str,float]:
    """Order the dictionary in reverse alphabetical order using the second string(elements) in the tuple """ 
    return elements[1]
check.expect("t0", reverse_alphabet(students),('Ebube', 'waffles', 9.9))
check.expect("t1", reverse_alphabet(countries),('Rayray', 'Egypt', 18))
check.expect("t2", students, [("Eden", "waffles", 2.5),("Ebube", "waffles", 9.9),("Mann", "pizza", 10.0),("Sarah", "apples", 7.5),("Safa", "apples", 15.6)])
check.expect("t3", countries, [('Mann', 'Tanzania', 19), ('Rayray', 'Egypt', 18), ('Ashmita', 'Canada', 17), ('Angela', 'Canada', 18)])
    
def ascending_order (numbers:Tuple[str,str,float])->Tuple[str,str,float]:
    """Order the numbers in Tuple in ascending numerical order"""
    return numbers[2]
check.expect("t4", ascending_order(students),('Mann', 'pizza', 10.0))
check.expect("t5", ascending_order(countries),('Ashmita', 'Canada', 17))
check.expect("t6", students,[('Eden', 'waffles', 2.5), ('Ebube', 'waffles', 9.9), ('Mann', 'pizza', 10.0), ('Sarah', 'apples', 7.5), ('Safa', 'apples', 15.6)]) 
check.expect("t7", countries,[('Mann', 'Tanzania', 19), ('Rayray', 'Egypt', 18), ('Ashmita', 'Canada', 17), ('Angela', 'Canada', 18)])

def groups_by_mass(tuples: List[Tuple[str,str,float]]) -> None:
    """Sort the tuples in reverse alphabetical order and in ascending order for the numbers"""
    tuples.sort(key = ascending_order)
    tuples.sort(key = reverse_alphabet, reverse=True)

element_list = [("Ne","noble", 20.180),
                ("O","nonmetal", 15.999),
                ("Li","alkali", 6.94),
                ("H","metalloid", 1.008),
                ("N","nonmetal", 14.007),
                ("B","post-transition", 10.81),
                ("He","noble", 4.0026),
                ("C","nonmetal", 12.011),
                ("F","nonmetal", 18.998),
                ("Be","alkaline earth", 9.0122)]
check.expect("GM1", groups_by_mass(element_list), None)
check.expect("GM1m", element_list,
 [('B', 'post-transition', 10.81),
  ('C', 'nonmetal', 12.011),
  ('N', 'nonmetal', 14.007),
  ('O', 'nonmetal', 15.999),
  ('F', 'nonmetal', 18.998),
  ('He', 'noble', 4.0026),
  ('Ne', 'noble', 20.18),
  ('H', 'metalloid', 1.008),
  ('Be', 'alkaline earth', 9.0122),
  ('Li', 'alkali', 6.94)]
             )

komponents = [
    ("Mk16 Parachute", "parachute", 0.1),
    ("PB-X150 Xenon Container", "xenon tank", 0.1),
    ("Mk1 Lander Can", "pod", 0.66),
    ("GRAVMAX Negative Gravioli Detector", "sensor", 0.005),
    ("TS-12 Stack Separator", "coupling", 0.05),
    ("SC-9001 Science Jr.", "sensor", 0.2),
    ('RT-5 "Flea" Solid Fuel Booster', "booster", 1.50),
    ("Mk1 Command Pod", "pod", 0.84),
    ('RT-10 "Hammer" Solid Fuel Booster', "booster", 3.56),
    ("Heat Shield (1.25m)", "thermal", 0.3)]
check.expect("GM2", groups_by_mass(komponents), None)
check.expect("GM2m", komponents,
             [('PB-X150 Xenon Container', 'xenon tank', 0.1),
              ('Heat Shield (1.25m)', 'thermal', 0.3),
              ('GRAVMAX Negative Gravioli Detector', 'sensor', 0.005),
              ('SC-9001 Science Jr.', 'sensor', 0.2),
              ('Mk1 Lander Can', 'pod', 0.66),
              ('Mk1 Command Pod', 'pod', 0.84),
              ('Mk16 Parachute', 'parachute', 0.1),
              ('TS-12 Stack Separator', 'coupling', 0.05),
              ('RT-5 "Flea" Solid Fuel Booster', 'booster', 1.5),
              ('RT-10 "Hammer" Solid Fuel Booster', 'booster', 3.56)])
students = [
    ("Mann", "pizza", 10.0),
    ("Safa", "apples", 15.6),
    ("Sarah", "apples", 7.5),
    ("Ebube", "waffles", 9.9),
    ("Eden", "waffles", 2.5)]
check.expect("T1", groups_by_mass(students), None)
check.expect("T2", students, 
             [("Eden", "waffles", 2.5),
              ("Ebube", "waffles", 9.9),
              ("Mann", "pizza", 10.0),
              ("Sarah", "apples", 7.5),
              ("Safa", "apples", 15.6),])

countries = [
    ("Mann", "Tanzania", 19),
    ("Angela", "Canada", 18),
    ("Ashmita", "Canada", 17),
    ("Rayray", "Egypt", 18)]
check.expect("T3", groups_by_mass(countries), None)
check.expect("T4", countries, 
             [("Mann", "Tanzania", 19),
               ("Rayray", "Egypt", 18),
              ("Ashmita", "Canada", 17),
              ("Angela", "Canada", 18)])


# In[ ]:





# In[ ]:




