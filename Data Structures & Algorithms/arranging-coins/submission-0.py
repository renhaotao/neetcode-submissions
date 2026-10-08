class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        i = 1 
        tot = i

        while tot + (i+1) <= n:

            tot += (i+1)

            i += 1 

        return i 