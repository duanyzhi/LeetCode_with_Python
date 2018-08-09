'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

两个数组 一个存储他前面所有的数的乘积 两一个存储他的后面的所有数的乘积 两个数组在相乘即可
'''

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1]*n
        right =[1]*n
        for i in range(1,len(nums)):
            left[i]= left[i-1] * nums[i-1]
            right [n-1-i] =right[n-i] * nums[n-i]
        return list(map(lambda c:c[0]*c[1], zip(left,right)))

num = [1,2,3,4]
s = Solution()
out = s.productExceptSelf(num)
print(out)


# --------------------------------------------------------------------------------
