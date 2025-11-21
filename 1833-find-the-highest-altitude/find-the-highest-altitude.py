class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        point = 0
        max_ = 0
        for i in gain:
            point += i
            max_ = max(max_ , point)

        return max_
