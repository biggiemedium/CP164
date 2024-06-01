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
from utilities import pq_to_array


file = open("movies.txt", 'r')
array = file.readlines()
array1 = []
pq = Priority_Queue()
for x in array:
    pq.insert(x.strip())

pq_to_array(pq, array1)

for i in array1:
    print(i)
