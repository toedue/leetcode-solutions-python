class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)-1,-1,-2):
            result += min(nums[i],nums[i-1])
        return result


        





"""
The best way to do this is to pair numbers that are very close in value. This ensures that when we take the minimum of a pair, the number we "throw away" isn't much larger than the number we keep.
"""