class Solution:
    def isValid(self, s: str) -> bool:
        # Correct mapping: closing bracket -> opening bracket
        complement_map = {
            ")": "(",
            "}": "{", 
            "]": "["
        }
        
        st = []
        for i in s:
            if len(st) == 0:
                st.append(i)
            else:
                # Check if current char is closing bracket and matches top
                if i in complement_map and st[-1] == complement_map[i]:
                    st.pop()
                else:
                    st.append(i)
        
        return len(st) == 0