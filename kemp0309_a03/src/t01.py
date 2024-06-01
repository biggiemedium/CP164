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

from functions import stack_split_alt
from Stack_array import Stack

stack = Stack()
stack.push(8)
stack.push(14)
stack.push(12)
stack.push(9)
stack.push(8)
stack.push(7)
stack.push(5)

ss = stack_split_alt(stack)
print(ss)
