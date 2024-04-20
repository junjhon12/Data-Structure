class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def Check_Balance(self, root):
        def Depth_First_Search(root):
            if root is None:
                return [True, 0]
            left_Subtree = Depth_First_Search(root.left)
            right_Subtree = Depth_First_Search(root.right)
            Balanced = left_Subtree[0] and right_Subtree[0] and abs(left_Subtree[1] - right_Subtree[1]) <= 1
            return [Balanced, max(left_Subtree[1], right_Subtree[1]) + 1]
        return Depth_First_Search(root)[0]
        

def Tree_Check(n, edges):
    if n is None:
        return True
    adj_list = {i: [] for i in range(n)}
    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
        
    visited = set()
    
    def dfs(node, prev, visited):     # Add 'prev' parameter
        if node in visited:
            return False
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor == prev:
                continue
            if not dfs(neighbor, node, visited):   # Pass 'visited' as an argument
                return False
        return True
    return dfs(0, float('inf'), visited) and len(visited) == n

print(Tree_Check(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print()
root = Node(3)
root.left = Node(5)
root.right = Node(None)
root.left.left = Node(8)
root.left.right = Node(10)
root.left.left.left = Node(9)
print(root.Check_Balance(root))