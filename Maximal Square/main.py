
import sys


def Solution(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        columns = len(matrix[0])
        dp = [[0]*columns for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(columns):
                if i == 0 or j == 0:  # 第一行第一列
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
                res = max(res, dp[i][j])
        return res ** 2


n = int(input())

mt = []
for kk in range(n):
    num = sys.stdin.readline().strip()
    mt.append(list(map(int, num.split(" "))))

out = Solution(mt)
print(out)
