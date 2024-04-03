
# Class to represent Tree node
class Node:
    # A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inOrderTraversal(root):
    # If the root node is not None, then perform an in-order traversal of the BST
    if root:
        # The left subtree is visited first
        inOrderTraversal(root.left)
        # Then the root node is visited
        print(root.data, end=" ")
        # Finally, the right subtree is visited
        inOrderTraversal(root.right)

def deleteRootNode(root):
    # If the root node is None, then return None
    if root is None:
        return root
    # If the root node has no left child and no right child, then return None
    if root.left is None and root.right is None:
        return None
    # If the root node has no left child, then the root node is replaced by its right child
    if root.left is None:
        root.data = root.right.data
        root.left = root.right.left
        root.right = root.right.right
    # If the root node has a left child, then the root node is replaced by the maximum value in the left subtree
    else:
        # Find the maximum value in the left subtree
        parent = root
        current = root.left
        while current.right:
            parent = current
            current = current.right
        # Replace the root node with the maximum value in the left subtree
        root.data = current.data
        # If the maximum value in the left subtree has a left child, then the parent of the maximum value is updated
        if parent != root:
            parent.right = current.left
        else:
            parent.left = current.left
    # If the root has only one child, then the child is made the root
    if root.left is None:
        root = root.right
    elif root.right is None:
        root = root.left
    return root

# Test cases:
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(deleteRootNode(root))
print(inOrderTraversal(root))

# Test case 1: Null root
root = None
print(deleteRootNode(root))


# Test case 2: Root node has no left child
root = Node(4)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
print(deleteRootNode(root))

# Test case 3: Root has only one child
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
print(deleteRootNode(root))

# Test case 4: There's only one node in the BST
root = Node(4)
print(deleteRootNode(root))


