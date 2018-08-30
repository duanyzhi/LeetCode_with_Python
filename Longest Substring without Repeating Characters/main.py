class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: # 长度为1情况
            return 1
        big_str = ''
        cur_str = ''
        for ii in range(len(s)):
            for kk in range(ii, len(s)):
                if s[kk] not in cur_str:
                    cur_str += s[kk]
                else:
                    if len(cur_str) > len(big_str):
                        big_str = cur_str
                    cur_str = ''
                    break
        return len(big_str)

while True:
    str_in = input()
    S = Solution()
    out = S.lengthOfLongestSubstring(str_in)
    print(out)
