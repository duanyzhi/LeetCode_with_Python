# Minimum Path Sum

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example:**

```python
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```





# 题目解析

左上角到右下角距离和最小。

首先对于第一行而言，要到后面，肯定要加上前面的数。因此一次后面的数加上前面的数。

同理对于第一列也是。



后面方格中每个数，都是有上方的格子加过来或者从左边格子加过来的。我们取两个方向中较小的一个方向即可。