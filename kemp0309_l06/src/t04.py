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
array = [1, 2, 3, 4, 5]

source = List()
source2 = List()

for i in movies:
    source.append(i)

for i in array:
    source2.append(i)


source[1] = movies[0]  # set item
source2[1] = 5  # set item
print(source[1])  # get item
print(source2[1])  # get item
