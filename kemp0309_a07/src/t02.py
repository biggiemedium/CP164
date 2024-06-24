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

from Sorted_List_linked import Sorted_List

# clean
# intersection
# union
sl = Sorted_List()
sl2 = Sorted_List()
sl3 = Sorted_List()
array = [1, 1, 2, 2, 3, 4, 5]

for i in array:
    sl.insert(i)  # insert
    sl2.insert(i)
    sl3.insert(i)

print(sl.peek())  # peek
print(sl == sl2)
sl.remove(2)  # remove
print(sl == sl2)  # __eq__
sl.remove_many(1)  # remove many
print("__ Contains __")
for i in sl:  # __Contains__
    print(i)

print("get item [0]")
print(sl[0])  # __getitem__
print("Count (1)")
print(sl.count(1))
print("Find")
print(sl.find(4))
print("Max")
print(sl.max())
print("Min")
print(sl.min())
print("Index")
print(sl.index(3))
print("Intersection")
sl.intersection(sl2, sl3)
print("Union")
sl.union(sl2, sl3)
print("Clean")
sl.clean()
for i in sl:
    print(i)
