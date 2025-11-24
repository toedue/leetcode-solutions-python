class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i+1, n+1):
                if (j-i)%2:
                    ans += sum(arr[i:j])
        return ans