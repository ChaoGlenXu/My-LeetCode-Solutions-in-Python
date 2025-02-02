#2336. Smallest Number in Infinite Set
#Medium
#problem statement:   https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.next_smallest = 1
        self.the_set = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            ret = heapq.heappop(self.min_heap)
            self.the_set.remove(ret)
        else:
            ret = self.next_smallest
            self.next_smallest += 1
        return ret
            
    def addBack(self, num: int) -> None:
        if num < self.next_smallest and num not in self.the_set:
            self.the_set.add(num)
            heapq.heappush(self.min_heap, num)
    


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
