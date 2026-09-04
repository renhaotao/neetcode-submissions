class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l, r = 0, 1

        while r < len(prices):

            profit = prices[r] - prices[l]
            # print(l, r, profit, max_profit)

            if profit < 0:
                l = r
            else:
                max_profit = max(max_profit, profit)

            # if r < len(prices) - 1:
            r += 1

        return max_profit


        