"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-13"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_to_array

stack = Stack()
array = []

for x in range(9):  # iterating 0-8
    stack.push(x)

stack_to_array(stack, array)

print(array)
