#45. Jump Game II
#Medium
#problem statement:   https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def jump(self, nums: List[int]) -> int:
        res, l, r = 0, 0, 0
        
        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
             
