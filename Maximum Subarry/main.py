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