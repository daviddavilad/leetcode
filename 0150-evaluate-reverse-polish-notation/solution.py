class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            try:
                value = int(token) # If int does not raise valueError, then the token is an int
                stack.append(int(token))

            except ValueError: # Otherwise, it's an operator
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b)  # For decimal edge cases

                stack.append(result)
        
        return stack[-1]