class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            print(parens, p, left, right)
            if left:  # 左括号剩余
                print("left", left)
                generate(p + '(', left-1, right)
            if right > left: # 右括号剩余个数大于左括号剩余个数
                print("right", right, left)
                generate(p + ')', left, right-1)
            if not right:
                print("p", parens, p, len(p), type(p))
                parens.append(p)  # 相当于 "parens += p, " 这里一定要有， 为什么
            return parens
        return generate('', n, n)

s = Solution()
o  = s.generateParenthesis(2)
print(o)



# ------------------------------------------------------------------------------
