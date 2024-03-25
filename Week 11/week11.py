import collections
"""
3/25/2024

In order:
Visit the LST
Process the node
Visit the RST

Tree node:
- A tree node is a node that has a left child, a right child, and a value.
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
