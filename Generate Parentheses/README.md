# 题目

Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given *n* = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

n=2:

```
['(())', '()()']
```



生成合法符号

# 解题思路

用函数递归的形式。 n=2

```
gen('', 2, 2)
	只满足if left：
	gen('' + (', 1, 2)
	   p = '('
	   left=1, right=2  同时满足if left和if right > left两个，所以调用两个gen。
	   if left:
	       gen(p+'(', 0, 2)
	          p = '(('
	          left=0, right=2 只满足right > left 
	           if right > left:
	              gen(p + ')',0, 1)
	                 p = '(()'
	                 left=0, right=1 只满足right > left
	                 gen(p + ')',0, 0)
	                    p = '(())'
	                    left==right==0:
	                    parens.append(p)
	                    
	                    
	   if right > left:
	       p = '('
	       left=1, right=2 
	       gen(p + ')', 1, 1)
	          p = '()'
	          left = 1, right=1
	          只满足if left:
                gen(p + '(', 0, 1)
                p =  '()('
                left = 0, right=1 只满足right > left
                gen(p + ')', 0, 0)  # 左右括号都没了
                p = '(())'
                left=right=0
                parens.append(p)
                
 
```

首先left和right表示左括号和右括号剩余的个数。

个别说明：

对于gen('' + (', 1, 2)。当有一个左括号时，还剩一个左括号和两个右括号，所以下一个可以是左括号也可以是右括号。有两种情况。

gen(p+'(', 0, 2)  左括号没有了，只能加右括号。

gen(p + ')', 1, 1)  左括号剩一个，右括号剩一个，但是右括号个数不比左括号多，意思就是只能加左括号。

 

我只想说想出这个方法的真是个天才@https://leetcode.com/stefanpochmann/    

