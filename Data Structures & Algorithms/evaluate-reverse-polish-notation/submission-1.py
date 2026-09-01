class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token not in operators:
                # It's a number, push to stack
                stack.append(int(token))
            else:
                # It's an operator, pop two numbers
                b = stack.pop()  # Second operand (popped first)
                a = stack.pop()  # First operand (popped second)
                
                # Perform operation
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    # Handle division towards zero
                    result = int(a / b)
                
                stack.append(result)
        
        return stack[0]  # Final result