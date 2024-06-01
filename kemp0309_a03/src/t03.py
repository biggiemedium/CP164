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
from functions import stack_reverse
from utilities import stack_to_array

stack = Stack()
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array1 = []

for i in array:
    stack.push(i)

stack_reverse(stack)
stack_to_array(stack, array1)


print(array1)
