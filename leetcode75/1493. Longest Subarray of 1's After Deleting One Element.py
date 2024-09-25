#1493. Longest Subarray of 1's After Deleting One Element
#Medium
#problem statement:   https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        res = 0
        zero = 1
        lsub = 0
        rsub = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                if zero > 0: zero -= 1
                res = max(res, lsub + rsub)
                lsub = rsub
                rsub = 0
            else:
                rsub += 1
        
        if zero == 1: rsub -= 1

        return max(res, lsub + rsub)
            
