class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x % 10 == 0 and x != 0) or (x < 0 and x != 0):
            return False 
        
        reverse_x = 0
        while reverse_x < x:
            reverse_x = reverse_x*10 + x%10
            x //= 10
        return reverse_x == x or reverse_x//10 == x
