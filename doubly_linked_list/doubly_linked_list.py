"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def __str__(self):
        return '{self.value}'.format(self=self)

    def delete(self):
        # if it's not the head or tail
        if self.prev is not None and self.next is not None:
            self.next.prev = self.prev
            self.prev.next = self.next
        # if it's the head
        elif self.prev is None:
            self.next.prev = None
        # if it's the tail
        elif self.next is None:
            self.prev.next = None

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # new head will have `None` for `prev` and point to the current head for `next`
        new_node = ListNode(value)

        self.length = self.length + 1

        # if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length > 0:
            self.length = self.length - 1
        else:
            self.length = 0

        # need for return value
        curr_head = self.head

        # if list is not empty
        if self.head is not None:
            # if there's only 1 thing in list
            if self.head.next is None:
                self.head = None
                self.tail = None
            # if there's more than 1 thing in list
            else:
                # set second node to head
                second_node = self.head.next
                print('self.head: ', self.head)
                print('second_node: ', second_node)
                second_node.prev = None
                self.head = second_node
        
        # return value of head to be removed (or `None` if the list is empty)
        return curr_head.value if curr_head is not None else curr_head

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        self.length = self.length + 1

        # if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if there's only 1 thing in list
        elif self.head.next is None:
            new_node.prev = self.head
            self.tail = new_node
            self.head.next = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length > 0:
            self.length = self.length - 1
        else:
            self.length = 0

        # need for return value
        curr_tail = self.tail

        # if list is not empty
        if self.head is not None:
            # if there's only 1 thing in list
            if self.head.next is None:
                self.head = None
                self.tail = None
            # if there's more than 1 thing in list
            else:
                # set second to last node to tail
                penultimate_node = self.tail.prev

                penultimate_node.next = None
                self.tail = penultimate_node
        
        return curr_tail.value if curr_tail is not None else curr_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # my solution w/o .delete method
        # if list is not empty
        # if self.head is not None:
        #     # if there's more than 1 thing in list
        #     if self.head.next is not None:
        #         if node.prev:
        #             node.prev.next = node.next
                
        #         if node.next:
        #             node.next.prev = node.prev

        #         self.head.prev = node
        #         node.next = self.head
        #         node.prev = None

        #         self.head = node

        if node is self.head:
            return

        self.delete(node)
        self.add_to_head(node.value)


        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        print('\nself.head: ', self.head)
        print('self.tail: ', self.tail)
        print('self.length: ', self.length)
        # if list is empty
        if self.head is None:
            return None
        
        # if list has 1 item
        elif self.head is self.tail:
            self.head = None
            self.tail = None

        # if list has 2+ items

        # node is head
        elif self.head is node:
            self.head = node.next
            node.prev = None
            node.delete() # update prev and/or next pointers

        # node is tail
        elif node is self.tail:
            self.tail = node.prev
            node.next = None
            node.delete()

        # node is in the middle
        else:
            node.delete()

        
        
        if self.length > 0:
            self.length -= 1


           

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass