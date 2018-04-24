
def Solution(nums):
    v = [[]]
    for kk in range(len(nums)):
        add_vector = []
        for jj in range(len(v)):
            if not v[jj]:
                cur_v = [nums[kk]][::]
            else:
                cur_v = v[jj][::]
                cur_v.append(nums[kk])
            add_vector.append(cur_v)
        v.extend(add_vector)

    return v

num = [1, 2, 3]
out = Solution(num)
print(out)

# out2 = [num[ii:jj] for ii in range(len(num) + 1) for jj in range(ii +1 , len(num) + 1)]  # 连续



