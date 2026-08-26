class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}  # Count of each character in window
        left = 0         # Start of window
        max_freq = 0     # Maximum frequency in current window
        max_length = 0   # Result
        
        for right in range(len(s)):
            # Add current character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # Update max frequency
            max_freq = max(max_freq, char_count[s[right]])
            
            # Check if window is valid
            window_size = right - left + 1
            if window_size - max_freq <= k:
                # Valid window - update max length
                max_length = max(max_length, window_size)
            else:
                # Invalid window - shrink from left
                char_count[s[left]] -= 1
                left += 1
        
        return max_length