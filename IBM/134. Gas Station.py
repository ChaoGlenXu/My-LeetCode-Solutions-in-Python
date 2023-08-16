#134. Gas Station
#Medium 
#problem statement: https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        tot = 0
        start = 0
        for i in range(len(gas)):
            tot += (gas[i] - cost[i])
            if tot < 0:
                start = i + 1
                tot = 0
        return start
        
        '''
        #too slow, output time limit exceeded
        leng = len(gas)
        gasSum = sum(gas)
        costSum = sum(cost)

        if gasSum < costSum: 
            return -1 
        total = 0
        start = 0

        cur = 0
        while cur < leng :
            
            diff = gas[cur] - cost[cur]
            total += diff
            #print(cur)
            #print(f"diff: {diff}, total: {total}")

            if cur == leng - 1:
                if total < 0: return -1
                else: return start
            if total < 0:
                start += 1
                cur = start
                total = 0
                continue
            cur += 1

        '''

        # gas = [1,2,3,4,5]
        #cost = [3,4,5,1,2]
        #diff = [-2,-2,-2,3,3]
        #total = 3
        #start = 0
        #cur = 0


        # gas = [5,1,2,3,4]
        #cost = [4,4,1,5,1]
        #diff = [1,-3,1,-2,3]
        #total = -1
        #start = 3
        #cur = 3
        #return start



        
