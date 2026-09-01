class Solution:
    def isValid(self, s: str) -> bool:
        complement_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        st = []
        for char in s:
            if char in "({[":
                st.append(char)
            else:
                if not st or st[-1] != complement_map[char]:
                    return False
                st.pop()
        
        return len(st) == 0