#58. Length of Last Word
#Easy
#problem statement:   https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ''' #first way to solve it, this way take a lot time to get the logic smooth, so not recomending this
        c = 0
        for i in reversed(s):
            if i == " " and c == 0:
                continue
            if i != " ":
                c += 1
            if i == " " and c > 0: 
                return c
        return c
        '''

        #better general approach
        i, length = len(s)-1, 0

        while s[i] == " ": i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
