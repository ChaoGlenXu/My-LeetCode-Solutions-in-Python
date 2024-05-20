# 334. Increasing Triplet Subsequence
#Medium 
#problem statement: https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75




class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n1 = n2 = sys.maxsize

        for i in nums:
            if i <= n1: #<= is for n2 to be strictly greater than n1, without the =, it will cause n1 = n2        
                n1 = i
            elif i <= n2:
                n2 = i
            else:
                return True
        return False


        '''
        1, 2 , 1

        num_i = 0
        num_j = 4
        num_k = 

             j i 
        [2,1,5,0,4,6]
        '''

