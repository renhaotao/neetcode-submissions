class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## Bottom-up approach
        dp = dict()
        dp[0] = 0

        for i in range(1, amount+1):
            dp[i] = min([dp[i-j] + 1 for j in coins if i-j >=0], default=float('inf'))

        # print(dp)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

    # coinChange_bottomUp([1, 5, 10], 12)
    