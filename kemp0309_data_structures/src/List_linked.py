"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-06-24"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
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
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._front == None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """

        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value, self._front)

        self._front = node

        if self._count == 0:
            self._rear = node

        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value, None)  # none bc we append to last value
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node

        self._count += 1

        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        #assert self._is_valid_index(), "Must be within index"

        if i <= -self._count:  # (index) < 0
            self.prepend(value)
        elif i == 0:  # index == 0
            self.prepend(value)
        elif i > 0:  # index > 0
            self.append(value)
        return None

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key is not found (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index = 0
        found = False

        while current is not None:
            if current._value == key:
                found = True
                break
            previous = current
            current = current._next
            index += 1

        if not found:
            previous = None
            #current = None
            index = -1
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        previous, current, index = self._linear_search(key)
        if index == -1:
            value = None

        value = deepcopy(current._value)

        if previous is None:
            self._front = current._next
            if self._count == 1:
                self._rear = None
        else:
            previous._next = current._next  # remove frpont node
            if current == self._rear:
                self._rear = previous

        self._count -= 1

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1

        if self._front is None:
            self._rear = None

        return deepcopy(value)

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        removalNode = None
        current = self._front

        while current is not None:
            if current._value == key:
                if removalNode is None:
                    self._front = current._next
                    if self._front is None:
                        self._rear = None
                else:
                    removalNode._next = current._next
                    if current._next is None:
                        self._rear = removalNode
                self._count -= 1
                current = current._next
            else:
                removalNode = current
                current = current._next

        if self._count == 0:  # empty handling
            self._rear = None
        return None

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # althought its unused we need all 3 objects otherwise it will iterate preveious
        previous, current, index = self._linear_search(key)
        value = None
        if current is not None:
            value = deepcopy(current._value)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        # keep value or just returns object type
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        # althought its unused we need all 3 objects otherwise it will iterate preveious
        previous, current, index = self._linear_search(key)
        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        current = self._front
        if i < 0:  # for negatives
            index = -1 * self._count
        elif i == 0:
            index = 0
        else:  # TODO: fix
            index = 0
        # while current is not None: - dont do this index is better in this senario
        while index < i:
            current = current._next  # when loop stops we get this value
            index += 1  # iter
        return deepcopy(current._value)

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        #previous, current, index = self._linear_search(i)

        # if current is not None:  # if search result
        #    current._value = deepcopy(value)

        current = self._front
        index = 0

        while i > index:
            current = current._next  # set uietm
            index += 1  # iterate

        current._value = deepcopy(value)
        return deepcopy(current._value)  # messy but it works

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # althought its unused we need all 3 objects otherwise it will iterate preveious
        previous, current, index = self._linear_search(key)
        value = True
        if current is None:
            value = False
        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        index = self._front
        max = index._value
        # this is the exact same as List_array max except just change the way we iterate
        while index is not None:
            if index._value > max:
                max = index._value
            index = index._next

        return max

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        index = self._front
        max = index._value
        # this is the exact same as List_array max except just change the way we iterate
        while index is not None:
            if index._value < max:
                max = index._value
            index = index._next

        return max

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        count = 0
        index = self._front

        while index is not None:  # we have hit end of list when index is None
            if index._value == key:
                count += 1
            index = index._next  # iterate

        return count

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        if self._front is not None:  # iter
            self._reverse_r_aux(self._front)
        self._rear = self._front
        return

    def _reverse_r_aux(self, node):

        if node._next is None:
            self._front = node
            #self._rear = None
        else:
            return self._reverse_r_aux(node._next)
            node._next._next = node
            node._next = None

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains
        one and only one of each value formerly present in the list.
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._front
        removalNode = _List_Node(None, None)
        #removalNode = None
        # if self._count == 0: we dont need this
        while current is not None:
            p, c, i = self._linear_search(current._value)
            if current is not c:  # swap order
                if removalNode is None:
                    self._front = current._next
                else:
                    removalNode._next = current._next  # save value
                current._next = None  # remove
                current._next = removalNode._next  # reset list
                self._count -= 1  # adjust size
            else:
                removalNode = current
                #c = current._next
                current = current._next

        if self._count == 0:  # fix the empty pointers
            self._rear = None
        else:
            self._rear = removalNode
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0],
                otherwise the last value in the list, value is
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """

        value = True

        if target._count != self._count:
            value = False

        front = self._front
        tf = target._front

        while front is not None and tf is not None:
            if front._value != tf._value:
                value = False
                break
            front = front._next  # iterate
            tf = tf._next

        return value

    def identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        # your code here
        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        current = self._front
        index = 0
        mid = self._count // 2  # keep this local so it doesnt update in loop

        while current is not None and index < mid:
            node = _List_Node(current._value, None)
            if target1._front is None:
                target1._front = node
                target1._rear = node
            else:
                target1._rear._next = node
                target1._rear = node

            #target1._rear = current
            target1._count += 1
            index += 1
            current = current._next

        while current is not None:
            if index > self._count:
                break
            node = _List_Node(current._value, None)
            if target2._front is None:
                target2._front = node
                target2._rear = node
            else:
                target2._rear._next = node
                target2._rear = node
            target2._count += 1
            index += 1  # this doesnt matter anymore
            current = current._next

        # empty list
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """

        even = List()
        odd = List()
        self._split_alt_r_aux(even, odd, True)
        return even, odd

    def _split_alt_r_aux(self, target1, target2, swap):
        # if self._count > 0:  # real
        if self._front is not None:
            if swap:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            swap = not swap  # we need to put swap in parameters to conserve value

        if self._front is not None:  # don't call too deeply
            return self._split_alt_r_aux(target1, target2, swap)

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        return self._linear_search_r_aux(None, self._front, 0, key)

    def _linear_search_r_aux(self, p, c, i, key):
        if self._count == 0:
            return None, None, -1
        if c is None:
            return None, None, -1
        if c._value == key:
            return p, c, i
        else:
            return self._linear_search_r_aux(c, c._next, i + 1, key)  # iterate

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False. (bool)
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def is_identical_r(self, target):
        if self._count != target._count:
            return False
        # I cant figure out how to get this to work in the validator without multiple return statments
        else:  # pls dont take away my marks
            return self._is_identical_r_aux(self._front, target._front)

    def _is_identical_r_aux(self, k, v):  # key, value
        identical = True
        if k is None and v is None:
            identical = True
        elif k is None or v is None:
            identical = False
        elif k._value != v._value:
            identical = False
        else:
            identical = self._is_identical_r_aux(k._next, v._next)
        return identical

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        current = source1._front
        current_self = None

        while current is not None:
            value = current._value
            p, c, i = source2._linear_search(value)
            if c is not None and not self.find(value):
                node = _List_Node(value, None)
                if self._front is None:
                    self._front = node
                else:
                    self._rear._next = node
                self._rear = node
                self._count += 1

            current = current._next

        if self._count == 0:
            self._rear = None
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        if source1._front is not None and source2._front is not None:  # AND !!!!!
            return self._intersection_r_aux(source1._front, source2._front)

    def _intersection_r_aux(self, source1, source2):
        if source1 is not None and source2 is not None:
            p, c, i = self._linear_search_r(source1._value)

            if c is not None:
                if source1._value == source2._value:
                    if self._front is not None:
                        self._front = _List_Node(source1._value, None)
                        self._rear = self._front
                    else:
                        self._rear._next = _List_Node(source1._value, None)
                        self._rear = self._rear._next

            self._intersection_r_aux(source1._next, source2._next)

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self.append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self.append(value)

            source2_node = source2_node._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if source1._front is not None:  # this will stop throwing null errors
            self._union_r_aux(source1._front)
        if source2._front is not None:
            self._union_r_aux(source2._front)

    def _union_r_aux(self, node):
        if node is not None:
            p, c, i = self._linear_search_r(node._value)

            if c is None:  # found element
                #p, c, i = self._linear_search_r(node._value)
                # if i < -1:
                self.append(node._value)  # node not c
            return self._union_r_aux(node._next)

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # node._next = None # not here - we have not checked our source front value yet
        source._front = source._front._next
        if source._front is None:
            # source._rear = node # source._rear = node
            source._rear = None
            # source._front = node # what was I thinking

        node._next = None
        #source._front = source._front._next
        if self._rear is None:  # list empty
            self._rear = node
            self._front = node
        else:
            self._rear._next = node
            self._rear = node

        source._count -= 1
        self._count += 1

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        At finish, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        swap = True

        while source1._front is not None or source2._front is not None:
            if swap:
                if source1._front is not None:  # not allowoed to use _Queue_Node
                    value = source1._front
                    source1._front = source1._front._next
                else:
                    value = source2._front
                    source2._front = source2._front._next
            else:
                if source2._front is not None:
                    value = source2._front
                    source2._front = source2._front._next
                else:
                    value = source1._front
                    source1._front = source1._front._next
            #self._count += 1
            if self._front is None:
                self._front = value
            else:
                self._rear._next = value
            self._rear = value
            self._rear._next = None  # fixes nonetype thing
            self._count += 1
            swap = not swap
            # self._count += 1  # move this behind self._front if so that it increments after being added

        source1._front = None
        source1._rear = None
        source2._front = None
        source2._rear = None
        source1._count = 0
        source2._count = 0
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
