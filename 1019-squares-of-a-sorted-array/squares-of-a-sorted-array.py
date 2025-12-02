class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pointer1 = 0
        pointer2 = len(nums) - 1

        while pointer1 <= pointer2 :
            nums[pointer1] = nums[pointer1]*nums[pointer1]
             
            if pointer1 != pointer2:  # avoid squaring same middle element twice
                nums[pointer2] = nums[pointer2]*nums[pointer2]

            pointer1 += 1
            pointer2 -= 1

        # nums.sort()    
        # to beat the O(nlogn)
        l = 0
        r = len(nums)-1
        result = []

        while (l<=r):
            if nums[l] >= nums[r]:
                result.append(nums[l])
                l+=1
            else:
                result.append(nums[r])
                r -= 1
        return result[::-1]
            



        return nums


      