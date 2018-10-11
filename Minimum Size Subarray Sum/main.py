class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            print(right, n, total, left)
            total += n
            while total >= s:
                print("left", left, nums[left], result)
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0


S = Solution()
o = S.minSubArrayLen(7, [2,3,1,2,4,3])
print(o)