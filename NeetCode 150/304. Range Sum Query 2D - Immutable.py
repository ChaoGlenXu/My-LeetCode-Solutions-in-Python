#304. Range Sum Query 2D - Immutable
#Medium
#problem statement:    https://leetcode.com/problems/range-sum-query-2d-immutable/description/


class NumMatrix:

    def __init__(self, matrix: list[list[int]]):

        rows, cols = len(matrix), len(matrix[0])
        self.prefixes = [[0]*(cols+1) for _ in range(rows+1) ]

        for y in range(rows):
            prefix = 0
            for x in range(cols):
                prefix += matrix[y][x]
                above = self.prefixes[y][x + 1]
                self.prefixes[y + 1][x + 1] = prefix + above   

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        up = self.prefixes[row2][col1 - 1]
        left = self.prefixes[row1 - 1][col2]
        overlap = self.prefixes[row1 - 1][col1 - 1]
        res = self.prefixes[row2][col2] - left - up + overlap#overlap
        
        return res


    #passed all the test case, but can be improved by remove the if
    '''
    def __init__(self, matrix: list[list[int]]):

        rows, cols = len(matrix), len(matrix[0])

        self.mat = matrix
        self.prefix = [[0 for _ in range(cols)] for _ in range(rows) ]
        #print(self.prefix)

        for y in range(rows):
            for x in range(cols):
                s = matrix[y][x]
                if y - 1 >= 0: s += self.prefix[y - 1][x]
                if x - 1 >= 0: s += self.prefix[y][x - 1]
                if y - 1 >= 0 and x - 1 >= 0: s -= self.prefix[y - 1][x - 1]
                self.prefix[y][x] = s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left, up, overlap = 0, 0, 0
        if col1 - 1 >= 0: up = self.prefix[row2][col1 - 1]
        if row1 - 1 >= 0: left = self.prefix[row1 - 1][col2]
        if row1 - 1 >= 0 and col1 - 1 >= 0: overlap = self.prefix[row1 - 1][col1 - 1]
        res = self.prefix[row2][col2] - left - up + overlap#overlap
        
        return res
    '''

    '''
    def __init__(self, matrix: list[list[int]]):
        self.mat = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for y in range(row1, row2 + 1):
            for x in range(col1, col2 + 1):
                res += self.mat[y][x]
        return res
    '''

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
