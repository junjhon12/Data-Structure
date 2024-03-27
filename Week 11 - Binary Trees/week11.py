
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

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def level_order_traversal(root):
    LOT = [] #This isn't where time complexity is
    Q = collections.deque()
    Q.append(root)
    while Q:
        a_node = Q.popleft()
        LOT.append(a_node.value)
        # If the left child is not None, append it to the queue
        if a_node.left:
            Q.append(a_node.left)
        # If the right child is not None, append it to the queue
        if a_node.right:
            Q.append(a_node.right)
    # Exit the while loop
    return LOT

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(level_order_traversal(root))

"""
3/27/2024

Binary Search Tree:
- A binary search tree is a binary tree where the left child of a node has a value less than the node's value, and the right child has a value greater than the node's value.
- The left and right subtrees of a node are also binary search trees.

How would you describe a binary search tree?
- A binary search tree is a binary tree where the left child of a node has a value less than the node's value, and the right child has a value greater than the node's value.

Root -> 4
LST -> 2 | RST -> 6
LST -> 1 RST -> 3 | LST -> 5 RST -> 7

1) Node Level Property: The value of the left child is less than the value of the node, and the value of the right child is greater than the value of the node.
2) Subtree Level Property: The Node Level Property holds for all nodes in the left and right subtrees. Recursively, the left and right subtrees are also binary search trees.

Example of a Wrong Binary Search Tree and a Correct Binary Search Tree:
Wrong Binary Search Tree: 
    4
    / \
    2   6
    / \ / \
    1 3 5 3

Correct Binary Search Tree:
    4
    / \
    2   6
    / \ / \
    1 3 5 7
    
Inorder Traversal:
- Visit the left subtree.
- Process the node.
- Visit the right subtree.

[1, 2, 3, 4, 5, 6, 7]

Preorder Traversal:
- Process the node.
- Visit the left subtree.
- Visit the right subtree.

[4, 2, 1, 3, 6, 5, 7]

Binary Search Tree are always ascended sorted.
They're embedded everywhere in the real world.
They're used for searching, sorting, and indexing.

If you're trying to find 5.5 in a binary search tree, you would start at the root node, 4. Since 5.5 is greater than 4, you would move to the right child, 6. Since 5.5 is less than 6, you would move to the left child, 5. Since 5.5 is greater than 5, you would move to the right child, 7. Since 5.5 is less than 7, you would move to the left child, which is None. Since the left child is None, you would return False.
The worst case is the target doesn't exist in the tree, and you have to traverse the entire tree.
The time complexity is O(log_2 n) for a balanced tree.
What if it's not expected to be balanced? The time complexity is O(n) for an unbalanced tree.

Height Balanced Binary Search Tree:
- A height-balanced binary search tree is a binary search tree where the height of the left and right subtrees of any node differ by at most 1.

Inserting an element into a binary search tree:
- Start at the root node.
- If the value is less than the node's value, move to the left child.
- If the value is greater than the node's value, move to the right child.
- Repeat until you reach a None child.
- Insert the value as the left or right child of the None child.

Code example:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
    
Delete an element from a binary search tree:
- If the node to be deleted has no children, remove the node.
- If the node to be deleted has one child, replace the node with its child.
- If the node to be deleted has two children, replace the node with the smallest node in the right subtree.

Code example:
def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.value = find_min(root.right)
        root.right = delete(root.right, root.value)
    return root
    
Delete the root node:
- If the root node has no children, remove the root node.
- If the root node has one child, replace the root node with its child.
- If the root node has two children, replace the root node with the smallest node in the right subtree.

Approach 1) Replace the root with the highest element in the left subtree.
Approach 2) Replace the root with the smallest element in the right subtree.

Code example:
def delete_root(root):
    if root is None:
        return root
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    root.value = find_min(root.right)
    root.right = delete(root.right, root.value)
    return root
Time complexity: O(log_2 n) for a balanced tree, O(n) for an unbalanced tree.
    
How to validate a binary search tree?
- A binary search tree is valid if the Node Level Property holds for all nodes in the tree.
- To validate a binary search tree, you can use the Inorder Traversal algorithm to check if the values are sorted in ascending order.

From a definition perspective, a binary search tree is a binary tree where the left child of a node has a value less than the node's value, and the right child has a value greater than the node's value.

Code example:
def is_valid_bst(root):
    values = []
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            values.append(root.value)
            inorder_traversal(root.right)
    inorder_traversal(root)
    return values == sorted(values)
Time complexity: O(n)

Code example Recursive:
def is_valid_bst(root, min_val = float('-inf'), max_val = float('inf')):
    if root is None:
        return True
    if root.value <= min_val or root.value >= max_val:
        return False
    return is_valid_bst(root.left, min_val, root.value) and is_valid_bst(root.right, root.value, max_val)
    
    
"""
# This is very popular in BIG TECH interviews
def validBST(node, lower_bound, upper_bound):
    # A Null node is a valid BST
    if node is None:
        return True
    if node.value > lower_bound and node.value < upper_bound:
        return False
    if node.value <= lower_bound or node.value >= upper_bound:
        return False
    return validBST(node.left, lower_bound, node.value) and validBST(node.right, node.value, upper_bound)

validBST(root, float('-inf'), float('inf'))