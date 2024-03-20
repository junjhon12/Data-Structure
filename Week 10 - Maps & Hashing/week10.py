"""
 Date: 3/18/2024
 
 Fast Search
    - Fast search is a technique that allows you to search for a value in a collection of data in O(1) time.
    
 Array is the fastest way to search for a value in a collection of data. Due to the fact that the array is a contiguous block of memory, we can access any element in the array in O(1) time. Index is the key to fast search.
 
 Hash 
 
 a -> 1
 b -> 2
 ...
 z -> 26
 
 Cab -> 3 + 1 + 2 = 6
 Baba -> 2 + 1 + 2 + 1 = 6
 
Index 0:
Index 1: a
Index 2: b
Index 3: c
Index 4: d
Index 5: e
Index 6: f  -> Cab, Baba
Index 7: g
Index 8: h

We have constant time search because we can calculate the index of the value we are looking for in O(1) time.

Hash collision is when two different keys have the same hash value. It is a common problem in hash tables.
Two main ways to solve hash collision:
    - link Chaining (Linked List) -> O(1) time to insert, O(n) time to search, worst case O(n) time to delete
    - linear probing -> O(1) time to insert, O(1) time to search, O(1) time to delete
    
[link Chaining] : a technique that allows you to store multiple values in the same index of a hash table.
[Linear Probing] : a technique that allows you to store a value in the next available index of a hash table when a collision occurs.

[Hash load] : a technique that allows you to measure the fullness of a hash table.
load = # of entries / size of array

Dictionary vs Other Dictionary :
    
Java HashMap vs Hashtable:
    - HashMap is not synchronized, it is not thread safe. It is faster than Hashtable.
    - Hashtable is synchronized, it is thread safe. It is slower than HashMap.
    
Why not to exceed 3/4 load factor?
    - If the load factor is too high, the hash table will become slow.
    - If the load factor is too low, the hash table will waste memory.
    
Dictionary (Python 2.7) vs Dictionary (Python 3.7):
Changes: 
    - Python 2.7 dictionary is not ordered.
    - Python 3.7 dictionary is ordered.
    - Python 3.7 dictionary is faster than Python 2.7 dictionary.

WHat's the diffirence between an audit dictonary and a regular dictionary?
    - Audit dictionary is a dictionary that keeps track of the order of the keys that are inserted into it.
    
    3/20/2024
    
    Topic: 
    
    How to improve a linear structure?
    - Adding a pointer, known as Tree structure.
    
    Binary Tree:
    - A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.
    
    Example:                    (4)
                        (2)             (6)
                    (1)     (3)     (5)     (7)
    Node 1 to node 4 is the ancestor of node 1.
    They have leaf nodes, which are nodes that do not have any children. Pointed to Null.
    A Null set is a set that contains no elements. It's also a binary tree.
    A single node is also a binary tree.
    The depth can be determined by the number of edges from the root to the node.
    For example, the depth of 1 is 3. The depth of 7 is 3. The depth of 2 is 1.
    [Height of a binary tree] is the number of edges on the longest path from the root to a leaf.
    [Balanced binary tree] is a binary tree in which the depth of the left and right subtrees of every node differ by at most 1 for each node.
    [Subtree] is a tree that is part of another tree.
    Each node is a subtree of itself, also it's root.
    Null is our base case and stop condition.
    
    
                   (15)
            (14)         (10)
        (13)   (N)     (N)   (9)
     (7)   (N)      (N)    (N)  (5)
     
     This is not a balanced binary tree. The depth of the left and right subtrees of the root node differ by 2.
     
     Post-order is a depth-first search algorithm that traverses the left subtree, then the right subtree, and finally the root.
     A complete node is a node that has two children or no children.
"""