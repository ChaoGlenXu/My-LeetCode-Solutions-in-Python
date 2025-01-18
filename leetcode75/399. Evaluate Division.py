#399. Evaluate Division
#Medium
#problem statement:   https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        #self.visited = set() this gobal way can cause infinite loop in this case, so this should be a variable pass in dfs 
        for idx, eq in enumerate(equations):
            a, b = eq 
            adj[a][b] = values[idx]
            adj[b][a] = 1 / values[idx]
        #print(adj) #for debuging
        def dfs(src, target, visited): 
            #print(src + " " +  target + " " + str(visited)) #for debuging
            if (src not in adj) or (target not in adj): return -1
            if src == target: return 1
            visited.add(src)
            for each in adj[src]:
                if each not in visited:
                    result = dfs( each, target, visited)
                    if result != -1:  #-------------------
                        return result * adj[src][each]  #|
            return -1 #<---------------------------------- preventing this case
        return [dfs(q[0], q[1], set())for q in queries]

        '''
        if each == target:   
            self.visited.clear()
            return accu_val * adj[src][target]
        if each in self.visited: continue 
        
        accu_val *= adj[src][each]
        dfs(each, target, accu_val)
        '''
