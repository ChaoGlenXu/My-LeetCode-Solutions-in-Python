#27. Remove Element
#Easy
#problem statement:  https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #without using sort()
        k = 0
        for idx, i in enumerate(nums):
            if i != val:
                nums[k] = i
                k += 1
        return k

        '''
        #used the sort(), but may not be allowed in interview
        len_before, len_remove = len(nums), 0
        for idx, i in enumerate(nums):
            if i == val: 
                nums[idx] = float(inf)
                len_remove += 1
        nums.sort()
        return len_before - len_remove
        '''
