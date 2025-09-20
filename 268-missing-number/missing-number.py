class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        # sum(iterable, start=0) takes two arguments:
        # iterable → a sequence of numbers (like a list, tuple, or range)
        # start → a number to start adding from (default is 0)

        return sum(range(len(nums)+1)) - sum(nums)
