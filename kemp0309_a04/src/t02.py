"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-31"
------------------------------------------------------------------------
"""
from Queue_array import Queue

q1 = Queue()
q2 = Queue()

array = [1, 2, 3, 4, 5]

for i in array:
    q1.insert(i)
    q2.insert(i)

yes = q1 == q2
print(f"equal {yes}")
