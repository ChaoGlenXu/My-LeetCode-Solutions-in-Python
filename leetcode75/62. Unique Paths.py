#62. Unique Paths
#Medium
#problem statement:   https://leetcode.com/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for y in range(m-2, -1, -1):
            new_row = [1] * n

            for x in range(n-2, -1, -1):
                #print("x is " + str(x) + " y is: " + str(y))
                new_row[x] = new_row[x+1] + row[x]
                #print(new_row[x])
            row = new_row
            
        return row[0]
        
