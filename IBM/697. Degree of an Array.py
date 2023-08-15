#697. Degree of an Array
#Easy 
#problem statement: https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        start = {}
        end = {}

        for idx, i in enumerate(nums):
            if i not in count:
                count[i] = 1
                start[i] = idx
                end[i] = idx
            else:
                count[i]+= 1
                end[i] = idx

        theMax= max(count.values())

        sma = len(nums)
        for j in count:
            if count[j] == theMax:
                leng = end[j] - start[j] + 1 # note: +1 because the start[j] also counts as one
                if leng < sma:
                    sma = leng
        return sma

        
        '''
        cache = {}
        for idx, i in enumerate(nums):
            if i not in cache:
                cache[i] = 1
            else:
                cache[i]+= 1

        cache.
        '''
