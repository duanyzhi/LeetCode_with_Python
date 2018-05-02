"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

动态规划
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        dp = [nums[0]] * len(nums)

        for kk in range(1, len(nums)):
            dp[kk] = max(dp[kk - 1] + nums[kk], nums[kk])
            result = max(result, dp[kk])
        return result

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
S = Solution()
out = S.maxSubArray(arr)
print(out)