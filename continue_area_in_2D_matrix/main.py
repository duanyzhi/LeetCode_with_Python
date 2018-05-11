"""
八卦阵相传是由诸葛亮创设的一种战斗队形和兵力部署，由八种阵势组成。为了方便，采用矩阵来描述一个八卦阵，它由八个单阵组成，
每个单阵由多个兵力区域组成形成一种阵势，如下图所示，其中数字为一个兵力区域的士兵个数。假设单阵与单阵之间兵力区域不会相邻，
且单阵中每个兵力区域至少存在一个相邻兵力区域（注：相邻是指在其左上，正上，右上，右方，右下，正下，左下，左方与其相邻），
请用最快的速度计算出八个单阵中的兵力（士兵个数）的最大值和最小值。
20
20
34  0   0   0   0   0   0   0   0   0   0   0   0   0   0   10  0   0   0   30
0   23  10  5   5   0   0   0   5   5   5   5   5   0   0   0   30  0   40  0
0   9   0   0   5   0   0   0   4   4   4   4   4   0   0   0   0   30  0   0
0   8   7   7   0   5   0   0   3   3   3   3   0   0   0   0   7   0   9   0
0   9   0   0   5   0   5   0   0   12  12  0   0   0   0   10  0   0   0   9
0   0   0   0   5   0   0   5   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
40  30  3   6   6   0   0   0   0   0   0   0   0   5   5   0   0   0   10  0
0   0   20  0   0   6   6   0   0   0   0   0   0   0   5   6   5   10  10  0
40  30  3   7   6   0   0   0   0   0   0   0   0   0   0   6   0   0   10  0
0   0   0   0   0   0   0   17  0   0   0   0   17  0   0   6   5   7   7   0
0   0   0   0   0   0   0   0   7   0   0   7   0   0   0   0   0   0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   30  0   7   0   0   0   0   0   5   5   0   0   0   0   0   0   10  0   50
0   40  7   0   0   0   0   0   0   5   5   0   0   0   0   0   0   0   50  0
43  30  25  10  50  0   0   0   6   6   6   6   0   0   0   0   0   50  0   0

out:
323
116

找到最大的连续区域
"""
delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]  # 几个搜索方向


class Solution:
    def find_max_min(self, row, col, arr):
        all_list = []
        cur_add_list = []
        for ii in range(row):
            for jj in range(col):
                if arr[ii][jj] != 0:
                    if [ii, jj] in cur_add_list:
                        continue
                    else:
                        cur_add_list.extend([ii, jj])
                        out_list = [[ii, jj]]
                        search_list = [[ii, jj]]
                        while search_list:
                            cur_search = []
                            for file in search_list:
                                for direction in delta:
                                    pos = [file[0] + direction[0], file[1] + direction[1]]
                                    if row - 1 < pos[0] or pos[0] < 0 or col -1 < pos[1] or pos[1] < 0:
                                        continue
                                    elif pos in out_list:
                                        continue
                                    else:
                                        if arr[pos[0]][pos[1]] != 0:
                                            cur_search.append(pos)
                                            out_list.append(pos)
                            search_list = cur_search
                        all_list.append(out_list)
                        cur_add_list.extend(out_list)

        sum_list = []
        for file in all_list:
            sum_ = 0
            for num_ in file:
                sum_ += arr[num_[0]][num_[1]]
            sum_list.append(sum_)
        return max(sum_list), min(sum_list)


import sys
n1 = int(sys.stdin.readline().strip())
n2 = int(sys.stdin.readline().strip())

num_list = []
for kk in range(n1):
    num_s = sys.stdin.readline().strip()
    # num_s = num_s.split('  ')  # 几个空格
    # print(num_s)
    num = list(map(int, num_s.split('  ')))
    num_list.append(num)

S = Solution()
max_, min_ = S.find_max_min(n1, n2, num_list)
print(max_, min_)