class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = dict()
        result = ""
        for i in range(len(indices)):
            d[indices[i]] = s[i]

        sorted_d = dict(sorted(d.items()))

        for key in sorted_d:
            result += sorted_d[key]

        return result