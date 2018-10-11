# Minimum Size Subarray Sum

Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.

**Example:** 

```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

**Follow up:**

If you have figured out the *O*(*n*) solution, try coding another solution of which the time complexity is *O*(*n* log *n*). 



# 题目解析

找到最短连续子数组之和大于某个数



定义两个指针left和right用来表示这个子数组的边界。right,left都从0开始。然后right往右移动，求left到right的和。如果和大于目标s，那么说明值可能可以减小。left加一。然后重新判断值是否任然大于s，大于s则，left继续加一。缩小长度，否则停止。记录此刻的最小长度。然后right加一继续往后搜索。重复上面判断。