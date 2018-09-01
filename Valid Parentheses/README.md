# 题目

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

最常见的题型之一 判断输入字符符号是否合法

# 解题思路

判断是否合法，这里有点特殊的是如果合法，则s中至少有一对(), {},[]出现。Example 1/5中都至少会有一对括号。不能像Example 4，虽然有一对括号，但是不是挨着的所以也是不合法的。所以我们先找输入中出现的那一对括号。然后把这个括号删除，那么剩余的字符自然又组合出现了一个括号组合。就这样重复。