class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize pointers at both ends of the string
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
                
            # Move pointers closer together
            left += 1
            right -= 1
            
        return True