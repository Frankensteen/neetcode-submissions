class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Only store actual minimums
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Only push to min_stack if it's <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # Only pop from min_stack if we removed the minimum
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
    
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None