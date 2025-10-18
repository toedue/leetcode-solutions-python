class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0  # i -> child, j -> cookie
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # child is satisfied
            j += 1  # move to next cookie
        return i




