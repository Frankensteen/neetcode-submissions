class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Maps character to its last seen index
        left = 0         # Start of sliding window
        max_length = 0   # Result
        
        for right in range(len(s)):
            # If character was seen and is within current window
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # Jump to right after last occurrence
            
            char_index[s[right]] = right  # Update last seen index
            max_length = max(max_length, right - left + 1)  # Update max length
        
        return max_length