#1560. Most Visited Sector in a Circular Track
#Easy
#problem statement: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        li = [0 for i in range( n+1)]
        '''
        cache = {}
        for i in range(1, n):
            cache[i] = 0
        '''
        li[0] = -1
        maxLen = len(rounds)-1

        for idx, i in enumerate(rounds):
            print(f"idx:{idx}, i:{i}")
            #li[i] += 1
            to = i
            if idx+1 <= maxLen:
                while to != rounds[idx+1]:
                    
                    li[to] += 1
                    to += 1
                    if to > n: 
                        to = 1
            else:
                li[i] += 1
        
        most = max(li)
        res = []
        for idx,i in enumerate(li):
            if i == most:
                res.append(idx)
        return res
