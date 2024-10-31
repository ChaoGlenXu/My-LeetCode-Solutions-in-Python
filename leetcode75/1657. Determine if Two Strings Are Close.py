#1657. Determine if Two Strings Are Close
#Medium
#problem statement:   https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        #my approach with 2 lines of code
        if set(word1) != set(word2): return False
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values()) 
        
        '''
        if set(word1) != set(word2):
            return False

        freq1, freq2 = Counter(word1), Counter(word2)

        return sorted(freq1.values()) == sorted(freq2.values()) 
        '''

