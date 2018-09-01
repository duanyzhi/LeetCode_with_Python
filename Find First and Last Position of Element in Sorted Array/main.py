class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        begin, end = 0,len(nums)-1
        ret = [-1, -1]
        while begin < end:
            mid = int((begin + end)/2)

            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid
        print(begin)
        if nums[begin] != target:
            return [-1, -1]
        else:
            ret[0] = begin

        end = len(nums) - 1
        while begin <  end:
            mid = int((begin + end)/2 + 1)
            if nums[mid] > target:
                end = mid -1
            else:
                begin = mid
        ret[1] = end
        return ret



nums = [5,7,7,8,8,10]
target = 8

s = Solution()
o = s.searchRange(nums, target)
print(o)
