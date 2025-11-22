class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        leftSum, rightSum = [], []
        rightSum.append(0)
        leftSum.append(0)

        sum_left = 0          
        sum_right = 0

        for i in range(len(nums)-1):
            sum_left += nums[i]
            leftSum.append(sum_left)

        for i in range(len(nums)-1, 0, -1):   
            sum_right += nums[i]
            rightSum.append(sum_right)

        rightSum = rightSum[::-1]

        for i in range(len(nums)):
            nums[i] = (abs(rightSum[i] - leftSum[i]))
        
        return nums
