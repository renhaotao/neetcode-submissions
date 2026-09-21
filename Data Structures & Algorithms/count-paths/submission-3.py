class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def helper(x, y):

            if x==m and y==n:
                return 1
            elif x==m:
                if (x, y) not in cache:
                    cache[x, y] = helper(x, y+1)
                return cache[x, y]
            elif y==n:
                if (x, y) not in cache:
                    cache[x, y] = helper(x+1, y)
                return cache[x, y]
            else:
                if (x, y) not in cache:
                    cache[x, y] = helper(x+1, y) + helper(x, y+1)

                return cache[x, y]

        return helper(1, 1)