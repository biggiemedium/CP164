"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-19"
------------------------------------------------------------------------
"""
from Queue_linked import Queue

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qu = Queue()
qu2 = Queue()

for i in array:
    qu.insert(i)  # insert
    qu2.insert(i)

for i in qu:  # __iter__
    print(i)

print(len(qu))  # __len__
print(qu == qu2)  # __eq__
qu2.remove()  # remove
print(qu == qu2)
print(qu.peek())  # peek
print(qu.is_empty())  # is empty
print(qu.is_full())  # is full
target1, target2 = qu2.split_alt()
for i in target1:
    print(i)

for i in target2:
    print(i)

qu.combine(target1, target2)

for i in qu:
    print(i)
