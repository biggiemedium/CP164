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


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    # if slots >= 0: # because nobody would possibly ever insert a negative integer right?
    for i in values:
        # idk if I should name the object hash if hash() is internal
        has = hash(i)
        slot = has % slots
        print(f"{has: >8} {slot: >4} {i}")  # spacing

    return None
