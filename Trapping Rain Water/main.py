'''
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开始遍历，
用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], rightmax)-A[i]
就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。

leftmosthigh：存储每个数左边最高的数
rightmosthigh:存储每个数右边最高的数

比较的时候每个点的数必须小于他的左边最高的数和右边最高的数的最小值才可以 存储的水量做差即可
'''

# 复杂度O(n)
class Solution:
    """
    :type height: List[int]
    :rtype: int
    """
    def trap(self, height):
        leftmosthigh = [0 for _ in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax: leftmax = height[i]
            leftmosthigh[i] = leftmax

        rightmosthigh = [0 for _ in range(len(height))]
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax: rightmax = height[i]
            rightmosthigh[i] = rightmax

        sum = 0
        for i in range(len(height)):
            if min(rightmosthigh[i], leftmosthigh[i]) > height[i]:
                sum += min(rightmosthigh[i], leftmosthigh[i]) - height[i]
        return sum



hei = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
o = s.trap(hei)
print(o)


# ------------------------------------------------------------------------------
