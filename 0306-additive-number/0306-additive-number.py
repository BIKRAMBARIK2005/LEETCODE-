class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                if num[0] == '0' and i > 1:
                    break
                if num[i] == '0' and j - i > 1:
                    continue
                first = int(num[:i])
                second = int(num[i:j])
                if self.check(first, second, num[j:]):
                    return True
        return False
    def check(self, first, second, remain):
            while remain:
                s = first + second
                s_str = str(s)
                if not remain.startswith(s_str):
                    return False
                remain = remain[len(s_str):]
                first = second
                second = s
            return True