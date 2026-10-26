class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        Nrow, Ncol = len(grid), len(grid[0])
    
    
        x = [ c for c in range(Ncol) for r in range(Nrow) if grid[r][c]]
        y = [ r for r in range(Nrow) for c in range(Ncol) if grid[r][c]]

        min_dist = sum(x[~i] - x[i] for i in range(len(x)//2)) + sum(y[~i] - y[i] for i in range(len(y)//2))
        # 
        return min_dist

        # # find coordinates x and y
        # x, y = [], []

        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == 1:
        #             x.append(col)
        #             y.append(row)

        
        # # find medians 
        # x.sort()
        # # y.sort()
        
        # cx, cy = x[len(x)//2], y[len(y)//2]
        
        # min_distance = sum(abs(x[i] - cx) + abs(y[i] - cy) for i in range(len(x)))

        # return min_distance
        