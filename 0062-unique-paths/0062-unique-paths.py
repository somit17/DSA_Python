class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [] #List
        for i in range(m):
            row = []
            for j in range(n):
                row.append(1)
            grid.append(row)
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]