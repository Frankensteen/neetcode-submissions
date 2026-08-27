class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Create frequency map for s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        window_size = len(s1)
        
        # Check each substring of s2 with length equal to s1
        for i in range(len(s2) - window_size + 1):
            substring = s2[i:i + window_size]
            substring_count = {}
            
            # Count characters in current substring
            for char in substring:
                substring_count[char] = substring_count.get(char, 0) + 1
            
            # Compare with s1's character count
            if substring_count == s1_count:
                return True
        
        return False