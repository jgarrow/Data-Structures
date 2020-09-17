"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Implement the Stack class using an array as the underlying storage structure.
#    Make sure the Stack tests pass.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = self.size + 1

#     def pop(self):
#         last_element = None

#         if self.size > 0:
#             last_element = self.storage[self.size - 1]

#             self.storage.pop()
#             self.size = self.size - 1
        
#         return last_element


# Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.

import sys
sys.path.insert(1, '../singly_linked_list/')

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # if storage is empty
        if self.storage.head is None:
            # update the head
            self.storage.add_to_head(value)
        else:
            # otherwise, update the tail
            self.storage.add_to_tail(value)
        
        self.size = self.size + 1
            

    def pop(self):
        if self.storage.head is None:
            self.size = 0
            return None
        else:
            self.size = self.size - 1
            return self.storage.remove_tail()

        
            
# What is the difference between using an array vs. a linked list when 
#    implementing a Stack?

# As far as the code I wrote, they're pretty similar. Under the hood, since arrays are contiguous, the array has to be cloned somewhere else in memory that has enough space for the changes that are being made. And then after the updates are done, the original array gets deleted from memory. With a linked list, since the values don't all get stored in memory "next to" each other, so to speak, we only need to change the data in memory associated with the specific node we want instead of changing the entire list
