#389. Find the Difference
#easy 
#problem statement: https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        newS = sorted(s)
        newT = sorted(t)
        
        
        for idx, i in enumerate(newS):
            if i != newT[idx]:
                return newT[idx]

        return newT[len(t)-1]

        '''
        dic = {}
        for i in s:
            if i not in dic: 
                dic = 
        '''
        '''
        sset = set(s)
        tset = set(t)
        #res = tset - sset

        res = tset.difference(sset)
        print(res)
        return next(iter(res))
        '''
