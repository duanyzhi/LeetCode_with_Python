# Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.



# 题目解析

连续子序列和最大



令一个dp数组做来存储每个位置的最大。然后从前往后比较，每个位置的dp取值为max(dp[i-1]+num[i], num[i])

.看是加上前面的dp最大还是本身大。