class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top, bottom = 0, len(matrix) - 1 # rows indices
        left, right = 0, len(matrix[0]) - 1 # cols indices

        while top <= bottom and left <= right:
            # go left to right along top
            for j in range(left, right + 1):
                output.append(matrix[top][j])
            top += 1

            # go top to bottom along right
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            # go right to left along bottom
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    output.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1 

        return output

        