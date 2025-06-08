from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return 
        row, col = len(matrix), len(matrix[0])

        self.res_matrix = [[0] * (col+1) for _ in range(row+1)]

        for i in range(row):
            for j in range(col):
                self.res_matrix[i+1][j+1] = (self.res_matrix[i+1][j] + self.res_matrix[i][j+1] 
                                             - self.res_matrix[i][j] + matrix[i][j])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.res_matrix[row2+1][col2+1] - self.res_matrix[row1][col2+1] -
                self.res_matrix[row2+1][col1] + self.res_matrix[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)