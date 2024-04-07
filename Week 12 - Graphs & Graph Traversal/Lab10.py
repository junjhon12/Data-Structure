# Class to represent Tree node
class Node:
    # A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def is_bst(node):
    """
    Check if the given binary tree is a binary search tree (BST) by performing a check of constraints on node values for each sub-tree.
    """
    # Check if the node is None
    if node is None:
        return True
    
    # Check the constraints on node values for the current node
    if node.left is not None and node.left.data > node.data:
        return False
    if node.right is not None and node.right.data < node.data:
        return False
    
    # Recursively check the constraints on node values for the left and right sub-trees
    return is_bst(node.left) and is_bst(node.right)

def is_bst2(node):
    """
    Check if the given binary tree is a binary search tree (BST) by performing an in-order traversal and checking for violations of ascendingly sorted order.
    """
    # Create an empty stack
    stack = []
    # Set a variable to keep track of the previous node value
    prev = None

    # Traverse the tree in in-order
    while stack or node:
        # Reach the leftmost node of the current node
        while node:
            stack.append(node)
            node = node.left

        # Pop an item from the stack
        node = stack.pop()

        # Check for violation of ascendingly sorted order
        if prev and node.data < prev.data:
            return False

        # Update the previous node value
        prev = node

        # Move to the right child
        node = node.right

    # No violation found, return True
    return True

# Test the solution
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(is_bst(root))
print(is_bst2(root))
print()

# Test Case: Null
root = Node(None)
print(is_bst(root))
print(is_bst2(root))
print()

# Test Case: Single Node
root = Node(1)
print(is_bst(root))
print(is_bst2(root))
print()

# Test Case: Identical Nodes
root = Node(1)
root.left = Node(1)
root.right = Node(1)
print(is_bst(root))
print(is_bst2(root))
print()

# Test Case: False
root = Node(1)
root.left = Node(3)
root.right = Node(4)
print(is_bst(root))
print(is_bst2(root))
print()