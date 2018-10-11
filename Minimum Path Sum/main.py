def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):  # 第一行
        grid[0][i] += grid[0][i-1]
    for i in range(1, m): # 第一列
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

o = minPathSum(grid)
print(o)