#1143. Longest Common Subsequence
#Medium
#problem statement:   https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]
        #print(dp)

        for y in range(len(text2) - 1, -1, -1):
            for x in range(len(text1)-1, -1, -1):
                if text1[x] == text2[y]: dp[y][x] = dp[y+1][x+1] + 1
                else: dp[y][x] = max(dp[y+1][x], dp[y][x+1])
        return dp[0][0] 
