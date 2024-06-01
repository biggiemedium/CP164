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
from utilities import stack_to_array

stack = Stack()
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printArray = []

for i in array:
    stack.push(i)

stack.reverse()
stack_to_array(stack, printArray)
print(printArray)
