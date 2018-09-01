# 题目

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

在一个数组中查找某个元素，数组是排序好的，不过从中间断了一下，把小的部分放到了后面。

# 解题思路

因为题目要求复杂度为log(N)，所以首先想到二分法查找。

左右两端两个指针。然后找到中间数,判断下中间数和最小值大小，因为这里输入序列不是按顺序的。

如果中间值比最小值大，说明从最小值到中间值是一直增加的。然后判断target是不是在最小值和中间值中间。如果在这中间，把最大值指针移到中间值位置。如果没有，把最小值指针移到中间值位置。

如果中间值比最小值小，说明**中间值到最大值点位置的值是一直增加的**。那么判断target是不是在中间值和最大值之间，是则把最小值指针移到中间值位置，否则把最大值指针移到中间位置。