#20. Valid Parentheses
#easy 
#problem statement: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s) - 1
        #"{()[]{}}"
        stack = []
        for idx, i in enumerate(s):
            if i == '(' or i == '{' or i == '[' : 
                stack.append(i) 
                #else:
            else:
                #if idx - 1 >= 0:
                if len(stack) >= 1:
                    if (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):

                        c = stack.pop()
                        print(str(c) + str(i))
                    else: # ex: (i == ')' and s[idx-1] == '{')
                        return False
                else:
                    return False

        print(stack)
        if len(stack) >= 1:
            return False
        else: 
            return True
                
                    


        '''
        #use two pointer
        l = 0
        r = length 
        while l < r:
            if 
        '''
        '''
        for idx, i in enumerate(s):
            if i == "(" and idx + 1<= l:
                if s[idx+1] != ")":
                    return False
            if i == "[" and idx + 1<= l:
                if s[idx+1] != "]":
                    return False
            if i == "{" and idx + 1<= l:
                if s[idx+1] != "}":
                    return False
        return True
        '''
                
