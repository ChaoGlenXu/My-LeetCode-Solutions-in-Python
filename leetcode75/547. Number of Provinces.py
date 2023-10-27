#547. Number of Provinces
#Medium 
#problem statement: https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num_province = 0
        n = len(isConnected)
        def dfs(point):
            visited.add(point)
            for j in range(n):
                if isConnected[point][j] == 1 and j not in visited:
                    dfs(j)
        
        for i in range(n):
            if i not in visited:
                num_province += 1
                dfs(i)
        

        return num_province



        
