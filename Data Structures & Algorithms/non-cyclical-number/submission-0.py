class Solution:
    def isHappy(self, n: int) -> bool:
        Seen = set()
        def compute(n):
            result = 0
            while n > 0 :
                digit = n % 10
                result = result + digit ** 2
                n = n // 10
            return result
        while True:
            if n not in Seen:
                Seen.add(n)
            else:
                 return False
            n = compute(n)
            if n == 1:
                return True