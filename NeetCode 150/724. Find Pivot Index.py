#724. Find Pivot Index
#Easy
#problem statement:    https://leetcode.com/problems/find-pivot-index/description/


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s = sum(nums)
        left = 0
        
        for idx, n in enumerate(nums):
            val = s - n 
            if left * 2 == val: return idx
            left += n
        return -1
        
