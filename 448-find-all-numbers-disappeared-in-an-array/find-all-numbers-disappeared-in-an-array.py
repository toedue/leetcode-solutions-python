class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums: 
            pos = abs(i)-1   
            if nums[pos] > 0:
                nums[pos] *= -1 
        
        positions=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                positions.append(i+1)
        return positions