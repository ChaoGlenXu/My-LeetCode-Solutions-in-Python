#1926. Nearest Exit from Entrance in Maze
#Medium
#problem statement:   https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        res, y_len, x_len = 0, len(maze), len(maze[0])

        self.visited = set([(entrance[0], entrance[1])])            
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))    #to right, to left, to down, to up
        queue = deque([(entrance[0], entrance[1], 0)])

        while queue: # solving with bfs
            row, col, steps = queue.popleft()
            #print("popleft: " + str(row) + "  " + str(col) + "  " + str(steps)+ "----------")

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc    
                
                if 0 <= new_row < y_len and 0 <= new_col < x_len and maze[new_row][new_col] == ".":
                    if (new_row, new_col) in self.visited: continue
                    if new_row == 0 or new_col == 0 or new_row == y_len - 1 or new_col == x_len - 1: return steps + 1
                    
                    queue.append((new_row, new_col, steps + 1))
                    self.visited.add((new_row, new_col))
        return -1
