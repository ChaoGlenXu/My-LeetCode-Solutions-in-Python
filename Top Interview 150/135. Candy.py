#135. Candy
#Medium
#problem statement:   https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def candy(self, ratings: List[int]) -> int:
        #I solved this by myself for around 58 minutes (Top Interview 150)
        candies = [1] * len(ratings)

        more = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                more += 1
                candies[i] += more
            else: more = 0
        #print(candies)
        more = 0
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]:
                    more += 1
                    if candies[i] == 1: candies[i] += more
                    else: candies[i] = max(candies[i], 1+ more)
            else: more = 0
        #print(candies)
        return sum(candies)
