class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        min_sum = 0

        for num in nums:
            sum += num
            min_sum = min(min_sum, sum)

        if min_sum > 0:
            return 1
        else:
            return -min_sum + 1