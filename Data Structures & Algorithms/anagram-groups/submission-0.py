class Solution:

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1={}
        for i in strs:
            key="".join(sorted(i))
            if key in d1:
                d1[key].append(i)
            else:
                d1[key]=[i]
        result=[]
        for value in d1.values():
            result.append(value)
        return result
        