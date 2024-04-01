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
A graph can have cycles.

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
"""