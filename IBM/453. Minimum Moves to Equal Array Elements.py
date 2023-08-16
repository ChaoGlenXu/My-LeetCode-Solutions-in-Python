#453. Minimum Moves to Equal Array Elements
#Medium 
#problem statement: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution:
    def minMoves(self, nums: List[int]) -> int:

        nums.sort()

        lowest = nums[0]
        total = 0
        for i in nums:
            total += (i-lowest)

        return total
