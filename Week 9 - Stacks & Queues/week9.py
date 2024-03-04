'''
3/4/2024

Stack is a data structure that follows the Last In First Out (LIFO) principle.
The last element added to the stack is the first element to be removed.

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