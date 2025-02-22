#1318. Minimum Flips to Make a OR b Equal to c
#Medium
#problem statement:   https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0: count += (bit_a + bit_b)
            else: #bit_c = 1 
                if bit_a | bit_b == 0: count += 1
            
            a >>= 1
            b >>= 1
            c >>= 1

        return count
