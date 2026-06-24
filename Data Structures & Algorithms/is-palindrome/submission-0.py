import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string=re.sub(r'[^a-zA-Z0-9\s]', '', s)
        l1=clean_string.strip().split()
        s1="".join(l1)
        s2=s1.lower()
        if s2!=s2[::-1]:
            return False
        return True

        