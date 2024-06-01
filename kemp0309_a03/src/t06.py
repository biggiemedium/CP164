"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-05-24"
------------------------------------------------------------------------
"""

from functions import reroute

opstring = "SSXSSXXX"
values_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ss = reroute(opstring, values_in)
print(ss)
