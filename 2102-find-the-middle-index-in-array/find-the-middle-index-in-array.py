class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #
        total = sum(nums)
        leftSum = 0
        Sum = 0

        for i in range(len(nums)):
            Sum += nums[i]
            rightSum = total - Sum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1        