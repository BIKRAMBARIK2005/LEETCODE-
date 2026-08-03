from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        visited = set()
        q = deque()

        q.append(s)
        visited.add(s)

        found = False

        while q:
            size = len(q)

            for _ in range(size):
                cur = q.popleft()

                if isValid(cur):
                    ans.append(cur)
                    found = True

                if found:
                    continue

                for i in range(len(cur)):
                    if cur[i] not in "()":
                        continue

                    nxt = cur[:i] + cur[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

            if found:
                break

        return ans
            