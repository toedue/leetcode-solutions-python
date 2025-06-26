class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        counter =0
        for num in nums:
            if counter == 0:
                element = num
            if num != element:
                counter-=1
            else:
                counter +=1
        return element

        