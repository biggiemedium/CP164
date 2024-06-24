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

source.prepend(movies[0])
source.append(movies[3])
source.insert(0, movies[2])

source2.prepend(array[0])
source2.append(array[3])
source2.insert(0, array[2])

for i in source:
    print(i)

for i in source2:
    print(i)
