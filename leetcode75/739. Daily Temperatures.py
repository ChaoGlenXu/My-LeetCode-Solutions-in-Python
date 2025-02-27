#739. Daily Temperatures
#Medium
#problem statement:   https://leetcode.com/problems/daily-temperatures/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:       #res init 0 for ending element(s), stack = [temp, idx]
        res, len_t, stack = [0] * len(temperatures), len(temperatures), []  

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                t_pop, idx_pop = stack.pop()
                res[idx_pop] = idx - idx_pop
            stack.append([t,idx])
        return res
            
