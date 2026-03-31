class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def getpos(nums, target, starting):
            ans = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    if starting:        # search further left
                        right = mid - 1
                    else:               # search further right
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid +1
                    
                elif nums[mid] > target:
                    right = mid -1
            return ans
                    

        return [getpos(nums, target, True), getpos(nums, target, False)]
            