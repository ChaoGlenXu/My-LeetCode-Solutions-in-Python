#67. Add Binary
#Easy
#problem statement:   https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]

        carry = 0
        res = ""

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            res =  str(total % 2) + res 
            carry = total // 2
            
        if carry: #carry == 1
            res = "1" + res
        return res
