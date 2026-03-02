class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            self.arr.append(current_sum)
        

    def sumRange(self, left: int, right: int) -> int:

        right_sum = self.arr[right]
        left_sum = self.arr[left -1] if left > 0 else 0

        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)