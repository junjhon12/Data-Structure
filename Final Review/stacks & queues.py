# Simple stack implementation using list
def stack():
    stack = []
    
    stack.append(1)
    stack.append(2)
    stack.append(3)
    
    print(stack.pop(), 'is removed from the stack')
    print(stack)
    
print(stack())
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # This is the pointer to the next node

class Stack():
    def __init__(self):
        self.head = None
    
    def add(self, data):
        # If the head is empty, create a new node
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
    def remove(self):
        # If the head is empty, return None
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
        
    def print_result(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
        
s = Stack()
s.add(1)
s.add(2)
s.add(3)
s.remove()
s.print_result()
print()

# Using deque as a queue
from collections import deque
def enqueue_max():
    queue = deque()
    
    queue.append(1)
    queue.append(2)
    queue.append(3)
    
    print(queue.popleft(), 'is removed from the queue')
    print(queue)

print(enqueue_max())
print()

# Creating a Calculator using a stack
# Import deque since we are going to use it as a stack
from collections import deque

# The operator function takes in an operator and two numbers and returns the result of the operation
def operator(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        raise ValueError("Invalid operator: " + operator)
    
def calculator(expression: str) -> int:
    # If input is empty return null/0
    if not expression:
        return 0    
    # If input is 1 number return that number
    if len(expression.split()) == 1 and expression not in ['+', '-', '*', '/']:
        return int(expression)
    # If input is 1 operator return 0
    if len(expression.split()) == 1 and expression in ['+', '-', '*', '/']:
        return 0
    # If there are more operators than numbers return 0
    if expression.count('+') + expression.count('-') + expression.count('*') + expression.count('/') > expression.count(' '):
        return 0
    # If there is just 1 operator and 1 number return 0
    if expression.count(' ') == 1 and (expression.count('+') + expression.count('-') + expression.count('*') + expression.count('/')) == 1:
        return 0

    # Container for operators
    operators = ['+', '-', '*', '/']
    # Deque as a stack
    stack = deque()
    # Seperate the expression into a list of elements so we can iterate through them
    split_expression = expression.split(" ")
    # Iterate through the elements
    for i in split_expression:
        # If the element is an operator, pop the last two elements from the stack and calculate the result
        if i in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            # Calculate the result and push it to the stack
            result = operator(i, num1, num2)
            stack.append(result)
        # If the element is a number, push it to the stack
        else:
            stack.append(int(i))
    # Return the result
    return stack.pop()
    
# 3 + 5 - 1 = 7
print(calculator("3 5 + 1 -"))
# 4 + (13 / 5) = 6
print(calculator("4 13 5 / +"))
# 10 - 6 * (9 + 3) / -11 + 17 + 5 = 22
print(calculator("10 6 9 3 + -11 * / * 17 + 5 +"))