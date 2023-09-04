#649. Dota2 Senate
#Medium 
#problem statement:  https://leetcode.com/problems/dota2-senate/

import queue
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        q = deque()
        l = []

        for each in senate:
            q.append(each)
        '''

        s = list(senate)
        d, r = deque(), deque()

        for idx, i in enumerate(senate):
            if i == 'D':
                d.append(idx)
            else:
                r.append(idx)
        length = len(s)
        while d and r:
            dTurn = d.popleft()
            rTurn = r.popleft()

            if dTurn < rTurn:
                d.append(dTurn + length)
            else:
                r.append(rTurn + length)
        
        return "Dire" if d else "Radiant"


        
