class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            ptr1 = 0
            ptr2 = 0

            ans = []

            while ptr1 < len(left) and ptr2 < len(right):
                if left[ptr1] <= right[ptr2]:
                    ans.append(left[ptr1])
                    ptr1 += 1

                else:
                    ans.append(right[ptr2])
                    ptr2 += 1

            ans.extend(right[ptr2:])
            ans.extend(left[ptr1:])

            return ans

        def merge_sort(left, right, nums):
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2

            left = merge_sort(left, mid, nums)
            right = merge_sort(mid + 1, right, nums)

            return merge(left, right)

        return merge_sort(0, len(nums)-1, nums)