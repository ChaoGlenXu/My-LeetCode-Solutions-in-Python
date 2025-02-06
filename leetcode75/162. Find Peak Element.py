#162. Find Peak Element
#Medium
#problem statement:   https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        len_n = len(nums) #res, len_n = nums[0], len(nums) #res not being used
        l, r = 0, len_n-1

        while l <= r:
            #m = (l + r) // 2
            m = l + (r - l) // 2

            if m > 0 and nums[m] < nums[m-1]:
                r = m - 1
            elif m < len_n - 1 and nums[m] < nums[m+1]:
                l = m + 1
            else:
                return m    
        
        ''' # bad idea in this case, could be check after during else after checking left and right
        if m-1 >= 0 and m+1 < len_n and nums[m-1] < nums[m] and nums[m+1] < nums[m]: return m
        elif :  
        '''
