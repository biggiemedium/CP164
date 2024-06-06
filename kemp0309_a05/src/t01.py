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

from List_array import List
from Movie_utilities import read_movies

source = List()
source2 = List()
movie = open('movies.txt', 'r')
movies = read_movies(movie)

# append test
for i in movies:
    source.append(i)
    source2.append(i)


# equal test
equal = source == source2
print(f"Are sources equal: {equal}")

# remove_front test
source2.remove_front()
equal = source == source2  # update
print(f"Are sources equal: {equal}")

# __getitem__ test
print("__getitem__ test")
value = source[2]
print(value)

# remove_many test
source.remove_many("Horror of Dracula|1958|Terence Fisher|7.4|8")
# clean test
source.clean()

# combine test
source3 = List()
source3.combine(source, source2)
print("\n\n\n Combined List")
for i in source3:
    print(i)

# intersection test
print("\n\n\n Intersection test")
source3.intersection(source, source2)
for i in source3:
    print(i)

# Prepend test
source3.prepend("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
print("\n\n\n Prepend test")
print(source3.peek())

# split alt
empty = source3.is_empty()
print(f"is empty: {empty}")
target1, target2 = source3.split_alt()
empty = source3.is_empty()
print(f"is empty: {empty}")

print("\n Target 1:")
for i in target1:
    print(i)
print("\n\n\n Target 2:")
for i in target2:
    print(i)

# union test
print("Union test")
source3.union(target1, target2)


# split test
target3, target4 = source3.split()
print("\n\n\n Target 3:")
for i in target3:
    print(i)
print("\n\n\n Target 4:")
for i in target4:
    print(i)
