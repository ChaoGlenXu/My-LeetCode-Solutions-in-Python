#347. Top K Frequent Elements

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums

        #use the min-heap approach # this approach used the python library made the code much easier
        '''
        counted = Counter(nums)

        li = heapq.nlargest(k, counted.keys(), key = counted.get)
        return li   
        '''

        # use the bucket sort approach
        c = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for i in nums:
            if i not in c:
                c[i] = 1
            else: 
                c[i] += 1
        print(c)
        
        for j in c:
            freq[c[j]].append(j)
        print(freq)

        count = 0
        result = []
        for m in reversed(freq):
            if m != []:
                print(m[0])
                for e in m:
                    result.append(e)
                    count += 1
                    if count == k:
                    #print(count)
                        return result
                #result.append(m[0])
                #count += 1
                #print(count)
                
                





