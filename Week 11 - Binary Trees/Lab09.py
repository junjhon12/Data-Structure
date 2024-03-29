import collections

class Node:
# A function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        
    def Level_Order_Traversal(self, root):
        # This list will store the level order traversal of the tree
        LOT = []
        # This deque will store the nodes of the tree
        Q = collections.deque()
        # If the root is not None, add it to the deque
        Q.append(root)
        # While the deque is not empty, pop the leftmost node and add it to the list
        while Q:
            # Pop the leftmost node
            a_node = Q.popleft()
            LOT.append(a_node.data)
            # If the left or right child of the node is not None, add it to the deque
            if a_node.left:
                Q.append(a_node.left)
            # If the right child of the node is not None, add it to the deque
            if a_node.right:
                Q.append(a_node.right)
        return LOT
    
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(root.Level_Order_Traversal(root))

# Test Case: Null
root = Node(None)
print(root.Level_Order_Traversal(root))

# Test Case: Single Node
root = Node(1)
print(root.Level_Order_Traversal(root))

# Test Case: Identical Nodes
root = Node(1)
root.left = Node(1)
root.right = Node(1)
print(root.Level_Order_Traversal(root))
