#1466. Reorder Routes to Make All Paths Lead to the City Zero
#Medium
#problem statement:   https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a,b) for a, b in connections }
        neighbors = {city: [] for city in range(n)}
        self.change = 0
        visited = set()

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        #print(edges)
        #print(neighbors)

        def dfs(city):
            if city in visited:
                return
            
            visited.add(city)
            for neighbor in neighbors[city]:
                if neighbor in visited: #this make sure to exclude to its previous node, and it is very important, review this when review this question
                    continue
                if (neighbor, city) not in edges:
                    self.change += 1
                    #print("city: "+ str(city) + " neighbor :" + str(neighbor))
                
                dfs(neighbor)

        dfs(0)
        return self.change
