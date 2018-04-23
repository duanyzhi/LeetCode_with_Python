"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square（正方形） containing only 1's and return its area.

For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
0 0 1 1 1
1 0 0 1 0

Return 9
"""
import sys


def Solution_one(matrix):
    row = len(matrix)
    columns = len(matrix[0])
    dp = [[0]*columns for _ in range(row)]
    res = 0
    for i in range(row):
        for j in range(columns):
            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]
            elif matrix[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
            res = max(res, dp[i][j])
    print(dp)
    return res ** 2


def Solution_two(matrix):
    row = len(matrix)
    columns = len(matrix[0])
    dp = [0] * (columns + 1)
    res, pre = 0, 0
    for j in range(row):
        for i in range(1, columns):
            t = dp[i]
            print("--------------")
            print(i, j, t)
            if matrix[i - 1][j] == 1:
                dp[i] = min(dp[i], min(dp[i - 1], pre)) + 1
                res = max(res, dp[i])
            else:
                dp[i] = 0
            pre = t
            print(dp[i], res, pre, t)
    return res ** 2

n = int(input())

mt = []
for kk in range(n):
    num = sys.stdin.readline().strip()
    mt.append(list(map(int, num.split(" "))))

out = Solution_one(mt)
print(out)
