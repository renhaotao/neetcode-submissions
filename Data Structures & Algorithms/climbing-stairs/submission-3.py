from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def helper(x): # x is the number of stairs to go
            if x==1:
                return 1
            elif x ==0:
                return 1
            else:
                return helper(x-2) + helper(x-1) 

        return helper(n)
        