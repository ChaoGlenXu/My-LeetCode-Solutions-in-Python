#875. Koko Eating Bananas
#Medium
#problem statement:   https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length, max_k = len(piles), max(piles)
        l, r, res = 1, max_k, max_k
        
        def func(num):
            time = 0
            for i in piles:
                time += math.ceil(i / num)
            return time

        while l <= r :
            m = l + (r - l) //2
            time = func(m)
            
            if time <= h: #need to move to left
                r = m - 1
                res = m
            elif time > h: #need to move to right
                l = m + 1

        return res
