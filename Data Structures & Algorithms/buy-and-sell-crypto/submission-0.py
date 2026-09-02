class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        min_price = float('inf')

        for price in prices:
            sell = price - min_price
            profit = max(profit, sell)
            min_price = min(min_price, price)
        return profit

        