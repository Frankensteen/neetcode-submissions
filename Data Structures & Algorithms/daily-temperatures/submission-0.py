class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        result = [0] * n  # Initialize with zeros
        stack = []  # Stack to store indices
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            # Pop indices while current temp is greater than or equal to temp at stack top
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            
            # If stack is not empty, calculate distance
            if stack:
                result[i] = stack[-1] - i  # Distance to next warmer day
            else:
                result[i] = 0  # No warmer day ahead
            
            # Push current index to stack
            stack.append(i)
        
        return result