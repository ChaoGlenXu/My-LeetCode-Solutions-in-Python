#933. Number of Recent Calls
#Easy
#problem statement:     https://leetcode.com/problems/number-of-recent-calls/


import queue
class RecentCounter:

    def __init__(self):
        #q = deque()
        #out = [null]
        self.queue = deque()

    def ping(self, t: int) -> int:
        #q.append(t)
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

