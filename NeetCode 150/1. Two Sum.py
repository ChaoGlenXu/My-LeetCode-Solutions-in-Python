#1. Two Sum
#Easy
#problem statement:    https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = dict()

        for i in range(len(nums)):
            val = target - nums[i]
            if val in d :
                return [d[val], i]
            d[nums[i]] = i

        '''
        sorted_nums = sorted(nums)

        d = dict()
        for i in range (len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i 
            else:
                d[nums[i]] = [d[nums[i]], i]

        l, r = 0, len(nums)-1

        while l < r:
            if sorted_nums[l] + sorted_nums[r] < target: 
                l += 1
            elif sorted_nums[l] + sorted_nums[r] > target: 
                r -= 1
            else: #return [l, r]
                if sorted_nums[l] != sorted_nums[r]:
                    return [d[sorted_nums[l]], d[sorted_nums[r]] ]
                else:
                    return d[sorted_nums[l]]
        '''

