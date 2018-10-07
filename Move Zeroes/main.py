class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0  # 存储0的索引
        j = 1  # 存储1的索引
        if len(nums) == 1:
            pass
        elif len(nums) == 2:
            if nums[0] == 0:
                nums[0], nums[1] = nums[1], nums[0]
        else:
            while j < len(nums) and i < len(nums):
                while nums[i] !=0:
                    i += 1
                    if i == len(nums):
                        break
                j = min(i, len(nums)-1)
                while nums[j] == 0:
                    j += 1
                    if j == len(nums):
                        break
                if j < len(nums) and i < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)

    def moveZeroesz(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            print(i, zero)
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                print(i, zero, nums)


nums = [0,1,0,3,12]
nums1 = [1, 0]
nums2 = [4,2,4,0,0,3,0,5,1,0]
nums3 = [1]
nums4 = [1,2,3,1]
S = Solution()
S.moveZeroesz(nums2)
