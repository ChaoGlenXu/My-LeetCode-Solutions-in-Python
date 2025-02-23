#72. Edit Distance
#Medium
#problem statement:   https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #optimized for space complexity, now space: O(n)
        len1, len2 = len(word1), len(word2)
        if len2 == 0: return len1
        elif len1 == 0: return len2

        row = [len1-i for i in range(len1+1)] 

        for y in range(len2-1, -1, -1):
            new_row = [0]*len1 + [len2-y]
            for x in range(len1-1, -1, -1): 
                if word1[x] == word2[y]: new_row[x] = row[x+1]
                else: new_row[x] = 1+ min(row[x], new_row[x+1], row[x+1])
            row = new_row
        return row[0]


        '''
        #passed all the testcases, but space: O(m x n)
        len1, len2 = len(word1), len(word2)
        if len2 == 0: return len1
        elif len1 == 0: return len2
        dp = [[0 for i in range(len1+1)] for j in range(len2+1)]
        
        for y in range(len2, -1, -1): dp[y][len1] = len2-y 
        for x in range(len1, -1, -1): dp[len2][x] = len1-x
        #print(dp)

        for y in range(len2-1, -1, -1):
            for x in range(len1-1, -1, -1):
                if word1[x] == word2[y]:dp[y][x] = dp[y+1][x+1]
                else: dp[y][x] = 1 + min(dp[y][x+1], dp[y+1][x], dp[y+1][x+1])
        return dp[0][0]
        '''

