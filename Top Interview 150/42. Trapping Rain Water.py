#42. Trapping Rain Water
#Hard
#problem statement:   https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def trap(self, height: List[int]) -> int:
        #shorter and with slight improvement
        if not height: return 0
        max_l, max_r = height[0], height[-1], 
        l, r, res = 0, len(height)-1, 0

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]   
            else:
                r -= 1
                max_r = max(max_r, height[r])  
                res += max_r - height[r]
        return res

        ''' #passed all the test cases but could be improved slightly
        if not height: return 0
        max_l, max_r = height[0], height[-1], 
        l_p, r_p, res = 0, len(height)-1, 0

        while l_p < r_p:
            #print(max_l, max_r, l_p, r_p, res)
            if max_l <= max_r:
                if max_l - height[l_p] > 0: 
                    res += max_l - height[l_p]
                l_p += 1
                max_l = max(max_l, height[l_p])
            else:
                if max_r - height[r_p] >= 0: 
                    res += max_r - height[r_p]
                r_p -= 1
                max_r = max(max_r, height[r_p])         
        return res
        '''
