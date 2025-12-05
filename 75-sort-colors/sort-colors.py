def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:  #execpt the pivot
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + [pivot] + sorted_right



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        sorted_arr = quick_sort(nums)

        for i in range(len(nums)):
            nums[i] = sorted_arr[i]



    """

    arr = [2,0,2,1,1,0]
    pivot = 0


    | x | compare to pivot=0 | goes to |
    | - | ------------------ | ------- |
    | 2 | 2 > 0              | right   |
    | 0 | 0 <= 0             | left    |
    | 2 | 2 > 0              | right   |
    | 1 | 1 > 0              | right   |
    | 1 | 1 > 0              | right   |


    left  = [0]
    right = [2,2,1,1]

    Recursively sort left
    quick_sort([0])
    Length 1 → return [0]
    
    Recursively sort right:
    quick_sort([2,2,1,1])

    pivot = 1
    | x | <=1? | goes to |
    | - | ---- | ------- |
    | 2 | no   | right   |
    | 2 | no   | right   |
    | 1 | yes  | left    |

    left  = [1]
    right = [2,2]

    sort left:
    quick_sort([1]) → returns [1]
    
    sort right:
    quick_sort([2,2])
    left = [2]
    right = []
    pivot = 2

    sort left:
    quick_sort([2]) → returns [2]


    sorted result = [2] + [2] + []
               = [2,2]

    Combine Step:

    sorted_left = [1]
    sorted_right = [2,2]
    pivot = 1

    → [1] + [1] + [2,2] = [1,1,2,2]
    
    Final Combine:

    left_sorted = [0]
    pivot = 0
    right_sorted = [1,1,2,2]
    
    [0] + [0] + [1,1,2,2] = [0,0,1,1,2,2]














    """

      