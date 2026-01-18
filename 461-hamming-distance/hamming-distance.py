class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #
        x = bin(x)[2:].zfill(32)
        y = bin(y)[2:].zfill(32)
        ans = 0
        for i in range(32):
            if str(x)[i] != str(y)[i]:
                ans += 1
        return ans