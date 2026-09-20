#217. Contains Duplicate
#Easy
#problem statement:    https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = dict()
        for i in nums:
            if i not in d: 
                d[i] = 1
            else:
                #d[i] += 1
                return True
        return False
        

        
