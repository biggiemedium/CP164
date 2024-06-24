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

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in array:
    list.append(i)
    list2.append(i)

print(list.is_identical_r(list2))
list.remove(1)
print(list.is_identical_r(list2))
