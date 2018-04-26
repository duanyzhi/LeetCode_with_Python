"""
贪心算法思想：每次都会取最大的项。

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

题目思想是从index=0的数开始看看能不能跳到最后一个数，每个列表的数代表可以跳的格的个数

用贪心算法，每个格子都记录可以跳到的最大的格子的数
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_step = 0
        for kk in range(len(nums)):
            print(kk, nums[kk], max_step)
            max_step = max(max_step, kk + nums[kk])    # kk + nums[kk]表示当前步数可以跳的的最大值，可之前的比较，取较大的步数
            if max_step < kk + 1:
                return False
            if max_step >= len(nums):
                return True

num = [3, 2, 1, 0, 4]
S = Solution()
out = S.canJump(num)
print(out)
