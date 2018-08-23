"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
import sys

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        imin, imax, out, r = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = imax
            imax = max(max(imax*nums[i], imin*nums[i]), nums[i])
            imin = min(min(temp*nums[i], imin*nums[i]), nums[i])
            if imax > out:
                out = imax
        return out

# num = list(map(float, sys.stdin.readline().strip().split(' ')))
num = eval(sys.stdin.readline().strip())
s = Solution()
out = s.maxProduct(num)
print(out)
