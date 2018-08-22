'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0

        def dfs(root):
            if root:
                # root节点有左节点且左节点没有左节点且左节点没有右节点
                if root.left and not root.left.left and not root.left.right:
                    self.sum += root.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.sum

# ------------------------------------------------------------------------------
