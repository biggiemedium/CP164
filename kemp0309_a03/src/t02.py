"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-23"
------------------------------------------------------------------------
"""

from Stack_array import Stack

stack = Stack()
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in array:
    stack.push(i)

target1, target2 = stack.split_alt()
print(str(target1))
print(str(target2))
