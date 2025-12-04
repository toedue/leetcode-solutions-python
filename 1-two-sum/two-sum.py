class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        num_index = []
        
        for i in range(len(nums)):
            num_index.append((nums[i],i))
            
        num_index.sort()

        while (left <= right):
            add = num_index[left][0] + num_index[right][0]

            if add == target:
                return [num_index[left][1],num_index[right][1]]
            elif add > target:
                right -= 1
            elif add < target:
                left += 1


