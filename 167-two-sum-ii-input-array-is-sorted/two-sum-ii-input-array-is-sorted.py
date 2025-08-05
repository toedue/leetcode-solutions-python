class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,7,11,15]   traget=9
        pointer1 = 0
        pointer2 = len(numbers) - 1 
        
        while (pointer1 < pointer2):
            if numbers[pointer1] + numbers[pointer2] == target:
                return [pointer1+1,pointer2+1]
            elif numbers[pointer1] + numbers[pointer2] < target:
                pointer1 += 1
            else:
                pointer2 -= 1



        