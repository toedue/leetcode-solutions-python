class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maxx = summ/k
        for i in range(k,len(nums)):
            summ = summ + nums[i] - nums[i-k]
            avg = summ/k
            maxx = max(maxx, avg)
            
        return maxx
            


