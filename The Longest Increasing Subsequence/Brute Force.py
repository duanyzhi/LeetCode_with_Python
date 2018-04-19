#  求出最长子序列
#  4 5 60 70 6 7 8 80 1  >> 4 5 6 7 8 80
#  4 10 13 6 7 9 11 14 2 8 19 20  >> [4, 6, 7, 9, 11, 14, 19, 20]
# -1 2 3 4 5 4 5 6 7 8 9 10 1 1 3 4 5 6 7 8 9 10 11 12 13 14 56 >> [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 56]
#  方法一，穷举。这是一种动态规划问题，不能单单直接解决。而是要将其转化成其他容易解决的问题。
# 算法相当于循环嵌套遍历列表，所以复杂度为O(n**2)
import sys

class Solution(object):
    def Long_list(self, arr):
        dp = [1]*len(arr)   # 序列dp[i]用来表示以arr[i]结尾的最长子序列的长度。这是我们动态规划里新设置的要解决的较为容易的列表。
        for ii in range(1, len(arr)):
            for jj in range(ii):
                if arr[ii] > arr[jj] and dp[jj] + 1 > dp[ii]:   # 满足条件说明序列可以增加
                    dp[ii] = dp[jj] + 1
        max_count = max(dp)
        max_index = dp.index(max_count)
        out_list = [arr[max_index]]
        cur_count = max_count
        for kk in range(max_index-1, -1, -1):   # 依次取出对应序列元素
            if dp[kk] == cur_count - 1:
                out_list.insert(0, arr[kk])    # 在列表头部增加元素
                cur_count -= 1
        return out_list


if __name__ == "__main__":
    S = Solution()
    arr = sys.stdin.readline().strip()
    arr = list(map(int, arr.split(" ")))
    out = S.Long_list(arr)
    print(out)
