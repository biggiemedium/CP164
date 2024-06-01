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

from Queue_circular import Queue

pq = Queue()

pq.insert(5)
pq.insert(10)
pq.insert(15)

pq.remove()
print(pq.peek())
full = pq.is_full()
empty = pq.is_empty()
print(f"full: {full}")
print(f"empty: {empty}")
