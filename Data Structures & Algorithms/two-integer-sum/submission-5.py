class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Binary Search
        # l1=[[num,i] for i,num in enumerate(nums)]
        # l1.sort()
        # left,right=0,len(nums)-1
        # while left<=right:
        #     curr_val=l1[left][0]+l1[right][0]
        #     if curr_val == target:
        #         return [min(l1[left][1],l1[right][1]),max(l1[left][1],l1[right][1])]
        #     elif curr_val > target:
        #         right-=1
        #     elif curr_val < target:
        #         left+=1
        #     else:
        #         return [-1,-1]

        # Hashmap 
        visitedMap={}
        for i, n  in enumerate(nums):
            pair_value=target-n
            if pair_value in visitedMap:
                return [visitedMap[pair_value],i]
            visitedMap[n]=i   


