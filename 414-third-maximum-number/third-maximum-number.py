class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        nums = list(set_nums)
        
        nums.sort(reverse = True)

        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]