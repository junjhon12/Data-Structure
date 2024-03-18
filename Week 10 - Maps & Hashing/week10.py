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
"""