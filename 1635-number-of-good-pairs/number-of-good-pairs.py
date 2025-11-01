class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        result = 0
        for num in nums:
            d[num] = d.get(num,0) +1

        for key, value in d.items():
            if value >= 2:
                result += ((value * (value -1))//2)

        return result
