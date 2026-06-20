class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in strs:
            word=str(len(i))+"#"+i
            encoded_string+=word
        return encoded_string

        

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            word_len=int(s[i:j])
            word=s[j+1:j+1+word_len]
            result.append(word)
            i=j+1+word_len
            
        return result
