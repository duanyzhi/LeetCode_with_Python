class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: T
        :rtype: T
        """
        if len(s)==0:
        	return ""
        maxLen=1
        start=0
        for i in range(len(s)):
            print(i, maxLen, s[i], s[i-maxLen-1:i+1], s[i-maxLen-1:i+1][::-1])
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue
            print(i, maxLen, s[i], s[i - maxLen:i+1], s[i - maxLen:i+1][::-1])
            if i - maxLen > 0 and s[i - maxLen:i+1] == s[i - maxLen:i+1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start+maxLen]


S = Solution()
out = S.longestPalindrome("cadebbedz")
print(out)
