class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter =0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if (nums[i]==nums[j] and i<j and ((i*j)%k==0)):
                    counter+=1
        return counter
