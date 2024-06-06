"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: James Patrick Kemp
ID:     169060309
Email:  kemp0309@wlu.ca
__updated__ = "2024-06-03"
------------------------------------------------------------------------
"""


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """

    if len(bag) == 0:
        value = []
    else:
        value = bag_to_set(bag[:-1])
        if bag[-1] not in value:
            value.append(bag[-1])
    return value


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    value = False
    if len(s) <= 1:
        value = True
    else:
        if not s[0].isalpha():
            value = is_palindrome(s[1:])
        elif not s[-1].isalpha():
            value = is_palindrome(s[:-1])
        elif s[0].lower() == s[-1].lower():
            value = is_palindrome(s[1:-1])
        else:
            value = False
    return value


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    value = 0

    if power == 0:
        value = 1

    elif power > 0:
        value = base * to_power(base, power - 1)

    else:  # for decimals
        value = 1 / to_power(base, -power)

    return value


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """

    vowels = "aeiou"
    value = 0
    if s == "":
        value = 0
    else:
        value = (1 if s[0].lower() in vowels else 0) + vowel_count(s[1:])

    return value


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """

    value = 0
    if m % n == 0:
        value = n
    else:
        value = gcd(n, m % n)
    return value


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    value = 0
    if x < 0 or y < 0:
        value = x - y
    else:
        value = recurse(x - 1, y) + recurse(x, y - 1)

    return value
