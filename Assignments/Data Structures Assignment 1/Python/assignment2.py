class Calculator:
    def __init__(self):
        self.data = self
    
    def evaluate_expression(self, expression):
        # If the expression is empty, return "Invalid expression"
        if expression == "":
            return "Invalid expression"
        
        # Tokenize the expression
        tokens = expression.split()
        
        # two stacks for operands and operators
        number = []
        operators = []
        
        # Define operator precedence (higher number means higher precedence)
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        
        # Function to perform arithmetic operations
        def perform_operation():
            operator = operators.pop()
            operand2 = number.pop()
            operand1 = number.pop()
            if operator == '+':
                number.append(operand1 + operand2)
            elif operator == '-':
                number.append(operand1 - operand2)
            elif operator == '*':
                number.append(operand1 * operand2)
            elif operator == '/':
                number.append(operand1 / operand2)
        
        # Iterate through each token in the expression
        for token in tokens:
            # If the token is a number, add it to the operands stack
            if token.isdigit():
                number.append(int(token))
            elif token in precedence:
                # If the current operator has higher precedence than the previous operator, perform the previous operation
                while operators and precedence[token] <= precedence[operators[-1]]:
                    perform_operation()
                operators.append(token)
        
        # Perform remaining operations
        while operators:
            perform_operation()
        
        # The result is the only element left in the operands stack
        return number[0]

# Test cases:
calculator = Calculator()
expression = "10 * 2 - 15"
print(calculator.evaluate_expression(expression))

expression = "10 + 2 * 6"
print(calculator.evaluate_expression(expression))

expression = "100 * 2 / 25"
print(calculator.evaluate_expression(expression))

expression = "100 * 2 / 25 + 3"
print(calculator.evaluate_expression(expression))

expression = "2 7 + 3 -"
print(calculator.evaluate_expression(expression))

expression = "10 * 2 - 15"
print(calculator.evaluate_expression(expression))

#Test Cases
# Null
expression = ""
print(calculator.evaluate_expression(expression))
# One element
expression = "10"
print(calculator.evaluate_expression(expression))
# Same element
expression = "10 10"
print(calculator.evaluate_expression(expression))
# Same element with operator
expression = "10 10 +"
print(calculator.evaluate_expression(expression))

# Time complexity: O(n) since we're handling the element one by one
# Space complexity: O(n) since we're using two stacks to store the operands and operators
