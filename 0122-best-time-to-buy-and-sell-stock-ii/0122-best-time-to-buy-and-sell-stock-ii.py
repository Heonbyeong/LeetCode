class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(len(prices)):
            if i < len(prices)-1:
                profit = prices[i+1] - prices[i]

                if profit > 0:
                    total_profit += profit

        return total_profit
            