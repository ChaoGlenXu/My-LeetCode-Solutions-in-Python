#14. Longest Common Prefix
#Easy
#problem statement:   https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for idx in range(len(strs[0])):
            for s in strs:
                if len(s) == idx: return res
                if s[idx] != strs[0][idx]: return res
            res += strs[0][idx]
        return res
