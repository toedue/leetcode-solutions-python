class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        result = []
        for j in range (col):
            new_row = []
            for i in range(row):
                new_row.append(matrix[i][j])
            result.append(new_row)

        return result 

        