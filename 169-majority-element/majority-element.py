class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)

        #loop on the nums and store it on the dictionary
        for i in range(n):
            dic[nums[i]] += 1

        #loop on the dictionary and find the major element
        for num in nums:
            if dic[num] > n/2:
                return (num)


