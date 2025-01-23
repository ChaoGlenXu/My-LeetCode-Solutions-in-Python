#994. Rotting Oranges
#Medium
#problem statement:   https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        l_y , l_x, directions = len(grid), len(grid[0]), ((0, 1), (0, -1), (1, 0), (-1, 0))
        res_time, rotten, fresh = 0, set(), 0
        #find each rotten orange, and bfs for each
        for index_y, y in enumerate(grid):
            for index_x, x in enumerate(y):
                if grid[index_y][index_x] == 2: rotten.add((index_y, index_x, 0))
                if grid[index_y][index_x] == 1: fresh += 1
        queue = deque(rotten)
        
        while queue:
            row, col, time = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if 0 <= new_r < l_y and 0 <= new_c < l_x and grid[new_r][new_c] == 1:
                    if time + 1 > res_time: res_time = time + 1
                    queue.append((new_r, new_c, time + 1))
                    fresh -= 1
                    grid[new_r][new_c] = 2

        return -1 if fresh > 0 else res_time
      
