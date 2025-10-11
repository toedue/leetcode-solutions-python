class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum =0
        max_sum = nums[0]
        for num in nums:
            current_sum = max(current_sum + num, num )
            max_sum = max(max_sum, current_sum)

        return max_sum

"""
s,e
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = -2
max_sum = -2

  s e
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = -1
max_sum = -1
# current_sum -1 is less that the new number added +1 as a net so we cut -2
   s,e
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 1 so current_sum = max(current_sum + num, num)
max_sum = 1 so max_sum= (max_sum , current_sum)

    s  e
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = -2 so current_sum = max(current_sum + num/-2, num/-3)

        s,e
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 4 so current_sum = max(current_sum + num/2, num/4)
max_sum = 4 so max_sum= (max_sum , current_sum)

         s  e
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 3 so current_sum = max(current_sum + num/3, num/-1)

         s    e 
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 5 so current_sum = max(current_sum + num/5, num/2)
max_sum = 5 so max_sum= (max_sum , current_sum)

         s      e 
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 6 so current_sum = max(current_sum + num/6, num/1)
max_sum = 6 so max_sum= (max_sum , current_sum)

         s         e 
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 1 so current_sum = max(current_sum + num/1, num/-5)
max_sum = 6 so max_sum= (max_sum , current_sum)

         s           e 
[-2,1,-3,4,-1,2,1,-5,4]
current_sum = 5 so current_sum = max(current_sum + num/5, num/4)
max_sum = 6 so max_sum= (max_sum , current_sum)
"""