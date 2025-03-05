#80. Remove Duplicates from Sorted Array II
#Medium
#problem statement:  https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #more optimal for space
        count, k = 1, 1
        for idx, i in enumerate(nums[1:], start=1):
            if i != nums[idx-1]:
                count = 1
                nums[k] = i
                k += 1
            else:
                count += 1
                if count <= 2: 
                    nums[k] = i
                    k += 1    
        return k
        

        '''
        #using dictionary to check twice
        d, k = {}, 0
        for idx, i in enumerate(nums):
            if i not in d:
                d[i] = 1
                nums[k] = i
                k += 1
            else:
                if d[i] == 1: 
                    d[i] += 1
                    nums[k] = i
                    k += 1
        return k
        '''
