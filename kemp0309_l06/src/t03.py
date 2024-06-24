"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-21"
------------------------------------------------------------------------
"""

from Movie_utilities import read_movies
from List_linked import List

movie = open('movies.txt', 'r')
movies = read_movies(movie)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

source = List()
source2 = List()

for i in movies:
    source.append(i)

for i in array:
    source2.append(i)

source.remove(movies[0])
source2.remove(array[0])

if movies[2] in source:
    print("in")

if array[2] in source2:
    print("in")

print(source.peek())
print(source2.peek())
