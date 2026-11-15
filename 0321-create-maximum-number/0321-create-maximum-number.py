class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def max_subsequence(nums, k):
            stack = []
            remove = len(nums) - k
            for num in nums:
                while stack and remove > 0 and stack[-1] < num:
                    stack.pop()
                    remove -= 1
                stack.append(num)
            return stack[:k]
        def greater(a, i, b, j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            return j == len(b) or (i < len(a) and a[i] > b[j])
        def merge(a, b):
            result = []
            i = 0
            j = 0
            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1
            return result
        maximum = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end + 1):
            j = k - i
            first = max_subsequence(nums1, i)
            second = max_subsequence(nums2, j)
            candidate = merge(first, second)
            if candidate > maximum:
                maximum = candidate
        return maximum

        
        