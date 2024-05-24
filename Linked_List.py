class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def from_head_or_tail(self, index_num):
        next_frequency = index_num + 1
        prev_frequency = self.__size + 1 - next_frequency
        if next_frequency < prev_frequency:
            self.current = self.__header
            for _ in range(0, next_frequency):
                self.current = self.current.next
        elif next_frequency >= prev_frequency:
            self.current = self.__trailer
            for _ in range(0, prev_frequency):
                self.current = self.current.prev

        #O(n)

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        newest = self.__Node(val)
        newest.next = self.__trailer
        newest.prev = self.__trailer.prev
        self.__trailer.prev.next = newest
        self.__trailer.prev = newest
        self.__size = self.__size + 1
        #O(1)
        #complete

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        newest = self.__Node(val)
        if index < 0:
            raise IndexError
        if self.__size == 0:
            raise IndexError
        if index >= self.__size:
            raise IndexError
        self.from_head_or_tail(index)
        newest.next = self.current
        newest.prev = self.current.prev
        self.current.prev.next = newest
        self.current.prev = newest
        self.__size = self.__size + 1
        #O(n)

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if self.__size == 0:
            raise IndexError
        if index + 1 > self.__size:
            raise IndexError
        if index < 0:
            raise IndexError
        self.from_head_or_tail(index)
        value = self.current.val
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current.next = None
        self.current.prev = None
        self.__size = self.__size - 1
        return value
        #O(n)

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if self.__size == 0:
            raise IndexError
        if index + 1 > self.__size:
            raise IndexError
        if index < 0:
            raise IndexError
        self.from_head_or_tail(index)
        return self.current.val
        #O(n)

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size == 0:
            return self
        value_removed = self.remove_element_at(0)
        self.append_element(value_removed)
        #O(n)

    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        str_list = "[ "
        if self.__size == 0:
            return "[ ]"
        current = self.__header.next
        a = 0
        while current is not self.__trailer:
            if a == 0:
                str_list = str_list + str(current.val)
            else:
                str_list = str_list + ", " + str(current.val)
            current = current.next
            a += 1
        str_list = str_list + " ]"
        return str_list

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.current_node = self.__header.next
        return self
        #O(1)

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.current_node is self.__trailer:
            raise StopIteration
        to_return = self.current_node.val
        self.current_node = self.current_node.next
        return to_return
        #O(n)

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        rev_list = Linked_List()
        if self.__size == 0:
            return rev_list
        new_list = []
        current = self.__header.next
        while current is not self.__trailer:
            new_list.append(current.val)
            current = current.next
        for i in range(1, self.__size + 1):
            rev_list.append_element(new_list[-i])
        return rev_list
        #O(n)

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests.
    dll = Linked_List()
    elements = {
        1: 1, 
        2: "String",
        3: None,
    }
    for i in range(0, 4):
        if i == 0:
            pass
        else:
            dll.append_element(elements[i])
        print("for when the list is " + str(len(dll)) + " (from len method) nodes long")
        print("the string representation is " + str(dll))
        rdll = reversed(dll)
        print("the reversed form of the current list is " 
        + str(rdll) + " and the length of it is " + str(len(rdll)))
        print("intialize index validity test! lists reset for every test")
        print("for insertion")
        try:
            test_dll = Linked_List()
            for val in dll:
                test_dll.append_element(val)
            a = 0
            test_dll.insert_element_at("insertion", a)
            print("successfully inserted an element at " + str(a))
            a = len(test_dll)//2
            test_dll.insert_element_at("insertion", a)
            print("successfully inserted an element at " + str(a))
            a = len(test_dll)
            test_dll.insert_element_at("insertion2", a)
            print("successfully inserted an element at " + str(a))
            print("list after change is " + str(test_dll))
            print("the length of list after insertion is " + str(len(test_dll)))
        except IndexError:
            print("invalid index! at " + str(a))
            print("list after change is " + str(test_dll))
            print("the length of list after insertion is " + str(len(test_dll)))

        print("for removal")
        try:
            test_dll = Linked_List()
            for val in dll:
                test_dll.append_element(val)
            a = 0
            print("element removed: " + str(test_dll.remove_element_at(a)))
            print("successfully removed an element at " + str(a))
            a = len(test_dll)//2
            print("element removed: " + str(test_dll.remove_element_at(a)))
            print("successfully removed an element at " + str(a))
            a = len(test_dll)
            print("element removed: " + str(test_dll.remove_element_at(a)))
            print("successfully removed an element at " + str(a))
            print("list after change is " + str(test_dll))
            print("the length of list after removal is " + str(len(test_dll)))
        except IndexError:
            print("invalid index! at " + str(a))
            print("list after change is " + str(test_dll))
            print("the length of list after removal is " + str(len(test_dll)))
        print("for get_element")
        try:
            test_dll = Linked_List()
            for val in dll:
                test_dll.append_element(val)
            a = 0
            print("element returned: " + str(test_dll.get_element_at(a)))
            print("successfully returned the element at " + str(a))
            a = len(test_dll)//2
            print("element returned: " + str(test_dll.get_element_at(a)))
            print("successfully returned the element at " + str(a))
            a = len(test_dll)
            print("element returned: " + str(test_dll.get_element_at(a)))
            print("successfully returned the element at " + str(a))
        except IndexError:
            print("invalid index! at " + str(a))
        print("\n")
    print("negative index (-1) testing with " + str(dll))
    try:
        dll.remove_element_at(-1)
    except IndexError:
        print("negative index failed for removal")
    try:
        dll.insert_element_at("bruh", -1)
    except IndexError:
        print("negative index failed for insertion")
    try:
        dll.get_element_at(-1)
    except IndexError:
        print("negative index failed for get_element")
    print("\n")
    print("checking the iterators")
    print("for normal")
    for val in dll:
        print(val)
    print("\n")
    print("for reversed")
    for elem in rdll:
        print(elem)
