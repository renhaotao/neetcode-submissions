class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        B, S = 0, 1

        max_p = 0
        
        while S < len(prices):
            profit = prices[S] - prices[B]
            
            if profit < 0:
                B = S
                S = B + 1
            else:
                max_p = max(max_p, profit)
                S += 1 
                
        return max_p


        