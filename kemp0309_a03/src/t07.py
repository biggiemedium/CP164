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

from functions import is_mirror_stack

mirror1 = is_mirror_stack("cmc", "abc", "m")
mirror2 = is_mirror_stack("zzxzuzxzz", "xyz", "u")
mirror3 = is_mirror_stack("zzxzuzx", "xyz", "u")

print(f"{mirror1}")
print(f"{mirror2}")
print(f"{mirror3}")
