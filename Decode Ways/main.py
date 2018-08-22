'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

此问题有最右子问题，即如果当前位i和前一位i-1能组成小于等于26的两位数，那么前i个数字的解码方式
等于前i-2个数字的解码方式加上前i-1个数字的解码方式之和；否则，前i个数字的解码方式就等于前i-1个数字的解码方式。

假设数组dp[i]表示从头到字符串的第i位，一共有多少种解码方法的话，那么如果字符串的第i-1位和第i位
能组成一个10到26的数字，说明我们是在第i-2位的解码方法上继续解码。如果字符串的第i-1位和第i位不能
组成有效二位数字，而且第i位不是0的话，说明我们是在第i-1位的解码方法上继续解码。所以，如果两个条件
都符合，则dp[i]=dp[i-1]+dp[i-2]，否则dp[i]=dp[i-1]。
'''

class Solution:
    def numDecodings(self, s):
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            print(i, s[i - 1])
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]

st = "226"
s = Solution()

o = s.numDecodings(st)
print(o)

# ------------------------------------------------------------------------------
