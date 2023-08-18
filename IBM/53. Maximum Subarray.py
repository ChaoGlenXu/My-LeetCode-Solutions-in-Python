#53. Maximum Subarray
#Medium 
#problem statement: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #after learned the approach, I used 3.43 seconds to code this pass all test cases
        #approach: if the adds up is -ve,then total continue with 0  
        largest = nums[0]
        total = 0
        for i in nums:
            total += i
            if largest < total:
                largest = total
            if total < 0:
                total = 0
        return largest


        '''
        #passed 1/4 test cases, used 15 mins code time
        largest = 0

        res = []
        total = 0
        #new_tot =  0
        for i in nums:
            if total < total + i:
                total += i
                res.append(i)
                while len(res) >= 2 and total > total - res[0]:
                    total -= res[0]
                    res.pop(0)
        return total
        '''         
        
