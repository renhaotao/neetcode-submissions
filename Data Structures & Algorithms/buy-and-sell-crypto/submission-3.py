class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # start with brute force
        rtn = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                rtn = max(rtn, prices[j]-prices[i])

        return rtn


        