class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int) # space complexity O(n)
        n = len(nums)

        #loop on the nums and store it on the hashmap with their frequency
        for i in range(n):  # Time Complexity O(n)
            dic[nums[i]] += 1

        #loop on the hashmap and find the major element
        for num in nums: # Time Complexity O(n)
            if dic[num] > n/2:
                return (num)


