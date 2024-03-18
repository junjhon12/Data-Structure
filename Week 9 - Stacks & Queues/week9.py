'''
3/4/2024 - Monday

Stack is a data structure that follows the Last In First Out (LIFO) principle.
The last element added to the stack is the first element to be removed.
It's access restriction structure is called FILO (First In Last Out).

Pro:
- Fast operations
- Fast access to the last element
- Easy to implement

Con:
- Fixed size
- Slow access to other elements
- Slow search
- Slow to remove elements
- Slow to insert elements

Stack overflow is when the stack is full and you try to add more elements.

When trying to pop from an empty stack, it's called stack underflow.
The result is an error

Time complexity:
- Access: O(n) since we're handling the element one by one

Reverse Polish Notation (RPN) is a mathematical notation in which every operator follows all of its operands.
Example: 
RPM: 2 7 + 3 -
a = 3
b = 9
b - a = 6

Time complexity:
- Access: O(n)
Space complexity:
- O(n) -> Pre-Allocation

Polish Notation (PN) is a mathematical notation in which every operator precedes all of its operands.
Example:
PN: 2 * 6 + 2 / 1 - 3
2 * 6 = 12
a = 3
b = 16
b - a = 13
Time complexity:
- Access: O(n)
Space complexity:
- O(n) -> Pre-Allocation inside the two stacks

push will add an element to the top of the stack
peek will return the top element of the stack
pop will remove the top element of the stack
'''

def stack():
    #Empty stack
    stack = []
    
    #Add elements to the stack
    stack.append(1)
    stack.append(2)
    stack.append(3)
    
    #Remove elements from the stack
    print(stack.pop())
    
    #Print the stack
    print(stack)
    
print(stack())

# As a linked list
# 1 -> 5 ->3 -> 7 -> Null
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
        
    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
        
s = Stack()
s.push(1)
s.push(5)
s.push(3)
s.push(7)
s.print_stack()

# As an array
# [5, 3, 2, 1, 0, 5, 9] output after popping last element
# Output: [5, 3, 2, 1, 0, 5]
def stack():
    stack = []
    stack.append(5) #First in
    stack.append(3)
    stack.append(2)
    stack.append(1)
    stack.append(0)
    stack.append(5)
    stack.append(9) #Last in
    print(stack.pop())
    print(stack)
    
print(stack())

"""
3/6/2024 - Wednesday

Call stack is a stack data structure that stores information about the active subroutines of a computer program.
Recursion is not memory free, it uses the call stack to store the return address of the function.

F(4) = 4 * F(3) = 4 * 3 * F(2) = 4 * 3 * 2 * F(1) = 4 * 3 * 2 * 1 * F(0) = 4 * 3 * 2 * 1 * 0 = 24

| F(0) |    F(0) = 0
| F(1) |    F(1) = 1
| F(2) |    F(2) = 2  Recursion Fall Stack
| F(3) |    F(3) = 6
| F(4) |    F(4) = 24
|______|
 Stack  -> O(n)
 
 There is no Recursion without a Call Stack, never.
 Recursive Binary has extra memory due to the call stack.
 How does the fibonacci knows the previous value?
 
 
 
 New Topic: Queues
 
    Queue is a data structure that follows the First In First Out (FIFO) principle.
    Array and Linked List are the two main ways to implement a queue.
    
    
    Head: 5 -> 4 -> 3 -> 2 -> 1 -> Null
    
    Base Average: 5 | 4 | 9 | 7 | 11 | 8
    
    Pro:
    - Fast operations
    - Fast access to the first element
    - Easy to implement
    
    Con:
    - Fixed size
    - Slow access to other elements
    - Slow search
    - Slow to remove elements
    - Slow to insert elements
    
    Time complexity:
    - Access: O(n) since we're handling the element one by one
    Space complexity:
    - O(n) -> Pre-Allocation
    
    When in queue a used space is called a base. To prevent overflow, we can use a circular queue.
    That way,  can use the empty spaces in the base.
    
    Double Ended Queue (Deque) is a queue that allows insertion and removal of elements from both ends.
 
    Head-> 1, 4, 2, 3, 7 <-Tail
    Find the maximum element in the queue.
    In constant time, we can find the maximum element in the queue.
    The maximum element is always at the head or tail of the queue.
    You need an extra data structure to keep track of the maximum element.
    
                Head
    Main Queue: 1,  4,                      2,      3
    Max Queue:  1 -> 4 (replace 1 with 4) -> 4, 2 -> 4, 3
    If a new item, i, is greater than the last element in the max queue, pop the last element and append i.
        remove from tail of Max Q
    equal to Max Q
    Time complexity: O(1)
    Space complexity: O(n) -> Pre-Allocation inside the two stacks
    
    Function:
    # a new item i
      while i > tail item of Max Q
        remove from tail of Max Q
      enqueue to Max Q
      
    Accessing from the head is stack, accessing from the tail is a queue.
    
    Read landing content
    FIrst is intro
    second an third is what you want to focus on
    
    Python:
    from collections import deque
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.popleft()
    print(q)
    
    Enque process in the Max Queue
        while new element(i) > tail element of Max Queue
            remove tail element of Max Queue
        append new element(i) to Max Queue
        
    Time complexity:
    - Access: O(n)
    Space complexity:
    - O(n) -> Pre-Allocation
    
    Code:
    from collections import deque
from collections import deque
    class MaxQueue:
        def __init__(self):
            self.q = deque()
            self.max_q = deque()
            
        def enqueue(self, i):
            while self.max_q and i > self.max_q[-1]:
                self.max_q.pop()
            self.max_q.append(i)
            self.q.append(i)
            
        def dequeue(self):
            if self.q[0] == self.max_q[0]:
                self.max_q.popleft()
            return self.q.popleft()
            
        def max(self):
            return self.max_q[0]
            
    q = MaxQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    print(q.max())
    
    deque process
    if head(max queue) == head(queue)
        remove head(max queue)
    remove head(queue)
    
    Time complexity:
    - Access: O(n)
    Space complexity:
    - O(n) -> Pre-Allocation
    
    Deque:
    if Main Queue(front) == Max Queue(front)
        remove from Max Queue(front)
    else
        remove from Main Queue(front)
        
    Time complexity: O(1)
    Space complexity: O(n) -> inside Max Queue
"""
from collections import deque
def enqueue_max(q, max_q, i):
    while max_q and i > max_q[-1]:
        max_q.pop()
    max_q.append(i)
    q.append(i)

q = deque()
max_q = deque()

enqueue_max(q, max_q, 1)
enqueue_max(q, max_q, 4)
enqueue_max(q, max_q, 2)
enqueue_max(q, max_q, 3)

print(q)
print(max_q)