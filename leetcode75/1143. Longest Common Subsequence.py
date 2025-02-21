#1143. Longest Common Subsequence
#Medium
#problem statement:   https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #optimized for space, now Runtime 323ms Beats 96.88% Memory 17.78MB Beats 97.20%
        dp_1d_row = [0] * (len(text1) + 1)

        for y in range(len(text2) -1, -1, -1):
            new_row = [0] * (len(text1) + 1)
            for x in range(len(text1) -1, -1, -1):
                if text1[x] == text2[y]: new_row[x] = 1 + dp_1d_row[x + 1]
                else: new_row[x] = max(new_row[x + 1], dp_1d_row[x])
            dp_1d_row = new_row
        return dp_1d_row[0]


        ''' #this version: Runtime 462ms Beats65.50%  Memory 43.63MB Beats 28.54%
        #this can be more optimized for space complexity from O(m x n) to O(n)
        dp = [[0 for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]
        #print(dp)

        for y in range(len(text2) - 1, -1, -1):
            for x in range(len(text1)-1, -1, -1):
                if text1[x] == text2[y]: dp[y][x] = dp[y+1][x+1] + 1
                else: dp[y][x] = max(dp[y+1][x], dp[y][x+1])
        return dp[0][0] 
        '''
