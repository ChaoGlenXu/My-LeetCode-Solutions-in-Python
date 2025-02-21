#714. Best Time to Buy and Sell Stock with Transaction Fee
#Medium
#problem statement:   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #at day 0
        hold, not_hold, len_p= - prices[0], 0, len(prices)

        for i in range(1, len_p):
            cur_hold = max(hold, not_hold - prices[i])
            cur_not_hold = max(not_hold, hold + prices[i] - fee)
            hold, not_hold = cur_hold, cur_not_hold
        return not_hold 
