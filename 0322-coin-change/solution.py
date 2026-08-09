class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = the min number of coins needed to make up amount i
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i - coin] + 1
                    )
        return dp[amount] if dp[amount] <= amount else -1
