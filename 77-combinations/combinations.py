class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, currCombination):
            if len(currCombination) == k:
                res.append(currCombination.copy())
                return

            for i in range(start, n+1):
                currCombination.append(i)
                backtrack(i + 1, currCombination)
                currCombination.pop()

        backtrack(1, [])

        return res


