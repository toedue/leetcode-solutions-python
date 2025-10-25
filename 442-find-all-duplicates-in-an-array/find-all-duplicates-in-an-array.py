class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dublicate = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dublicate.append(index + 1)
            nums[index] = -nums[index]

        return dublicate

            