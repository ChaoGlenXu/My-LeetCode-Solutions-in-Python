#1356. Sort Integers by The Number of 1 Bits
#Easy 
#problem statement: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        
        #approach 1 faster than approach 2
        arr.sort()
        d = {}
        for i in arr:
            #bi = bin(i)
            #print(bi)
            count1 = bin(i).count('1')
            if count1 in d:
                d[count1].append(i)
            else:
                d[count1] = [i]

        res = []
        #sort(d).
        for each in sorted(d.keys()):
            res.extend(d[each])

        return res





        '''
        #approach 2 : works! accepted
        d = {}
        for i in arr:
            #bi = bin(i)
            #print(bi)
            count1 = bin(i).count('1')
            if count1 in d:
                d[count1].append(i)
            else:
                d[count1] = [i]

        res = []
        #sort(d).
        for each in sorted(d.keys()):
            for eachInt in sorted(d[each]):
                res.append(eachInt)

        return res
        '''
