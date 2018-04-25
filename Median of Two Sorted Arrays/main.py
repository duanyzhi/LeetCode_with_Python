"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

题目要求O(log(m+n))的时间复杂度，一般来说都是分治法（Divide and Conquer）或者二分搜索
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        k = (m + n) / 2
        if (m + n) % 2 == 0:  # 总数为偶数
            return (self.findKth(nums1, nums2, m, n, k) + self.findKth(nums1, nums2, m, n, k + 1))/2
        else:     # 奇数
            return self.findKth(nums1, nums2, m, n, int(k) + 1)

    def findKth(self, nums1, nums2, len1, len2, k):  # 找到第K个大的值
        if not nums1:
            return nums2[int(k) - 1]
        if not nums2:
            return nums1[int(k) - 1]
        p1, p2 = int(len1/2), int(len2/2)
        if nums1[p1] < nums2[p2]:
            nums1, nums2 = nums2, nums1
            p1, p2 = p2, p1
        if k < p1 + p2 + 2:
            nums1 = nums1[:p1]
        else:
            if p2 != 0:
                nums2 = nums2[p2:]
                k -= p2
            else:
                nums2 = []
                k -= 1
        if nums1 == [] and len(nums2) == 1:
            return nums2[0]
        if nums2 == [] and len(nums1) == 1:
            return nums1[0]
        else:
            return self.findKth(nums1, nums2, len(nums1), len(nums2), k)
a = [1, 2, 3]
b = [3, 4, 5]

S = Solution()
out = S.findMedianSortedArrays(a, b)
print(out)
