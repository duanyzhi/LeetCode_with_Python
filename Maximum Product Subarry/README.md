# 题目描述

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:**

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

找出输入数组中连续数相乘的最大值，也可以是一个值相乘



# 题目分析思路

imax = max(max(imax\*nums[i], imin\*nums[i]), nums[i])  # 存储前一个数的最大值

 imin = min(min(temp\*nums[i], imin\*nums[i]), nums[i]) # 存储前一个值的最小值 最小值原因是有负数存在



i = 1

   imax = max(max(2\*3, 2\*3 ), 3) = 6

   Imin = min(min(2\*3, 2\*3), 3) = 3

  	out = 6

i = 2

   imax = max(max(6\*-2, 3*\-2), -2) = -2

  imin = min(min(6\*-2, 3\*-2), -2) = -12

i =   