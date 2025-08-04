class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = len(nums) -1
        # [3,2,4]
        nums_with_indices = [(value,index) for index, value in enumerate(nums)]
        # [(3,0),(2,1),(4,2)]

        nums_with_indices.sort()

        # [(2,1),(3,0),(4,2)]

        while pointer_1 < pointer_2:
            if nums_with_indices[pointer_1][0] + nums_with_indices[pointer_2][0] == target:
                return [nums_with_indices[pointer_1][1],nums_with_indices[pointer_2][1]]
            elif nums_with_indices[pointer_1][0] + nums_with_indices[pointer_2][0] > target:
                pointer_2 -= 1
            elif nums_with_indices[pointer_1][0] + nums_with_indices[pointer_1][0] < target:
                pointer_1 += 1
