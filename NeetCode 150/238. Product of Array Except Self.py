#238. Product of Array Except Self
#Medium
#problem statement:    https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        prefix, postfix, res = 1, 1, [None] * size

        for idx in range(size):
            res[idx] = prefix
            prefix *= nums[idx]

        for idx in range(size -1, -1, -1):
            res[idx] *= postfix
            postfix *= nums[idx] 
        return res
