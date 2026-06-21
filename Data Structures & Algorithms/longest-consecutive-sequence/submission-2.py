class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0  # Fix 1: Handle empty list edge case
        result=1
        i=0
        # O(n) using set
        s1=set(nums)
        for num in s1:
            if num-1 not in s1: # streak start
                current_num=num
                count=1
                while current_num+1 in s1:
                    count+=1
                    current_num+=1
                result=max(count,result)
        return result

        
            
        
        


                

        