#17. Letter Combinations of a Phone Number
#Medium
#problem statement:   https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res, length = [], len(digits)

        def backtrack(idx_dig, cur_str):
            if len(cur_str) == length:
                res.append(cur_str)
                return
            for i in d[digits[idx_dig]]:
                backtrack(idx_dig + 1, cur_str + i )

        if digits: backtrack(0, "")
        return res
