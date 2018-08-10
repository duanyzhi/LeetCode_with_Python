'''
https://leetcode.com/problems/surrounded-regions/description/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
广度优先搜索（BFS）
广度优先搜索在进一步遍历图中顶点之前，先访问当前顶点的所有邻接结点。
a .首先选择一个顶点作为起始结点，并将其染成灰色，其余结点为白色。
b. 将起始结点放入队列中。
c. 从队列首部选出一个顶点，并找出所有与之邻接的结点，将找到的邻接结点放入队列尾部，将已访问过
结点涂成黑色，没访问过的结点是白色。如果顶点的颜色是灰色，表示已经发现并且放入了队列，如果顶点的颜色是白色，表示还没有发现
d. 按照同样的方法处理队列中的下一个结点。
基本就是出队的顶点变成黑色，在队列里的是灰色，还没入队的是白色。

'''
class Solution:
    def dfs(self, x, y, matrix):
        if x < 0 or x > len(matrix)-1 or y < 0 or y > len(matrix[0])-1 or matrix[x][y] != 'O':
            return
        matrix[x][y] = '#'
        print("matrix", matrix)
        self.dfs(x-1, y, matrix)
        self.dfs(x, y-1, matrix)
        self.dfs(x+1, y, matrix)
        self.dfs(x, y+1, matrix)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) > 0:
            m, n =0, 0
            for n in range(len(board[0])):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for m in range(1, len(board)):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for n in range(len(board[0])-2, -1, -1):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for m in range(len(board)-2, 0, -1):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '#':
                        board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'
# Solution 2
def solve(board):
    '''
    #python中any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
    #python中all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False
    '''
    if not any(board): return  # 判断是否为空对象

    m, n = len(board), len(board[0])
    save = [ij for k in range(max(m, n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]  # 存储矩阵周围一圈的点 从周围一圈开始
    print("save", save)
    while save:
        i, j = save.pop()  # pop取最后一个
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

    print(board)
    board[:] = [['XO'[c == 'S'] for c in row] for row in board]

board = [ ['X', 'X', 'X', 'X',],
          ['X', 'O', 'O', 'X',],
          ['X', 'X', 'O', 'X',],
          ['X', 'O', 'X', 'X'] ]

# s = Solution()
# s.solve(board)
# print(board)

solve(board)
print(board)
