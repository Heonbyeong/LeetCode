class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max_benefit = 100001, 0, 0
        for price in prices:
            if buy > price:
                buy = price
                sell = 0
                continue
                
            if price > sell:
                sell = price
            
            max_benefit = max(max_benefit, sell - buy)

        return max_benefit