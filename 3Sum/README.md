# 题目详情

Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

**Example:**

```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

⚠️输出结果任意两个列表元素不能相同。但是输入的nums中元素有可能相同

# 解题思路

最简单直接便利两边搜索 复杂度n(n+1)/2. 运行超时



## 改进

用一个循环 剩下两个数，分别用两个指针从列表两端向中间搜索，然后判断三个数是不是0。

另外需要先对nums排序，这样从两边往中间搜索的时候就有方向了，当和大于0，说明数太大，需要将输入减小，即右边指针的数太大了，右边指针往中间移动。反过来如果和小于0，说明左边数太小了。

还有一点需要注意的是重复数字的出现，需要判断一下是不是重复数字避免重复计算相同情况。