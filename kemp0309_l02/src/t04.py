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
from utilities import stack_test

file = open("movies.txt", 'r')  # must be in '' ??
array = file.readlines()
stack_test(array)
