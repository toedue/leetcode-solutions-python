class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Greedy 
        goal = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False

        #time complexity = O(n)