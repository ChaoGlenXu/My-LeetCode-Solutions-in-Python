#55. Jump Game
#Medium
#problem statement:   https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1 
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal: goal = i
        return True if goal == 0 else False
        
