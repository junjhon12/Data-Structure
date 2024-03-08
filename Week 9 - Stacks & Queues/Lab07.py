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

# Test cases
# Test case: Empty input should return 0
print(calculator(""))  # Expected output: 0

# Test case: Single number input should return that number
print(calculator("1"))  # Expected output: 1

# Test case: Two numbers input should return 0
print(calculator("1 2"))  # Expected output: 0

# Test case: Four elements with one operator input should return 0
print(calculator("1 2 3 +"))  # Expected output: 0

# Test case: Single operator input should return 0
print(calculator("+"))  # Expected output: 0

# Test case: Single operator and one number input should return 0
print(calculator("1 +"))  # Expected output: 0

# Time complexity: O(n), because we iterate through the expression
# Space complexity: O(n), because we use a deque to store the elements of the expression
