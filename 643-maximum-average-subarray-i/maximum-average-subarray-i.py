class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_avg = current_sum/ k

        for r in range (k, len(nums)):
            current_sum = current_sum - nums[r-k] + nums[r]
            avg = current_sum/k
            max_avg = max(max_avg, avg)

        return max_avg
