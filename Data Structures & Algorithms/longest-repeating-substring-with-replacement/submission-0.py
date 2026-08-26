class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # For uppercase English letters (0-25)
        char_count = [0] * 26
        left = 0
        max_freq = 0
        max_length = 0
        
        for right in range(len(s)):
            # Increment count of current character
            char_count[ord(s[right]) - ord('A')] += 1
            
            # Update max frequency
            max_freq = max(max_freq, char_count[ord(s[right]) - ord('A')])
            
            # Check validity
            window_size = right - left + 1
            if window_size - max_freq <= k:
                max_length = max(max_length, window_size)
            else:
                # Shrink window
                char_count[ord(s[left]) - ord('A')] -= 1
                left += 1
        
        return max_length