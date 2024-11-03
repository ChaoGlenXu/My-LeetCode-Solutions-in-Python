#394. Decode String
#Medium
#problem statement:   https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for char in s:  
            if char != ']': stack.append(char)
            else:
                substr,num = '', ''
                while  stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()      
                #get the number
                while stack and stack[-1].isdigit():    
                    num = stack.pop() + num
                
                stack.append(int(num) * substr)
        return "".join(stack)
  
