class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = dict()
        result = ""
        n = len(indices)
        for i in range(n):
            d[indices[i]] = s[i]

        for i in range(n):
            result += d[i]

        return result