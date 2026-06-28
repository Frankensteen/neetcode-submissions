class Solution:
    def maxArea(self, arr: List[int]) -> int:
        maxArea=-1
        i,j=0,len(arr)-1
        while j>i:
            area=min(arr[i],arr[j])*(j-i)
            maxArea=max(area,maxArea)
            if arr[j]>=arr[i]:
                i+=1
            else:
                j-=1
        return maxArea
        