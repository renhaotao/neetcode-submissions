class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # holding / just sold / free and idle

        H_dict = dict()
        S_dict = dict()
        R_dict = dict()

        def H(i):
            if i not in H_dict:
                if i==0:
                    H_dict[0] = -prices[0]
                else:
                    H_dict[i] = max(H(i-1),  # either held it from yesterday,
                                    R(i-1) - prices[i]) # or bought it today

            return H_dict[i]


        def S(i):
            if i not in S_dict:
                if i==0:
                    S_dict[i] = -float('inf')
                else:
                    S_dict[i] = H(i-1) + prices[i]

            return S_dict[i]

        def R(i):
            if i not in R_dict:
                if i==0:
                    R_dict[i]= 0
                else:
                    R_dict[i] = max(R(i-1), S(i-1))

            return R_dict[i]

        return max(S(n-1), R(n-1))

      