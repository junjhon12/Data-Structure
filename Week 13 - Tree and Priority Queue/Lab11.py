
from collections import deque

class Graph:
    def __init__(self, v):  # Constructor
        self.V = v  # No. of vertices
        self.adj = [[] for _ in range(v)]  # adjacency lists

    def add_edge(self, v, w):  # to add an edge to graph
        self.adj[v].append(w)  # Add w to the list of v.

    # Recursive DFS Traversal
    def dfs(self, v, visited):
        # Mark the current node as visited
        visited.add(v)
        # Print the node
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.adj[v]:
            # If the neighbor is not visited, then recur for it
            if neighbor not in visited:
                # Recur for the neighbor
                self.dfs(neighbor, visited)
    
    def traverse_dfs(self):
        # Create a set to store visited nodes
        visited = set()
        # Call the recursive helper function to print DFS traversal
        self.dfs(0, visited)

        
    # Iterative DFS Traversal
    def traverse_dfs_iterative(self):
        # Create a stack for DFS
        stack = deque()
        # Create a set to store visited nodes
        visited = set()
        # Push the current node onto the stack
        stack.append(0)  # Start with Node/Vertex 0
        # While the stack is not empty
        while stack:
            # Pop a node from the stack
            v = stack.pop()
            # If the node has not been visited
            if v not in visited:
                # Mark the node as visited
                visited.add(v)
                # Print the node
                print(v, end=" ")
                # Push all the neighbors of the node onto the stack
                for neighbor in self.adj[v]:
                    # If the neighbor has not been visited
                    stack.append(neighbor)
        print()
        
            
# Using Recursion
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(3, 5)
g.traverse_dfs()
print()

# Using Iteration
g.traverse_dfs_iterative()

# Test Cases

# Single Node
g = Graph(1)
g.traverse_dfs()
print()
g.traverse_dfs_iterative()

# 2 Nodes
g = Graph(2)
g.add_edge(0, 1)
g.traverse_dfs()
print()
g.traverse_dfs_iterative()

# Identical Edges
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.traverse_dfs()
print()
g.traverse_dfs_iterative()

# Null 
g = Graph(0)
g.traverse_dfs()
print()
g.traverse_dfs_iterative()
# Time Complexity: O(V + E)
# Space Complexity: O(V)


