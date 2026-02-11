class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num3 = set(nums1 + nums2)
        first = []
        second = []
        for item in num3:
            if item not in nums2:
                first.append(item)
            elif item not in nums1:
                second.append(item)
        return [first, second]