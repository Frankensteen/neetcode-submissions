import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keeps only letters and numbers, then converts to lowercase
        s1 = "".join(char.lower() for char in s if char.isalnum())
        return s1 == s1[::-1]

        