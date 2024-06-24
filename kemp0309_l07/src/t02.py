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

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in array:
    list.append(i)

target1, target2 = list.split_alt_r()

for i in target1:
    print(i)

for i in target2:
    print(i)
