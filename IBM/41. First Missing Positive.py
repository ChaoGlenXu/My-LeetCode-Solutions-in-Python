#41. First Missing Positive
#Hard
#problem statement: https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cache = {}
        nums.sort()
        for i in nums:
            cache[i] = 1

        leng = len(nums)
        for i in range(1, leng+1):
            if i not in cache:
                return i 
        return leng + 1

        '''
        minN = 1
        for i in range(leng):

            if i < 0:
                continue
            
            else:
                if i == minN:
                    minN += 1
                else:
                    minN = i
        '''
        
                
