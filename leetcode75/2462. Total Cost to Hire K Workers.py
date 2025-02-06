#2462. Total Cost to Hire K Workers
#Medium
#problem statement:   https://leetcode.com/problems/total-cost-to-hire-k-workers/description/?envType=study-plan-v2&envId=leetcode-75

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        #below are optimized for space and memory by removing index from heap
        min_heap = []
        res, n = 0, len(costs)
        left, right = 0, n-1 
        
        for l in range(min(candidates, n)):
            heapq.heappush(min_heap, (costs[l], "left"))
            left +=1
        left -= 1 #make it pointing the index
   
        for _ in range(candidates):
            if left < right:
                heapq.heappush(min_heap, (costs[right], "right"))
                print("right pushed: " + str(right))
                right -= 1
        right += 1 #make it pointing the index
 
        for i in range(k):
            cost,  side = heapq.heappop(min_heap)
            res += cost

            if side == "left" and left + 1 < right:
                heapq.heappush(min_heap, (costs[left+1],  "left"))
                left += 1
            elif side == "right" and  right - 1 > left:
                heapq.heappush(min_heap, (costs[right-1],  "right"))
                right -= 1
        
        return res

        ''' # the code that passed all the test cases
        min_heap = []
        res, n = 0, len(costs)
        left, right = 0, n-1 
        
        for l in range(min(candidates, n)):
            heapq.heappush(min_heap, (costs[l], l, "left"))
            left +=1
        left -= 1 #make it pointing the index
        #for r in range(n-1, max(-1, n-1-candidates), -1): this is very inconvient and brain draining way
        for _ in range(candidates):
            if left < right:
                heapq.heappush(min_heap, (costs[right], right, "right"))
                print("right pushed: " + str(right))
                right -= 1
        right += 1 #make it pointing the index
        #print(left)
        #print(right)
        for i in range(k):
            cost, index, side = heapq.heappop(min_heap)
            res += cost

            if side == "left" and left + 1 < right:
                heapq.heappush(min_heap, (costs[left+1], left+1, "left"))
                left += 1
            elif side == "right" and  right - 1 > left:
                heapq.heappush(min_heap, (costs[right-1], right-1, "right"))
                right -= 1
        
        return res
        '''


        # i found a very easy way to get the same output required # this is wrong cuz i misunderstood this question
'''
        costs = sorted(costs)

        res = 0
        for i in range(k):
            res += costs[i]

        return res
'''

'''
        [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
        [17,12,10,2,7,11,20,8]
        [17,12,10,7,11,20,8]
'''
