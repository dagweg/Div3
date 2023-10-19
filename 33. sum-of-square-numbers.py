class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2: return True
        
        left , right = 0 , int(sqrt(c))

        while left <= right:
            sum_squares = left**2 + right**2
            print(sum_squares)
            if c == sum_squares:
                return True
            elif sum_squares < c:
                left += 1
            else:
                right -= 1

        return False
