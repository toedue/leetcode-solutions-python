class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        ptr1 = 1
        for ptr2 in range(1,len(nums)):
            if nums[ptr2] != nums[ptr2 - 1]: 
                nums[ptr1] = nums[ptr2]
                ptr1 += 1
        return ptr1