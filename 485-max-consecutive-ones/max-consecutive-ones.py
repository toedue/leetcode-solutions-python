class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #
        i = 0
        maxx=0
        for j in range(len(nums)):
            if nums[j] != 1:
                length = (j-i)
                maxx = max(maxx,length)
                i = j +1
        maxx = max(maxx, len(nums) - i) #if the array ends with 1

        return maxx
            
                 
