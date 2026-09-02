class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for subA in range(1, amount+1):
            minCoins = float('inf')
            for coin in coins:
                if subA - coin >= 0:
                    minCoins = min(minCoins, 1 + dp[subA - coin])
            dp[subA] = minCoins

        return dp[amount] if dp[amount] != float('inf') else -1

        