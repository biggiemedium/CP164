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

array = [11, 22, 33, 44, 55]

for i in array:
    list.append(i)

list.reverse_r()
for i in list:
    print(i)
