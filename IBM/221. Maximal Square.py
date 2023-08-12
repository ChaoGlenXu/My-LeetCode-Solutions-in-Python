#221. Maximal Square
#Medium 
#problem statement: https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {} #stores the maxinum square's length
        c_len = len(matrix)
        r_len = len(matrix[0])

        def help(col, row):
            if col >= c_len or row >= r_len:
                return 0
            
            if(col, row) in cache:
                return cache[(col, row)]
                
            #else is below:
            right = help(col, row+1)
            down = help(col+1, row)
            diag = help(col+1, row+1)

            #initialize             
            if matrix[col][row] == "1": 
                cache[(col,row)] = 1 + min(right, down, diag)
                return cache[(col,row)]
            else: 
                cache[(col,row)] = 0
                return 0

        help(0,0)
        print(cache)
        return max(cache.values())**2
