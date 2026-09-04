class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buying_day in range(0, len(prices) - 1, 1):
            for selling_day in range(buying_day, len(prices), 1):
                max_profit = max(max_profit, prices[selling_day] - prices[buying_day])

        return max_profit