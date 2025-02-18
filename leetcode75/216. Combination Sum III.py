#216. Combination Sum III
#Medium
#problem statement:   https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]: 
        def backtrack(ith, sum, count, path):
            if sum == n and count == k:
                res.append(path) 
                return
            for each in range(ith, n+1):
                if each > 9 or sum + each > n or each+1 >= n+1 or count >= k: break
                #print(each)
                backtrack(each + 1, sum + each, count + 1 , path + [each])
        
        res = []
        if n >= k: backtrack(1, 0, 0, [])
        return res
