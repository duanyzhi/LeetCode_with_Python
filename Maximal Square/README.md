# 题目描述

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example:**

```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

```
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
0 0 1 1 1
1 0 0 1 0

Output: 9

```

找出输入矩阵中最大的正方形(全1)的面积



# 解题思路

动态规划，但是要设置一个动态规划的矩阵dp [i, j]存储的是以i,j点为右下角的正方形的面积大小

判断矩阵元素是不是1，

dp[ i , j]  = min(dp [i - 1,  j - 1]  , min(dp[ i,  j - 1] , dp [i - 1, j ] ) + 1 # 比较i j 和上方 左方。左上几个dp中小的一个(最小矩阵意思就是i,j点的左上) i,j 和它相连的三个点中最小的dp，然后在加上自己，就是目前其最大的dp。



初始化dp

1 0 1 0 0 

1 0 0 0 0 

1 0 0 0 0 

 1 0 0 0 0



i = 1， j=2是元素为1，则dp[1, 2] = min(dp[0, 1], min(dp[1, 1] , dp[0, 2]) +1= min(0, min(0, 1) ) + 1 = 1

Res = max(res, dp[i, j]) = 1



i = 1, j =3 

​    dp[1, 3] = min(1, min(1, 0 )) + 1 = 1  #  1， 3左上 左都满足是1，dp也都是1， 但是上方却是0，所以dp也是0,因此取最小的dp为0，不能加一起，所以1，3的dp还是1



   dp[1, 4] = 1



dp[2, 2] = min(0, min(1, 1)) + 1  = 1

dp[2, 3] = min(1, min(1, 1)) + 1 = 2.   # 2,3的左上，左，上都是1，所以2，3是2

dp[2, 4] = min(1, min(2, 1)) + 1 = 2   # 2, 4只有左是2，其余都是1，所以还是1 

   










