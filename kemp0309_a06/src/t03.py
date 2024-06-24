"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-20"
------------------------------------------------------------------------
"""
from Deque_linked import Deque

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qu = Deque()
qu2 = Deque()

print(qu2.is_empty())
for i in array:
    qu.insert_front(i)  # insert
    qu2.insert_rear(i)
print(qu2.is_empty())

for i in qu:  # __iter__
    print(i)

print(len(qu))  # __len__
print(qu == qu2)
qu2.remove_front()  # remove
qu2.remove_rear()
print(qu.peek_front())  # peek
print(qu.peek_rear())  # peek
