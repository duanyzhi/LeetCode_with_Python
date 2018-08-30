# 遍历 复杂度: n + (n-1) + (n-2) + ..+1 = n(n+1)/2  + if in = n**3
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         out_list = []
#         for ii in range(len(nums)-2):
#             for jj in range(ii + 1, len(nums)-1):
#                 if -(nums[ii] + nums[jj]) in nums[jj+1:]:
#                     _index = nums[jj+1:].index(-(nums[ii] + nums[jj]))
#                     new_list = [nums[ii], nums[jj], nums[jj+_index+1]]
#                     new_list.sort()
#                     if new_list not in out_list:
#                         out_list.append(new_list)
#
#         return out_list

# ------------------------------------------------------------------------------
# 改进  删除一个for循环 dp改进
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort() # 排序
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  # 过滤相同的元素避免重复计算
                continue
            l, r = i+1, len(nums)-1  # 两个方向向中间搜索
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:  # 太小 数要大写
                    l +=1
                elif s > 0: # 和太大 最大的数要小点
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]]) # nums从小到大排序
                    while l < r and nums[l] == nums[l+1]: # 过滤重复元素？
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

s = Solution()
o = s.threeSum([-1, 0, 1, 2, -1, -4])
print(o)


# ------------------------------------------------------------------------------
