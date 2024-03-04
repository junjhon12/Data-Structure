'''
3/4/2024

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
print(s.pop())
s.print_stack()
print(s.pop())

# As an array
# [5, 3, 2, 1, 0, 5, 9]

def stack():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(5)
    print(stack.pop())
    print(stack)