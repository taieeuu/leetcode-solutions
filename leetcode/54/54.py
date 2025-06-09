class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return []
        col = len(matrix[0])
        res = matrix[0]
        if row>1:
            for j in range(1, row):
                res.append(matrix[j][col-1])
            for i in range(col-2, -1, -1):
                res.append(matrix[row-1][i])
            
            if col>1:
                for j in range(row-2, 0, -1):
                    res.append(matrix[j][0])

        M = []
        for i in range(1, row-1):
            t = matrix[i][1:-1]
            M.append(t)
        return res + self.spiralOrder(M)
