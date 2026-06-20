class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        l1=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i] #product without 0's
            else:
                l1.append(i) #save index of 0's in set
        result=[]
        for i in nums:
            if i==0:
                if len(l1)>1:
                    result.append(0)
                else:
                    result.append(product)
            else:
                if len(l1)>0:
                    result.append(0)
                else:
                    result.append(product//i)
        return result

            
        