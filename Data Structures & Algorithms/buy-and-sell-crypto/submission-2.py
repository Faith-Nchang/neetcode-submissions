class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit = 0

        buy_price = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            maxProfit = max(profit, maxProfit)
            buy_price = min(buy_price, prices[i])

        return maxProfit