class Solution:
    def isPalindrome(self, x: int) -> bool:
        compare = (str(x) == str(x)[::-1])
        return compare