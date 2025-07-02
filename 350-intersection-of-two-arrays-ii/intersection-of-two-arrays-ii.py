class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =[]
        c = Counter(nums1)
        for num in nums2:
            if c[num] > 0:
                result.append(num)
                c[num] -= 1
        return result 