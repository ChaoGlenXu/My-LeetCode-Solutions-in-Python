#1383. Maximum Performance of a Team
#Hard 
#problem statement: https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff, spd in zip(efficiency, speed):
            eng.append([eff, spd])
        
        eng.sort(reverse = True)

        minHeap = []
        res, totSpd = 0, 0
        for eff, spd in eng:
            if len(minHeap) == k:
                totSpd -= heapq.heappop(minHeap)
            totSpd += spd
            heapq.heappush(minHeap, spd)
            res = max(res, eff * totSpd)

        return res % (10**9 + 7)

