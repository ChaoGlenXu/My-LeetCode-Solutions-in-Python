#136. Single Number
#Easy
#problem statement:   https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums: res ^= i # ^ is xor 
        return res
