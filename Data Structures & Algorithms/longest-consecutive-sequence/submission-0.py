class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0  # Fix 1: Handle empty list edge case
        nums.sort()
        result=1
        i=0
        #brute force approach using two pointer and sort
        while i < len(nums)-1:
            count=1
            j=i+1
            while j<len(nums) and nums[j]-nums[j-1]<=1 :
                # Fix 3: Skip duplicate numbers instead of incrementing count
                if nums[j] == nums[j-1]:
                    j+=1
                    continue
                count+=1
                j+=1
            result=max(count,result)
            i=j
        return result





                

        