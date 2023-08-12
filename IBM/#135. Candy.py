#135. Candy
#Hard
#problem statement: https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:

        #two array approach
        highest_idx = len(ratings) - 1
        l_li = [1 for i in ratings]
        r_li = [1 for i in ratings]
        #left to right
        for idx, i in enumerate(ratings):
            if (idx + 1 <= highest_idx) and i < ratings[idx+1]:
                l_li[idx+1] = l_li[idx] + 1
        print(l_li)
            
        for idx, i in reversed(list(enumerate(ratings))):
            #print("idx: {}, i: {}".format(idx, i))
            if idx - 1 >= 0 and i < ratings[idx-1]:
                r_li[idx-1] = r_li[idx] + 1
        print(r_li)
        res = []
        count = 0
        for h in range(highest_idx + 1):
            res.append(max(l_li[h],r_li[h] )) 
            count += res[h]
        print(res)
        return count
