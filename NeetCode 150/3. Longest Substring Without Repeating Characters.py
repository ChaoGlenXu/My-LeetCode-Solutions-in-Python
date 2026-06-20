
class Solution:

    #alternatively:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


'''
first solution that works
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        res = 0
        temp = 0
        left = 0
        for i, ch in enumerate(s): 
            if ch not in d: 
                temp += 1
                
            else:
                left = max( d[ch], left)
                temp = i - left

            if temp > res: res = temp
            d[ch] = i
        return res
        

'''