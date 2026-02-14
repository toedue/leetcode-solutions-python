class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row = len(matrix)
        # col = len(matrix[0])

        n = len(matrix)

        copy = [row[:] for row in matrix]


        for i in range(n):
            for j in range(n):
                matrix[i][j] = copy[n - 1 - j][i]
