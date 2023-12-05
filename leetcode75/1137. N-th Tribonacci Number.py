#1137. N-th Tribonacci Number
#Easy
#problem statement:   https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        count = 2
        if n < 3:
            return arr[n]

        while count < n :
            count += 1
            arr[0], arr[1], arr[2] = arr[1], arr[2], sum(arr)
        return arr[2]
