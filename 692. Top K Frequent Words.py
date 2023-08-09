from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        #my brute force approach
        '''
        d = dict()
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        l = []
        for j in d:
            if j 

        '''

        '''
        #step 1: organize it to 
        counted = {}
        freq = [[] for i in range(len(words) + 1)]

        for i in words:
            counted[i] = 1 + counted.get(i, 0)

        #create this bucket list
        for j in counted:
            freq[counted[j]].append(j)

        '''
        #decided use the library from now on since it is much faster
        counted = Counter(words)

        heap = [(-freq, word) for word, freq in counted.items()]

        heapq.heapify(heap)

        result = [heapq.heappop(heap)[1] for i in range(k)]
        return result

