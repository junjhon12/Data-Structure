# Class to represent Tree node
class Node:
    # A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def is_bst(node):
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

# Test the solution
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(is_bst(root))


# 