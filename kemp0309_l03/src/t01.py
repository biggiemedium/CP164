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
from utilities import array_to_pq

file = open("movies.txt", 'r')
pq = Priority_Queue()
array = file.readlines()
array_to_pq(pq, array)
for i in range(len(pq)):
    print(i)
