#56. Merge Intervals
#Medium 
#problem statement: https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        out = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = out[-1][1]

            if start <= lastEnd:
                out[-1][1] = max(end, lastEnd)
            else:
                out.append([start, end])
        return out
                

        '''
        #for i in
        res = []
        end = len(intervals) -1 
        prev = [intervals[0][0], intervals[0][1]]
        #print(prev[1])
        for idx, i in enumerate(intervals):
            print(idx)
            print(i[0])
            print("-----------")
            #print(i[0])
            #print(temp[1])
            if idx == 0:
                print("why")
                continue 
            if i[0] <= prev[1]:
                print("should")
                prev[1] = i[1]
                #print(prev)
            else:
                print("should it")
                print(prev)
                res.append(prev)
                print(res)
                prev[0] = i[0]
                prev[1] = i[1]
                #print(res)
                print(prev)        
        #res.append(prev)
        return res
        '''
