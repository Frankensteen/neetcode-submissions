class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        i,j=0,0
        global_max=0
        while i<len(s) and j<len(s):
            if s[j] not in s1:
                s1.add(s[j])
                global_max=max(j-i+1,global_max)
                j+=1
            else:         
                s1.discard(s[i])
                i+=1
                
        return global_max
            
                    


                
        