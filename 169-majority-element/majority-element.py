class Solution:
    #
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)
        for i in range(n):
            dic[nums[i]] += 1
        for num in nums:
            if dic[num] > n/2:
                return (num)


