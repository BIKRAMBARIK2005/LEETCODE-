class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = 0
        for i in range(0,len(nums), 1):
            if nums[i] != count:
                return count
            count += 1
        return count
        