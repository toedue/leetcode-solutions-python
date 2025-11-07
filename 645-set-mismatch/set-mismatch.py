class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n_sum = (n*(n+1))//2
        s_sum =0
        s = set()
        for num in nums:
            if num in s:
                temp = num
            else:
                s.add(num)
        for num in s:
            s_sum += num
        missing = n_sum - s_sum
        return [temp, missing]