"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-07-01"
------------------------------------------------------------------------
"""

from functions import hash_table
from Movie_utilities import read_movies


movies = read_movies(open('movies.txt', 'r'))
ss = hash_table(7, movies)

# print(ss)
