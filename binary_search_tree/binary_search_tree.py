"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            new_node = BSTNode(value)

            # recursive approach
            if value < self.value:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(value) # recursive call
            elif value >= self.value:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(value) # recursive call


            # iterative approach
            # curr_node = self
            # while curr_node:
            #     # look on the left side of this node
            #     if value < curr_node.value:

            #         # if there's another node, update
            #         if curr_node.left:
            #             curr_node = curr_node.left

            #         # if curr_node is the leaf, add new_node as left child
            #         else:
            #             curr_node.left = new_node
            #             curr_node = None # exit loop
                
            #     # look on the right side of this node (value that's same as root goes to right)
            #     elif value >= curr_node.value:

            #         # if there's another node, update
            #         if curr_node.right:
            #             curr_node = curr_node.right

            #         # if curr_node is the leaf, add new_node as right child
            #         else:
            #             curr_node.right = new_node
            #             curr_node = None # exit loop


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False
        else:
            # recursive method
            if target is self.value:
                return True
            elif target < self.value:
                if self.left is None: 
                    return False
                else:
                    return self.left.contains(target)
            elif target > self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)

            # iterative method        
            # curr_node = self
            # while curr_node:
            #     # look to the right
            #     if target > curr_node.value:
            #         curr_node = curr_node.right

            #     # look to the left
            #     elif target < curr_node.value:
            #         curr_node = curr_node.left
                
            #     # we found it!
            #     elif target is curr_node.value:
            #         return True # exit loop
            
            # return False

    # Return the maximum value found in the tree
    def get_max(self):
        # only check right branch
        # go right until we reach the end
        # return value at the far most right leaf
        if self.value is None:
            return
        else:
            curr_node = self
            max_value = self.value

            while curr_node:
                if curr_node.right is None:
                    max_value = curr_node.value
                    curr_node = None
                else:
                    curr_node = curr_node.right
                
            return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

        fn(self.value)
            


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
