"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

要求复杂度第 采用二分法或分治法来
我们可以选择从数组右上角数字比较，如果这个数字比target大，那么说明最后一列全比Target大删除这列。
如果比target小那么说明这一行都比target小，删除这一行。
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])

        ii = 0
        jj = column - 1
        while jj >= 0 and ii < row:
            if matrix[ii][jj] == target:
                return True
            elif matrix[ii][jj] > target:
                jj -= 1
            else:
                ii += 1

        return False

S = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 1
out = S.searchMatrix(matrix, target)
print(out)
