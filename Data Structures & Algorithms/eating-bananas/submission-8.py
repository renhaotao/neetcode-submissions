class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        min_speed = max(piles)
        while l <= r:
            k = (l+r)//2

            time_needed = sum([ math.ceil(i/k) for i in piles])

            if time_needed > h:
                l = k + 1
            else:
                min_speed = min(min_speed, k)
                r = k-1

        return min_speed


       