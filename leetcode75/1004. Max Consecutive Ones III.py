#1004. Max Consecutive Ones III
#Medium
#problem statement:   https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        #my intial solution that passed all the test cases
        l , res= 0, 0
        list0 = []
        for idx in range(len(nums)):

            if nums[idx] == 0:
                list0.append(idx)
                if len(list0) > k:
                    l = list0.pop(0)
                    l += 1
 
            print(idx - l + 1)
            #my algo: idx is or is fliped to 1 anyways
            res = max(idx - l + 1, res)

        return res
            

        
