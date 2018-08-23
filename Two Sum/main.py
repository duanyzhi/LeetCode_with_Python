"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

注意leetcode输入是[2,7,11,15]  在输入时候是一个字符形式，包括[]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num]=i
        else:
            return -1

S = Solution()
num_in = input()
nums = num_in[1:-1].split(',')
num_int = [int(n) for n in nums]
t = int(input())
print(S.twoSum(num_int, t))
