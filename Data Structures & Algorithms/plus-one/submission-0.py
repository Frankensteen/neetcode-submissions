class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Start with adding 1
        
        # Process from right to left
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            
            # If no carry, we're done
            if carry == 0:
                return digits
        
        # If we still have carry, add 1 at the beginning
        if carry == 1:
            return [1] + digits
            
        return digits