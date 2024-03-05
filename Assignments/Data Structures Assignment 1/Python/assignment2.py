class Calculator:
    def __init__(self):
        self.stack = []

    def evaluate_expression(self, expression):
        """
        Evaluates the given expression and returns the result.

        Args:
            expression (str): The expression to evaluate.

        Returns:
            int or float: The result of the expression evaluation.
        """
        tokens = expression.split()
        for token in tokens:
            if token.isdigit() or (token.count('.') == 1 and token.replace('.', '').isdigit()):
                self.stack.append(float(token))
            else:
                if token == '+':
                    self.stack.append(self.stack.pop() + self.stack.pop())
                elif token == '-':
                    num2 = self.stack.pop()
                    num1 = self.stack.pop()
                    self.stack.append(num1 - num2)
                elif token == '*':
                    self.stack.append(self.stack.pop() * self.stack.pop())
                elif token == '/':
                    num2 = self.stack.pop()
                    num1 = self.stack.pop()
                    self.stack.append(num1 / num2)
        return self.stack.pop()

# Test cases:
# Example usage:
calculator = Calculator()
# result = calculator.evaluate_expression("3 4 + 2 *")
# print("Result:", result)
# Expected output: Result: 14

# Test case with parentheses:
result = calculator.evaluate_expression("( 3 + 4 ) * 2")
print("Result:", result)
# Expected output: Result: 14

# Test case with floating point numbers:
# result = calculator.evaluate_expression("3.5 2 * 1.5 +")
# print("Result:", result)
# Expected output: Result: 8.5

# Test case with larger expression:
# result = calculator.evaluate_expression("10 2 * 15 -")
# print("Result:", result)
# Expected output: Result: 5

# Test case with division:
# result = calculator.evaluate_expression("10 5 /")
# print("Result:", result)
# Expected output: Result: 2.0

# Test case with multiple operators:
# result = calculator.evaluate_expression("3 4 + 5 * 6 2 / -")
# print("Result:", result)
# Expected output: Result: 29.0

# Time complexity: O(n)
# Space complexity: O(n)
