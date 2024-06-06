"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-06"
------------------------------------------------------------------------
"""

from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies

# split_alt

source = Sorted_List()
source2 = Sorted_List()
source3 = Sorted_List()
source4 = Sorted_List()
movie = open('movies.txt', 'r')
movies = read_movies(movie)

for i in movies:
    source.insert(i)
    source2.insert(i)


# __eq__ test
equal = source == source2
print(f"Are sources equal: {equal}")
source2.pop(0)
equal = source == source2
print(f"Are sources equal: {equal} \n\n")

# __getitem__ test
first = source2[0]  # peek
print(f"__getitem__ test: {first} \n\n")

# peek test
peek = source2.peek()
print(f"Peek test: {peek} \n\n")

# __contains test
contains = source[0] in source2
print(f"contains test: {contains} \n\n")

# count test
count = source2.count(source[5])
print(f"Count test: {count} \n\n")

# find test
find = source2.find(source[4])
print(f"Find test: {find} \n\n")

index = source2.index(source[4])
print(f"Index test: {index} \n\n")

# max test
max = source.max()
print(f"Max test: {max} \n\n")

# min test
min = source.min()
print(f"min test: {min} \n\n")

# clean test
clean = source.clean()
print(f"clean test: {clean} \n\n")

# remove front test
# remove test
print("remove_front and remove test:  \n\n")
source.remove_front()
source.remove(source2[4])
for i in source:
    print(i)

# remove_many test
print("remove_many test:  \n\n")
source.remove_many(source2[2])
for i in source:
    print(i)

# Union test
print("Union test \n\n")
source3.union(source, source2)
for i in source3:
    print(i)

# intersection test
print("Intersection test \n\n")
source4.intersection(source, source2)
for i in source4:
    print(i)

# split test
print("Split test \n\n")
array1, array2 = source.split()
print("Array 1")
for i in array1:
    print(i)
for i in array2:
    print(i)

# split_key test
array1.split_key(array2[4])
for i in array1:
    print(i)

# Split_alt test
target1, target2 = array2.split_alt()
print("split alt test")
print("target 1")
for i in target1:
    print(i)
print("Target 2")
for i in target2:
    print(i)
