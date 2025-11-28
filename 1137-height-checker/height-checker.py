class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = 0

        for expect, height in zip(expected, heights):
            if expect != height:
                counter += 1

        return counter
