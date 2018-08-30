# 题目

Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Example 1:**

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2:**

```
Input: "cbbd"
Output: "bb"
```



求最长回文(从前从后和从后往前看是一样的)



# 解题思路

i用来表示以i结尾的最大回文   回文长度为maxLen 如果检测出第一个回文(第一次检测出两个字符一样)maxLen += 1.之后在检测出回文就是两边都有一个字符，maxLen += 2.