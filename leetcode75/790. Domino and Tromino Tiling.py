#790. Domino and Tromino Tiling
#Medium
#problem statement:   https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def numTilings(self, n: int) -> int:
        #save memory approach, now the memory shows: 17.68 MB
        mod = 10**9 + 7
        ff, f, t = 1, 1, 0

        for i in range(2, n+1):
            f_curr = f + ff + 2 * t
            t = t + ff

            ff = f
            f = f_curr

        return f % mod

        '''
        #approach that relized that t and b are equal number  memmory: 18.34 MB
        mod = 10**9 + 7
        f, t = {0: 1, 1: 1}, {1: 0}

        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2] + 2 *t[i-1]
            t[i] = t[i-1] + f[i-2]

        return f[n] % mod
        '''

        ''' #most intuitive approach but use a lot memory
        mod = 10**9 + 7
        f, t, b = {0: 1, 1: 1}, {1: 0}, {1: 0} 

        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2] + t[i-1] + b[i-1]
            t[i] = b[i-1] + f[i-2]
            b[i] = t[i-1] + f[i-2]
        return f[n] % mod
        '''
