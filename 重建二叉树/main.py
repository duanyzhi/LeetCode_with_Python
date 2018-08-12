

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
        return flag

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

s = Solution()
out = s.reConstructBinaryTree(pre, tin)

print("root:", out.val)  # 1
print(out.left.val)   # 2
print(out.left.left.val) # 4
print(out.left.left.right.val)  # 7
print(out.right.val) # 3
print(out.right.left.val) # 5
print(out.right.right.left.val) # 8
print(out.right.right.val) # 6

# ------------------------------------------------------------------------------
