class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in strs:
            word=str(len(i))+"#"+i
            encoded_string+=word
        return encoded_string

        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the next '#' starting from index i
            j = s.find("#", i)
            
            # Extract length and read the word
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            
            # Move pointer past the current word
            i = j + 1 + length
            
        return res
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
