class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        H_state = {}
        S_state = {}
        R_state = {}

        def H(i): # max profit by the end of day i, holding a coin
            if i == 0:
                return - prices[0]
            else:
                if i not in H_state:
                    H_state[i] = max(H(i-1), R(i-1)-prices[i])
                return H_state[i]

        def R(i): # max profit by the end of day i, having a rest day (no cd, not after selling, no coin)
            if i ==0:
                return 0
            else:
                if i not in R_state:
                    R_state[i] = max(R(i-1), S(i-1))
                return R_state[i] # either I rest both yesterday and today
                                        # or I sold a coin yesterday

        def S(i): # max profit by the end of day i, having sold a coin
            if i==0:
                return -float('inf')
            else:
                if i not in S_state:
                    S_state[i] = H(i-1) + prices[i]
                return S_state[i] # either i sold the coin i held yesterday
                                                    # or i rest yesterday and sell today

        return max(H(len(prices)-1), R(len(prices)-1), S(len(prices)-1))
        