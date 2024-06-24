"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-24"
------------------------------------------------------------------------
"""

from List_linked import List

# combine
# intersection

list = List()
list2 = List()
array = [1, 1, 2, 3, 4, 5]
for i in array:
    list.append(i)  # append
    list2.append(i)

print(list == list2)
list.remove_many(1)
list.remove_front()
print(list == list2)
print(list[0])
list.append(1)
list.append(1)
# list2.clean()
for i in list:
    print(i)

list.prepend(1)
print(list[0])

target1, target2 = list2.split_alt()
for i in target1:
    print(i)
for i in target2:
    print(i)

target1, target2 = list.split()
for i in target1:
    print(i)
for i in target2:
    print(i)

list.union(target1, target2)
list.intersection(target1, target2)
for i in target1:
    print(i)
for i in target2:
    print(i)

target2.combine(target1, list2)
print("Combine")
for i in target2:
    print(i)
