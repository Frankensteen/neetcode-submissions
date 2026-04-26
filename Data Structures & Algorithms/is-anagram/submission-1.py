class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for i in t:
            if i not in d.keys():
                return False
            else:
                d[i]-=1
                if d[i]<0:
                    return False
        for i in d.values():
            if i!=0:
                return False
        return True
            


        