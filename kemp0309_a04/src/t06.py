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

from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
array = [5, 8, 12, 8, 7, 9, 14]

for i in array:
    source.insert(i)

target1, target2 = source.split_key(7)
while not target1.is_empty():
    print(target1.peek())
    target1.remove()

while not target2.is_empty():
    print(target2.peek())
    target2.remove()
