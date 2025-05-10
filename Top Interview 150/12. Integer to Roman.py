#12. Integer to Roman
#Medium
#problem statement:  https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def intToRoman(self, num: int) -> str:
        to_roman = [ ['I', 1], ['IV', 4], ['V', 5], 
        ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], 
        ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], 
        ['CM', 900], ['M', 1000] ]

        res = ""

        for c, i in reversed(to_roman):
            if num // i:
                count = num // i
                res += c * count
            num %= i

        return res

