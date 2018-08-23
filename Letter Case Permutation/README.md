# 题目描述

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

```
Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
```

**Note:**

- `S` will be a string with length at most `12`.
- `S` will consist only of letters or digits.

 

有一个纯字符串，编写一段代码，列出其所有字符的大小写组合

# 解题思路

先生成所有的字符的大小写，然后使用全排列将所有字符组合一起就可以了。

i.isalpha()     # 判断i是不是字符



itertools.product()  # 生成输入的笛卡尔积

`product(A, B)` returns the same as `((x,y) for x in A for y in B)`.

`product(A, repeat=4)` means the same as `product(A, A, A, A)`.



S = "a1b2"

L = [['a', 'A'], '1', ['b', 'B'], '2']  # 每个字符的大小写格式

print(*L)   # 列表或者字典前面加星号表示将列表解开成n个(n是列表长度)独立的参数，传入函数。

> > >['a', 'A'] 1 ['b', 'B'] 2 



Pools= map(tuple, args):   [('a', 'A'), ('1',), ('b', 'B'), ('2',)] 



