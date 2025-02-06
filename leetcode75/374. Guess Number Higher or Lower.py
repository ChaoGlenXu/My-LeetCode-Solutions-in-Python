#374. Guess Number Higher or Lower
#Medium
#problem statement:   https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import math

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
 
        while True:
            m = (l + r) // 2 
            res = guess(m)
            if res == 0: return m
            elif res == -1: r = m - 1
            elif res == 1: l = m + 1

# 1,2,3,4,5,6,7,8 pick = 6//consider m is odd or even case separately
        '''
        #wrong, failed a lot test cases
        #num = n
        start, end = 1, n
        my_guess = math.floor((end + start)/2)
        res = guess(my_guess)
        
        while True:
            if res == -1:
                end = math.ceil(end - (end - start)/2)
                res = guess(math.ceil((end+start)/2))
                if res == 0: return math.ceil((end+start)/2)
            elif res == 1:
                start = math.floor(start + (end-start)/2)
                res = guess(math.floor((end + start)/2))
                if res == 0: return math.floor((end + start)/2)
        
        '''



                # 1, 2, 3, 4, 5, 6
        #def divide(num):
        #    if 
