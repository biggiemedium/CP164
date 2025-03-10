"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Daniel Hyatt
ID:     169059480
Email:  hyat9480@mylaurier.ca
__updated__ = "2024-04-22"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy
from _ast import If
from locale import currency


class List:
    """
    A linked List class.
    """

    def split_count(self, count):
        """
        -------------------------------------------------------
        Splits source into separate target lists based on count.
        At finish target1 contains count nodes, target2 contains 
        remaining nodes from source, and source is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_count(count)
        -------------------------------------------------------
        Parameters:
            count - the number of nodes in target1 (int >= 0)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            target1 - contains count nodes from source (List)
            target2 - contains remaining nodes from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        current = self._front
        i = 0
        
        while current is not None and i < count:
            target1.append( current )
            current = current._next
            
            i += 1
            
        while current is not None:
            target2.append( current )
            current = current._next
            
        self._front = None
        self._rear = None
        self._count = 0
        
        return target1, target2


    def replace_many(self, key, value):
        """
        -------------------------------------------------------
        Replace every occurrence of key in source with value.
        List is otherwise unchanged.
        Use: source.replace_many(key, value)
        -------------------------------------------------------
        Parameters:
            key - a key that may be in source (?)
            value - the replacement for key (?)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            None.
        -------------------------------------------------------
        """
        temp = self._front
        
        while temp is not None:
            if temp._value == key:
                temp._value = value
                
            else:
                temp = temp._next
                
        return None
    

    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            None
        -------------------------------------------------------
        """
        if self._count > 1:
            current = self._front
            
            while current is not None and current._next is not self._rear:
                current = current._next # loops until the next value is the last, this gives the second last value
                
            self._rear._next = self._front
            self._front = self._rear
            self._rear = current
            self._rear._next = None
                
        return None

    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """
        one = self._front
        two = self._front
        loop = False 
        
        while two is not None and two._next is not None:
            one = one._next
            two = two._next._next
            
            if one == two:
                loop = True
                break
        
        return loop

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​‌​​‌​​‌‌​​​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
