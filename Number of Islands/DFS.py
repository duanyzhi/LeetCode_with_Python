class Solution(object):
    def numIslands(self, graph):
        """
        :type graph: List[List[str]]
        :rtype: int
        """
        if len(graph) == 0:
            return 0
        count = 0  # 存储所有的islands节点和对应的值
        for row in range(len(graph)):  # 行
            for col in range(len(graph[0])):  # 列
                if graph[row][col] == '1':
                    self.dfs(graph, row, col)
                    print(type(graph))
                    count += 1
        return count

     
    def dfs(self, graph, row, col):
        '''
        根据起始点row, col开始往周围搜素，采用函数迭代，如果不满足条件推出
        增加一个小trick，当访问过的节点把graph内容变为#号，表示这个节点访问过了，防止再次访问
        这里所有的dfs函数都在numIslands内部调用，因此graph更改后会作用与整个函数
        '''
        if row < 0 or row >=len(graph) or col < 0 or col >= len(graph[0]) or graph[row][col] != "1":
            return 
        graph[row][col] = '#'  # 访问过的节点变为# 
        self.dfs(graph, row + 1, col)  # 上
        self.dfs(graph, row - 1, col)  # 下
        self.dfs(graph, row, col - 1)  # 左
        self.dfs(graph, row, col + 1)  # 右
        # self.dfs(graph, row - 1, col - 1)  # 左上 
        # self.dfs(graph, row - 1, col + 1)  # 右上 
        # self.dfs(graph, row + 1, col - 1)  # 左下 
        # self.dfs(graph, row + 1, col + 1)  # 右下
    
s = Solution()
o = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(o)