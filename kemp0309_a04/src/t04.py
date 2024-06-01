"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-01"
------------------------------------------------------------------------
"""

from Queue_array import Queue

q1 = Queue()
q2 = Queue()
q3 = Queue()

array = [5, 8, 12, 8]
array2 = [7, 9, 14]

for i in array:
    q1.insert(i)

for i in array2:
    q2.insert(i)

q3.combine(q1, q2)
while not q3.is_empty():
    print(q3.peek())
    q3.remove()
