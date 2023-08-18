#49. Group Anagrams
#Medium 
#problem statement: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = {}
        for i in strs:
            letters = sorted(i)
            same = ''.join(letters) 
            if same in cache: 
                cache[same].append(i)
            else:
                cache[same] = [i]
        '''
        res = []
        for same in cache:
            res.append(cache[same])
        '''
        return cache.values()
