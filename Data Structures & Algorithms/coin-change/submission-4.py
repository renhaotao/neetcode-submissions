class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(amount, cache):
            if amount == 0:
                return 0
            elif amount-min(coins) < 0:
                return float('inf')

            if amount not in cache:
                cache[amount] = 1+min(helper(amount-c, cache) for c in coins if amount-c >= 0)
            return cache[amount]

            # return

        result = helper(amount, {})
        return -1 if result == float('inf') else result