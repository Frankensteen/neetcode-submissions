class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            complement=target - numbers[i]
            j=i+1
            k=len(numbers)-1
            while k>=j:
                mid=(k+j)//2
                mid_val=numbers[mid]
                if complement==mid_val:
                    return[i+1,mid+1]
                elif complement > mid_val:
                    j=mid+1
                else:
                    k=mid-1
        return [0,0]