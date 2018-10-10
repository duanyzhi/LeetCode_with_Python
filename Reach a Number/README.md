# 题目
You are standing at position `0` on an infinite number line. There is a goal at position `target`.

On each move, you can either go left or right. During the *n*-th move (starting from 1), you take *n* steps.

Return the minimum number of steps required to reach the destination.

**Example 1:**

```
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
```



**Example 2:**

```
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
```



**Note:**

`target` will be a non-zero integer in the range `[-10^9, 10^9]`.

从0开始到一个目标点，第N步只能走N或-N个单位，最少步数



# 解题思路

假设我们一直加到n使得和:

Sum = 1 + 2 + .... + n >= target,根据一元二次方程求根定理：

n = $ \frac{-1+sqrt(1+8t)}{2} $

对n向上取整数

然后求的和sum = n(n+1)/2

1. 如果和sum等于traget，则直接是n

2. 求得差值res = sum - target

3. 如果res是偶数，那么就需要在[1,n]之间让一个数x变为-x即可，即加入res=4，那么说明n个数加在一起多了4.那么1+...+n=target + 4,我们如果令x=2,那么等式两边都减去-2x，则1+（-x）+3+...+n=target。即我们任然是只需要n步就可以到达target。只需要将其中一个数变为负的就好。

4. 如果res是奇数。

   4.1 如果n+1是偶数，那么在走n+1步在反向走n+2步：

          1+...+n+n+1-(n+2) = target + res -1

        那么res肯定是奇数，我们可以去x = (res - 1) /2,并令x步事为-x，那么自然可以走到target，这个时候步数为： n + 2 

     4.2 如果n + 1是奇数，那么我们只需要在走一步n+1步就可以了，那么有两个奇数相加肯定是偶数，

        1+....+n+n+1 = target + res + n +1

      那么res + n + 1肯定是偶数，我们可以令x = (res + n + 1)/2, x步为-x即可，那么这个时候的步数为n + 1



总的思想就是凑数使得res这部分为一个偶数就好。target为负数一个意思所以只需要算正数就好。