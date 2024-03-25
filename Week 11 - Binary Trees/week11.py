
"""
3/25/2024

In order:
Visit the LST
Process the node
Visit the RST

Tree node:
- A tree node is a node that has a left child, a right child, and a value.

A balanced tree is a tree where the height of the left and right subtrees of any node differ by at most 1.
example:
    4
    / \
    2   6
    / \ / \
    1 3 5 7
    
"""
"""
class Tree_Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
     
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()
"""

"""
Find order
4, 2, 6, 1, 3, 5, 7

Level order
result = []
q = collections.deque()
q.append(root)
while q:
    var = q.popleft()
    result.append(var.value)
    if var.left:
        q.append(var.left)
    if var.right:
        q.append(var.right)
        
# after while block exits
return result
"""
"""
root = Tree_Node(4)
root.left = Tree_Node(2)
root.right = Tree_Node(6)
root.left.left = Tree_Node(1)
root.left.right = Tree_Node(3)
root.right.left = Tree_Node(5)
root.right.right = Tree_Node(7)

result = []
q = collections.deque() # Space 
q.append(root)
while q:
    var = q.popleft()
    result.append(var.value)
    if var.left:
        q.append(var.left)
    if var.right:
        q.append(var.right)
print(result)

#Time complexity: O(n)
#Space complexity: O(n)
"""

"""
Simulaion of the code:
result = []
q = [4]
var = 4
result = [4]
q = [2, 6]
var = 2
result = [4, 2]
q = [6, 1, 3]
var = 6
result = [4, 2, 6]
q = [1, 3, 5, 7]
var = 1
result = [4, 2, 6, 1]
q = [3, 5, 7]
var = 3
result = [4, 2, 6, 1, 3]
q = [5, 7]
var = 5
result = [4, 2, 6, 1, 3, 5]
q = [7]
var = 7
result = [4, 2, 6, 1, 3, 5, 7]
q = []
return [4, 2, 6, 1, 3, 5, 7]
"""

"""
 3/25/2024
 
 Root -> 4
 LST(Left Subtree) -> 2 | RST(Right Subtree) -> 6
 LST(Left Subtree) -> 1 RST(Right Subtree) -> 3 | LST(Left Subtree) -> 5 RST(Right Subtree) -> 7
 
 class Tree_Node:
    def __init__(self, left = None, right = None, value = 0):
        self.left = left
        self.right = right
        self.value = value
        
How would you implement Inorder traversal?
- First, visit the left subtree.
- Then, process the node.
- Finally, visit the right subtree.

Inorder traversal is a depth-first traversal algorithm that processes the nodes in the following order:
- Visit the left subtree.
- Process the node.
- Visit the right subtree.
    Example in Python: 
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value)
            inorder_traversal(root.right)

Preorder traversal is a depth-first traversal algorithm that processes the nodes in the following order:
- Process the node.
- Visit the left subtree.
- Visit the right subtree.
    Example in Python:
    def preorder_traversal(root):
        if root:
            print(root.value)
            preorder_traversal(root.left)
            preorder_traversal(root.right)

How to reform this into a recursive function?
- Base case: if the node is None, return.
- Recursive case: call the function on the left subtree, process the node, and call the function on the right subtree.

In internship they'll likely ask you to convert a Recursive into an Iterative function.
"""
import collections
class Tree_Node:
    def __init__(self, left = None, right = None, value = 0):
        self.left = left
        self.right = right
        self.value = value

# Recursive, not what Internship will ask for
def inorder_traversal(root):
    # List to store the values
    IOT = []
    # Base case
    if root == None:
        return 
    # Recursive case
    inorder_traversal(root.left)
    # Process the node
    print(root.value)
    # Recursive case 
    inorder_traversal(root.right)
    # Append the value to the list
    IOT.append(root.value)
    inorder_traversal(root.right)
    
    inorder_traversal(root)
    return IOT

# Iterative, what Internship will ask for
def inorder_iterative(root):
    # This list will store the values
    IOT = []
    # This deque will store the nodes
    call_stack = collections.deque()
    # This will store the current node
    current = root
    # While loop to traverse the tree
    while current or len(call_stack) > 0:
        # If the current node is not None
        if current:
            # Append the current node to the call stack
            call_stack.append(current)
            # Move to the left child
            current = current.left
        else:
            # Pop the current node from the call stack
            current = call_stack.pop()
            IOT.append(current.value)
            current = current.right
            #Time complexity: O(n)
            #Space complexity: O(n)
            
    return IOT
# LOT(Left Order Traversal) -> 4, 2, 1, 3, 6, 5, 7
"""
level_Orders = [4, 2, 6, 1, 3, 5, 7]
LOT = [] #This isn't where time complexity is
Q = collections.deque()
Q.append(root)
while Q:
    a_node = Q.popleft()
    LOT.append(a_node.value)
    # If the left child is not None, append it to the queue
    if var.left:
        Q.append(a_node.left)
    # If the right child is not None, append it to the queue
    if var.right:
        Q.append(a_node.right)
    # Exit the while loop
return LOT
"""


