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
from utilities import array_to_stack

stack = Stack()
array = [
    1, 2, 3, 4, 5, 6, 7, 8, 9]

array_to_stack(stack, array)  # yes

while not stack.is_empty():
    print(stack.pop())
