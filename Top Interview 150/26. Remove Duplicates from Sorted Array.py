#26. Remove Duplicates from Sorted Array
#Easy
#problem statement:  https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for idx, i in enumerate(nums[1:], start=1):
            if i != nums[idx-1]:
                nums[k] = i
                k += 1
        return k
