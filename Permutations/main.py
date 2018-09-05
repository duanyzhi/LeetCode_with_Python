import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            print("i", i, nums[:i], nums[i+1:])
            for j in self.permute(nums[:i] + nums[i+1:]):
                print("j", nums[i], j)
                res.append([nums[i]] + j)
                print("res", res)
        return res

    def permute2(self, nums):
        '''
        第二种方法，调用itertools函数，这个函数是真的好
        '''
        return list(itertools.permutations(nums))



s = Solution()
o = s.permute([1,2,3])
print(o)


# ------------------------------------------------------------------------------
