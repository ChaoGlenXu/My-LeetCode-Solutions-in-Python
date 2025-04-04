#452. Minimum Number of Arrows to Burst Balloons
#Medium
#problem statement:   https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #concise code without comment
        points.sort()
        res, pre = len(points), points[0]

        for start, end in points[1:]:
            if start > pre[1]: pre = [start, end]
            else:
                res -= 1
                pre = [start, min(pre[1], end)]
        
        return res

        '''
        points.sort()
        res, pre = len(points), points[0]

        for start, end in points[1:]:
            if start > pre[1]: 
                pre = [start, end] #6 % faster than the following two line
                #pre[0] = start
                #pre[1] = end
            else:
                res -= 1
                pre = [start, min(pre[1], end)] #Runtime 165ms Beats 26.95% Memory 51.50MB Beats 34.77%
                #Runtime 196ms Beats 14.73% Memory 51.38MB Beats 77.05%
                #pre[0] = max(pre[0], start)  
                #pre[1] = min(pre[1], end)
        
        return res
        '''

        #all the following the commented out code are wrong and just keep track of the mistake that i made, the mistate i made the following is that i only kept track of pre_end, but should also keep track the current overlapping interval, the solution i did above was done after checking neetcode video explanation
        '''
        res, pre_end, low_inter_end = len(points), points[0][1], points[0][1]
        print(points)
        for start, end in points[1:]:
            if start > pre_end: 
                pre_end = end
            else:
                res -= 1
        return res
        '''

        '''
        res, pre_end, low_inter_end = 1, points[0][1], points[0][1]
        print(points)
        for start, end in points[1:]:
            if start > pre_end: 
                if end < low_inter_end: 
                    low_inter_end = end
                if start > low_inter_end: 
                    res += 1
                    low_inter_end = end
                res+= 1
                pre_end = end
            #else:
                #low_inter_end = end
        return res
        '''

