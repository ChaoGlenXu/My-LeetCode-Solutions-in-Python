# 11. Container With Most Water
#Medium
#problem statement: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        res = 0

        while l < r:
            c = min(height[l], height[r]) * (r-l)
            #print("c is: " + str(c))
            if  c > res:
                res = c
                #print("higher is: " + str(res))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            
        return res
