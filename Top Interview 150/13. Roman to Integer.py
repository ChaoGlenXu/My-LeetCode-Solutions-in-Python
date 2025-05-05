#13. Roman to Integer
#Easy
#problem statement:   https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 }
        res = 0

        for idx, c in enumerate(s):
            if idx+1 < len(s) and roman[c] < roman[s[idx+1]]:
                res -= roman[c]
            else: res += roman[c]
        return res
