class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        counter = 1
        for i in range(len(nums)):
            if nums[i] != nums[unique]:
                unique += 1
                nums[i], nums[unique] = nums[unique], nums[i]
                counter += 1
        return counter


"""
But the total number of unique elements should be unique + 1, not just the number of new elements
"""
