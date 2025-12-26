class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
        
"""
XOR = AB'+ A'B
A B ^
0 0 0
0 1 1
1 0 1
1 1 0

Duplicate numbers cancel each other
The remaining number is the answer

nums = [4, 1, 2, 1, 2]

result = 0
0 ^ 4 = 4  000-100 = 100
4 ^ 1 = 5  100-001 = 101
5 ^ 2 = 7  101-010 = 111
7 ^ 1 = 6  111-001 = 110
6 ^ 2 = 4  110-010 = 100

"""