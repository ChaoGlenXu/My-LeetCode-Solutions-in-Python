#735. Asteroid Collision
#Medium 
#problem statement: https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            while res and res[-1] > 0 and i < 0: #have a collision
                diff = res[-1] + i
                if diff < 0:
                    res.pop()
                elif diff > 0:
                    i = 0
                else:
                    res.pop()
                    i = 0
            if i:
                res.append(i)
        return res
                    
