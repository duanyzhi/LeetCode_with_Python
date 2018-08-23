
def Solution(object):
    def coin_change(self, coins, amount):
        max_dp = amount + 1

        dp = [max_dp for _ in range(amount + 1)]
        dp[0] = 0

        for kk in range(1, amount + 1):
            for coin in coins:
                if coin <= kk:  # 如果kk大于硬币的数值
                    dp[kk] = min(dp[kk], dp[kk - coin] + 1)

        return -1 if dp[amount] > amount else dp[amount]

# ------------------------------------------------------------------------------
