class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n+1) // 2
        smaller = nums[:mid]
        larger = nums[mid:]
        smaller.reverse()
        larger.reverse()
        i = 0
        j = 0
        for k in range(0, n):
            if k % 2 == 0:
                nums[k] = smaller[i]
                i += 1
            else:
                nums[k] = larger[j]
                j += 1
        return nums