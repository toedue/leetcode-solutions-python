class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pointer1 = 0
        pointer2 = len(nums) - 1
        result = []

        while pointer1 <= pointer2 :
            if abs(nums[pointer1]) < abs(nums[pointer2]):
                result.append(nums[pointer2]**2)
                pointer2 -= 1
            else: # abs(nums[pointer1]) >= abs(nums[pointer2]):
                result.append(nums[pointer1]**2)
                pointer1+=1

        l =0
        r = len(result) -1
        while (l<r):
            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1
        
        return result


            



      