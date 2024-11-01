#2352. Equal Row and Column Pairs
#Medium
#problem statement:   https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_count = Counter(tuple(row) for row in grid)
        n, result = len(grid), 0 #n is the length of the grid

        for y in range(n): #note: y is the each row, so y should now chage, x is the one should change for each row in the inner loop
            col = tuple( grid[x][y] for x in range(n))
            if col in row_count: result += row_count[col]
        
        return result
        
        
        
        
