class Solution:

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1={}
        for i in strs:
            key="".join(sorted(i))
            if key in d1:
                d1[key].append(i)
            else:
                d1[key]=[i]
        return list(d1.values())

        