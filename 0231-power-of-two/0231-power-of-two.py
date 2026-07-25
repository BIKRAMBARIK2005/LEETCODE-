class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        mul = 1
        while mul < n:
            mul *= 2
        return mul == n