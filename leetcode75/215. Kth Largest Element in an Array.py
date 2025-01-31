#215. Kth Largest Element in an Array\
#Medium
#problem statement:   https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #or could be done in in-place to save space
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        for _ in range(k-1): heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)

 
        '''#after sorting lol
        nums.sort()
        print(nums)
        return nums[-k]
        '''
