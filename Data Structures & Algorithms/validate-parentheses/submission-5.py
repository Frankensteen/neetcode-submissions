class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []
        
        # Hash map to match closing brackets with opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # For each character in string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # Pop the matching opening bracket
                stack.pop()
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
        
        # Valid if stack is empty (all brackets matched)
        return len(stack) == 0