def merge(left,right):
    i,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If list is empty or has one element, it's already sorted
        sorted_nums = merge_sort(nums)
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]





        """
        Merge Sort
        Merge sort is a divide-and-conquer algorithm:
        split the array into halves until size ≤ 1 (base case),

        merge sorted halves back together.
        Time: O(n log n). Space: O(n) (for merging).

        Step 1 — Divide
        Split the array into two halves until each half becomes only 1 element.
        example:
        [2, 0, 2, 1]  
        → split → [2, 0] and [2, 1]  
        → split → [2], [0], [2], [1]

        Step 2 — Conquer (Sort each half)
        Each small array with 1 element is already sorted.

        Step 3 — Merge
        Merge two sorted halves into one big sorted array:

        Merge [2] and [0] → [0, 2]
        Merge [2] and [1] → [1, 2]

        Final merge:
        [0, 2] + [1, 2] → [0, 1, 2, 2]
        


        example2:
        nums = [2, 0, 2, 1, 1, 0]

        Step 1 — Split:

        Left half:  [2, 0, 2]
        Right half: [1, 1, 0]

        Split again:
        Left:
        [2]  [0,2] → [0] [2]

        Right:
        [1]  [1,0] → [1] [0]

        Step 2 — Merge small pieces:

        [0] + [2] = [0,2]
        [1] + [0] = [0,1]

        Left side becomes:
        [2] + [0,2] = [0,2,2]
        Right side becomes:
        [1] + [0,1] = [0,1,1]

        Step 3 — Final Merge:
        [0,2,2] + [0,1,1] = [0,0,1,1,2,2]



                                      [2,0,2,1,1,0]
                                /                         \
                         [2,0,2]                           [1,1,0]
                      /          \                      /          \
                   [2]         [0,2]                [1]          [1,0]
                                /    \                            /    \
                             [0]    [2]                       [1]      [0]

                             → merge → [0,2]                → merge → [0,1]

                      → merge → [0,2,2]                → merge → [0,1,1]

                       FINAL MERGE → [0,0,1,1,2,2]






        """