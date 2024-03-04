"""
2/26/2024

Topic: Linked List

17, 15, 28, 31, 25
int => 4 bytes
Base address: 1000

Access(i, =3)   = Base Address + (dts) * i
                = 1000 + (4 * 3)
                = 1012
                
Time complexity is O(1) due to the contiguous memory.           
Base Address is known as the head of the linked list.
[17] -> [15] -> [28] -> [31] -> [25] -> NULL

The trade-off of a linked list is speed for memory.
The head is O(n) because it has to traverse the entire list to find the last element.
What would we lose if we hade the linked list as one class?
    - We would lose the ability to traverse the linked list.
    
Python default implmentation of a linked list is a list.
Python doesn't have a linked list class. Therefore, we have to create our own linked list class.
Why does Python not have a linked list class?
    - Python is a high-level language and is not concerned with the low-level implementation of a linked list.
    - Python is more concerned with the high-level implementation of a linked list. It's no longer used in the industry.
    
Program Problem:
    (7)->(6)->(19)->(14)    Expected Output: (14)->(19)->(6)->(7)
    Task: Reverse the linked list.
    
"""
# Given 7 -> 6 -> 19 -> 14 Expected Output: 14 -> 19 -> 6 -> 7

class Node:
    # Use self and data since we are creating a new node.
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList_Reverse:
    # Use self since we are creating a new linked list.
    def __init__(self):
        self.head = None
    # Use self and data since we are inserting a new node.
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # Use self since we are printing the linked list.
    def print_list(self):
        # Use temp since we are traversing the linked list.
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
ll = LinkedList_Reverse()
ll.insert(7)
ll.insert(6)
ll.insert(19)
ll.insert(14)
ll.print_list()

"""
Review:

[9][10][15][12]
[9] is head address
int -> 4 bytes
Accessing 3rd element: element(i, i=2) = Base Address + (dts) * i
1000 + (4 * 2) = 1008

n = 600M
i = 232M
If done with this will not be any different since the time complexity is O(1).

Reason why the whole list isn't used but instead is used in small containers is because it'll be more stressful when using CRUD(create, read, update, delete) operations.

Distadvatng/Trade-off when using liked list is the usemento f O(n) time complexity.

Cirular linked list is when the last element points to the first element.
[9] -> [10] -> [15] -> [12] -> [9]

Doubly linked list is when the elements point to the next and previous elements.
[9] <-> [10] <-> [15] <-> [12]

Use address to access the elements of the linked list.

Python DOES NOT have linked list

You can place pointers inside arrays.
"""

"""
2/28/2024

Topic: Linked List

Technical Interview Question:
7 -> 5 -> 15 -> 13 -> null
Expected Output:
13 -> 15 -> 5 -> 7 -> null
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def setNext(self, new_next):
        self.next = new_next
        
class linkedList_Reverse:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def print_list(self):
        # Use temp since we are traversing the linked list.
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
ll = linkedList_Reverse()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
print(ll.print_list())


"""
    Simulation:
    Given: 7 -> 5 -> 15 -> 13 -> NULL
    Expected Output: 13 -> 15 -> 5 -> 7 -> NULL
    1. prev = None, current = 7, temp = 5 -> 15 -> 13 -> NULL
    2. current.next = prev, prev = 7, current = 5, temp = 15 -> 13 -> NULL
    3. current.next = prev, prev = 5, current = 15, temp = 13 -> NULL
    4. current.next = prev, prev = 15, current = 13, temp = NULL
    5. current.next = prev, prev = 13, current = NULL, temp = NULL
    6. self.head = prev
    7. 13 -> 15 -> 5 -> 7 -> NULL
    Time Complexity: O(n) n is the number of nodes in the linked list
    Space Complexity: O(1)
    Memory Complexity: O(1)
    
    The program will run exactly the number of nodes in the linked list.
    
    Why linked list isn't used in the industry?
    - The trade-off of a linked list is speed for memory.
    Why does Big Tech companies use linked list?
    
"""

"""
Problem 2: linkedList Cycle
Given: 7 -> 10 -> 6 -> 9 cycle to 6
Expected Output: True, there is a cycle
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    def setNext(self, new_next):
        self.next = new_next
        
class LinkedList_Cycle:
    def __init__(self):
        self.head = None 
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def print_list(self):
        # Use temp since we are traversing the linked list.
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
    def check_cycle(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            # Slow pointer moves one step
            slow = slow.next
            # Fast pointer moves two steps
            fast = fast.next.next
            # If the two pointers meet, then there is a cycle
            if slow == fast:
                return 'True, there is a cycle'
        return 'False, there is no cycle'
    
ll = LinkedList_Cycle()
ll.add(7)
ll.add(10)
ll.add(6)
ll.add(9)
ll.head.next.next = ll.head.next
print(ll.check_cycle())
