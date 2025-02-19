#198. House Robber
#Medium
#problem statement:   https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for i in nums:
            curr = max(prev1, i + prev2 )
            prev2, prev1 = prev1, curr
        return prev1
