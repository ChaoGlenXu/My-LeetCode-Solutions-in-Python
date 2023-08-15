#844. Backspace String Compare
#Easy 
#problem statement: https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(input):
            new = []
            for idx, i in enumerate(input):
                if i == '#': 
                    if len(new) > 0:
                        new.pop()
                else:
                    new.append(i)
            return new
        
        s_new = ''.join(build(s))
        t_new = ''.join(build(t))
        
        return s_new == t_new
        '''
        if s_new == t_new:
            return True
        else: 
            return False

       
        sL = list(s)
        tL = list(t)
        print(sL)
        print(tL)
        def help(input):
            l = len(input) - 1
            for idx, i in enumerate(input):
                print(idx)
                if idx + 1 <= l and input[idx+1] == '#':
                    input.pop(idx)
                    input.pop(idx)
                    print(input)

                #if idx +  1 < l:
                #    if idx ==
            #return input
        
        help(sL)
        #print(sL)
        help(tL)
        #print(tL)
        nS = ''.join(sL)
        nT = ''.join(tL)


        if nS == nT:
            return True
        else: 
            return False
        '''
