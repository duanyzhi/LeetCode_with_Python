"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
import sys


def Solution(nums):
    if len(nums) ==1:
        return nums[0]
    else:
        big_product = nums[0]*nums[1]
        for kk in range(1, len(nums) - 1):
            cur_product = nums[kk]*nums[kk + 1]
            if cur_product > big_product:
                big_product = cur_product
        return big_product

# num = list(map(float, sys.stdin.readline().strip().split(' ')))
num = eval(sys.stdin.readline().strip())
out = Solution(num)
print(out)
