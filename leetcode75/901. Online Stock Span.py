#901. Online Stock Span
#Medium
#problem statement:   https://leetcode.com/problems/online-stock-span/description/?envType=study-plan-v2&envId=leetcode-75

class StockSpanner:

    def __init__(self):
        self.stack = [] #[price, span]

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            price_pop, last_span = self.stack.pop()
            span += last_span
        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
