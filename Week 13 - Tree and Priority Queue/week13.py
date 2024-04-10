"""
4/8/2024

Week 13

Last Structure: 

Linked List doesn't want to be an array. It wants to be a tree.

Question: How wuld you implement a tree as an array?

Heap/ Heap Q/ Priority Queue

Max Heap: The parent is always greater than the children

Example:            100
                90      80
            70  60      50  40
            
You notice that the parent is always greater than the children. 
Compare to Binary Search Tree, the parent is greater than the left child and less than the right child.

In Max Heap the root node is the largest value.
Heap is a complete binary tree.
Binary Tree: A tree where each node has at most 2 children.

Towards the leaf nodes, the tree is filled from left to right.

Example of a incomplete binary tree:        100
                                        90      80
                                    70  60      null  40
But this is complete:                       100
                                        90      80
                                    70  60  50  40  NULL
    Reason: The tree is filled from left to right. SO if left is unfilled but right is filled, it is not a complete binary tree.
    
How do we implement a heap as an array?
    1. Root is at index 0
    2. For any node at index i:
        - Left child is at index 2i + 1
        - Right child is at index 2i + 2
        - Parent is at index (i - 1) // 2
        
Example: |100|90|80|70|60|50|40|  |
            0  1  2  3  4  5  6  7  8
            
For any nodes at index i:
Parent is at index (i - 1) // 2
or Parent(i) = ((i - 1) / 2)

Inserting 20:
                 100
            90         80
        70    60    50   40
    20
New Array: 

Deleting a node:
    1. Remove the root node.
    2. Replace the root node with the last node.
    3. Heapify the tree.
    
Deleting the root node:
    Replace the root node with the last node.
    
TIme Complexity: O(log n) since you have to cut the tree in half.

The root will be lower than the children.
Which means the root is the minimum value of the tree.

                    0          n = 5
                |   |   |
                1   2   3
                |
                4
Is this a tree?
Remember that a tree is a graph without cycles.
Trees are connected graphs.    

Logic(Recursive):

We use a SET to avoid infinite loops.
We use a stack to keep track of the nodes.
        
edges = [[0,1], [0,2], [0,3], [1,4]]

0 - [1 - 2 - 3]
1 - [0 - 4]
2 - [0]
3 - [0]
4 - [1]

Build the adjacency list:
{0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}

if n == None:
    return True;
adj_list = {i: [] for i in range(n)}
for node1, node2 in edges:
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
    
visited = set()

dfs stands for Depth First Search

def dfs(node, visited):     Cycle Checking
    if node in visited:
        return False;
    visited.add(node)
    for neighbor in adj_list[node]:
        if neighbor == prev:
            continue
        if not dfs(neighbor, node):
            return False
    return True
    
return(dfs(0, float('inf'))) and len(visited) == n

Time Complexity: O(n)
Space Complexity: O(n) located in the visited set.

    
Connected Components:
def connected_components(n, edges):
    adj_list = {i: [] for i in range(n)}
    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
        
    visited = set()
    components = 0
    for node in range(n):
        if dfs(node, None):
            components += 1
    return components
    
Graph Valid Tree:

    
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def dfs(node, prev, visited, adj_list):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor == prev:
                continue
            if not dfs(neighbor, node, visited, adj_list):
                return False
            return True
        

    
"""
4/10/2024

A Node property of a min heap is that the parent is [ALWAYS] less than the children.
Subtree is recursively a heap in each node.

Example:            10
                11     15
            20  32   45  50
            
Left Child: 2i + 1
Right Child: 2i + 2
Parent: (i - 1) // 2

What's the difference between priority queue and heap queue thread safety?
Priority Queue is thread safe.
Heap Queue is not thread safe.

Thread unsafe means that it is not safe to use in a multi-threaded environment.

Out of heap queue and priority queue, which one is based off the other?
Heap Queue is based off Priority Queue.
"""

"""
                        3
                    5       NULL
                8       10
            9    NULL  NULL  NULL
            
A Balance Tree is a tree where the height of the left and right subtrees of any node differ by at most 1.
"""
# Traversal should be converted to 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def check_balance(self, root):
        def depth_first_search(root):
            if root is None:
                return [True, 0]
            left_subtree = depth_first_search(root.left)
            right_subtree = depth_first_search(root.right)
            #Balance is the difference between the left and right subtree heights
            balance = (left_subtree[0] and right_subtree[0]) and (abs(left_subtree[1] - right_subtree[1]) <= 1)
            
            return [balance, max(left_subtree[1], right_subtree[1]) + 1]
        return depth_first_search(root)[0]

    
    
root = Node(3)
root.left = Node(5)
root.right = Node(None)
root.left.left = Node(8)
root.left.right = Node(10)
root.left.left.left = Node(9)
print(root.check_balance(root))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root.check_balance(root))
