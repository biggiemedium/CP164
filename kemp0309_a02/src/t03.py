"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-16"
------------------------------------------------------------------------
"""

from Movie_utilities import get_by_genre
from Movie_utilities import read_movies

movies = read_movies(open('movies.txt', 'r'))
ss = get_by_genre(movies, 1)
for i in ss:
    print(i)
