import math 
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        n = math.ceil((-1 + math.sqrt(1 + 8*abs(target)))/2)
        
        s = n*(n + 1)/2

        if s == target:
            return n

        res = int(s - target) 

        if res&1 == 0:  # res是偶数
            return n 
        else:
            if (n + 1)&1 == 0:
                return n + 2
            else:
                return n + 1
    

S = Solution()
o = S.reachNumber(2)
print(o)


