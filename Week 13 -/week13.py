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
        
edges = [[0,1], [0,2], [1,3], [1,4]]

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
    
"""

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
    
