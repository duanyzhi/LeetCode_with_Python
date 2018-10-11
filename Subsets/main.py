# Iteratively
def subsets(nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res

def subsets1(nums):
    res = [[]]
    for num in sorted(nums):
        sub = []
        for item in res:
            sub.append(item+[num])
        res += sub
    return res

# 输出子序列是连续的
def subsetsc(nums):
    sub = []
    for ii in range(len(nums) + 1):
        for jj in range(ii +1 , len(nums) + 1):
            sub.append(nums[ii:jj])
    return sub

nums = [3, 2, 1]
o = subsetsc(nums)
print(o)