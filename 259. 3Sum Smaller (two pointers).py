
#problem statement: https://leetcode.com/problems/3sum-smaller/

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        total = 0
        length = len(nums)
        if length < 3:
            return 0
            
        nums.sort()

        #two pointer approach
        for idx, i in enumerate(nums):
            toR = idx + 1
            toL = length - 1
            while toR < toL:
                sum3 = i + nums[toR] + nums[toL]
                if sum3 < target:
                    total += toL - toR
                    toR += 1
                else:
                    toL -= 1
                

        return total
