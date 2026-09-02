class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        significant_bit = 1

        for i in range(1,n+1):
            if significant_bit * 2 == i:
                significant_bit = i
            dp[i] = 1 + dp[i - significant_bit]
        return dp
        