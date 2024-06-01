"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-30"
------------------------------------------------------------------------
"""

from utilities import list_to_array
from utilities import array_to_list
from List_array import List
from Movie_utilities import read_movies


llist = List()
array = []
movies = read_movies(open('movies.txt', 'r'))

array_to_list(llist, movies)

list_to_array(llist, array)

for k in array:
    print(k)
