from collections import deque

def calculate(operator, number1, number2): 
    # Calculate the result based on the operator
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2

def evaluate_postfix(expression: str) -> int:  # Converts to integer
    # If the expression is empty, return 0
    if expression == "":
        return 0
    # If the expression has only operator, return 0
    if len(expression) == 1 and expression in ['+', '-', '*', '/']:
        return 0
    operators = ['+', '-', '*', '/']
    stack = deque()  # Use deque as a stack since it's faster than list
    # Split the expression into a list of elements
    split_expression = expression.split(" ")
    # Iterate through the splitted elements
    for i in split_expression:
        # If the element is an operator, pop the last two elements from the stack and calculate the result
        if i in operators:
            number2 = stack.pop()
            number1 = stack.pop()
            # Calculate the result and push it to the stack
            result = calculate(i, number1, number2)
            stack.append(result)
        # If the element is a number, push it to the stack
        else:
            stack.append(int(i))
    
    return stack.pop()

# Test cases
print(evaluate_postfix("4 13 5 / +")) # 6
print(evaluate_postfix("10 6 9 3 + -11 * / * 17 + 5 +")) # 22
print(evaluate_postfix("2 7 + 3 -"))
# Test Case Null
print(evaluate_postfix(""))
# Test Case 1 element
print(evaluate_postfix("1"))
# Test Case 2 elements
print(evaluate_postfix("1 2"))
# Test Case 3 elements with 1 operator
print(evaluate_postfix("1 2 3 +"))
# Test Case 1 operator
print(evaluate_postfix("+"))

# Time complexity: O(n), where n is the number of elements in the expression
# Space complexity: O(n), where n is the number of elements in the expression
"""
By useing a deque as a stack, I can easily pop and append elements to the stack.
The reason why it's faster than a list is because it's implemented as a doubly-linked list, so it's faster to pop and append elements.
"""