class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numbers = set()
        for l,r in ranges:
            for i in range(l, r+1):
                numbers.add(i)

        for j in range(left, right + 1):
            if j not in numbers:
                return False
        return True


            