#151. Reverse Words in a String
#Medium
#problem statement:   https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        rev_words = words[::-1]
        print(rev_words)

        return " ".join(rev_words)
