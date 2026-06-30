class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_mat = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_mat.append([i, j])

        for i, j in zero_mat:
            for r in range(len(matrix)):
                matrix[r][j] = 0
            for c in range(len(matrix[0])):
                matrix[i][c] = 0

        

        
        