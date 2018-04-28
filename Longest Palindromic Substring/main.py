"""
Given a Ting s, find the longest palindromic subTing in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

求最长回文（从左右读都一样）
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: T
        :rtype: T
        """
        T = "#" + "#".join(s) + "#"
        i = 0
        mx = 0
        id = 0
        p = [0] * len(T)
        while i < len(T):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1

            while i - p[i] >= 0 and i + p[i] < len(T) and T[i - p[i]] == T[i + p[i]]:
                p[i] += 1

            if mx < p[i] + i:
                mx = p[i] + i
                id = i
            i += 1
        max_index = p.index(max(p))

        return T[max_index - max(p) + 2:max_index + max(p):2]

S = Solution()
out = S.longestPalindrome("cbbd")
print(out)

