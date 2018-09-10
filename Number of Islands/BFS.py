import collections  # 调用collections 之前都没用过这个函数...
qu = collections.deque()  # 调用队列

class Solution(object):
    def numIslands(self, graph):
        """
        :type graph: List[List[str]]
        :rtype: int
        """
        if len(graph) == 0:
            return 0
        count = 0  
        check = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
        for row in range(len(graph)):  # 行
            for col in range(len(graph[0])):  # 列
                if graph[row][col] == '1' and not check[row][col]:
                    self.bfs(graph, check, row, col)
                    count += 1
        return count

     
    def bfs(self, graph, check, i, j):
        qu.append((i, j))
        while qu:
            i, j = qu.popleft()
            if 0<=i<len(graph) and 0<=j<len(graph[0]) and graph[i][j]=='1' and not graph[i][j]:
                check[i][j] = True
                qu.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
    
s = Solution()
o = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(o)