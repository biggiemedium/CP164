"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-21"
------------------------------------------------------------------------
"""

from List_linked import List

list = List()
list2 = List()
list3 = List()
array = [1, 6, 7, 8, 9, 10]

for i in array:
    list.append(i)
    list2.append(i)
list3.intersection_r(list, list2)

print("Intersecting")
for i in list3:
    print(i)
