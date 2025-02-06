#2300. Successful Pairs of Spells and Potions
#Medium
#problem statement:   https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        #improved version
        potions.sort()
        len_s, len_p = len(spells), len(potions)
        res = [None] * len_s

        for idx, i in enumerate(spells):
            target = success / i
            l, r = 0, len_p - 1
            lowest_id = len_p

            while l <= r:
                m = (l + r) // 2
                if potions[m] >= target:
                    r = m - 1
                    lowest_id = m
                elif potions[m] < target:
                    l = m + 1
            res[idx] = len_p - lowest_id
        return res

        #[1,7,7,8,9]
        # 0,1,2,3,4 the index

        ''' #my code that passed all the testcase
        potions.sort()
        len_s, len_p = len(spells), len(potions)
        res = [None] * len_s
        print(potions)
        for idx, i in enumerate(spells):
            target = success / i
            l, r = 0, len_p - 1

            # c = 0
            # while c < len_p + 3:
            while True:
                if r < 0:
                    res[idx] = len_p
                    break
                if l >= len_p:
                    res[idx] = 0
                    break

                # c += 1 # for testing

                if l > r:
                    res[idx] = len_p - l  # or len_p - r - 1
                    break

                if l == r:
                    if potions[l] >= target:
                        res[idx] = len_p - l
                    else:
                        res[idx] = len_p - l - 1
                    break

                m = (l + r) // 2

                if potions[m] >= target:
                    r = m - 1
                elif potions[m] < target:
                    l = m + 1
        return res
        '''
