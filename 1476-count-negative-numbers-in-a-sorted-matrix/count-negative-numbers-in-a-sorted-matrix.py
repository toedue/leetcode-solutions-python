class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = []
        counter = 0
        for i in range(row):
            for j in range(col):
                res.append(grid[i][j])

        res.sort()
        for num in res:
            if num >= 0:
                break
            counter += 1

        return counter
