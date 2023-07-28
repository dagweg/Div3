# 15 minutes
class Solution:
    def reverse(self, x: int) -> int:

        y = 0
        s = -1 if x < 0 else 1
        x = abs(x)
        n = len(str(x))
        for i in range(n):
            y = y + (x % 10) * pow(10,n-i-1)
            x = x//10

        if not -2**31 <= y <= 2**31 - 1:
            return 0
        
        return s * y
    
