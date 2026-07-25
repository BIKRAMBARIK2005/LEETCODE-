class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = '+'
        number = 0
        s += '+'
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack.append(stack.pop() * number)
                elif sign == '/':
                    stack.append(int(stack.pop()/float(number)))
                sign = ch
                number = 0
        return sum(stack)