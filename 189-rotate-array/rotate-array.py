class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # this will make it rotate if k > n

        nums[:] = nums[-k:] + nums[:-k]
