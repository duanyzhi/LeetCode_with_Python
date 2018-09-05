# 题目

Given a collection of **distinct** integers, return all possible permutations.

**Example:**

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```



# 解题思路

题目是输出所有的可能组合排列的形式。

```python
		nums == [1,2,3]
    	if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(3):
            # i = 0, nums[:i] == [], nums[i+1:] ==[2, 3]
            for j in self.permute(nums[:i] + nums[i+1:]):
                # self.permute([] + [2, 3]):
                # nums == [2, 3]
                # res = []
                # for i in range(2):
            		# i = 0, nums[:i] == [], nums[i+1:] == [3]
            		# for j in self.permute(nums[:i] + nums[i+1:]):
                        ```
                    	# self.permute([] + [3])
                        # nums == [3]
                        # return [3]
                        ```
                        # j = 3
                        # res = nums[i] + j = [2, 3][0] + 3 = [[2, 3]]
                    # i = 1, nums[:i] = [2], nums[i+1:] = []
                    # for j in self.permute(nums[:i] + nums[i+1:]):
                    	# return [2]
                        # nums[i] + j = [3, 2]
                        # res = [[2, 3], [3, 2]]
                # j in [[2, 3], [3, 2]]  
                # nums = [1, 2, 3]
                res = nums[i] + j = [[1, 2, 3], [1, 3, 2]]
            # i = 1, nums[:i] == [1], nums[i+1:] == [3]
            for j in self.permute(nums[:i] + nums[i+1:]):   
                nums[i] + j = [2] + [1, 3], [2] + [3, 1] = [2, 1, 3], [2, 3, 1]
                res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
            # i = 2, nums[:i] == [1, 2], nums[i+1:] = []
            	nums[i] + j = [3, 1, 2], [3, 2, 1]
                res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

先确定第一个元素，考虑剩下的列表的排列组合。剩下的列表又可以先确定一个元素，在考虑剩下的组合，就这样一值迭代知道最后只有一个元素的，返回。



# 解法二

itertools.permutations()函数