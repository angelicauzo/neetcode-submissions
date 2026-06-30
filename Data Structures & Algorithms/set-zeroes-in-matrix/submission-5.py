class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        mat_zero = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mat_zero.append([i, j])

        for i, j in mat_zero:
            for r in range(len(matrix)):
                matrix[r][j] = 0
        
        for i, j in mat_zero:
            for c in range(len(matrix[0])):
                matrix[i][c] = 0
