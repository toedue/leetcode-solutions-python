

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def counting_sort(arr):
            maxx = max(arr)

            # Step 1: count frequencies
            counts = [0] * (maxx + 1)
            for x in arr:
                counts[x] += 1

            # Step 2: fill back the array
            i = 0
            for c in range(maxx + 1):
                while counts[c] > 0:
                    arr[i] = c
                    i += 1
                    counts[c] -= 1

        counting_sort(nums)
