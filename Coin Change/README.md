# 题目描述

'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

给一个coins列表表示不同的几个硬币值，amount表示总的需要的钱数。问怎么用最少的硬币个数来组成所需的总钱数。



# 题目分析及解答

以Example为例：

coins = [1, 2, 5]

amount:     1     2     3     4     5     6     7     8     9     10     11

初始化dp= [0    12   12   12   12  12   12   12   12   12    12]  用来存储加到每个amount所需要多少个coins

kk = range(1, 12)

kk = 1:

for coin in coins:  # 遍历所有的coins的值，每一个都和当前kk相比

​    if coin <= kk:     # 判断当前的amount是否大于coins里的值，如果大于说明可以用coins里的值表示。

更新dp[kk],查询dp[kk]本身和kk - coins的值，比如coin=1，kk-coin=0, dp[0]即amount为0的时候的dp，说明kk可以用amount=0时候的dp值在加上1（1表示当前的coin=1）,即之前的0在加上1就可以表示新的kk。然后和dp[kk]本身比较即可。

​	dp[kk] = min(dp[kk], dp[kk - coin] + 1)   

​	dp[1] = 1



Kk = 2:

​	for coin in coins:

​		coin = 1:

​                       kk - 1 = 2 -1 , dp[1]= 1 # 说明2可以 用1 + 1来表示

​				dp[2] = min(12, 1+ 1) = 2

​		coin = 2:

​			kk - 2 = 0,  dp[0] = 0 , 说明2可以用0 + 2来表示

​				dp[2] = min(2, 0 + 1) = 1

.....

最后dp[12]就表示了最后的值，如果没有可以加一起得到amount的值，那么dp[12]=12,此时判断输出

​	



