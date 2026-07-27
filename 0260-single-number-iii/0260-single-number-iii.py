class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        counts = {}
        for x in nums:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        for num in counts:
            if counts[num] == 1:
                ans.append(num)
        return ans 

        