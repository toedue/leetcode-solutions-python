class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        counter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] < 0:
                    counter += 1

        return counter
