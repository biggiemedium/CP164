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

from Stack_array import Stack
from enum import Enum


MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

OPERATORS = "+-*/"


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    stack = Stack()
    mirrored = None
    split = string.split()
    n = len(string)
    i = 0

    for s in split:
        stack.push(s)

    if stack.is_empty():
        mirrored = MIRRORED.INVALID_CHAR

    while i < n and string[i] != m:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            return MIRRORED.INVALID_CHAR

    if i == n:
        return MIRRORED.NOT_MIRRORED

    i += 1

    while i < n and not stack.is_empty():
        c = stack.pop()
        if string[i] != c:
            return MIRRORED.MISMATCHED
        else:
            i += 1

    if not stack.is_empty():
        return MIRRORED.TOO_MANY_LEFT

    if i < n:
        return MIRRORED.TOO_MANY_RIGHT

    return MIRRORED.IS_MIRRORED


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    values_out = []
    inV = 0

    for op in opstring:
        if op == 'S':
            if inV < len(values_in):
                stack.push(values_in[inV])
                inV += 1
            else:
                return None
        elif op == 'X':
            if not stack.is_empty():
                values_out.append(stack.pop())
            else:
                return None
        else:
            return None

    return values_out


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    stack = Stack()
    split = string.split()

    for token in split:
        if token not in OPERATORS:
            stack.push(token)
        else:
            operand2 = float(stack.pop())
            operand1 = float(stack.pop())
            result = None
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            else:
                result = operand1 / operand2
            stack.push(result)

    return stack.pop()


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    stack = Stack()
    array = []

    while not source.is_empty():
        array.append(source.pop())

    while array:
        source.push(array.pop(0))

    return None


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """

    target1 = []
    target2 = []
    switch = False

    count = 0
    while not source.is_empty():
        if count % 2 == 0:
            target1.append(source.pop())
        else:
            target2.append(source.pop())
        count += 1

    return target1, target2
