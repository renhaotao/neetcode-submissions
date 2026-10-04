class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(residual, dp):
            # print("residual", residual)
            if residual == 0:
                return 0
            if residual not in dp:
                viable_path = [helper(residual - j, dp) + 1 for j in coins if residual - j >=0]
                # print("residual: {}".format(residual), viable_path)

                tmp = min(viable_path, default=False)
                if not tmp:
                    tmp = float('inf')
                dp[residual] = tmp
                # print("dp[{}]={}".format(residual, tmp))

            return dp[residual]


        # print(failed)

        rst = helper(amount, {})

        if rst == float('inf'):
            return -1
        else:
            return rst
    