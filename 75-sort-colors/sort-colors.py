def counting_sort(arr):
    maxx = max(arr) #O(n)
    counts = [0]* (maxx+1)

    for num in arr:  #O(n)
        counts[num] +=1
    
    i=0
    for count in range(maxx + 1):
        while counts[count] > 0:
            arr[i] = count
            i +=1
            counts[count] -= 1

    


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counting_sort(nums)






        """
        arr = [2,0,2,1,1,0]

        1. Count frequencies

        counts = [0,0,0]   # because max value is 2

        | x | counts  |
        | - | ------- |
        | 2 | [0,0,1] |
        | 0 | [1,0,1] |
        | 2 | [1,0,2] |
        | 1 | [1,1,2] |
        | 1 | [1,2,2] |
        | 0 | [2,2,2] |

        0 appears 2 times  
        1 appears 2 times  
        2 appears 2 times  

        2. Write back the sorted array

        i = 0
        counts = [2,2,2]

Loop through c = 0:
        counts[0] = 2
        → arr[0] = 0
        → arr[1] = 0
        counts becomes [0,2,2]
Now c = 1:
        counts[1] = 2
        → arr[2] = 1
        → arr[3] = 1
        counts becomes [0,0,2]
Now c = 2:
        counts[2] = 2
        → arr[4] = 2
        → arr[5] = 2
        counts becomes [0,0,0]
Final arr:
        [0,0,1,1,2,2]










        """