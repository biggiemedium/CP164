"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-14"
------------------------------------------------------------------------
"""

from Movie_utilities import read_movies
from Linked_list import List

movie = open('movies.txt', 'r')
movies = read_movies(movie)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

source = List()
source2 = List()

for i in movies:
    source.append(i)

for i in array:
    source2.append(i)

print("Min")
print(source.min())
print(source2.min())
print("Max")
print(source.max())
print(source2.max())
print("Count")
print(source.count(movies[1]))
print(source2.count(array[5]))
