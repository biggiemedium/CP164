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

from utilities import list_test
from List_array import List
from Movie_utilities import read_movies
from Movie_utilities import get_by_year

llist = List()
movies = read_movies(open('movies.txt', 'r'))
ss = get_by_year(movies, 1888)
print(list_test(ss))
