class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        maxx = 1
        for j in range(1,len(nums)):
            if nums[j] <= nums[j-1]:
                length = (j - i)
                maxx = max(maxx,length)
                i = j
        length = (len(nums)-i)
        maxx = max(maxx,length)
        return maxx