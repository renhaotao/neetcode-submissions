class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        # find coordinates x and y
        x, y = [], []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x.append(col)
                    y.append(row)

        
        # find medians 
        x.sort()
        y.sort()
        
        cx, cy = x[len(x)//2], y[len(y)//2]
        
        min_distance = sum(abs(x[i] - cx) + abs(y[i] - cy) for i in range(len(x)))

        return min_distance
        