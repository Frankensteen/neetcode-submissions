class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1={}
        for i in nums:
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        l1=[]
        for key,value in d1.items():
            l1.append([key,value])
        l1.sort(key=lambda x:x[1])
        result=[]
        while k>0:
            temp=l1.pop()
            result.append(temp[0])
            k-=1
        return result


        