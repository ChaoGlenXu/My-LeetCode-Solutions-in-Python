#274. H-Index
#Medium
#problem statement:   https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for idx, i in enumerate(citations, start = 1):
            #print(idx, i)
            if i >= idx: res = idx
            else: break
        return res 
