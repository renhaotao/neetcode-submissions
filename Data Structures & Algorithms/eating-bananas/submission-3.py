class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        min_eating_rate = max(piles)

        while l <= r:
            k = (r-l)//2 + l

            eating_time = sum([-(-p//k) for p in piles])

            if eating_time > h:
                l = k + 1
            elif eating_time <= h:
                min_eating_rate = min(min_eating_rate, k)
                r = k-1

        return min_eating_rate