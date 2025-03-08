#134. Gas Station
#Medium
#problem statement:   https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): return -1
        res, len_gas, total = 0, len(gas), 0
        for i in range(len_gas):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i+1
        return res
        
    #[-2, -2, -2, 3, 3]
