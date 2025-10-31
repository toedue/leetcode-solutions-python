class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        d = dict()
        for i in range (len(nums)):
            d[nums[i]] = i

        nums.sort()
        largest = nums[len(nums)-1]
        for num in nums:
            if num != largest and num*2 > largest:
                return -1
        return d[largest]