'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

slow = f(slow)
fast = f(f(fast))

我们重复此步骤直到slow与fast彼此相等
'''

# O(n)复杂度
class Solution(object):
    def findDuplicate(self, nums):
        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = 0
        fast = 0

        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)

            if slow == fast:
                break

        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
            print("find", slow, finder)

            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow

# O(nlogn)复杂度
# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         low, high = 1, len(nums) - 1
#         while low <= high:
#             mid = (low + high) >> 1
#             cnt = sum(x <= mid for x in nums)
#             if cnt > mid:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return low

# O(n)
# class Solution:
#     def findDuplicate(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)
#

num = [3,1,3,4,2]
s = Solution()
o = s.findDuplicate(num)
print(o)
