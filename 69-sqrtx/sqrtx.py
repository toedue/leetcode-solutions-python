class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1 
        left = 0
        right = x 

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:   # mid^2 is too big
                right = mid - 1     # search smaller numbers
            else:               # mid^2 < x 
                ans = mid       # mid could be the answer
                left = mid + 1   # try to find a larger valid value

        return ans