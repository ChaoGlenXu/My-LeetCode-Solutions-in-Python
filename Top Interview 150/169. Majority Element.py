#169. Majority Element
#Easy
#problem statement:  https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #most optimal-Boyer-Moore Voting Algorithm
        res, c = 0, 0
        for i in nums:
            if c == 0: res = i
            c += (1 if res == i else -1)
        return res

        '''
        #impoved version:
        d , maj , half = {}, [nums[0], 1], len(nums)/2
        for i in nums:
            d[i] = 1 + d.get(i, 0)
            if d[i] > maj[1]: maj[0], maj[1] = i, d[i]
            if maj[1] > half: break #improve time complexity a little bit
        return maj[0] 
        '''

        '''
        d , maj , half = {}, [nums[0], 1], len(nums)/2
        for i in nums:
            if i not in d: d[i] = 1
            else:
                d[i] += 1
                if d[i] > maj[1]: maj[0], maj[1] = i, d[i]
                if maj[1] > half: break #improve time complexity a little bit
        return maj[0] 
        '''
        
