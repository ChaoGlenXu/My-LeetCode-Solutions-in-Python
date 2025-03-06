#121. Best Time to Buy and Sell Stock
#Easy
#problem statement:   https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r , max_p = 0, 1, 0
        while r < len(prices):
            if prices[l] < prices[r]: max_p = max(max_p, prices[r]-prices[l])
            else: l = r
            r += 1
        return max_p  


