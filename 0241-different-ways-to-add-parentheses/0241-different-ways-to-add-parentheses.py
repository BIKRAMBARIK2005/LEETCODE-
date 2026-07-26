class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        result = []
        for i, ch in enumerate(expression):
            if ch in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if ch == "+":
                            result.append(l + r)
                        elif ch == "-":
                            result.append(l - r)
                        else:
                            result.append(l * r)
        if not result:
            result.append(int(expression))
        return result