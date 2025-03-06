#189. Rotate Array
#Medium
#problem statement:   https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Runtime 11ms Beats 24.08% Memory 25.66MB Beats 46.48%
        # in place with O(1) extra space 
        k ,l ,r = k % len(nums), 0 , len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        l ,r = 0 , k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        l ,r = k , len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        #Runtime 1022ms Beats 6.74% Memory 25.47MB Beats 92.23%
        #first way passed all test cases, but not in place
        #for i in range(k): nums.insert(0, nums.pop())
