class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {}
        for i in range(len(s)):
          last_index[s[i]] = i
        stack = []
        seen = set()
        for i in range(len(s)):
          ch = s[i]
          if ch in seen:
            continue
          while stack and stack[-1] > ch and last_index[stack[-1]] > i:
            removed = stack.pop()
            seen.remove(removed)
          stack.append(ch)
          seen.add(ch)
        return ''.join(stack)