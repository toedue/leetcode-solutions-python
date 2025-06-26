class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        result= []
        for i in nums2:
            if i in set_nums1:
                result.append(i)
                set_nums1.remove(i)
        
        return result

