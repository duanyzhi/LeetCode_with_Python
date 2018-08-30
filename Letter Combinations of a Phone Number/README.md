# 题目

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![img](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example:**

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

输入2-9的数字，输出可能对应的所有字符串组合，每个数字对应三个不同的字符。





# 解题思路

感觉这题有点像[letter case permutation](https://leetcode.com/problems/letter-case-permutation/description/)  输出所有大小写组合





这里只是把对应关系换成了数字和字符对应 



主要还是itertools.product函数的实现。只要实现这个函数的功能就可以了