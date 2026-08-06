class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self.add(i+1, nums[i])
    def add(self, index, val):
        while index <= self.n:
            self.bit[index] += val
            index += (index & -index)
    def prefixSum(self, index):
        s = 0
        while index > 0:
            s += self.bit[index]
            index -= (index & -index)
        return s
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, diff)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefixSum(right + 1) - self.prefixSum(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)