'''
0 2 6 4
inf 0 3 inf
7 inf 0 1
5 inf 12 0

Floyd最短路径算法
path[i][j]表示从点i到j的距离 inf:此路不通 用99999表示
求每个点到其他点的最短路径
row
col
1 --> 0: 直接走没有路
1 --> 2 --> 3 --> 0 = 3+1+5=9
'''
path = [[0, 2, 6, 4],
        [99999, 0, 3, 99999],
        [7, 99999, 0, 1],
        [5, 99999, 12, 0]]


def find_min_path(arr):
    '''
    arr是正方形
    '''
    min_path = arr[::]
    N = len(arr)
    for ii in range(N):  # row
        for jj in range(N):  # col
            for kk in range(N):
                if arr[ii][jj] > arr[ii][kk] + arr[kk][jj]:
                    arr[ii][jj] = arr[ii][kk] + arr[kk][jj]

    return arr

o = find_min_path(path)
print(o)

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
