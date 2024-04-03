"""
4/1/2024
Week 12 - Graphs & Graph Traversal

Graphs
- A graph is a set of nodes and edges that connect the nodes.
- A graph can be directed or undirected.
- A graph can be weighted or unweighted.
- A graph can be cyclic or acyclic.

G = (V, E)
- V is a set of vertices (nodes)
- E is a set of edges
                                        V1
V = {V1, V2, V3}               e1 2 |       | e1 3
E = {e1 2, e1 3}                   V2      V3           V4

Difference between graph and tree: 
A tree is a connected graph with no cycles. 
A graph can have cycles without being connected.

Undirected Graphs: Edges have no direction. (V1, V2) == (V2, V1)
Directed Graphs: Edges have a direction. (V1, V2) != (V2, V1)           V1 -> V2 but not V2 -> V1
Bidirectional Graphs: Edges have two directions. (V1, V2) == (V2, V1)   V1 <-> V2

Bidirectional Graphs and Undirected Graphs behave the same way.

Problem:
V1 -> V2 -> V3 -> V1    This is a cycle. A Cyclical Graph.

V1 -> V2 -> V3 -> V1  V4  This is a tree. A Tree Graph.
V1 -> V2 -> V3 -> V1      This is a graph with a cycle.

All trees are graphs but not all graphs are trees.

Difference between an abstract data type and a data structure: 
An abstract data type is a concept or model that defines a set of operations.
A data structure is an implementation of an abstract data type.

A Matrix is one way to represent a graph.
- A matrix is a 2D array.
- The matrix is a square matrix.
- The matrix is symmetric for undirected graphs.
- The matrix is not symmetric for directed graphs.

Another way to represent a graph is with an adjacency list.

4/3/2024

Graph Problem:  1 -> 2 -> 3
                1 -> 4
                
Adjacency matrix:
    1 2 3 4
1   0 1 0 1
2   0 0 1 0
3   0 0 0 0
4   0 0 0 0      

Widely used form: Adjacency List
1: [2, 4]
2: [3]
3: [] or Null
4: [] or Null

1 to 4 is the vertex list (Y axis) |V|
Edge list (X axis) is across |E|

Code:
{i : []] for i in range(1, 5)} typical data structure for an adjacency list.
                <---|E|--->    
1 -> 2  <     |   1: [2, 3]
|   |   |     |   2: [4]
3 -> 4  <    |V|  3: [4, 5]
|   |         |   4: [2, 6]
5 -> 6        |   5: [6]
                  6: []  

Depth First Search (DFS)
- A graph traversal algorithm.
- Visits all the nodes in a graph until you hit null.
- Uses a stack to keep track of nodes.
- Uses a recursive approach.

Example:
1 -> 3 -> 5 -> 6 -> Null
5
3 -> 4 -> 2 -> 4 -> 2 (Stack Overflow)
1 -> 2 -> 4 -> 2 -> 4 -> 2 (Stack Overflow)

How to avoid a stack overflow or infinite loop?: 
- Keep track of visited nodes.
- Use a set to keep track of visited nodes.

1) Go to the first node.
2) Declare a stack
3) Push the first node onto the stack and record the node in the hash set.
4) While the stack is not empty:
    item = stack.pop()
    Process the item
    for each element j in the edge list:
        if j is not in the visited set:
            stack.push(j) and record in the used set
            visited.add(j)
5) Return the visited set.

stack = []
visited = set()

Depth First Search -> 1, 3, 5, 6, 4, 2
Space complexity is O(V) -> The number of vertices.
TIme complexity is O(V + E) because you have to visit every vertex and edge.

Depth First Search (DFS) Algorithm
1) Go to the first node.
2) Declare a stack
3) Push the first node onto the stack and record the node in the hash set.
4) While the stack is not empty:
    item = stack.pop()
    Process the item
    for each element j in the edge list:
        if j is not in the visited set:
            stack.push(j) and record in the used set
            visited.add(j)

Breath First Search (BFS) Algorithm
1) Go to the first node.
2) Declare a queue
3) Enqueue the first node onto the queue and record the node in the hash set.
4) While the queue is not empty:
    item = queue.dequeue()
    Process the item
    for each element j in the edge list:
        if j is not in the visited set:
            queue.enqueue(j) and record in the used set
            visited.add(j)
5) Return the visited set.

Brea
"""
def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

