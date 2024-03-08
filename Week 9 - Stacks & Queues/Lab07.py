"""
Instructions:
Below is how the expression is represented. This expression is also known as an
”post-fix” string expression
3 5 + 1 -

Please remember, there are space(s) between operands/operators in the expression. So your solution needs to think of this aspect.

Design a simple calculator that helps you solve the expression given. To
solve the problem a Stack will help - for which - You can use the collections.deque data structure provided in Python.
”Deques are a generalization of stacks and queues (the name is pronounced
“deck” and is short for “double-ended queue”)”

Please be reminded that you need to design the calculator and not use
in-built math methods from the programming language library to solve
the expression. Doing So would lead to a straight score of Zero ! Also at
the end of the program as a comment mention the time and space complexity of your solution. Time and space complexity is worth 15 points
each !

Very Very Important :
(1) Your code should be well commented which explains all the steps you are
performing to solve the problem. A submission without code comments
will immediately be deducted 15 points !
(2) As a comment in your code, please write your test-cases on how you would
test your solution assumptions and hence your code.
A submission without test cases (as comments) will immediately be deducted 15 points ! Please Remember : Although, written as comments -
You will address your test cases in the form of code and not prose :)
"""
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
    
print(calculator("3 5 + 1 -"))
print(calculator("4 13 5 / +"))
print(calculator("10 6 9 3 + -11 * / * 17 + 5 +"))

# Test cases
# Test case Null
print(calculator(""))
# Test case 1 element
print(calculator("1"))
# Test case 2 elements
print(calculator("1 2"))
# Test case 4 elements with 1 operator
print(calculator("1 2 3 +"))

# Time complexity: O(n), because we iterate through the expression
# Space complexity: O(n), because we use a deque to store the elements of the expression
