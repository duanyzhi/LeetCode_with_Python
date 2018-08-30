class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        let = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        L = [let[int(d) - 2] for d in digits]
        return [''.join(i) for i in product(L)]

def product(args):
    '''
    相当于 itertools.product 函数
    '''
    pools = map(tuple, args)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]  # for 循环遍历加入
    for prod in result:
        yield tuple(prod)

s = Solution()
o = s.letterCombinations("23")
print(o)
# ------------------------------------------------------------------------------
