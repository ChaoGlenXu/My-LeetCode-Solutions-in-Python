#169. Majority Element
#Easy
#problem statement:   https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return nums[0]

        m = len(nums) // 2
        
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                if dic[i] > m:
                    return i
