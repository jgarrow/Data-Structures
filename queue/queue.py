"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Implement the Queue class using an array as the underlying storage structure.
#    Make sure the Queue tests pass.
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size = self.size + 1


#     def dequeue(self):
#         # if list is not empty
#         if self.size > 0:
#             self.size = self.size - 1
#             return self.storage.pop(0)


# Re-implement the Queue class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Queue tests pass.

# import sys
# sys.path.insert(1, '../singly_linked_list/')

# from singly_linked_list import LinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_head(value)
#         self.size = self.size + 1

#     def dequeue(self):
#         # make sure size can't go below zero
#         if self.size > 0:
#             self.size = self.size - 1
#         else:
#             self.size = 0

#         ret_val = self.storage.tail

#         if ret_val is not None:
#             ret_val = self.storage.tail.get_value()

#         self.storage.remove_tail()
#         return ret_val

# import sys
# sys.path.insert(1, '../doubly_linked_list/') 

# from doubly_linked_list import DoublyLinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_head(value)
#         self.size = self.storage.length

#     def dequeue(self):
#         curr_tail = self.storage.remove_from_tail()
#         self.size = self.storage.length

#         return curr_tail


import sys
sys.path.insert(1, '../binary_search_tree/')

from binary_search_tree import BSTNode

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = BSTNode(None)
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(value)
        self.size += 1

    def dequeue(self):
        curr_tail = self.storage.remove_from_tail()
        self.size = self.storage.length

        return curr_tail


#  What is the difference between using an array vs. a linked list when 
#    implementing a Queue?

# Really similar to difference between arrays and linked list in a Stack except that you change which end of the linked list to remove from with a Queue