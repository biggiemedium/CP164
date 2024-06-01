"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-22"
------------------------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test

file = open("movies.txt", 'r')
array = file.readlines()
pq = Priority_Queue()
priority_queue_test(array)
