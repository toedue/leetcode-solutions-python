class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength = float("inf")
        i = 0
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            while summ >= target:
                minlength = min(minlength, j-i +1)
                summ -= nums[i]
                i+=1
            
        return 0 if minlength == inf else minlength