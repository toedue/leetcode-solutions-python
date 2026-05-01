class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # count of elements not equal to val
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

        #[2, 3, 1, 2, 3, 2, 4] , val =2
        # i                (n-1)

        #[4, 3, 1, 2, 3, 2, 4]
        # i            (n-1)

        #[4, 3, 1, 2, 3, 2, 4]
        # i            (n-1)

        #[4, 3, 1, 2, 3, 2, 4]
        #    i         (n-1)

        #[4, 3, 1, 2, 3, 2, 4]
        #       i      (n-1)

        #[4, 3, 1, 2, 3, 2, 4]
        #          i   (n-1)

        #[4, 3, 1, 2, 3, 2, 4]
        #          i(n-1)

        #[4, 3, 1, 3, 3, 2, 4]
        #          i
        #        (n-1)

        


