class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, value):
        new_node = Node(value)

        # if linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
    
    def add_to_tail(self, value):
        new_node = Node(value)

        # if linked list is empty
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.set_next_node(None)
            self.tail.set_next_node(new_node)
            self.tail = new_node
    
    def remove_head(self):
        # if linked list is empty
        if self.head is None:
            return None
        else:
            return_value = self.head.get_value()

            # if there's only 1 thing in the list, get rid of it
            if self.head == self.tail:
                self.head = None
                self.tail = None
            
            # if there's more than 1 thing in the list
            else:
                # set head to the second node -- the current head's next_node
                self.head = self.head.get_next_node()
            
            return return_value
    
    def remove_tail(self):
        # if linked list is empty
        if self.tail is None:
            return None
        else:
            return_value = self.tail.get_value()

            # if there's only 1 thing in the list, get rid of it
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                # loop through list to find node whose next_node is the current tail

                # look at each node, check is next_node == self.tail
                # to get next node for loop, call get_next_node

                curr_node = self.head

                while curr_node is not None:
                    # if the current node is the second to last in the list
                    if curr_node.get_next_node() == self.tail:
                        # update its next_node to None
                        curr_node.set_next_node(None)

                        # then update the tail to be the current node
                        self.tail = curr_node
                    # if the current node isn't second to last, go to the next node
                    else:
                        curr_node = curr_node.get_next_node()

            return return_value
    
    def contains(self, value):
        curr_node = self.head

        while curr_node is not None:
            if curr_node.get_value() == value:
                return True
        
        return False