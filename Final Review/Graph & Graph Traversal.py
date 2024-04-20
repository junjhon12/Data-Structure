class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def Check_of_Constraint_BST(Node):
    if Node is None:
        return True
    
    if Node.left is not None and Node.left.data > Node.data: 
        return False
    if Node.right is not None and Node.right.data < Node.data:
        return False
    
    return Check_of_Constraint_BST(Node.left) and Check_of_Constraint_BST(Node.right)

def In_Order_Traversal_BST(Node):
    stack = []
    prev = None
    
    while stack or Node:
        while Node:
            stack.append(Node)
            Node = Node.left
        Node = stack.pop()
        
        if prev and Node.data < prev.data:
            return False
        
        prev = Node
        Node = Node.right
    
    return True

def Depth_First_Search(graph, start):
    stack = [start]
    visited = set()  # Use a set instead of a list for visited nodes

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

def Breadth_First_Search(graph, start):
    queue = [start]
    visited = set()  # Use a set instead of a list for visited nodes

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited


graph = {
    1: {3, 5},
    2: {4},
    3: {5, 6},
    4: {2},
    5: {6},
    6: {5}
}

print(Depth_First_Search(graph, 2))
print(Breadth_First_Search(graph, 1))


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(Check_of_Constraint_BST(root))
print(In_Order_Traversal_BST(root))
