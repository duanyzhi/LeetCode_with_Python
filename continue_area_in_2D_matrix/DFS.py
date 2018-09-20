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


class Solution(object):
    def fun(self, graph):
        """
        :type graph: List[List[str]]
        :rtype: int
        """
        if len(graph) == 0:
            return 0
        count = 0  # 存储所有的islands节点和对应的值
        out_list = []
        for row in range(len(graph)):  # 行
            for col in range(len(graph[0])):  # 列
                if graph[row][col] != 0:
                    person = []
                    self.dfs(graph, row, col, person)
                    out_list.append(person)
                    count += 1
        print(out_list)
        dp = []
        for ss in out_list:
            dp.append(sum(ss))
        return count, max(dp)

     
    def dfs(self, graph, row, col, person):
        '''
        根据起始点row, col开始往周围搜素，采用函数迭代，如果不满足条件推出
        增加一个小trick，当访问过的节点把graph内容变为#号，表示这个节点访问过了，防止再次访问
        这里所有的dfs函数都在numIslands内部调用，因此graph更改后会作用与整个函数
        '''
        if row < 0 or row >=len(graph) or col < 0 or col >= len(graph[0]) or graph[row][col] == 0:
            return 
        person.append(graph[row][col])
        graph[row][col] = 0  # 访问过的节点变为0
        self.dfs(graph, row + 1, col, person)  # 上
        self.dfs(graph, row - 1, col, person)  # 下
        self.dfs(graph, row, col - 1, person)  # 左
        self.dfs(graph, row, col + 1, person)  # 右
        self.dfs(graph, row - 1, col - 1, person)  # 左上 
        self.dfs(graph, row - 1, col + 1, person)  # 右上 
        self.dfs(graph, row + 1, col - 1, person)  # 左下 
        self.dfs(graph, row + 1, col + 1, person)  # 右下




s = Solution()
o = s.fun(num_list)
print(o)